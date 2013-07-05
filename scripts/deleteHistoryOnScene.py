# Delete all history in scene with some exceptions (defined in exceptionList)

import maya.cmds as cmds

# Function which deletes history on an object
def deleteConstructionHistory(item):
	if cmds.objExists(item):
		try:
			cmds.delete(item, constructionHistory=True)
		except:
			cmds.warning('Could not delete history for object ' + item)

# Function which finds needle in haystack
def findFirstMatchInString(list, text):
	for part in list:
		if (part in text):
			return True
		else:
			return False


# Main app
def checkForHistory(array, exceptionList):
	log = ['\n---- Scene-wide history deletion ----']
	allConnectionTypes = []
	skipItemList = []
	
	for item in array:
		if cmds.objExists(item):
			if cmds.referenceQuery(item, isNodeReferenced=True) == False:
				#print item + ': ' + str(cmds.listHistory(item)) # Debug
				if len( cmds.listHistory(item)) > 0:
					
					#print 'Analyzing ' + item
					

					for historyItem in cmds.listHistory(item):
						if cmds.nodeType( historyItem ) in exceptionList:
							log.append('Skipping (history connection): \t\t' + item + ': ' + cmds.nodeType( item ))
							if item not in skipItemList:
								skipItemList.append(item)
						
					connections = cmds.listConnections(item)
					if connections != None:
						for connection in connections:
							if cmds.nodeType( connection ) in exceptionList:
								log.append('Skipping (connection): \t\t\t\t' + item + ': ' + cmds.nodeType( connection ))
								if item not in skipItemList:
									skipItemList.append(item)
								

	# Remove objects from array which should keep history
	for item in skipItemList:
		array.remove(item)
	log.append('Number of items to skip: ' + str(len(skipItemList)) )

	# Perform double check
	for item in array:
		#print 'Scheduled for history deletion: ' + item
		if item in skipItemList:
			cmds.warning( 'Warning: Items that should have been removed from deletion list is still present in deletion list.' )
	
	# Print log
	for line in log:
		print line
				
	return array
	
	
	

# Initialize app and carry out the order to perform the history deletion
def deleteHistoryOnScene(mode):
    error = False

    # Mode based off toggle
    if mode == 'keepVRayMeshAndDeformers':
    	exceptionList = ['VRayMesh', 'blendShape', 'nonLinear', 'ffd', 'cluster', 'softMod', 'sculpt', 'jiggle', 'wire']
    
    elif mode == 'keepVRayMeshOnly':
        exceptionList = ['VRayMesh']
    
    else:
        cmds.warning('No valid mode found')
        error = True


    if error == False:
    	# Commence gathering of scene info
    	scheduledForDeletion = checkForHistory( cmds.ls(type='shape'), exceptionList )
    	
    	# Print summary
    	print '\n---- Summary ----'
    	scheduledForDeletion = list(set(scheduledForDeletion)) # Remove any duplicate from list
    	print 'Commencing history deletion for ' + str( len( scheduledForDeletion ) ) + ' objects...'
    	
    	# Commence scene history deletion
    	for item in scheduledForDeletion:
    		deleteConstructionHistory(item)
    		pass
    	
    	print 'Done!'
    	cmds.confirmDialog(title='History deletion complete', message='Done. Check script editor for output.\n\nVerify that V-Ray proxies and other critical history-based features are still intact - or you can undo this task.')
   	


# Start script by one of the following, different modes
# deleteHistoryOnScene('keepVRayMeshAndDeformers')
# deleteHistoryOnScene('keepVRayMeshOnly')

