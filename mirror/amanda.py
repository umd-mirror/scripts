from . import MirrorRunner

class AmandaMirrorRunner(MirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/dl.sourceforge.net/pub/sourceforge/a/project/am/amanda/'
  rsync_filter_list = ['- index.html']


