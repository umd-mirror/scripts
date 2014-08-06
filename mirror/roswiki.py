from . import RsyncMirrorRunner

class RosWikiMirrorRunner(RsyncMirrorRunner):
  base_subdir = 'ros-wiki'
  source = 'rsync://wiki.ros.org/wiki_mirror/'
  rsync_filter_list = ['P /doc']

