import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraEPELMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/epel'
  # source = 'rsync://download.wpi.edu:874/fedora-epel/'
  # source = 'rsync://archive.linux.duke.edu/fedora-epel/'
  # source = 'rsync://fedora-archives.ibiblio.org/fedora-epel/'
  # source = 'rsync://ftp.heanet.ie/fedora-epel/'
  source = 'rsync://mirror.rit.edu/epel/'
  rsync_filter_list = ['- debug', '- /testing', '- SRPMS', '- /3', '- /4', '- /5']
  rsync_preserve_hardlinks = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')])
    RsyncMirrorRunner.post_update(self, verbose, dry_run)

