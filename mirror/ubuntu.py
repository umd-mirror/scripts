from . import RsyncMirrorRunner, APTMirrorRunner

class UbuntuMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://archive.ubuntu.com/ubuntu/'

  rsync_delete_delay = False
  rsync_delay_updates = False

  rsync_filter_list = ['- /Archive-Update-in-Progress-*']

#class UbuntuMirrorRunner(APTMirrorRunner):
#  source = 'http://archive.ubuntu.com/ubuntu'
#  apt_releases = ['lucid', 'maverick', 'natty']
#  apt_architectures = ['i386', 'amd64']
#  apt_slots = ['', '-updates', '-backports', '-proposed', '-security']
#  apt_parts = ['main', 'multiverse', 'restricted', 'universe']

