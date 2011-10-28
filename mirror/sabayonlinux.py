import os
from . import MirrorRunner, EXTRAS

class SabayonMirrorRunner(MirrorRunner):
  #HOST=rsync.sabayonlinux.org::SabayonLinux
  source='rsync://ftp.surfnet.nl/sabayonlinux/'
  rsync_filter_from = os.path.join(EXTRAS, 'sabayonlinux.exclude')


