from . import MirrorRunner, APTMirrorRunner

class UbuntuMirrorRunner(MirrorRunner):
  source = 'rsync://archive.ubuntu.com/ubuntu/'

  rsync_delete_delay = True
  rsync_delay_updates = True

  rsync_filter_list = ['- /Archive-Update-in-Progress-*']

#class UbuntuMirrorRunner(APTMirrorRunner):
#  source = 'http://archive.ubuntu.com/ubuntu'
#  apt_releases = ['lucid', 'maverick', 'natty']
#  apt_architectures = ['i386', 'amd64']
#  apt_slots = ['', '-updates', '-backports', '-proposed', '-security']
#  apt_parts = ['main', 'multiverse', 'restricted', 'universe']

