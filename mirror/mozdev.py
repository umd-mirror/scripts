from . import MirrorRunner

class MozdevMirrorRunner(MirrorRunner):
  source = 'rsync://rsync.mozdev.org/mozdev/'
