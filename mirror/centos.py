from . import MirrorRunner

class CentOSMirrorRunner(MirrorRunner):
  source = 'rsync://us-msync.centos.org/CentOS/'
  # rsync_filter_list = ['- /3*', '- /2*']

