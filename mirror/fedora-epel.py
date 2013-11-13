import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraEPELMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/epel'
  # source = 'rsync://download.wpi.edu:874/fedora-epel/'
  source = 'rsync://fedora-archives.ibiblio.org/fedora-epel/'
  rsync_filter_list = ['- debug', '- /testing', '- SRPMS']
  rsync_preserve_hardlinks = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')])
    RsyncMirrorRunner.post_update(self, verbose, dry_run)

