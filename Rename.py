from pathlib import Path
import uuid
import sys
#same for any file extension.
def main():
    cwd = Path.cwd()
    jpeg_files = sorted([p for p in cwd.iterdir() if p.is_file() and p.suffix.lower() == ".jpeg"])

    if not jpeg_files:
        print("No .jpeg files found in the current directory.")
        return

    print(f"Found {len(jpeg_files)} .jpeg files. Renaming to 1.jpeg ... {len(jpeg_files)}.jpeg")
    temp_paths = []
    try:
        for original in jpeg_files:
            tmp_name = f".tmp_{uuid.uuid4().hex}"
            tmp_path = cwd / tmp_name
            original.rename(tmp_path)
            temp_paths.append(tmp_path)
            print(f"Temp-renamed: {original.name} -> {tmp_path.name}")
    except Exception as e:
        print("Error during temp rename:", e)
        print("Attempting to abort (no further changes).")
        sys.exit(1)
    try:
        for i, tmp in enumerate(temp_paths, start=1):
            final = cwd / f"{i}.jpeg"
            if final.exists():
                print(f"Removing existing file with target name: {final.name}")
                final.unlink()
            tmp.rename(final)
            print(f"Renamed: {tmp.name} -> {final.name}")
    except Exception as e:
        print("Error during final rename:", e)
        print("You may need to inspect the directory to resolve partially-completed renames.")
        sys.exit(1)

    print("Done.")

if __name__ == "__main__":
    main()
