#!/usr/bin/env ruby

numbers = (1..999).to_a
numbers.select! { |number| (number % 3 == 0 || number % 5 == 0) }
puts numbers.inject { |sum, x| sum + x }
