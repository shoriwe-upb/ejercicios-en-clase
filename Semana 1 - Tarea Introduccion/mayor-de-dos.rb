def main()
  # Require for the first value
  print "Number a:"
  a = gets.strip.to_f

  # Require for the second value
  print "Number b:"
  b = gets.strip.to_f

  if a > b
    puts "a is greater"
  elsif a < b
    puts "b is greater"
  else
    puts "Both are equal"
  end

end

main