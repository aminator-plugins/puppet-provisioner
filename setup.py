from setuptools import setup, find_packages
setup(
    name = "TEMPLATE",
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', ),

    # data_files = [
    #     ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.puppet.yml']),
    # ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'puppet = aminatorplugins.provisioner.puppet:PuppetProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "Rob Sweet",
    author_email = "rob@ldg.nt",
    description = "Puppet provisioner for Netflix's Aminator",
    license = "Apache 2.0",
    keywords = "aminator plugin puppet",
)
