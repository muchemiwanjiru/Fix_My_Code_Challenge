# Convert command-line arguments to integers and sort them numerically
sorted_arguments = ARGV.map(&:to_i).sort

# Print the sorted arguments
sorted_arguments.each { |arg| puts arg }
