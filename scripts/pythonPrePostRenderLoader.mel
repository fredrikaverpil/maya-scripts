// Pre/post render script loader 1.0
//
// Apply to Tractor .alf like this:
// preRenderString = '{pythonPreRenderLoader("' + filepath + '/' + '", "myscript.py");}'
// postRenderString = '{pythonPreRenderLoader("' + filepath + '/' + '", "myscript.py");}'
//  ... + ' -preRender ' + preRenderString + ' -postRender ' + postRenderString + ...

global proc pythonPrePostRenderLoader(string $path, string $pythonfile)
{
	print("Loading Python script" + $pythonfile + " ...\n");
	string $noPy = `substitute ".py" $pythonfile ""`;
	python("import sys\nsys.path.append(\"" + $path + "\")\nimport " + $noPy + "\n" + $noPy + "." + $noPy + "()");
} 
