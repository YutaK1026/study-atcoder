array = []
array = [1,2,3]
(1..5).to_a
p array[0]
p "aaa"

array  = ["a","b","c","d"]
array[4] = "e"
array.push("f")
p array

array << "hoge"
p array

array = (1..5).to_a
array.insert(3,777)
p array

arrayA  = ["a", "b", "c"]
arrayB  = ["d", "e", "f"]
arrayA.concat(arrayB)
p arrayA

array  = ['ruby','javascript','php','python']
newArray = array.join(',')
p newArray
puts "#{newArray}"

array = (1..5).to_a
def map_test(array)
  array.map do |a|
    a*2
  end
end

newArray = map_test(array)
p newArray
p array