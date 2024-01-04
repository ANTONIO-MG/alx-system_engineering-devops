# Install flask vi pip3  using Puppet

exec { 'install pip':
  command => '/usr/bin/apt-get install pip'
}

exec { 'install Flask':
  command => '/usr/bin/pip3 install flask'
}

package { 'pip':
  ensure => 'installed',
  before => Exec['install pip']
}

package { 'Flask':
  ensure  => 'installed',
  before  => Exec['install flask'],
  require => Package['pip']
}
