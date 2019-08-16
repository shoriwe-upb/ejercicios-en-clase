def main
  arguments = ARGV
  if arguments.length <= 1
    puts "numero-mayor.rb number1 number2[number3][numberN]"
  else
    max_n = 0
    arguments.each_index do |index|
      if arguments[max_n].to_f < arguments[index].to_f
        max_n = index
      end
    end
    puts arguments[max_n]
  end
end

main
