arr = ["a", "b", "c", "d", "e", "f"]

def test(words)
  for x in words do 
    throw :hello,1 if x == "d"
    print x

  end
end

catch :hello do
  test(arr)
end
