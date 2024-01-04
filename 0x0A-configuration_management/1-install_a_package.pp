# Install flask vi pip3  using Puppet

exec { 'install pip3':
  command => '/usr/bin/apt-get install -y python3-pip'
}

exec { 'install flask':
  command => '/usr/bin/gem install puppet-lint -v 2.1.1'
}

package { 'pip':
  ensure => 'installed',
  before => Exec['install pip']
}

package { 'flask':
  ensure  => 'installed',
  before  => Exec['install flask'],
  require => Package['pip']
}
