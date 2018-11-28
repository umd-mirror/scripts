from . import RsyncMirrorRunner

class EclipseMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.osuosl.org/eclipse'

  rsync_delete_delay = True
  rsync_delay_updates = True
