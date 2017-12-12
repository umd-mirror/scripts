from . import RsyncMirrorRunner

class LinuxMintPackagesMirrorRunner(RsyncMirrorRunner):
  source = 'rsync://rsync-packages.linuxmint.com/packages/'

  base_subdir = 'linuxmint/packages'

  rsync_filter_list = ['- /*.sh', '- /*.php', '- /*.php.old']

  rsync_delete_delay = True
  rsync_delay_updates = True

