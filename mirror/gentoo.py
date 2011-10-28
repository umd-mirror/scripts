from . import MirrorRunner

class GentooMirrorRunner(MirrorRunner):
  source = 'rsync://ftp.ussg.iu.edu/gentoo-distfiles/'

  rsync_filter_list = ['- /releases/.test/THIS-FILE-SHOULD-NOT-BE-PUBLIC.txt']

