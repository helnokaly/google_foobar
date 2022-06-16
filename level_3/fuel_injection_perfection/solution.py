from collections import deque

class Binary:
  def __init__(self, n):
    self.data = [int(c) for c in bin(long(n))[2:]]
    self.data = deque(reversed(self.data))
  
  # count number of bits
  def bit_count(self):
    return len(self.data)
  
  # binary shift right
  # shift bits to the right
  def right_shift(self):
    return self.data.popleft()
  
  # adds one
  def add_one(self):
    index = 0
    while index < len(self.data):
      if self.data[index] == 0:
        self.data[index] = 1
        return
      else:
        self.data[index] = 0
      index += 1
    self.data.append(1)
  
  # subtracts one
  def sub_one(self):
    index = 0
    while index < len(self.data):
      if self.data[index] == 1:
        self.data[index] = 0
        for j in range(index - 1, -1, -1):
          self.data[j] = 1
        # delete right most trailing zeros
        while self.data[len(self.data) - 1] == 0:
          self.data.pop()
        return
      index += 1
    raise Exception("trying to subtracte from a zero number")

  # count the rightmost bits of 1
  # for example: 10111 -> 3
  def count_rightmost_ones(self):
    count = 0
    for index in range(0, len(self.data)):
      if self.data[index] == 1:
        count += 1
      else:
        break
    return count

# algorihtm description:
# convert the input number to a binary representation
# if rightmost bit is 0, right shift (equivalent to divide by 2 with zero remainder)
# else count rightmost bits of 1
#   if count == 1: subtract 1
#   else if count > 1 add 1
def solution(n):
  n_bin = Binary(n)
  op_count = 0
  while n_bin.bit_count() > 1:
    rightmost_ones = n_bin.count_rightmost_ones()

    # special case where my algorithm does not apply
    # if number is 3 it should go like this 3 -> 2 -> 1
    if rightmost_ones == 2 and n_bin.bit_count() == 2:
      op_count += 2
      break
    elif rightmost_ones == 0:
      n_bin.right_shift()
      op_count += 1
    elif rightmost_ones == 1:
      n_bin.sub_one()
      op_count += 1
    elif rightmost_ones > 1:
      n_bin.add_one()
      op_count += 1
  return op_count


# print(solution('78479437574375439758437589473857357934795'))
print(solution('3'))
# test2('78479437574375439758437589473857357934795')
# print(solution('7'))