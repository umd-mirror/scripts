from . import RsyncMirrorRunner

class EclipseMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://mirror.zorinos.com/isos'

  rsync_delete_delay = True
  rsync_delay_updates = True
