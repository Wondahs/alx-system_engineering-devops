#!/usr/bin/env ruby

# Read input
input = ARGV[0]

# Set pattern
regex = /^\d{10}$/

# Return result
result = input.scan(regex)
puts result.join
