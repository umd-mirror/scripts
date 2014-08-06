from . import RsyncMirrorRunner

class ArchAssaultMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://mirror.jmu.edu/archassault/'
  rsync_delete_delay = True
  rsync_delay_updates = True

