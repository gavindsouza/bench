import os
from bench.utils import exec_cmd

def execute(bench_path):
	exec_cmd('curl --compressed -o- -L https://yarnpkg.com/install.sh | bash', os.path.join(bench_path, 'apps/frappe'))