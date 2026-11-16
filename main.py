import os
import shutil
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent
    src_file = base_dir / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dst_file = out_dir / "entry.png"

    shutil.copyfile(src_file, dst_file)
    src_size = src_file.stat().st_size
    dst_size = dst_file.stat().st_size
    if src_size != dst_size:
        raise SystemExit(f"Error: byte size mismatch between source ({src_size} bytes) and destination ({dst_size} bytes)")

    print(f"Wrote {dst_size} bytes to {dst_file}")

if __name__ == "__main__":
    main()
