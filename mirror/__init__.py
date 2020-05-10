# ...
import datetime
import os
import re
import shutil
import subprocess
import tempfile

basedir = '/pool/mirrors'
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

def rsync(source, dest, archive=False, verbose=False, preserve_perm=False, dry_run=False, delete_excluded=False, filter_from=None, delete=False, progress=False, delete_delay=False, delay_updates=False, hardlinks=False, timeout=None, safe_links=False, password_file=None):
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
    '-H' if hardlinks else None,
    '--timeout=%d' % timeout if timeout else None,
    '--safe-links' if safe_links else None,
    '--password-file=%s' % password_file if password_file else None
  ]

  opts = [opt for opt in opts if opt] # remove null fields

  rsync_cmd = ["/home/mirror/scripts/rsync-no-vanished"]
  #rsync_cmd = ["/usr/bin/rsync"]
  rsync_cmd.extend(opts)
  rsync_cmd.extend([source, dest])

  if verbose:
    print("rsync command: ", ' '.join(rsync_cmd))

  #retcode = subprocess.call(rsync_cmd)

  process = subprocess.Popen(rsync_cmd,
                             bufsize=0)
  retcode = process.wait()

  if retcode != 0:
    raise Exception("rsync failed")

class MirrorRunner(object):
  base = None # Full path to target
  base_subdir = None # Path within mirrors directory (base overrides)
  status_directory = None # Path where mirror.umd.edu.*.txt will go

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
    timestamp = datetime.datetime.utcnow()

    if self.status_directory is not None:
      statdir = self.status_directory
    else:
      statdir = self.base

    if os.path.ismount(statdir):
      # bytes = int(subprocess.check_output(['sudo', '/usr/local/bin/get_lused.sh', statdir]))
      bytes = int(subprocess.check_output(['/sbin/zfs', 'get', '-H', '-o', 'value', '-p', 'lused', statdir]))
    else:
      bytes = int(subprocess.check_output(['du', '-sB1', '--apparent-size', statdir + '/', '--exclude=lost+found']).split("\t")[0])

    gigabytes = bytes/1024/1024/1024
    print("SIZE: " + str(gigabytes) + " GB")

    if not dry_run:
      tmp_size_path = os.path.join(statdir, "mirror.umd.edu.size.txt.tmp")
      size_file = open(tmp_size_path, 'w')
      size_file.write("{0} ({1} GB)\n".format(bytes, gigabytes))
      size_file.close()

      os.rename(tmp_size_path, os.path.join(statdir, "mirror.umd.edu.size.txt"))

      tmp_timestamp_path = os.path.join(statdir, "mirror.umd.edu.timestamp.txt.tmp")
      timestamp_file = open(tmp_timestamp_path, 'w')
      timestamp_file.write(timestamp.strftime("%s (%c)") + "\n")
      timestamp_file.close()

      os.rename(tmp_timestamp_path, os.path.join(statdir, "mirror.umd.edu.timestamp.txt"))

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
  rsync_timeout = 600
  rsync_safe_links = True
  rsync_password_file = None

  def update(self, verbose, dry_run):
    all_filters = []
    all_filters.append('P /lost+found')
    all_filters.append('P /mirror.umd.edu.*.txt')
    all_filters.append('- .~tmp~')

    if self.rsync_filter_from is not None:
      all_filters.extend(open(self.rsync_filter_from, "r").read().split("\n"))

    if self.rsync_filter_list is not None:
      all_filters.extend(self.rsync_filter_list)

    (combined_filter_fd, combined_filter_path) = tempfile.mkstemp(prefix=self.module_name)
    os.fchmod(combined_filter_fd, 0644)
    combined_filter = os.fdopen(combined_filter_fd, 'w')
    combined_filter.write("\n".join(all_filters))
    combined_filter.flush()

    rsync(self.source, self.base, self.rsync_archive, verbose, self.rsync_preserve_perm, dry_run, self.rsync_delete_excluded, combined_filter_path, self.rsync_delete, verbose, self.rsync_delete_delay, self.rsync_delay_updates, self.rsync_preserve_hardlinks, self.rsync_timeout, self.rsync_safe_links, self.rsync_password_file)

    os.unlink(combined_filter_path)

class APTMirrorRunner(MirrorRunner):
  ALL_UBUNTU_RELEASES = ['warty', 'hoary', 'breezy', 'dapper', 'edgy', 'feisty', 'gutsy', 'hardy', 'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick', 'natty', 'oneiric', 'precise', 'quantal', 'raring', 'saucy', 'trusty', 'utopic', 'vivid', 'wily', 'xenial', 'yakkety', 'zesty', 'artful', 'bionic', 'cosmic']
  LTS_UBUNTU_RELEASES = ['dapper', 'hardy', 'lucid', 'precise', 'trusty', 'xenial', 'bionic']

  apt_releases = []
  apt_architectures = []
  apt_slots = ['']
  apt_parts = []

  def pre_update(self, verbose, dry_run):
    MirrorRunner.pre_update(self, verbose, dry_run)

    (apt_cfg_fd, self.apt_cfg_path) = tempfile.mkstemp(prefix=self.module_name)
    apt_cfg = os.fdopen(apt_cfg_fd, 'w')
    
    #apt_header = os.path.join(EXTRAS, 'apt_header')

    apt_cfg.write("set base_path    /home/mirror/var/apt-mirror-%s\n" % self.module_name)
    #apt_cfg.write("set mirror_path  %s\n" % basedir)
    apt_cfg.write("set mirror_path  /home/mirror/apt\n")
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
      self.status_directory = os.path.join("/home/mirror/apt", source_match.group(2))

  def post_update(self, verbose, dry_run):
    os.unlink(self.apt_cfg_path)
    MirrorRunner.post_update(self, verbose, dry_run)


