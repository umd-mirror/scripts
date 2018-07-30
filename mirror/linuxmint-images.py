from . import RsyncMirrorRunner

class LinuxMintImagesMirrorRunner(RsyncMirrorRunner):
  #source = 'rsync://ftp.heanet.ie/pub/linuxmint.com/'
  source = 'rsync://pub.linuxmint.com/pub/'

  base_subdir = 'linuxmint/images'

