from . import APTMirrorRunner

class ROSMirrorRunner(APTMirrorRunner):
  source = 'http://packages.ros.org/ros/ubuntu'
  apt_releases = list(set(APTMirrorRunner.ALL_UBUNTU_RELEASES[11:] + ['wheezy', 'jessie', 'stretch']))
  apt_architectures = ['i386', 'amd64', 'arm64', 'armhf']
  apt_parts = ['main']

