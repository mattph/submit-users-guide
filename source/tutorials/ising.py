import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Example script.')

# Add arguments
parser.add_argument('--temperature', type=float, help='Temperature value')
parser.add_argument('--length', type=int, help='Length of the chain')
parser.add_argument('--steps', type=int, help='Number of Monte Carlo steps')

# Parse arguments
args = parser.parse_args()

# Use the arguments
print(f"Temperature: {args.temperature}, Length: {args.length}, Steps: {args.steps}")

