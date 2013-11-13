from . import RsyncMirrorRunner

class XBMCMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.xbmc.org/main/'
