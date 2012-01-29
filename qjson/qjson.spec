Name:           qjson
Version:        0.7.1
Release:        4%{?dist}
Summary:        A qt-based library that maps JSON data to QVariant objects
Summary(zh_CN.UTF-8): 映射 JSON 数据至 QVariant 对象的 Qt 库

Group:          Development/Languages
Group(zh_CN.UTF-8): 开发/语言
License:        GPLv2+
URL:            http://sourceforge.net/projects/qjson/
Source0:        http://downloads.sourceforge.net/project/qjson/qjson/0.7.1/qjson-0.7.1.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt4-devel >= 4.0
BuildRequires:  cmake >= 2.6
BuildRequires:  doxygen

%description
JSON is a lightweight data-interchange format. It can represents integer, real
number, string, an ordered sequence of value, and a collection of
name/value pairs. QJson is a qt-based library that maps JSON data to
QVariant objects.

%description -l zh_CN.UTF-8
JSON 是轻量级的数据交换格式。它能够表示整数、小数、字符串、有序序列值和
名字/值的对偶集合。QJson 是映射 JSON 数据至 QVariant 对象的 Qt 库。

%package devel
Summary:  Development files for qjson
Summary(zh_CN.UTF-8): qjson 的开发文件
Group:    Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
Requires: qt4-devel >= 4.0
Requires: pkgconfig
Requires: cmake

%description devel
The %{name}-devel package contains the libraries and header files required for
developing applications that use %{name}.

%description devel -l zh_CN.UTF-8
%{name}-devel 软件包包含了使用 %{name} 开发应用程序所需的库和头文件。

%prep
%setup -qn qjson

%build
mkdir build
cd build
%cmake \
    -DQJSON_BUILD_TESTS=1 \
    -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules/ \
    ..

pushd %{_builddir}/%{buildsubdir}/doc
doxygen
popd

sed -i -e 's/-fno-exceptions -fno-check-new -fno-common//' \
-e 's/-fno-threadsafe-statics -fvisibility=hidden -fvisibility-inlines-hidden//' \
-e 's/-ansi//' src/CMakeFiles/qjson.dir/flags.make


make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot}

%check
cd build
LD_PRELOAD=%{_lib}/libqjson.so \
           tests/testparser
LD_PRELOAD=%{_lib}/libqjson.so \
           tests/testserializer

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/qjson/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/Modules/FindQJSON.cmake
%{_libdir}/*.so

%changelog
