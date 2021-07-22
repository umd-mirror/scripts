from . import RsyncMirrorRunner

class EclipseMirrorRunner(RsyncMirrorRunner):
  #source = 'rsync://rsync.osuosl.org/eclipse'
  #source = 'rsync://rsync.gtlib.gatech.edu/eclipse'
  source = 'rsync://download.eclipse.org/eclipseMirror'

  rsync_delete_delay = True
  rsync_delay_updates = True
