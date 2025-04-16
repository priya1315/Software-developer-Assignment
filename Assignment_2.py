import os
import re
from pathlib import Path
import shutil


# SCONSTRUCT file interesting lines
# config.version = Version( # major=15, # minor=0, # point=6, # patch=0 #)

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6

def update_buildnum(filename: str, pattern_str: str, replacement: str):
    source_path = os.environ.get("SourcePath")
    build_num = os.environ.get("BuildNum")
    if not source_path or not build_num:
        raise EnvironmentError("Please set 'SourcePath' and 'BuildNum' environment variable")
    file_path = Path(source_path) / "develop" / "global" / "src" / filename
    temp = file_path.with_name(f"{filename}.tmp")

    file_path.chmod(0o755)
    pattern = re.compile(pattern_str)
    updated = False

    with file_path.open("r") as fin, temp.open("w") as fout:
        for line in fin:
            updated_line = pattern.sub(f"{replacement}{build_num}", line)
            if updated_line != line:
                updated = True
            fout.write(updated_line)
        if not updated:
            raise ValueError(f"Could not find {pattern_str} in {filename}")

        shutil.move(str(temp), str(file_path))
        print(f"{filename} updated successfully with build number {build_num}")


def main():
    update_buildnum("SConstruct", r"point=\d+", "point=")
    update_buildnum("VERSION", r"ADLMSDK_VERSION_POINT=\d+", "ADLMSDK_VERSION_POINT=")


main()
