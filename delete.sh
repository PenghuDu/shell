#!/bin/bash

echo "Deleting $* ..."
echo "Move $# files to recycle bin."
mv $* -t ~/recyclebin/	# $1表示第一个参数，$*表示所有参数，$0表示文件名，$#表示参数个数
exit 0
