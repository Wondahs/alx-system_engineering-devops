#!/usr/bin/env ruby

# Read input
input = ARGV[0]

# Set pattern
regex = /\[(?:from:|to:|flags:)(.*?)\]/

# Return result
result = input.scan(regex)
puts result.join(",")
