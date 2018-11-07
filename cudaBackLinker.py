import os
import argparse
import re

def main():
	parser = argparse.ArgumentParser(description = 'Symlinks cuda 10 files to cuda 9')
	parser.add_argument('cudaPath', metavar='/path/to/cuda/lib64', nargs=1, help='The path to the cuda directory, usually /usr/local/cuda/lib64 but ymmv.')
	args = parser.parse_args()

	files = [f for f in os.listdir(args.cudaPath[0]) if re.match(r'lib[a-z]*.so.10.0(.[0-9]*)*', f)]
	for f in files:
		os.symlink(f, (f.replace('.10', '.9', 1)))

if __name__ == "__main__":
	main()