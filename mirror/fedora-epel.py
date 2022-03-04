import os
import subprocess

from . import RsyncMirrorRunner, EXTRAS

class FedoraEPELMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'fedora/epel'
  # source = 'rsync://download.wpi.edu:874/fedora-epel/'
  source = 'rsync://archive.linux.duke.edu/fedora-epel/'
  # source = 'rsync://fedora-archives.ibiblio.org/fedora-epel/'
  # source = 'rsync://ftp.heanet.ie/fedora-epel/'
  # source = 'rsync://mirror.rit.edu/epel/'
  # source = 'rsync://rsync.gtlib.gatech.edu/fedora-epel/'
  rsync_filter_list = ['- debug', '- SRPMS', '- /3', '- /4', '- /5', '- /4AS', '- /4ES', '- /4WS', '- /5Client', '- /5Server']
  #rsync_filter_list = ['- debug', '- /testing', '- SRPMS', '- /3', '- /4', '- /5']
  rsync_preserve_hardlinks = True

  def post_update(self, verbose, dry_run):
    if not dry_run:
      my_env = os.environ.copy()
      my_env["FEDORA_MIRROR_REPORT_PASSWORD"] = open(os.path.join(EXTRAS, 'fedora-report-mirror.password'), "r").read().strip()
      subprocess.call([os.path.join(EXTRAS, 'report_mirror'), '-c', os.path.join(EXTRAS, 'report_mirror.conf')], env=my_env)
    RsyncMirrorRunner.post_update(self, verbose, dry_run)
