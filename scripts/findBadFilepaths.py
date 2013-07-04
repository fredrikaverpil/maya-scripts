# This script searches all nodes for filepaths which begin with C:, R: or X: ...

import maya.cmds as cmds


def findFirstMatchInString(list, text):
	for part in list:
		if (part in text):
			return True # Found match
	return False # Did not find match


errors = 0

# Start out with ALL nodes possible
nodeTypes = cmds.allNodeTypes()
nodeTypesFiltered = []
# Remove the following node types
nodeTypes.remove('objectFilter')
nodeTypes.remove('objectMultiFilter')
nodeTypes.remove('objectNameFilter')
nodeTypes.remove('objectScriptFilter')
nodeTypes.remove('objectTypeFilter')
nodeTypes.remove('containerBase')
nodeTypes.remove('mesh')
nodeTypes.remove('reference')
nodeTypes.remove('deleteComponent')
nodeTypes.remove('VRayMtl')
nodeTypes.remove('transform')
for nodeType in nodeTypes:
	if findFirstMatchInString(['poly', 'container', 'object', 'reference','VRayMtl', 'transform', 'mesh', 'component', 'group', 'nurbs', 'curve', 'motionPath', 'offset', 'selection'], nodeType):
		#print 'Skipping ' + nodeType + ' from nodeTypes...'
		pass
	else:
		nodeTypesFiltered.append(nodeType)



#with open("c:/filepathDebug.txt", "a") as myfile:
#	myfile.truncate()

#for nodeType in nodeTypes:
for nodeType in nodeTypesFiltered:
	#with open("c:/filepathDebug.txt", "a") as myfile:
	#	myfile.write(str(nodeType) + '\n')
	#print nodeType # USE THIS TO IDENTIFY ERROROUS QUERIES
	nodes = cmds.ls(type=nodeType)
	for node in nodes:
		attributes = cmds.listAttr(node, write=True, hasData=True )
		for attribute in attributes:
			try:
				if findFirstMatchInString(['C:', 'R:', 'X:'], cmds.getAttr(node+'.'+attribute) ):
					print 'Found invalid drive letter in : ' + cmds.getAttr(node+'.'+attribute)
					errors += 1
			except:
				pass

print '\n-------Summary -------'
print 'Found ' + str(len(nodeTypes)) + ' possible node types.'
print 'Found ' + str(len(nodes)) + ' nodes in scene.'
print 'Found ' + str(errors) + ' invalid filepaths.'
