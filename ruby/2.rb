class Myclass
    attr_accessor :hoge, :fuga # 可変長引数なので複数定義可
    def initialize
        puts "init"
    end
    #initializeに書いた内容は、初期化時に実行される。ここには普通はself.ってやつを書く
end

my_instance = Myclass.new

class MyClass_1
    def self.class_method_a
        puts "self.class_method_a"
    end

    class << self
        def class_method_b
            puts "class_method_b"
        end 
        def class_method_c
            puts "class_method_c"
        end
    end
end

#クラスの継承
"""
通常、サブクラスはスーパークラスのインスタンスメソッド、クラスメソッドのみを継承する
ただ、インスタンスメソッド(intialize)の中で定義されているものについては継承が可能
これは、freezeした場合でも上書きされる
"""

#class SuperClass
 #   attr_accessor :name
  #  def initialize
   #     name = "init"
    #end
#end

#class MyClass_2 < SuperClass
 #   def greet(name)
  #      super
   #     return "#{name}"
    #end
#end
#myclasser = MyClass_2.new
#puts myclasser.greet

#スーパークラスを指定していない場合は、objectクラスが自動的に決定される


class Foo
    def foo(arg=nil)
        p arg
    end
end

class Bar < Foo
    def foo(arg)
        super(arg)
    end
end
Bar.new.foo 5

#ネスト
class MyClass_3
    class SweetMyClass
    end
end

MyClass_3.new
MyClass_3::SweetMyClass.new