import pathlib
import random
import re

root_path = pathlib.Path(__file__).parent.resolve()
readme_path = root_path / 'README.md'

readme = readme_path.open().read()
r = re.compile(r"dummyresetter1=\d\d\d")
readme_path.open('w').write(r.sub("dummyresetter1="+str(random.randint(100,999)),readme))

readme = readme_path.open().read()
r = re.compile(r"dummyresetter2=\d\d\d")
readme_path.open('w').write(r.sub("dummyresetter2="+str(random.randint(100,999)),readme))