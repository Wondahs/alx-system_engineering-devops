#!/usr/bin/env ruby

# Read input
input = ARGV[0]

# Set pattern
regex = /hbt{2,5}n/

# Return result
result = input.scan(regex)
puts result.join
