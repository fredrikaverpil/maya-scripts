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
nodeTypes.remove('polyTweakUV')
nodeTypes.remove('polySplitRing')
nodeTypes.remove('polySoftEdge')
nodeTypes.remove('polySmoothFace')
nodeTypes.remove('polyPlanarProj')
nodeTypes.remove('polyNormalizeUV')
nodeTypes.remove('polyNormal')
nodeTypes.remove('polyMoveVertex')
nodeTypes.remove('polyMoveFace')
nodeTypes.remove('polyMoveEdge')
nodeTypes.remove('polyExtrudeFace')
nodeTypes.remove('polyBevel')
nodeTypes.remove('polyAutoProj')


'''
# Construct your own list of nodes to check
nodeTypes = []
nodeTypes.append('VRayLightIESShape')
nodeTypes.append('VRayMesh')
nodeTypes.append('VRayLightDomeShape')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
nodeTypes.append('')
'''


with open("c:/filepathDebug.txt", "a") as myfile:
	myfile.truncate()

for nodeType in nodeTypes:
	with open("c:/filepathDebug.txt", "a") as myfile:
		myfile.write(str(nodeType) + '\n')
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
