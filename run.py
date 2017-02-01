#run.py

import subprocess


if __name__ == '__main__':

	import os
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"app.py")
	
	subprocess.call(["python", path])