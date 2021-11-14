# shell out to swift-demangle to handle swift symbol names 
#
import subprocess
result = subprocess.run(['/usr/bin/xcrun', '--find', 'swift-demangle'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
if result.returncode == 0:
	demangle_str = result.stdout.decode('utf-8')
	for f in bv.functions:
		result = subprocess.run([demangle_str, '-simplified', '-compact', symbol], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
		if result.returncode == 0:
			f.name = demangle(f.name)
else:
	log_error('Unable to find swift-demangle.')