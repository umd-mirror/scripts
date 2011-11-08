from . import RsyncMirrorRunner

class MozdevMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mozdev.org/mozdev/'
