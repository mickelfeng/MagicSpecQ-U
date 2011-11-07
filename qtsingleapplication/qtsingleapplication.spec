%define _qt4_qmake qmake-qt4
%define _qt4_lrelease lrelease-qt4
Summary:        Qt library to start applications only once per user
Summary(zh_CN.UTF-8): 用于为每个用户仅启动一次应用程序的 Qt 库
Name:           qtsingleapplication
Version:        2.6
Release:        2%{?dist}
Group:          System Environment/Libraries
Group(zh_CN.UTF-8):   系统环境/库
License:        GPLv3 or LGPLv2 with exceptions
URL:            http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtsingleapplication
Source0:        http://get.qt.nokia.com/qt/solutions/lgpl/qtsingleapplication-%{version}_1-opensource.tar.gz
Patch0:         qtsingleapplication-build.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  qt4-devel
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

%description -l zh_CN.UTF-8
对某些应用程序而言，针对每个用户仅仅启动一次是有必要的甚至是必须的。
今后任何启动此应用程序的尝试均应激活任何业已运行的实例，并且可能在
该实例里执行请求的动作，例如载入一个文件。

QtSingleApplication 类提供一个接口用以侦测运行中的实例，并且发送命令
字符串到该实例。

对于控制台(非图形用户界面) 应用程序，提供了 QtSingleCoreApplication
变体，她可以避免依赖 Qt 的图形用户界面。


%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	qt4-devel

%description	devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.

%prep
%setup -q -n %{name}-%{version}_1-opensource
%patch0 -p1


%build
touch .licenseAccepted
# Does not use GNU configure
./configure -library
%{_qt4_qmake}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# libraries
mkdir -p $RPM_BUILD_ROOT%{_qt4_libdir}
cp -a lib/* $RPM_BUILD_ROOT%{_qt4_libdir}
mkdir -p %{buildroot}%{_libdir}
ln -s ./qt4/lib/libQtSolutions_SingleApplication-2.6.so %{buildroot}%{_libdir}/libQtSolutions_SingleApplication-2.6.so


# headers
mkdir -p $RPM_BUILD_ROOT%{_qt4_headerdir}/QtSolutions/
cp -a \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    $RPM_BUILD_ROOT%{_qt4_headerdir}/QtSolutions

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LGPL_EXCEPTION.txt LICENSE.* README.TXT
%{_qt4_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc examples
%{_libdir}/*.so
%{_qt4_libdir}/lib*.so
%{_qt4_headerdir}/QtSolutions/

%changelog
* Sun May 30 2010 Liu Songhe <athena_star {at} 163 {dot} com> - 2.6-1
- Port to magic linux 2.5

* Sun Apr 11 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.6-1
- Initial Fedora package. Specfile partly borrowed from opensuse

* Thu Dec  3 2009 Todor Prokopov <koprok@nand.bg>
- Initial package.
