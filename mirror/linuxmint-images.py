from . import RsyncMirrorRunner

class LinuxMintImagesMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://ftp.heanet.ie/pub/linuxmint.com/'

  base_subdir = 'linuxmint/images'

