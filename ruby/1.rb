puts "Hello"

puts 37
puts 2+2
puts 16%3

puts "プログラミング言語は"+"Pythonではありません"

name = "じょｎ"
number = 3
puts "名前は#{name}です"

score = 90
if score > 100
    puts "合格"
else
    puts "不合格ですよ奥さん"
end

names = ["Yamada","SUzuki"]
puts names[1]

languages = ["日本語", "英語", "スペイン語"]
languages.each do |language|
  puts "#{language}を話せます"
end

exam = {"subject" => "Math","score" => 90}
puts exam["subject"]
exam["score"] = 100
puts exam["score"]

def introduce(nam)
    puts "私の名前は#{nam}です。"
end

introduce("おはよう")


class Menu
    attr_accessor :name
    attr_accessor :price
    def info
        puts"料理名と価格が表示されます"
        return "#{self.name} #{self.price}"
    end
end
menu1 = Menu.new
menu1.name = "ピザ"
menu1.price = 800
puts menu1.info
