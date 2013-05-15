#!/bin/bash
# 是否必须有中文翻译
DEBUG=1
LOG=1
if [ $LOG = "1" ];then
        LOGFILE=build.log
        rm -f $LOGFILE
else
        LOGFILE=/dev/null
fi
debug_echo ()
{
        if [ $DEBUG = "1" ];then
                echo $1
        fi
}
debug_runsh ()
{
        if [ $DEBUG = "1" ];then
                sh $1
        else
                sh $1 >> "$LOGFILE" 2>&1
        fi
}
debug_run ()
{
        if [ $DEBUG = "1" ];then
                "$@"
        else
                "$@" >> "$LOGFILE" 2>&1
        fi
}
#进入脚本所在的目录
pushd $(dirname $0)
#判断 spec 文件是否合适，这个不是完全准确
SPECNAME=$(ls *.spec)
debug_echo "当前的 spec 文件名是 $SPECNAME"
CURRENTPATH=$(basename `pwd`)
debug_echo "当前 spec 所在的目录是 $CURRENTPATH"
DIR=`echo $SPECNAME|cut -d. -f1`
if ! [ $DIR = $CURRENTPATH ];then
        echo "spec 文件名和所在目录的名字不一致，请检查原因。"
        exit 1
fi
#联得当前的版本号
if ! (debug_run rpmspec -q --qf "%{VERSION}\n" $SPECNAME | sed -n '1p');then
	echo "spec 文件有问题"
	exit 1
else
	CURVER=$( rpmspec -q --qf "%{VERSION}\n" $SPECNAME | sed -n '1p')
fi
debug_echo "当前版本为$CURVER"
#联得新版本号
URL=http://ftp.acc.umu.se/pub/GNOME/sources/cantarell-fonts/0.0
rm -f index.html && wget $URL -O index.html
new1="LATEST-IS-"
new2="<\\/a"
NEWVER=$(grep "$new1.*$new2" index.html | sed "s/.*$new1//" | sed "s/$new2.*//" | sed 's/^[ ]\{1,\}//;s/[ ]\{1,\}$//g')
debug_echo "网站版本为 $NEWVER"
rm -f index.html
#对比版本号，若新则修改spec，执行自动打包脚本.
if [ $NEWVER != $CURVER ];then
	sed -i 's/auto_ver '"$CURVER"'/auto_ver '"$NEWVER"'/g' $SPECNAME | sed -i 's/Version: '"$CURVER"'/Version: '"$NEWVER"'/g' $SPECNAME
	./打包.sh
fi
popd
