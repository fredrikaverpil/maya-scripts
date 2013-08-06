import os
import sys
 
# Settings
windows = 'X:' # The mounted server share's drive letter
osx = '/Volumes/include' # The server's volume mount
buildsLocation = '/bin/vray/builds/' # The server path without drive letter or mounted volume/share.
buildFolderName = 'maya2012_vray22001' # The name of the build folder, containing the maya_root, maya_vray, vray folders and the source.mel file.
buildMayaVersion = '2012' # The version of Maya which the V-Ray plug-in has been compiled for.
licenseLocation = '/bin/vray/license/' # The location of the XML license file
 
 
 
# Detect OS and determine drive letter (win) or mount (mac)
volume = ''
if(sys.platform == 'win32'):
	volume = windows
elif(sys.platform == 'darwin'):
	volume = osx
 
# Set (and reset) environment variables which may not have already been set...
try:
	print(os.environ['MAYA_SCRIPT_PATH'])
except KeyError:
	os.environ['MAYA_SCRIPT_PATH'] = ''
try:
	print(os.environ['MAYA_PLUG_IN_PATH'])
except KeyError:
	os.environ['MAYA_PLUG_IN_PATH'] = ''
 
# Set environment variables
if(sys.platform == 'win32'):
	print('Setting Windows environment variables...')
	os.environ['MAYA_RENDER_DESC_PATH'] = volume + buildsLocation + buildFolderName + '/maya_root/bin/rendererDesc'
	os.environ['VRAY_FOR_MAYA' + buildMayaVersion + '_MAIN_x64'] = volume + buildsLocation + buildFolderName + '/maya_vray'
	os.environ['VRAY_FOR_MAYA' + buildMayaVersion + '_PLUGINS_x64'] = volume + buildsLocation + buildFolderName + '/maya_vray/vrayplugins'
	os.environ['VRAY_AUTH_CLIENT_FILE_PATH'] = volume + licenseLocation
	os.environ['PATH'] = os.environ['PATH'] + ';' + volume + buildsLocation + buildFolderName + '/maya_root/bin'
	os.environ['MAYA_PLUG_IN_PATH'] = os.environ['MAYA_PLUG_IN_PATH'] + ';' + volume + buildsLocation + buildFolderName + '/maya_vray/plug-ins'
	os.environ['MAYA_SCRIPT_PATH'] = os.environ['MAYA_SCRIPT_PATH'] + ';' + volume + buildsLocation + buildFolderName + '/maya_vray/scripts'
	os.environ['XBMLANGPATH'] = volume + buildsLocation + buildFolderName + '/maya_vray/icons/%B' + ';' + volume + buildsLocation + buildFolderName + '/maya_vray/icons/'
	os.environ['VRAY_PATH'] = volPipeline + vrayBaseLocation + buildName + '/maya_vray/bin'
	os.environ['VRAY_TOOLS_MAYA' + buildMayaVersion + '_x64'] = volPipeline + vrayBaseLocation + buildName + '/vray/bin'
elif(sys.platform == 'darwin'):
	print('Setting OS X environment variables...')
	os.environ['MAYA_RENDER_DESC_PATH'] = volume + buildsLocation + buildFolderName + '/maya_root/bin/rendererDesc'
	os.environ['VRAY_FOR_MAYA' + buildMayaVersion + '_MAIN_x64'] = volume + buildsLocation + buildFolderName + '/maya_vray'
	os.environ['VRAY_FOR_MAYA' + buildMayaVersion + '_PLUGINS_x64'] = volume + buildsLocation + buildFolderName + '/maya_vray/vrayplugins'
	os.environ['VRAY_AUTH_CLIENT_FILE_PATH'] = volume + '/bin/vray/license'
	os.environ['PATH'] = os.environ['PATH'] + ':' + volume + buildsLocation + buildFolderName + '/maya_root/bin'
	os.environ['PATH'] = os.environ['PATH'] + ':' + volume + buildsLocation + buildFolderName + '/maya_vray/bin'
	os.environ['PATH'] = os.environ['PATH'] + ':' + volume + buildsLocation + buildFolderName + '/vray/bin'
	os.environ['MAYA_PLUG_IN_PATH'] = os.environ['MAYA_PLUG_IN_PATH'] + ':' + volume + buildsLocation + buildFolderName + '/maya_vray/plug-ins'
	os.environ['MAYA_SCRIPT_PATH'] = os.environ['MAYA_SCRIPT_PATH'] + ':' +volume + buildsLocation + buildFolderName + '/maya_vray/scripts'
	os.environ['XBMLANGPATH'] = volume + buildsLocation + buildFolderName + '/maya_vray/icons/%B' + ':' + volume + buildsLocation + buildFolderName + '/maya_vray/icons/'
	os.environ['VRAY_PATH'] = volPipeline + vrayBaseLocation + buildName + '/maya_vray/bin'
	os.environ['VRAY_TOOLS_MAYA' + buildMayaVersion + '_x64'] = volPipeline + vrayBaseLocation + buildName + '/vray/bin'
	os.environ['DYLD_LIBRARY_PATH'] = volume + buildsLocation + buildFolderName + '/maya_root/MacOS/'
 
# Source the three MEL files
sourceStatement = "-script " + volume + buildsLocation + buildFolderName + "/source.mel"
 
# Set up OS-specific exec command
if(sys.platform == 'win32'):
	command = "\"C:/Program Files/Autodesk/Maya" + buildMayaVersion + "/bin/maya.exe\" " + sourceStatement
elif(sys.platform == 'darwin'):
	command = '/Applications/Autodesk/maya' + buildMayaVersion + '/Maya.app/Contents/bin/maya ' + sourceStatement
 
# Launch Maya
os.system(command)
