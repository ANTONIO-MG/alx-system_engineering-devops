# puppet configuration file the creates a file on a agent
file {'/tmp/school':
  ensure  => present, # ensures the file is presnet or creates one
  content => 'I love Puppet.', # writes the content to teh file
  mode    => '0744', # sets the permissions of the file
  owner   => 'www-data', # sets the owner of the file
  group   => 'www-data', # sets the group persmission
}
