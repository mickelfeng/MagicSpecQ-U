%define desktop_vendor magicgroup

%define _rc %{nil}
%define mgcver 3.0

Summary: smart's config file
Summary(zh_CN.UTF-8): smart 的配置文件
Name: smart-config
Version: 1.2
Release: 7%{?dist}
License: GPL
Group: Applications/System
Group(zh_CN.UTF-8): 应用程序/系统
URL: http://www.smartpm.org/

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: smart >= %{version}

%description
Smart's config files。

%description -l zh_CN.UTF-8
smart 的配置文件。

%prep

name='Magic Linux';version='%{mgcver}'

%{__cat} >rpm-db.channel<<EOF
[rpm-db]
name = RPM Database on this system
type = rpm-sys
EOF

%{__cat} >all.channel<<EOF
[all-magiclinux0]
type = apt-rpm
name = $name $version APT All Repository from magiclinux0
baseurl = http://apt.magiclinux.org:81/magic/%{mgcver}/unstable
components = all
 
[all-lcuc2]
type = apt-rpm
name = $name $version APT All Repository from lcuc2
baseurl = http://www.321211.net/apt/magic/%{mgcver}/unstable
components = all
EOF

%{__cat} >extras.channel<<EOF
[extras-magiclinux0]
type = apt-rpm
name = $name $version APT Extras Repository from magiclinux0
baseurl = http://apt.magiclinux.org:81/magic/%{mgcver}/unstable
components = extras

[extras-lcuc2]
type = apt-rpm
name = $name $version APT Extras Repository from lcuc2
baseurl = http://www.321211.net/apt/magic/%{mgcver}/unstable
components = extras
EOF

%{__cat} >nosrc.channel<<EOF
[nosrc-magiclinux0]
type = apt-rpm
name = $name $version APT Nosrc Repository from magiclinux0
baseurl = http://apt.magiclinux.org:81/magic/%{mgcver}/unstable
components = nosrc

[nosrc-lcuc2]
type = apt-rpm
name = $name $version APT Nosrc Repository from lcuc2
baseurl = http://www.321211.net/apt/magic/%{mgcver}/unstable
components = nosrc
EOF

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/smart/channels/

%{__cp} -apv *.channel %{buildroot}%{_sysconfdir}/smart/channels/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/smart/channels/

%changelog
* Tue Dec 18 2007 Liu Di <liudidi@gmail.com> - 0.5%{mgcver}mgc
- update to magic %{mgcver} config

* Fri Apr 06 2007 Liu Di <liudidi@gmail.com> - 0.50-1mgc
- first spec
