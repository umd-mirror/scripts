from . import RsyncMirrorRunner

class TurnKeyLinuxMirrorRunner(RsyncMirrorRunner):
  #source = 'rsync://ftp.heanet.ie/mirrors/sourceforge/t/project/tu/turnkeylinux/'
  #source = 'rsync://rsync.mirrorservice.org/turnkeylinux.org/'
  #source = 'rsync://mirror.serverloft.com/turnkeylinux/'
  source = 'rsync://mirror.turnkeylinux.org/turnkeylinux/'
