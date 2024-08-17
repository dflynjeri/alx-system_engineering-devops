#0-create_a_file.pp
#The code will create a file name school inside the /tmp directory
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
