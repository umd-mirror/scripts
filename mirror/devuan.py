from . import RsyncMirrorRunner

class DevuanMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://files.devuan.org/devuan/'

  rsync_delete_delay = True
  rsync_delay_updates = True
