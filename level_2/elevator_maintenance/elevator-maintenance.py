from functools import cmp_to_key

def solution(l):
  result = l.copy()
  result = map(lambda i: Version(i), result)
  result = sorted(result, key=cmp_to_key(cmpVer))
  result = map(lambda v: v.versionString, result)
  return list(result)

class Version:
  def __init__(self, versionString):
    self.versionString = versionString
    self.major = 0
    self.minor = 0
    self.revision = 0

    parts = versionString.split('.')
    self.PartsCount = len(parts)

    if self.PartsCount == 3:
      self.major = int(parts[0])
      self.minor = int(parts[1])
      self.revision = int(parts[2])
    elif self.PartsCount == 2:
      self.major = int(parts[0])
      self.minor = int(parts[1])
    else:
      self.major = int(parts[0])

def cmpVer(x, y):
  if x.major < y.major:
    return -1
  elif x.major > y.major:
    return 1
  elif x.minor < y.minor:
    return -1
  elif x.minor > y.minor:
    return 1
  elif x.revision < y.revision:
    return -1
  elif x.revision > y.revision:
    return 1
  else:
    return x.PartsCount - y.PartsCount


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
# Output:
#     0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
# Output:
#     1.0,1.0.2,1.0.12,1.1.2,1.3.3