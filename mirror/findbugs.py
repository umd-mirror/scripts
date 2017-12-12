from . import RsyncMirrorRunner

class FindBugsMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync.mirrorservice.org/downloads.sourceforge.net/f/fi/findbugs/'
