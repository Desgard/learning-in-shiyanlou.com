$i = 0
$num = 3
puts "begin while"

while $i < $num do
  puts("Inside the loop(while) i = #$i")
  $i += 1
end

puts "end while"

$i = 0
puts("Inside the loop(do while) i = #$i")

begin 
  puts("Inside the loop(do while) i = #$i")
  $i += 1
end while $i < $num

puts "end do while"

