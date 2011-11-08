from . import RsyncMirrorRunner

class AmandaMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/dl.sourceforge.net/pub/sourceforge/a/project/am/amanda/'
  rsync_filter_list = ['- index.html']


