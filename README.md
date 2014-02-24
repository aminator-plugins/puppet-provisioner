# Puppet Provisioner for Aminator
*Based on initial work by Archie Cowan.*

## Installation

First, install Aminator. Then install the Puppet provisioner for Aminator:

```
sudo aminator-plugin install puppet
```

Then you will need to make add an environment that uses the Puppet provisioner to your `/etc/aminator/environments.yml` file. For example:

```
    ec2_puppet_debian:
        cloud: ec2
        distro: debian
        provisioner: puppet
        volume: linux
        blockdevice: linux
        finalizer: tagging_ebs

    ec2_puppet_redhat:
        cloud: ec2
        distro: redhat
        provisioner: puppet
        volume: linux
        blockdevice: linux
        finalizer: tagging_ebs
```

## Accepted arguments

```
--puppet-env-vars - Extra arguments for Puppet.  Can be used to include a Puppet class with -e.

--puppet-args - Extra arguments for Puppet.  Can be used to include a Puppet class with -e.

--puppet-master - Hostname of Puppet Master

--puppet-certs-dir - Used when generating/copying certs for use with Puppet Master

--puppet-private-keys-dir - Used when generating/copying certs for use with Puppet Master
```

## Usage with a Master

### Basic

```
sudo aminate -B ami-35792c5c some-host.domain.com
```

Puppet will use the default hostname 'puppet' to try to talk to the Puppet Master server and generate certs with the name in the last argument.


### Master specified

```
sudo aminate -B ami-35792c5c --puppet-master=puppet-master.domain.com some-host.domain.com
```

Puppet will use the specified hostname to try to talk to the Puppet Master server and generate certs with the name in the last argument.


## Usage Masterless


### Masterless with one manifest

```
sudo aminate -B ami-35792c5c /full/path/to/some_manifest.pp
```

Aminator will look at the last argument and try to find that file.  If it does, Aminator will assume that you want to run Puppet in Masterless mode (apply) and will pass in the specified manifest.


### Masterless with modules

```
sudo aminate -B ami-35792c5c /full/path/to/my_manifest_tarball.tgz
```

Aminator will untar the manifests to /etc/puppet/modules (or /etc/puppet if the tarball contains a modules directory) and run Puppet apply.


### Masterless passing custom facts

```
sudo aminate -B ami-35792c5c --puppet-env-vars="FACTER_my_fact=some_value; FACTER_fact2=value2" /full/path/to/my_manifest_tarball.tgz
```

Aminator will add the specified variables to the environment for Puppet runs.  The most obvious use for this is to pass custom facts to Puppet that are used in the Puppet manifests.  Pairs are delimited by semi-colon.


### Masterless with modules and arguments for the apply

```
sudo aminate -B ami-35792c5c --puppet-args="-e 'include my_module::my_class'" /full/path/to/my_manifest_tarball.tgz
```

Aminator will untar the manifests and run Puppet apply, passing the contents of puppet_args in the commandline.

