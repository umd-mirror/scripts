from . import RsyncMirrorRunner

class UbuntuISOMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://us.rsync.releases.ubuntu.com/releases/'
