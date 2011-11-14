import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraLinuxMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/linux'
  # source = 'rsync://fedora-archives.ibiblio.org/fedora-enchilada/linux/'
  # source = 'rsync://archive.linux.duke.edu:874/fedora/linux/'
  # source = 'rsync://mirrors.rit.edu/fedora-enchilada/linux/'
  source = 'rsync://ftp.heanet.ie/fedora-enchilada/linux/'

  rsync_filter_from = os.path.join(EXTRAS, 'fedora-linux.exclude')
  rsync_preserve_hardlinks = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')])

