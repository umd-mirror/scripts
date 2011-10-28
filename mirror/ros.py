from . import APTMirrorRunner

class ROSMirrorRunner(APTMirrorRunner):
  source = 'http://packages.ros.org/ros/ubuntu'
  apt_releases = ['jaunty', 'karmic', 'lucid', 'maverick', 'natty', 'oneiric']
  apt_architectures = ['i386', 'amd64', 'src']
  apt_parts = ['main']

