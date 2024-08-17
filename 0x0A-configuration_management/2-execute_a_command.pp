# 2-execute_a_command.pp
# This Puppet manifest kills a process named 'killmenow' using pkill

exec { 'kill_killmenow':
  command   => '/usr/bin/pkill killmenow',
  provider  => 'shell',
  returns   =>  [0, 1],
}

