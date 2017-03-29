$LOAD_PATH << '.'

require "support"

class Decade
  include Week
  no_of_yrs = 10
  def no_of_months
    puts Week::FIRST_DAY
    number = 10 * 12
    puts number
  end
end

puts Week::FIRST_DAY
Week.weeks_in_month
Week.weeks_in_year
