from . import RsyncMirrorRunner

class GentooPortageMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://ftp.ussg.iu.edu/gentoo-portage/'
