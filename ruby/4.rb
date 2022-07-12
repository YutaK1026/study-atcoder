hash = {} #=> {}
hash.class #=> Hash

hash1 = { "key1" => "value1", "key2" => "value2" } # => {"key1"=>"value1", "key2"=>"value2"}
puts hash1.class #=> Hash

# シンボルをキーとしたhashの宣言
hash2 = { :key1 => "value1", :key2 => "value2" } # => {:key1=>"value1", :key2=>"value2"}
hash2.class #=> Hash

hash3 = { key1: "value1", key2: "value2"} # => {:key1=>"value1", :key2=>"value"
hash3.class #=> Hash

with_default_value_hash = Hash.new("default!!!") # => {}
# :keyで得られるデフォルト値に対して、upcase!で大文字化した場合。。。
with_default_value_hash[:key].upcase! # => "DEFAULT!!!"
# :key2で得られるのがデフォルト値だった場合、upcase!で破壊された値となる
with_default_value_hash[:key2] # => "DEFAULT!!!"
"""
defaultの値を設定しなければ、nilが返ってくる
ただ、default設定を、ブロックを用いないで記述すると
　upcase!で値を破壊されかねない
解決策は以下の通り
"""

with_protected_default_value_hash = Hash.new { "default!!!" } # => {}
with_protected_default_value_hash[:key].upcase! # => "DEFAULT!!!"
with_protected_default_value_hash[:key2] # => "default!!!"
"""
{}で囲うことで、それがブロックになって保護される
"""