from . import APTMirrorRunner

class ROSMirrorRunner(APTMirrorRunner):
  source = 'http://packages.ros.org/ros/ubuntu'
  apt_releases = list(set(APTMirrorRunner.ALL_UBUNTU_RELEASES[7:] + ['wheezy']) - set(['intrepid']))
  apt_architectures = ['i386', 'amd64', 'armel', 'armhf']
  apt_parts = ['main']

