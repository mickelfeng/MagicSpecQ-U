Name: uClibc
Version: 0.9.32
Release: 3%{?dist}
Summary: C library for embedded Linux
Summary(zh_CN.UTF-8): 嵌入式 Linux 使用的 C 库

Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
License: LGPLv2
URL: http://www.uclibc.org/
Source0: http://www.uclibc.org/downloads/%{name}-%{version}.tar.xz
Source1: uClibc.config
Patch0: epoll-asm-fix.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%global debug_package %{nil}
# This package only contains a static library

ExcludeArch: ppc64
# uclibc 0.9.30 does not support ppc64

%description
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.

%description -l zh_CN.UTF-8
嵌入式 Linux 使用的 C 库，它比 GNU C 库要小的多，不过几乎全部 glibc 
支持的程序都在 uClibc 上工作的很好。

%package devel
Summary: Header files and libraries for uClibc library
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Provides: uClibc-static = %{version}-%{release}

%description devel
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.
This package contains the header files and libraries
needed for uClibc package.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .epoll

cat %{SOURCE1} >.config1
iconv -f windows-1252 -t utf-8 README >README.pom
mv README.pom README

%build
mkdir kernel-include
cp -a /usr/include/asm kernel-include
cp -a /usr/include/asm-generic kernel-include
cp -a /usr/include/linux kernel-include

arch=`uname -m | sed -e 's/i.86/i386/' -e 's/ppc/powerpc/' -e 's/armv7l/arm/' -e 's/armv5tel/arm/'`
echo "TARGET_$arch=y" >.config
echo "TARGET_ARCH=\"$arch\"" >>.config
%ifarch %{arm}
echo "CONFIG_ARM_EABI=y" >>.config
echo "ARCH_ANY_ENDIAN=n" >>.config
echo "ARCH_LITTLE_ENDIAN=y" >>.config
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
cat .config1 >>.config

yes "" | make oldconfig %{?_smp_mflags}
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib
make install PREFIX="$RPM_BUILD_ROOT/"
make install_headers PREFIX="$RPM_BUILD_ROOT/" DEVEL_PREFIX=""
cp -a kernel-include/* $RPM_BUILD_ROOT/include/

# move libraries to proper subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/uClibc
mv  $RPM_BUILD_ROOT/lib/*  $RPM_BUILD_ROOT/%{_libdir}/uClibc/
rm -rf  $RPM_BUILD_ROOT/lib/

# move the header files to /usr subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/uClibc
mv  $RPM_BUILD_ROOT/include/*  $RPM_BUILD_ROOT/%{_includedir}/uClibc
rm -rf  $RPM_BUILD_ROOT/include/

magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root,-)
%doc README docs/Glibc_vs_uClibc_Differences.txt docs/threads.txt docs/uClibc_vs_SuSv3.txt
%doc TODO DEDICATION.mjn3 MAINTAINERS
%doc docs/PORTING COPYING.LIB
%{_includedir}/uClibc
%{_libdir}/uClibc

%changelog
* Wed May 02 2012 Liu Di <liudidi@gmail.com> - 0.9.32-3
- 为 Magic 3.0 重建


