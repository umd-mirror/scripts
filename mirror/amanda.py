from . import RsyncMirrorRunner

class AmandaMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/downloads.sourceforge.net/a/project/am/amanda/'
  rsync_filter_list = ['- index.html']


