from . import RsyncMirrorRunner

class AntergosMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/repo.antergos.com/'
  rsync_delete_delay = True
  rsync_delay_updates = True
  rsync_preserve_hardlinks = True

