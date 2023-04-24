import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraLinuxMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/linux'
  #source = 'rsync://fedora-archives.ibiblio.org/fedora-enchilada/linux/'
  # source = 'rsync://archive.linux.duke.edu:874/fedora/linux/'
  # source = 'rsync://mirrors.rit.edu/fedora-enchilada/linux/'
  source = 'rsync://archive.linux.duke.edu/fedora-enchilada/linux/'
  # source = 'rsync://ftp.heanet.ie/fedora-enchilada/linux/'

  rsync_filter_from = os.path.join(EXTRAS, 'fedora-linux.exclude')
  rsync_preserve_hardlinks = True
  rsync_preserve_perm = True
  rsync_delete_excluded = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      my_env = os.environ.copy()
      my_env["FEDORA_MIRROR_REPORT_PASSWORD"] = open(os.path.join(EXTRAS, 'fedora-report-mirror.password'), "r").read().strip()
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')], env=my_env)
    RsyncMirrorRunner.post_update(self, verbose, dry_run)
