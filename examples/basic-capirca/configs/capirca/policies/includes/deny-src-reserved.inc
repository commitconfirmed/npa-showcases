term deny-from-reserved {
  comment:: "Deny Reserved IPs"
  source-address:: RESERVED
  action:: deny
}