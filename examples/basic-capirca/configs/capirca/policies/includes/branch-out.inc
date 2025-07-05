term permit-google-dns {
  destination-address:: GOOGLE_PUBLIC_DNS_ANYCAST
  destination-port:: DNS
  protocol:: tcp
  action:: accept
}
term permit-web-access {
  destination-address:: ANY
  destination-port:: HTTP HTTPS
  protocol:: tcp udp
  action:: accept
}
term default-deny {
  action:: deny
}