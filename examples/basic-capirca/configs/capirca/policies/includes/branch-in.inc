term permit-tcp-replies {
  option:: tcp-established
  protocol:: tcp
  action:: accept
}
term permit-quic-replies {
  source-port:: HTTP HTTPS
  protocol:: udp
  action:: accept
}
term permit-dns-replies {
  source-port:: DNS
  protocol:: udp
  action:: accept
}
term default-deny {
  action:: deny
}