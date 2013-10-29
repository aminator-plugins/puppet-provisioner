# Puppet Provisioner for Aminator

## Usage

### Basic

```
aminate -B ami-35792c5c some-host.domain.com
```

Puppet will use the default hostname 'puppet' to try to talk to the Puppet Master server and generate certs with the name in the last argument.



### Masterless with one manifest

```
aminate -B ami-35792c5c /full/path/to/some_manifest.pp
```

Aminator will look at the last argument and try to find that file.  If it does, Aminator will assume that you want to run Puppet in Masterless mode (apply) and will pass in the specified manifest.


### Masterless with modules

```
aminate -B ami-35792c5c /full/path/to/my_manifest_tarball.tgz
```

Aminator will untar the manifests to /etc/puppet/modules (or /etc/puppet if the tarball contains a modules directory) and run Puppet apply.


### Masterless with modules and arguments for the apply

```
aminate -B ami-35792c5c --puppet-args="-e 'include my_module::my_class'" /full/path/to/my_manifest_tarball.tgz
```

Aminator will untar the manifests and run Puppet apply, passing the contents of puppet_args in the commandline.

