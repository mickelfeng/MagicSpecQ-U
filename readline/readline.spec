Summary: A library for editing typed command lines
Name: readline
Version: 6.2
Release: 5%{?dist}
License: GPLv3+
Group: System Environment/Libraries
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
# upstream patches
Patch1: ftp://ftp.cwru.edu/pub/bash/readline-6.2-patches/readline62-001
# fix file permissions, remove RPATH, use CFLAGS
Patch20: readline-6.2-shlib.patch
# add TTY input audit support
Patch21: readline-6.1-audit.patch
Requires(post): /usr/sbin/install-info
Requires(preun): /usr/sbin/install-info
BuildRequires: ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel
Requires(post): /usr/sbin/install-info
Requires(preun): /usr/sbin/install-info

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The readline-static package contains the static version of the readline
library.

%prep
%setup -q
%patch1 -p0
%patch20 -p1 -b .shlib
%patch21 -p1 -b .audit

pushd examples
rm -f rlfe/configure
iconv -f iso8859-1 -t utf8 -o rl-fgets.c{_,}
touch -r rl-fgets.c{,_}
mv -f rl-fgets.c{_,}
popd

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

#mkdir $RPM_BUILD_ROOT/%{_lib}
#mv $RPM_BUILD_ROOT%{_libdir}/libreadline.so.* $RPM_BUILD_ROOT/%{_lib}
#for l in $RPM_BUILD_ROOT%{_libdir}/libreadline.so; do
#    ln -sf $(echo %{_libdir} | \
#        sed 's,\(^/\|\)[^/][^/]*,..,g')/%{_lib}/$(readlink $l) $l
#done

rm -rf $RPM_BUILD_ROOT%{_datadir}/readline
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*

magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/ldconfig
/usr/sbin/install-info %{_infodir}/history.info.gz %{_infodir}/dir &> /dev/null
/usr/sbin/install-info %{_infodir}/rluserman.info.gz %{_infodir}/dir &> /dev/null
:

%postun -p /usr/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   /usr/sbin/install-info --delete %{_infodir}/history.info.gz %{_infodir}/dir &> /dev/null
   /usr/sbin/install-info --delete %{_infodir}/rluserman.info.gz %{_infodir}/dir &> /dev/null
fi
:

%post devel
/usr/sbin/install-info %{_infodir}/readline.info.gz %{_infodir}/dir &> /dev/null
:

%preun devel
if [ $1 = 0 ]; then
   /usr/sbin/install-info --delete %{_infodir}/readline.info.gz %{_infodir}/dir &> /dev/null
fi
:

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING NEWS README USAGE
%{_libdir}/libreadline*.so.*
%{_libdir}/libhistory*.so.*
%{_infodir}/history.info*
%{_infodir}/rluserman.info*

%files devel
%defattr(-,root,root,-)
%doc examples/*.c examples/*.h examples/rlfe
%{_includedir}/readline
%{_libdir}/lib*.so
%{_mandir}/man3/*
%{_infodir}/readline.info*

%files static
%defattr(-,root,root,-)
%{_libdir}/lib*.a

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 6.2-5
- 为 Magic 3.0 重建

* Sun Apr 22 2012 Liu Di <liudidi@gmail.com> - 6.2-4
- 为 Magic 3.0 重建

* Thu Feb 02 2012 Liu Di <liudidi@gmail.com> - 6.2-3
- 为 Magic 3.0 重建

