# ...
import os
import re
import shutil
import subprocess
import tempfile

basedir = '/home/mirror/archives'
EXTRAS = '/home/mirror/scripts/mirror/extras'

def is_disabled():
  return os.access('/home/mirror/disable_mirrors', os.R_OK)

def get_lock(module):
  lock_path = '/home/mirror/scripts/mirror/%s.lock' % module
  
  if os.path.exists(lock_path):
    # try to claim the lock when the holder has died
    lock_file = open(lock_path, 'r')
    pid = lock_file.read()
    lock_file.close()

    pid = int(pid) if pid else 0

    # let this lock be re-entrant
    if pid == os.getpid():
      return True

    process_running = True

    if pid == 0:
      process_running = False

    try:
      os.kill(int(pid), 0)
    except OSError:
      process_running = False

    if process_running:
      return False
    else:
      os.unlink(lock_path)

  lock_file = open(lock_path, 'w')
  lock_file.write(str(os.getpid()))
  lock_file.close()

  return True

def rsync(source, dest, archive=False, verbose=False, preserve_perm=False, dry_run=False, delete_excluded=False, filter_from=None, delete=False, progress=False, delete_delay=False, delay_updates=False, hardlinks=False):
  opts = [
    '-rlt' if archive else None,
    '--delete' if delete else None,
    '-v' if verbose else '-q',
    '-p' if preserve_perm else None,
    '-n' if dry_run else None,
    '--progress' if progress else None,
    '--delete-excluded' if delete_excluded else None,
    '--filter=. %s' % filter_from if filter_from else None,
    '--delete-delay' if delete_delay else None,
    '--delay-updates' if delay_updates else None,
    '-H' if hardlinks else None
  ]

  opts = [opt for opt in opts if opt] # remove null fields

  rsync_cmd = ["/home/mirror/scripts/rsync-no-vanished"]
  rsync_cmd.extend(opts)
  rsync_cmd.extend([source, dest])

  retcode = subprocess.call(rsync_cmd)

  if retcode != 0:
    raise Exception("rsync failed")

class MirrorRunner:
  base = None # Full path to target
  base_subdir = None # Path within mirrors directory (base overrides)

  def __init__(self):
    self.module_name = self.__class__.__module__[7:]
    if self.base_subdir is None:
      self.base_subdir = self.module_name
    if self.base is None:
      self.base = "%s/%s" % (basedir, self.base_subdir)

  def run(self, verbose=False, dry_run=False):
    """Execute the mirror runner, causing an update"""
    self.pre_update(verbose, dry_run)
    self.update(verbose, dry_run)
    self.post_update(verbose, dry_run)

  def pre_update(self, verbose, dry_run):
    pass

  def update(self, verbose, dry_run):
    pass

  def post_update(self, verbose, dry_run):
    pass

class RsyncMirrorRunner(MirrorRunner):
  source = None

  rsync_archive = True
  rsync_preserve_perm = False
  rsync_preserve_hardlinks = False
  rsync_delete = True
  rsync_delete_excluded = False
  rsync_delete_delay = False
  rsync_delay_updates = False
  rsync_filter_from = None
  rsync_filter_list = None


  def update(self, verbose, dry_run):
    if self.rsync_filter_list is not None:
      if self.rsync_filter_from is not None:
        raise Exception("you cannot specify both rsync_filter_from and rsync_filter_list")
      (filter_fd, self.rsync_filter_from) = tempfile.mkstemp(prefix=self.module_name)
      filter = os.fdopen(filter_fd, 'w')
      filter.write("\n".join(self.rsync_filter_list))
      filter.close()

    rsync(self.source, self.base, self.rsync_archive, verbose, self.rsync_preserve_perm, dry_run, self.rsync_delete_excluded, self.rsync_filter_from, self.rsync_delete, verbose, self.rsync_delete_delay, self.rsync_delay_updates, self.rsync_preserve_hardlinks)

    if self.rsync_filter_list is not None:
      os.unlink(self.rsync_filter_from)

    if not dry_run:
      subprocess.call("date > %s/mirror.umd.edu.txt" % self.base, shell=True)

class APTMirrorRunner(MirrorRunner):
  apt_releases = []
  apt_architectures = []
  apt_slots = ['']
  apt_parts = []

  def pre_update(self, verbose, dry_run):
    (apt_cfg_fd, self.apt_cfg_path) = tempfile.mkstemp(prefix=self.module_name)
    apt_cfg = os.fdopen(apt_cfg_fd, 'w')
    
    #apt_header = os.path.join(EXTRAS, 'apt_header')

    apt_cfg.write("set base_path    /home/mirror/var/apt-mirror-%s\n" % self.module_name)
    apt_cfg.write("set mirror_path  %s\n" % basedir)
    apt_cfg.write("set _autoclean   1\n")

    #shutil.copyfileobj(open(apt_header, 'rb'), apt_cfg)
    
    for release in self.apt_releases:
      for slot in self.apt_slots:
        for arch in self.apt_architectures:
          for part in self.apt_parts:
            apt_cfg.write("deb-%s %s %s%s %s\n" % (arch, self.source, release, slot, part))

    apt_cfg.write("clean %s\n" % self.source)

    apt_cfg.close()

  def update(self, verbose, dry_run):
    # apt-mirror likes to die and leave lock files everywhere. We'll just use our own.
    try:
      os.unlink('/home/mirror/var/apt-mirror-%s/var/apt-mirror.lock' % self.module_name)
    except OSError:
      pass

    if not dry_run:
      cmd = [os.path.join(EXTRAS, 'apt-mirror'), self.apt_cfg_path]
      if verbose:
        retcode = subprocess.call(cmd)

        if retcode != 0:
          raise Exception("apt-mirror failed")
      else:
        try:
          output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
          raise Exception("apt-mirror failed with output: " + output)

    source_match = re.match('(https?://)?([^/]+)(/.+)?', self.source)
    if source_match:
      subprocess.call("date > %s/%s/mirror.umd.edu.txt" % (basedir, source_match.group(2)), shell=True)

  def post_update(self, verbose, dry_run):
    os.unlink(self.apt_cfg_path)


