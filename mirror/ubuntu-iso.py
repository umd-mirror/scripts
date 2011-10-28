from . import MirrorRunner

class UbuntuISOMirrorRunner(MirrorRunner):
  #source = 'rsync://rsync.releases.ubuntu.com/releases/'
  #source = 'rsync://rsync.gtlib.gatech.edu/ubuntu-releases/'
  #source = 'rsync://mirror.lstn.net/ubuntu-releases/'
  source = 'rsync://mirrors.rit.edu/ubuntu-releases/'

  rsync_delete = False

#SRV1=rsync://ubuntu.osuosl.org/ubuntu-releases
#SRV2=rsync://rsync.releases.ubuntu.com/releases/
#SRV3=rsync://mirrors.rit.edu/ubuntu-releases/
#SRV4=rsync://www.club.cc.cmu.edu/ubuntu-iso/CDs/
#SRV5=rsync://lug.mtu.edu/ubuntu-releases/
#SRV6=rsync://mirror.anl.gov/ubuntu-iso/CDs/
#SRV7=rsync://mirrors.login.com/ubuntu-iso/
#SRV8=rsync://archive.ubuntu.com/ubuntu-iso/
#SRV9=rsync://se.archive.ubuntu.com/ubuntu-releases/

#$RSYNC $STOPTS $SRV2 $BASE/ubuntu-iso --partial --exclude='*-alpha*' --delete-excluded
