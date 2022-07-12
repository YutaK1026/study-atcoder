class SuperMyClass
    def initialize
        name = "init"
        #nameの初期化、初期化するだけ　そんだけ
        @superVar = "init"
    end
    def greet(name)
        puts "#{name}"
    end
end
class MyClass < SuperMyClass
    def greet(name)
        super
    end
end
MyClass.new.greet("やぁ")
"""
こういう感じに、superclassの同名のメソッドと同じ処理を行ってくれるみたい
"""

foo = MyClass.new
foo.greet("こんにちは")
"""
fooという変数に、MyClassを定義出来た
"""
