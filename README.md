# Mirror Scripts

These are the Python scripts that run the [University of Maryland's Free Software Mirror](https://mirror.umd.edu/).

The mirror server is generously hosted by the University of Maryland [Division of Information Technology](https://it.umd.edu/) in their colocation space on campus.
It is connected to the campus backbone with dual 10Gig fiber connections.

Check out our traffic stats at the bottom of our home page, linked above.

## Adding a new mirror

1. Storage

```sh
zfs create pool/mirrors/NAME
cd /home/mirror/web/
ln -s /pool/mirrors/NAME/ NAME
chown mirror:mirroradmin /pool/mirrors/NAME
```

2. Add a script in the `mirror` directory (based on an existing script).

3. Add a job in Jenkins to run the script on a schedule.

4. Add a table entry and a new entry in the [website](https://github.com/umd-mirror/web).

5. Add an rsync module in the rsyncd configuration.
