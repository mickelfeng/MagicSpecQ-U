%define rversion %{kde4_kdelibs_version}
#define svn_number rc1
%define real_name qtruby

%define kde4_enable_final_bool ON

Name: %{real_name}
Summary: qtruby
Summary(zh_CN.UTF-8): qtruby
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
Version: %{rversion}
Release: 1%{?dist}
License: LGPL
URL: http://extragear.kde.org/apps/kipi
Source0: http://mirrors.ustc.edu.cn/kde/stable/%{version}/src/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: cmake >= 2.6.2
BuildRequires: gettext

%description


%description -l zh_CN.UTF-8
。

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
%package devel
Summary: Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发文件
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}

%description devel
Contains the development files.

%description devel -l zh_CN.UTF-8
%{name} 的开发文件。包含 libbtcore 的开发文件。

%prep
%setup -q -n %{real_name}-%{rversion}

%build
mkdir build
cd build
%cmake ..

make %{?_smp_mflags}

%install
cd build
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

magic_rpm_clean.sh

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/ruby/vendor_ruby/*
%{_datadir}/ruby/vendor_ruby/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_datadir}/qtruby4/cmake/*
%{_libdir}/*.so

%changelog
* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
