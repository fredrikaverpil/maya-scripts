# This script collects any texture files from a shader into a textures folder, residing next to the .ma

import os, sys, re, shutil

volResurser = '//192.168.0.230/Resurser'
shadersDir = os.path.dirname(__file__).replace('R:',volResurser).replace('r:',volResurser)


folderContents = os.walk( shadersDir )
for item in folderContents:
	for filename in item[2]:
		if ('.ma' in filename) and (not '.swatch' in filename) and (not '_collected.ma' in filename):

			folder = item[0]
			mayascene = filename
			print '\nChecking ' + mayascene + '...'


			# Create textures folder if it does not exist
			if not os.path.exists( os.path.join(shadersDir, folder, 'textures') ):
				print 'Creating textures folder folder in ' + folder
				os.makedirs( os.path.join(shadersDir, folder, 'textures') )

			# Traverse through maya scene for filepaths
			if '.ma' in mayascene:
				infile = open( os.path.join(shadersDir, folder, mayascene), 'r')
				outfile = open( os.path.join(shadersDir, folder, mayascene.replace('.ma','_collected.ma')), 'w')
				
				for line in infile:
					if ( 'p:/' in line.lower() ) or ( 'r:/' in line.lower() ) or ( 'x:/' in line.lower() ) or ( 'c:/' in line.lower() ):
						# Copy texture file
						textureFileSrc = line[ line.rfind('"string"')+10 : -3]
						textureFileBasename = os.path.basename( textureFileSrc )
						textureFileDst = os.path.join(shadersDir, folder, 'textures', textureFileBasename)
						if not os.path.exists( os.path.join(shadersDir, folder, 'textures', textureFileBasename) ):
							print 'Copying ' + textureFileSrc + ' to ' + textureFileDst + ' ...'
							shutil.copyfile( textureFileSrc, textureFileDst )
						

						# Replace string in maya scene
						newLine = line[ : line.rfind('"string"')+10]
						newLine = newLine + textureFileDst.replace('\\','/') + '";\n'
						line = newLine

					# Write new .ma file with rerouted texture paths
					outfile.write(line)

				infile.close()
				outfile.close()


				# Delete original .ma file
				try:
					os.remove( os.path.join(shadersDir, folder, mayascene) )
				except:
					print 'Warning: Unable to delete old maya scene file.'

				# Rename new .ma file
				try:
					os.rename( os.path.join(shadersDir, folder, mayascene.replace('.ma','_collected.ma')), os.path.join(shadersDir, folder, mayascene) )
				except:
					print 'Warning: Unable to rename newly created maya scene file.'


print '\nDone!'
