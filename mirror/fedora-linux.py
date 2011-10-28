import os
import subprocess

from . import MirrorRunner, EXTRAS

class FedoraLinuxMirrorRunner(MirrorRunner):
  base_subdir = 'fedora/linux'
  source = 'rsync://fedora-archives.ibiblio.org/fedora-enchilada/linux/'
  # source = 'rsync://archive.linux.duke.edu:874/fedora/linux/'

  rsync_filter_from = os.path.join(EXTRAS, 'fedora-linux.exclude')

  def post_update(self, verbose, dry_run):
    if not dry_run:
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')])

