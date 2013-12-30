Scripts
================

Python
------

* RenderScriptConsolidator.mel - Consolidate any number of Python and/or MEL scripts to be run as -preRender or -postRender (this script supersedes pythonPrePostRenderLoader.mel)
* checkTracingDepth.py - Check for V-Ray shaders with high tracing depth settings
* collectTextures.py - Traverse .ma scene file andcollect any texture files into a textures folder, residing next to the .ma scene file
* colorRemapper.py - Create a color remap network for selected texture(s)
* crashFileLoader.py - Finds the latest crash save file and loads it
* deleteAllRenderLayers.py - Delete all renderlayers (including imported ones from references, which do not show up in the render layer list)
* deleteHistoryOnScene.py - Delete all history on shape nodes with the option to exclude certain nodes such as VRayMesh and deformers
* deleteMentalRayNodes.py - Remove mental ray nodes (does not really work)
* findBadFilepaths.py - Identify filepaths of the current scene (including references) which include your choice of drive letters
* printFilePaths.py - Print file paths of each file texture
* pythonPrePostRenderLoader.mel - Loads a pre-render or post-render Python script (superseded by RenderScriptConsolidator.mel)
* samplerInfoMaker.py - Create a sampler info network for selected texture(s)



MEL
---

* basePivot.mel - Centers pivot for selected object - but places it in the base of the object (min Y)
