def comparePluralForms(a, b):
  pass
  
def comparePluralPropers(a,b):
  if(a == b + 's'):
    return True
  if(a + 's' == b):
    return True
  return False
