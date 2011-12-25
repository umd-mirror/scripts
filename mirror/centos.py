from . import RsyncMirrorRunner

class CentOSMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://us-msync.centos.org/CentOS/'
  # rsync_filter_list = ['- /3*', '- /2*']
  rsync_preserve_perm = True

