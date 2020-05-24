from . import APTMirrorRunner

class ROSMirrorRunner(APTMirrorRunner):
  source = 'http://packages.ros.org/ros/ubuntu'
  # get updates from https://github.com/ros-infrastructure/mirror/blob/master/mirror/files/mirror.list
  apt_releases = list(set(['jessie', 'stretch', 'buster', 'trusty', 'xenial', 'bionic', 'focal']))
  apt_architectures = ['i386', 'amd64', 'arm64', 'armhf']
  apt_parts = ['main']

