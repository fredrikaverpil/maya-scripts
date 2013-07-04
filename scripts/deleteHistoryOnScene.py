# Delete all history in scene with some exceptions (defined in exceptionList)

import maya.cmds as cmds

def deleteConstructionHistory(item):
	try:
		cmds.delete(item, constructionHistory=True)
	except:
		cmds.warning('Could not delete history for object ' + item)

def findFirstMatchInString(list, text):
	for part in list:
		if (part in text):
			return True
	return False


def checkForHistory(array):
	log = ['\n']
	exceptionList = ['VRayMesh', 'blendShape', 'nonLinear', 'ffd', 'cluster', 'softMod', 'sculpt', 'jiggle', 'wire']
	
	for item in array:
		if cmds.objExists(item):
			if cmds.isFromReferencedFile(item) == False:
				foundException = False
				if len( cmds.listHistory(item)) > 1:
					#print cmds.listHistory(item)
					#print item + ' has history.\n'
					connections = cmds.listConnections(item)
					if connections != None:
						for connection in connections:
							if findFirstMatchInString(exceptionList, cmds.nodeType( connection )):
								foundException = True
								log.append('Exception found for ' + item + '.' + connection)
						if foundException == False:
							log.append('Deleting history on ' + item)
							deleteConstructionHistory(item)
	return log


def deleteHistoryOnScene():
	logTransforms = checkForHistory( cmds.ls(type='transform') )
	logShapes = checkForHistory( cmds.ls(type='shape') )

	for line in logTransforms:
		print line

	for line in logShapes:
		print line


deleteHistoryOnScene()
