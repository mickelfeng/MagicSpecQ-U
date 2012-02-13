Summary: Tiny C Compiler
Summary(zh_CN.UTF-8): 小型 C 编译器
Name: tcc
Version: 0.9.25
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
Group(zh_CN.UTF-8): 开发/语言
URL: http://bellard.org/tcc/

Source: http://download.savannah.nongnu.org/releases/tinycc/tcc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
TCC (Tiny C Compiler) is small, fast, unlimited, and safe. You can compile and 
execute C code everywhere (e.g., on rescue disks). It generates optimized x86 
code, and can compile, assemble, and link several times faster than 'gcc -O0'. 
Any C dynamic library can be used directly. It includes an optional memory and 
bounds checker, and bounds-checked code can be mixed freely with standard code. 
C script is also supported--just add '#!/usr/bin/tcc' at the first line of your 
C source, and execute it directly from the command line.

%description -l zh_CN.UTF-8
TCC 是一个小型，快速，无限制和安全的 C 编译器。

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Summary(zh_CN.UTF-8): %name 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description devel -l zh_CN.UTF-8
%name 的开发包。

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall tccdir="%{buildroot}%{_libdir}/tcc" docdir="%{buildroot}%{_datadir}/doc/tcc"
%{__mv} %{buildroot}%{_datadir}/doc/tcc rpm-docs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO rpm-docs/*
%doc %{_mandir}/man1/tcc.1*
%{_bindir}/tcc
%{_libdir}/tcc/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libtcc.h
%{_libdir}/libtcc.a

%changelog

