# Created by Fredrik Averpil

import maya.cmds as cmds

def createNetwork():
	# Create 
	nodeRamp = cmds.shadingNode('ramp', asTexture=True)
	nodeSamplerInfo = cmds.shadingNode('samplerInfo', asUtility=True)
	
	# Make connections between sampler info and ramp
	cmds.connectAttr( nodeSamplerInfo+'.facingRatio', nodeRamp+'.uCoord', f=True)
	cmds.connectAttr( nodeSamplerInfo+'.facingRatio', nodeRamp+'.vCoord', f=True)
	
	return nodeSamplerInfo, nodeRamp




def run():
	selectedNodes = cmds.ls(sl=True)
	if len(selectedNodes) == 0:
		createNetwork()
	else:
		nodeSamplerInfo, nodeRamp = createNetwork()
		

		if len(selectedNodes) > 1:
		    part = float( 1.0/(len(selectedNodes)-1) )
		else:
		    part = float( 1.0/len(selectedNodes) )

		    
		for x in range(0, len(selectedNodes)):
		    pos = (1.0-(part*x))
		    print pos
		    # Create entry
		    #cmds.setAttr( nodeRamp+'.colorEntryList[' + str(x-1) + '].position', pos )
		    cmds.setAttr( nodeRamp+'.colorEntryList[' + str(x) + '].position', (pos) )
		    # Create connection
		    try:
		        cmds.connectAttr( selectedNodes[x]+'.outColor', nodeRamp+'.colorEntryList[' + str(x) + '].color', f=True)
		    except:
		        pass
		    try:
		        cmds.connectAttr( selectedNodes[x]+'.output', nodeRamp+'.colorEntryList[' + str(x) + '].color', f=True)
		    except:
		        pass
		    try:
		        cmds.connectAttr( selectedNodes[x]+'.outValue', nodeRamp+'.colorEntryList[' + str(x) + '].color', f=True)
		    except:
		        pass
		    
		    if len(selectedNodes) == 1:
		        cmds.setAttr( nodeRamp+'.colorEntryList[' + str(x+1) + '].position', 0.0 )
		        cmds.setAttr( nodeRamp+'.colorEntryList[' + str(x+1) + '].color', 1, 1, 1)
		        
		        
