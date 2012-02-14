Name:           teckit
Version:        2.5.1
Release:        3%{?dist}
Summary:        Conversion library and mapping compiler
Summary(zh_CN.GB18030): 转换库和映射编译器
License:        LGPLv2+ or CPL
Group:          Development/Libraries
Group(zh_CN.GB18030):	开发/库
URL:            http://scripts.sil.org/teckit
Source0:        http://scripts.sil.org/svn-view/teckit/TAGS/TECkit_2_5_1.tar.gz
Patch0:		TECkit_2_5_1-gcc44.patch
BuildRequires:  expat-devel zlib-devel libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%description -l zh_CN.GB18030
TECkit 是一个低级别的工具箱，它可以由其它需要编码转换的程序
（比如导入遗留数据到基于 Unicode 的程序）使用。因此 TECkit 
的主要组件是一个转换库，即 "TECkit 引擎"。这个引擎和一个特
定二进制格式的映射表有关，这有一个编译器，可以从对人可读的
映射描述（一个简单的文本文件）中建立这样的表。

%package devel
Summary:        Conversion library and mapping compiler
Summary(zh_CN.GB18030):	%{name} 的开发包
Group:          Development/Libraries
Group(zh_CN.GB18030):	开发/库
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description devel
TECkit is a low-level toolkit intended to be used by other
applications that need to perform encoding conversions (e.g., when
importing legacy data into a Unicode-based application). The
primary component of the TECkit package is therefore a library that
performs conversions; this is the "TECkit engine". The engine
relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such
tables from a human-readable mapping description (a simple text file).

%description -l zh_CN.GB18030
%{name} 的开发包。

%prep
%setup -q -n TECkit_2_5_1
%patch0 -p1

%{__chmod} 0755 ./autogen.sh
%{__chmod} 0755 ./configure
%{__rm} -r zlib*

%build
./autogen.sh
%configure --disable-static
make %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_libdir}/*.la

%check
make check

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc license/{LICENSING.txt,License_CPLv05.txt,License_LGPLv21.txt}
%attr(0755,root,root) %{_bindir}/sfconv
%attr(0755,root,root) %{_bindir}/teckit_compile
%attr(0755,root,root) %{_bindir}/txtconv
%attr(0755,root,root) %{_libdir}/libTECkit.so.*
%attr(0755,root,root) %{_libdir}/libTECkit_Compiler.so.*

%files devel
%defattr(0644,root,root,0755)
%doc docs/*.pdf
%{_includedir}/teckit/
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so

%changelog
* Tue Feb 14 2012 Liu Di <liudidi@gmail.com> - 2.5.1-3
- 涓� Magic 3.0 閲嶅缓

* Thu Jan 08 2009 Liu Di <liudidi@gmail.com> - 2.5.1-1%{?dist}
- 重建
