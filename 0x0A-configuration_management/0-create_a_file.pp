-- puppet configuration file the creates a file on a agent
file {'/tmp/school':
  ensure => present,
  content => 'I love Puppet.',
  mode => '0744',
  owner => 'www-data', 
  group => 'www-data',
}
