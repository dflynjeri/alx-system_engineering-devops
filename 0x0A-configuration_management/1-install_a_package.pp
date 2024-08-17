# 1-install_a_package.pp
# This code will install the package puppet-lint
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
