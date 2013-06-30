import os, sys, subprocess
 
# Settings
windows = 'X:' # The server share's drive letter
osx = '/Volumes/include' # The server's volume mount
buildsLocation = '/bin/vray/builds/' # The server path without drive letter or mounted volume/share.
buildFolderName = 'maya2012_vray22001' # The name of the build folder, containing the maya_root, maya_vray, vray folders and the source.mel file.
 
 
 
# Determine drive letter or mount and then kill any running instances of the vray slave
volume = ''
if(sys.platform == 'win32'):
	volume = windows
	# Kill any already running instances of vray daemon
	command = "TASKKILL /F /IM \"vray.exe\""
	os.system(command)
	command = "TASKKILL /F /IM \"vrayspawner.exe\""
	os.system(command)
elif(sys.platform == 'darwin'):
	volume = osx
	output = ''
	proc=subprocess.Popen("ps -clx | grep 'vray.exe' | awk '{print $2}' | head -1", shell=True, stdout=subprocess.PIPE, ) # Find any running processes of vray with: ps aux | grep vray.exe | grep -v grep
	output=proc.communicate()[0]
	if (str(output) != ''):
		try:
			os.system( 'kill -9 ' +  output)
			print('Killed already running V-Ray Slave process with ID ' + str(output))
		except:
			print('Failed to kill already running V-Ray Slave process with ID ' + str(output))
 
 
# Launch slave
if(sys.platform == 'win32'):
	command = "C:\\Windows\\System32\\cmd.exe /C start " + volume + buildsLocation + buildFolderName + "\\maya_vray\\bin\\vray.exe -server -portNumber=20207"
elif(sys.platform == 'darwin'):
	os.environ['DYLD_LIBRARY_PATH'] = volume + buildsLocation + buildFolderName + '/maya_vray/lib'
	command = volume + buildsLocation + buildFolderName + '/maya_vray/bin/vray $* -portNumber=20207 -server'
	subprocess.Popen( command , shell=True, stdout=subprocess.PIPE)