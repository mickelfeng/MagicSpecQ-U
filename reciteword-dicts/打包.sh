#!/bin/bash
# 是否必须有中文翻译
DEBUG=0
LOG=1
BUMP=0
SAVEPATH="~/"
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
#判断一些环境变量，首先是是否必须有中文翻译
if [ -z "$MUSTUSEZH" ];then
        MUSTUSEZH=0
fi
if [ -z "$MUSTUSECLEAN" ];then
	MUSTUSECLEAN=0
fi
if [ -f ~/.magicspecrc ];then
        . ~/.magicspecrc
fi
debug_echo "MUSTUSEZH 变量是 $MUSTUSEZH"
debug_echo "MUSTUSECLEAN 变量是 $MUSTUSECLEAN"
#判断当前目录下是否有 .spec 文件，并取得其文件名
SPECCOUNT=`ls *.spec 2>/dev/null | wc -l`
debug_echo "spec文件数量是 $SPECCOUNT"
if [ $SPECCOUNT -gt 1 ];then
	echo "当前目录的 .spec 文件过多，只有一个 spec 文件的情况下，脚本才能正确执行"
	exit 1
fi
if [ $SPECCOUNT = "0" ];then
	echo "当前目录中没有 .spec 文件，脚本退出！"
	exit 1
fi
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
if !  (debug_run rpmspec -P $SPECNAME );then
	echo "spec 文件格式有错误，请检查，脚本退出！" 
	exit 1
fi
if ! (rpmspec -P $SPECNAME | grep "Summary(zh_CN.UTF-8)" > /dev/null); then
	if [ $MUSTUSEZH = "1" ];then
		echo "spec 中没有中文简介，请添加"
		exit 1
	else
		debug_echo "spec 中没有中文简介"
	fi
fi
if ! (rpmspec -P $SPECNAME | grep "Group(zh_CN.UTF-8)" > /dev/null); then
        if [ $MUSTUSEZH = "1" ];then
                echo "spec 中没有中文组，请添加"
                exit 1
        else
                debug_echo "spec 中没有中文组"
        fi
fi
if ! (rpmspec -P $SPECNAME | grep "description -l zh_CN.UTF-8" > /dev/null); then
        if [ $MUSTUSEZH = "1" ];then
                echo "spec 中没有中文描述，请添加"
                exit 1
        else
                debug_echo "spec 中没有中文描述"
        fi
fi
if ! (rpmspec -P $SPECNAME | grep "magic_rpm_clean.sh" > /dev/null); then
        if [ $MUSTUSECLEAN = "1" ];then
                echo "spec 中没有清理语句，请添加"
		#这里要做自动添加的尝试，但有些难
                exit 1
        else
                debug_echo "spec 中没有清理语句"
        fi
fi
#还应该有路径判断，不过这个好像不是必须的，而且有几个包特殊，考虑加不加呢。
#下面开始建立打包的环境
mkdir SOURCES RPMS BUILD
#准备相关的源代码
cp * SOURCES
#下载 spec 中指定的源码及补丁，注意 spec 中必须事先写好。
if ! ( debug_run spectool -D -S -C $(pwd)/SOURCES -g $SPECNAME) ; then
	echo "无法正常下载源代码，尝试使用其它途径"
	exit 1
fi
#判断编译依赖关系
for i in `rpmspec -q --buildrequires $SPECNAME`;do
	if ! (rpm -qa |grep -q $i);then
		debug_run smart install $i -y
	fi
done
if [ $BUMP = "1" ];then
	rpmdev-bumpspec -c "重新编译" -u "Liu Di <liudidi@gmail.com>" $SPECNAME
fi
#开始打包
if ! (debug_run rpmbuild -ba $SPECNAME --define '_topdir '$(pwd)'');then
	echo "打包过程出错，请检查 build.log 文件"	
	exit 1
else	
	mv RPMS/*/*.rpm $SAVEPATH
fi
rm -rf BUILD BUILDROOT RPMS SOURCES SPECS SRPMS
popd
