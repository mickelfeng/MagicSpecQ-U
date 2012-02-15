Name: torsocks
Summary: Use socks-friendly applications with Tor
Summary(zh_CN.UTF-8): 使用 tor 处理 socks 代理程序
Version: 1.2
Release: 1%{?dist}
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
License: GPL
Source0: http://torsocks.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
URL: http://code.google.com/p/torsocks/
Prefix: %{_prefix}
Packager: Liu Di <liudidi@gmail.com>

%description
Use socks-friendly applications with Tor

%description -l zh_CN.UTF-8
使用 tor 处理 socks 代理程序

%package devel
Summary: Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发文件
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%description devel -l zh_CN.UTF-8
%{name} 的开发文件。


%prep
%setup -q

%build
%configure 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/torsocks/*.la
magic_rpm_clean.sh

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files
%defattr(-,root,root)
%{_sysconfdir}/*.conf
%{_bindir}/tor*
%{_bindir}/usewithtor
%{_libdir}/torsocks/lib*.so.*
%{_mandir}/*
%{_datadir}/run_tests.sh

%files devel
%defattr(-,root,root)
%{_libdir}/torsocks/libtorsocks.a
%{_libdir}/torsocks/libtorsocks.so
%{_datadir}/*.patch
%{_datadir}/README*
%{_datadir}/DEBUG
%{_datadir}/SOCKS*
%{_datadir}/*.txt


%changelog
* Sun Aug 5 2007 kde <athena_star {at} 163 {dot} com> - 0.18-1mgc
- update to 0.18
- modify the spec file

* Sat Jun 23 2007 Ni Hui <shuizhuyuanluo@126.com> - 0.17-1mgc
- initialize the first spec file for MagicLinux-2.1
