from . import RsyncMirrorRunner

class RosWikiMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'ros-wiki'
  source = 'rsync://rsync.osuosl.org/ros_wiki_mirror/'
  rsync_filter_list = ['P /doc']

