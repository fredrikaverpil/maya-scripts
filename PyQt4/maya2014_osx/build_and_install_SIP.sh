#!/usr/bin/env bash 
MAYAQTBUILD="`dirname \"$0\"`" # Relative 
export MAYAQTBUILD="`( cd \"$MAYAQTBUILD\" && pwd )`" # Absolutized and normalized 
cd $MAYAQTBUILD 
export SIPDIR=$MAYAQTBUILD/sip-4.14.5 
export MAYA_LOCATION=/Applications/Autodesk/maya2014
cd $SIPDIR 
$MAYA_LOCATION/Maya.app/Contents/bin/mayapy ./configure.py --arch=x86_64 
make
sudo make install