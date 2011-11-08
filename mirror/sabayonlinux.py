import os
from . import RsyncMirrorRunner, EXTRAS

class SabayonMirrorRunner(RsyncMirrorRunner):
  #HOST=rsync.sabayonlinux.org::SabayonLinux
  source='rsync://ftp.surfnet.nl/sabayonlinux/'
  rsync_filter_from = os.path.join(EXTRAS, 'sabayonlinux.exclude')


