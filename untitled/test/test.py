import sys,ldap,ldap.asyncsearch

s = ldap.asyncsearch.LDIFWriter(
  ldap.initialize('ldap://10.20.2.6:389'),
  sys.stdout
)

s.startSearch(
  'dc=mypaas'
  ',dc=com',
  ldap.SCOPE_SUBTREE,
  '(objectClass=*)',
)

try:
  partial = s.processResults()
except ldap.SIZELIMIT_EXCEEDED:
  sys.stderr.write('Warning: Server-side size limit exceeded.\n')
else:
  if partial:
    sys.stderr.write('Warning: Only partial results received.\n')

sys.stderr.write(
  '%d results received.\n' % (
    s.endResultBreak-s.beginResultsDropped
  )
)