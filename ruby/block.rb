"""
ブロックとはなんぞや

"""


array = [1,2,3]
array.each do |i|
  p i
end
#=> 1
#   2
#   3

# mapの例
array = [1,2,3]
double_array = array.map do |n|
  n * 2
end
# => [2, 4, 6]