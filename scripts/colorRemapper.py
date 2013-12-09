import maya.cmds as cmds

def createNetwork():
	# Create 
	nodeRGBToHSV = cmds.shadingNode('rgbToHsv', asUtility=True)
	nodeRamp = cmds.shadingNode('ramp', asTexture=True)
	
	# Make connections between rgbToHsv and ramp
	cmds.connectAttr( nodeRGBToHSV+'.outHsvH', nodeRamp+'.uCoord', f=True)
	cmds.connectAttr( nodeRGBToHSV+'.outHsvV', nodeRamp+'.vCoord', f=True)
	
	# Modify ramp
	cmds.removeMultiInstance( nodeRamp+".colorEntryList[1]", b=True)
	cmds.setAttr( nodeRamp+".colorEntryList[2].color", 1, 1, 1)
	cmds.setAttr( nodeRamp+".colorEntryList[0].color", 0, 0, 0)
	cmds.setAttr( nodeRamp+".colorEntryList[2].position", 1)
	
	return nodeRGBToHSV, nodeRamp




def run():
	selectedNodes = cmds.ls(sl=True)
	if len(selectedNodes) == 0:
		createNetwork()
	else:
		for node in selectedNodes:
			nodeRGBToHSV, nodeRamp = createNetwork()
			try:
				cmds.connectAttr(node+'.outColor', nodeRGBToHSV+'.inRgb', f=True)
			except:
				pass
			try:
				cmds.connectAttr(node+'.output', nodeRGBToHSV+'.inRgb', f=True)
			except:
				pass    	  
			try:
				cmds.connectAttr(node+'.outValue', nodeRGBToHSV+'.inRgbR', f=True)
				cmds.connectAttr(node+'.outValue', nodeRGBToHSV+'.inRgbG', f=True)
				cmds.connectAttr(node+'.outValue', nodeRGBToHSV+'.inRgbB', f=True)
			except:
				pass    	

