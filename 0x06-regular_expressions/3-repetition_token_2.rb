#!/usr/bin/env ruby

# Read input
input = ARGV[0]

# Set pattern
regex = /hbt+n/

# Return result
result = input.scan(regex)
puts result.join
