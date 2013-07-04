# Delete all history in scene with some exclusions (defined in exclusionList)

import maya.cmds as cmds


def deleteConstructionHistory(item):
	try:
		cmds.delete(item, constructionHistory=True)
	except:
		cmds.warning('Could not delete history for object ' + item)

def checkForHistory(array):
	log = ['\n']
	for item in array:
		if len( cmds.listHistory(item)) > 0:
			#print cmds.listHistory(item)
			#print item + ' has history.\n'
			if cmds.objExists(item + '.showBBoxOnly') == False:	# If this is not a vrayproxy node, go ahead and check if it has a connection to the .inMesh
				if cmds.objExists(item + '.inMesh') == False:		# If object has no input connections to .inMesh, go ahead and delete history
					log.append(item)
					deleteConstructionHistory(item)
				else:
					# Start checking for exclusions such as deformers which will abort history deletion
					foundDeformer = False
					connections = cmds.listConnections(item + '.inMesh')
					if connections == None:
						log.append(item)
						deleteConstructionHistory(item)
					else:
						exclusionList = ['VRayMesh', 'blendShape', 'nonLinear', 'ffd', 'cluster', 'softMod', 'sculpt', 'jiggle', 'wire']
						for connection in connections:
							# print cmds.nodeType( connection )
							if cmds.nodeType( connection ) in exclusionList:
								foundDeformer = True
								#print 'Found deformer on ' + item + ' (' + connection + ') - skipping this object'
						if foundDeformer == False:
							#print 'Deleting history on ' + item
							log.append(item)
							deleteConstructionHistory(item)
	return log


def deleteHistoryOnScene():
	logTransforms = checkForHistory( cmds.ls(type='transform') )
	logShapes = checkForHistory( cmds.ls(type='shape') )

deleteHistoryOnScene()
