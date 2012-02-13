Summary: Magic Deskop Service Info
Summary(zh_CN.UTF-8): Magic 桌面服务管理器
Name: Sinfo
Version: 0.5
Release: 2%{?dist}
License: GPL
URL: http://ftp.magiclinux.org.cn/haulm
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
#Source0:%{name}-%{ver}.tar.bz2
Source0: Sinfo-%{version}.tar.gz
Source1: Sinfo.desktop
Prefix: %{_prefix}
Requires: rp-pppoe,ppp
Packager: haulm<haulm@126.com>, Magic Group
Autoreqprov: 0
%description
Magic Deskop Service Info

%description -l zh_CN.UTF-8
Magic 桌面服务管理器

%prep

%setup -q -n Sinfo

%Build
qmake-qt4 -project
qmake-qt4
make 
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/Sinfo
mkdir -p %{buildroot}/usr/share/applications/
install -m 755 ./Sinfo %{buildroot}/opt/Sinfo
install -m 644 ./service.ini %{buildroot}/opt/Sinfo/
cp %{SOURCE1} %{buildroot}/usr/share/applications/
%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}
%files
%defattr(-,root,root)
/opt/Sinfo
/usr/share/applications/
%changelog
