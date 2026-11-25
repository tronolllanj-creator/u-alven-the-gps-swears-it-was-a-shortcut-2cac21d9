"""
GPS excuse: 1-200 chars, single line, plain text, UTF-8.
"""
import os
import sys

# The GPS's excuse line.
LINE = "I told the map the lake was a shortcut; it blamed the duck for the detour."

def main() -> int:
    # Resolve output directory from environment or default.
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    # Ensure the directory exists.
    os.makedirs(out_dir, exist_ok=True)
    # Build the full output path.
    out_path = os.path.join(out_dir, 'entry.txt')
    # Write the line plus a single trailing newline, UTF-8 encoded.
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(LINE + '\n')
    # Also print to stdout for visibility.
    print(LINE)
    print("chars: %d" % len(LINE), file=sys.stderr)
    return 0

if __name__ == '__main__':
    sys.exit(main())
