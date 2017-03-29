def decla_te(*decla)
    puts "The number of parameters is #{ decla.length}"
    for i in 0... decla.length
        puts "The parameter is #{ decla [i]}"
    end
end
decla_te "Zara", "6", "F"
decla_te "Mac", "36", "M", "MCA"
