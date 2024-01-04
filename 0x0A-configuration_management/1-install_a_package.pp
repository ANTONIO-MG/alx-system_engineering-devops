# Install flask vi pip3  using Puppet

exec { 'install pip3':
  command => '/usr/bin/apt-get install -y python3-pip'
}

exec { 'install Flask':
  command => '/usr/bin/pip install Flask'
}

package { 'pip':
  ensure => 'installed',
  before => Exec['install pip']
}

package { 'Flask':
  ensure  => 'installed',
  before  => Exec['install Flask'],
  require => Package['pip']
}
