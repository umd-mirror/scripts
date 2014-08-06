from . import RsyncMirrorRunner, APTMirrorRunner

class RaspbianMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://archive.raspbian.org/archive/'

  rsync_delete_delay = True
  rsync_delay_updates = True
