from . import RsyncMirrorRunner

class FindBugsMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/download.sourceforge.net/pub/sourceforge/f/project/fi/findbugs/'
