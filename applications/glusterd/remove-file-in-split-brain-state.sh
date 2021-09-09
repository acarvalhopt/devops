#!/bin/bash

#Usage:
# gluster volume heal gluster info split-brain
# ./remove-file-in-split-brain.sh <path-to-file>

BRICK=/srv/gluster/brick
SBFILE=$1
GFID=$(getfattr -n trusted.gfid --absolute-names -e hex ${BRICK}${SBFILE} | grep 0x | cut -d'x' -f2)
rm -rf ${BRICK}${SBFILE}
rm -rf ${BRICK}/.glusterfs/${GFID:0:2}/${GFID:2:2}/${GFID:0:8}-${GFID:8:4}-${GFID:12:4}-${GFID:16:4}-${GFID:20:12}