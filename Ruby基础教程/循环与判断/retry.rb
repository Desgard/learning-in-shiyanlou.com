n = 0
begin 
  puts 'Try to do something'
  raise 'oops'

rescue => ex
  puts ex
  n += 1
  retry if n < 3
end 

puts "OK, I give up"

