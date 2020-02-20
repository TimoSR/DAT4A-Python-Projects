import sys

if __name__ == '__main__':
    input_lines = sys.stdin.read().split('\n')
    output_lines = reversed(input_lines)
    output_str = '\n'.join(output_lines)
    sys.stdout.write(output_str)