# Define this to link to which library version  eg. /lib64/ld-lsb-x86-64.so.3
%define lsbsover 3 

%ifarch %{ix86}
%define ldso ld-linux.so.2
%define lsbldso ld-lsb.so
%endif

%ifarch ia64
%define ldso ld-linux-ia64.so.2
%define lsbldso ld-lsb-ia64.so
%endif

%ifarch ppc
%define ldso ld.so.1
%define lsbldso ld-lsb-ppc32.so
%endif

%ifarch ppc64
%define ldso ld64.so.1
%define lsbldso ld-lsb-ppc64.so
%endif

%ifarch s390
%define ldso ld.so.1
%define lsbldso ld-lsb-s390.so
%endif

%ifarch s390x
%define ldso ld64.so.1
%define lsbldso ld-lsb-s390x.so
%endif

%ifarch x86_64
%define ldso ld-linux-x86-64.so.2
%define lsbldso ld-lsb-x86-64.so
%endif

%define upstreamlsbrelver 2.0
%define lsbrelver 4.1
%define srcrelease 1

Summary: Implementation of Linux Standard Base specification
Name: redhat-lsb
Version: 4.1
Release: 6%{?dist}
URL: http://www.linuxfoundation.org/collaborate/workgroups/lsb
Source0: https://fedorahosted.org/releases/r/e/redhat-lsb/%{name}-%{version}-%{srcrelease}.tar.bz2
Patch0: lsb-release-3.1-update-init-functions.patch
Patch1: redhat-lsb-lsb_start_daemon-fix.patch
Patch2: redhat-lsb-trigger.patch
Patch3: redhat-lsb-arm.patch
License: GPLv2
Group: System Environment/Base
BuildRequires: glibc-static

%ifarch %{ix86}
%define archname ia32
%endif
%ifarch ia64
%define archname ia64
%endif
%ifarch ppc
%define archname ppc32
%endif
%ifarch ppc64
%define archname ppc64
%endif
%ifarch s390
%define archname s390
%endif
%ifarch s390x
%define archname s390x
%endif
%ifarch x86_64
%define archname amd64
%endif

ExclusiveArch: %{ix86} ia64 x86_64 ppc ppc64 s390 s390x %{arm}

Requires: redhat-lsb-core%{?_isa} = %{version}
Requires: redhat-lsb-cxx%{?_isa} = %{version}
Requires: redhat-lsb-desktop%{?_isa} = %{version}
Requires: redhat-lsb-languages = %{version}
Requires: redhat-lsb-printing = %{version}
#Requires: redhat-lsb-trialuse = %{version}

Provides: lsb = %{version}
Provides: lsb-%{archname} = %{version}
Provides: lsb-noarch = %{version}

%description
The Linux Standard Base (LSB) is an attempt to develop a set of standards that
will increase compatibility among Linux distributions. It is designed to be 
binary-compatible and produce a stable application binary interface (ABI) for
independent software vendors.
The lsb package provides utilities, libraries etc. needed for LSB Compliant 
Applications. It also contains requirements that will ensure that all 
components required by the LSB are installed on the system.

%package submod-security
Group: System Environment/Base
Summary: LSB Security submodule support
Requires: nspr%{?_isa}
# Requires: nspr-devel
Requires: nss%{?_isa}

Provides: lsb-submod-security-%{archname} = %{version}
Provides: lsb-submod-security-noarch = %{version}

%description submod-security
The Linux Standard Base (LSB) Security submodule specifications define 
components that are required to be present on an LSB conforming system.

%package submod-multimedia
Group: System Environment/Base
Summary: LSB Multimedia submodule support
Requires: alsa-lib%{?_isa}

Provides: lsb-submod-multimedia-%{archname} = %{version}
Provides: lsb-submod-multimedia-noarch = %{version}

%description submod-multimedia
The Linux Standard Base (LSB) Multimedia submodule specifications define 
components that are required to be present on an LSB conforming system.

%package core
Group: System Environment/Base
Summary: LSB Core module support
# gLSB Library
Requires: glibc%{?_isa}
Requires: glibc-common
Requires: libgcc%{?_isa}
Requires: ncurses-libs%{?_isa}
Requires: pam%{?_isa}
Requires: zlib%{?_isa}

# gLSB Command and Utilities
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /bin/cpio
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/ed
Requires: /bin/egrep
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/find
Requires: /bin/grep
Requires: /bin/gunzip
Requires: /bin/gzip
Requires: /bin/hostname
Requires: /bin/kill
Requires: /bin/ln
Requires: /bin/ls
Requires: /bin/mailx
Requires: /bin/mkdir
Requires: /bin/mknod
Requires: /bin/mktemp
Requires: /bin/more
Requires: /bin/mount
Requires: /bin/mv
Requires: /bin/nice
Requires: /bin/ps
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/rmdir
Requires: /bin/sed
Requires: /bin/sh
Requires: /bin/sleep
Requires: /bin/sort
Requires: /bin/stty
Requires: /bin/sync
Requires: /bin/tar
Requires: /bin/touch
Requires: /bin/true
Requires: /bin/umount
Requires: /bin/uname
Requires: /bin/zcat
Requires: /sbin/fuser
Requires: /sbin/pidof
Requires: /sbin/shutdown
Requires: /usr/bin/[
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /usr/bin/awk
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/chfn
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /usr/bin/cut
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /usr/bin/du
Requires: /usr/bin/env
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /usr/bin/file
Requires: /usr/bin/find
Requires: /usr/bin/fold
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/gettext
Requires: /usr/bin/groups
Requires: /usr/bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/lp
Requires: /usr/bin/lpr
Requires: /usr/bin/m4
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /usr/bin/mkfifo
Requires: /usr/bin/msgfmt
Requires: /usr/bin/newgrp
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
Requires: /usr/bin/pax
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/renice
Requires: /usr/bin/seq
Requires: /usr/bin/split
Requires: /usr/bin/strings
Requires: /usr/bin/strip
Requires: /usr/bin/su
Requires: /usr/bin/tail
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /usr/bin/tr
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /usr/bin/wc
Requires: /usr/bin/xargs
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod
Requires: redhat-lsb-submod-security%{?_isa} = %{version}

Provides: lsb-core-%{archname} = %{version}
Provides: lsb-core-noarch = %{version}
#Obsoletes: redhat-lsb < %{version}

%description core
The Linux Standard Base (LSB) Core module support provides the fundamental
system interfaces, libraries, and runtime environment upon which all conforming
applications and libraries depend.

%package cxx
Group: System Environment/Base
Summary: LSB CXX module support
Requires: libstdc++%{?_isa}
Requires: redhat-lsb-core%{?_isa} = %{version}

Provides: lsb-cxx-%{archname} = %{version}
Provides: lsb-cxx-noarch = %{version}

%description cxx
The Linux Standard Base (LSB) CXX module supports the core interfaces by
providing system interfaces, libraries, and a runtime environment for 
applications built using the C++ programming language. These interfaces 
provide low-level support for the core constructs of the language, and 
implement the standard base C++ libraries.

%package desktop
Group: System Environment/Base
Summary: LSB Desktop module support
Requires: xdg-utils
# LSB_Graphics library
Requires: libICE%{?_isa}
Requires: libSM%{?_isa}
Requires: libX11%{?_isa}
Requires: libXext%{?_isa}
Requires: libXi%{?_isa}
Requires: libXt%{?_isa}
Requires: libXtst%{?_isa}
Requires: mesa-libGL%{?_isa}
Requires: mesa-libGLU%{?_isa}
# gLSB Graphics and gLSB Graphics Ext Command and Utilities
Requires: /usr/bin/fc-cache
Requires: /usr/bin/fc-list
Requires: /usr/bin/fc-match
# gLSB Graphics Ext library
Requires: cairo%{?_isa}
Requires: freetype%{?_isa}
Requires: libjpeg-turbo%{?_isa}

%ifarch %{ix86}
Requires: libpng12.so.0
%endif
%ifarch x86_64
Requires: libpng12.so.0()(64bit)
%endif
Requires: libpng%{?_isa}
Requires: libXft%{?_isa}
Requires: libXrender%{?_isa}
# toolkit-gtk
Requires: atk%{?_isa}
Requires: gdk-pixbuf2%{?_isa}
Requires: glib2%{?_isa}
Requires: gtk2%{?_isa}
Requires: pango%{?_isa}
# toolkit-qt4
Requires: qt4%{?_isa}
Requires: qt4-gui%{?_isa}
# toolkit-qt3
Requires: qt%{?_isa}
# xml
Requires: libxml2%{?_isa}
Requires: redhat-lsb-submod-multimedia%{?_isa} = %{version}
Requires: redhat-lsb-core%{?_isa} = %{version}

Provides: lsb-desktop-%{archname} = %{version}
Provides: lsb-desktop-noarch = %{version}
Provides: lsb-graphics-%{archname} = %{version}
Provides: lsb-graphics-noarch = %{version}
Obsoletes: redhat-lsb-graphics < %{version}

%description desktop
The Linux Standard Base (LSB) Desktop Specifications define components that are
required to be present on an LSB conforming system.

%package languages
Group: System Environment/Base
Summary: LSB Languages module support
# Perl and Perl non-builtin modules
Requires: /usr/bin/perl
Requires: perl(CGI)
Requires: perl(Class::ISA)
Requires: perl(CPAN)
# Locale::Constants has been Locale::Codes::Costants, so we need
# create a /usr/share/perl5/vendor_perl/Constants.pm manually.
# Requires: perl(Locale::Constants)
# perl(Locale::Constants) requires perl(Locale::Codes)
# DB module is a builtin module, but perl package doesn't contain this provide.
# Requires: perl(DB)
# we also need perl(Pod::Plainer), we need to rpm this package ourself
Requires: perl(Locale::Codes)
Requires: perl(File::Spec)
Requires: perl(Scalar::Util)
Requires: perl(Test::Harness)
Requires: perl(Test::Simple)
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Pod::Plainer)

# python
Requires: /usr/bin/python
# java
Requires: redhat-lsb-core%{?_isa} = %{version}

Provides: lsb-languages-%{archname} = %{version}
Provides: lsb-languages-noarch = %{version}

%description languages
The Linux Standard Base (LSB) Languages module supports components for runtime
languages which are found on an LSB conforming system.

%package printing
Group: System Environment/Base
Summary: LSB Printing module support
# gLSB Printing Libraries
Requires: cups-libs
# gLSB Printing Command and Utilities
Requires: /usr/bin/foomatic-rip
Requires: /usr/bin/gs
Requires: redhat-lsb-core%{?_isa} = %{version}

Provides: lsb-printing-%{archname} = %{version}
Provides: lsb-printing-noarch = %{version}
Obsoletes: redhat-lsb-printing < %{version}

%description printing
The Linux Standard Base (LSB) Printing specifications define components that 
are required to be present on an LSB conforming system.

%package trialuse
Group: System Environment/Base
Summary: LSB Trialuse module support
Requires: redhat-lsb-submod-multimedia%{?_isa} = %{version}
Requires: redhat-lsb-submod-security%{?_isa} = %{version}
Requires: redhat-lsb-core%{?_isa} = %{version}

Provides: lsb-trialuse-%{archname} = %{version}
Provides: lsb-trialuse-noarch = %{version}

%description trialuse
The Linux Standard Base (LSB) Trialuse module support defines components
which are not required parts of the LSB Specification.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0 -b .triggerfix
%patch3 -p1 -b .arm

%build
cd lsb-release-%{upstreamlsbrelver}
make

%pre
# remove the extra symlink /bin/mailx -> /bin/mail
if [ -e /bin/mailx ]; then
   if [ -L /bin/mailx ]; then
     rm -f /bin/mailx
   fi 
fi

%install
# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir} $RPM_BUILD_ROOT/%{_lib} $RPM_BUILD_ROOT%{_mandir} \
         $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT/usr/lib/lsb \
         $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/ $RPM_BUILD_ROOT%{_sbindir} \
         $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}

# manually add Locale::Constants. This module is just an alias of Locale::Codes::Constants
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}/Locale
cp -p Constants.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Locale
cp -p Constants.pod $RPM_BUILD_ROOT%{perl_vendorlib}/Locale

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
cd lsb-release-%{upstreamlsbrelver}
make mandir=$RPM_BUILD_ROOT/%{_mandir} prefix=$RPM_BUILD_ROOT/%{_prefix} install
cd ..
# we keep more lsb information in /usr/share/lsb
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules   
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/submodules

# relations between modules and submodules
modules="core cxx desktop languages printing trialuse"
submodules="core perl python cpp toolkit-gtk toolkit-qt toolkit-qt3"
submodules="${submodules} xml multimedia security desktop-misc graphics graphics-ext"
submodules="${submodules} printing"

core="core security"
cxx="cpp"
desktop="desktop-misc graphics graphics-ext multimedia toolkit-gtk toolkit-qt toolkit-qt3"
desktop="${desktop} xml"
languages="perl python"
printing="printing"
trialuse="security multimedia"

for mod in ${modules};do
  touch $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/${mod}-%{lsbrelver}-%{archname}
  touch $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/${mod}-%{lsbrelver}-noarch
done

for submod in ${submodules};do
  touch $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/submodules/${submod}-%{lsbrelver}-%{archname}
  touch $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/submodules/${submod}-%{lsbrelver}-noarch
done
for moddir in ${modules};do
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/${moddir}
done

for submod in ${core};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/core/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/core/${submod}-%{lsbrelver}-noarch
done
for submod in ${cxx};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/cxx/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/cxx/${submod}-%{lsbrelver}-noarch
done
for submod in ${desktop};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/desktop/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/desktop/${submod}-%{lsbrelver}-noarch
done
for submod in ${languages};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/languages/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/languages/${submod}-%{lsbrelver}-noarch
done
for submod in ${printing};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/printing/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/printing/${submod}-%{lsbrelver}-noarch
done
for submod in ${trialuse};do
  ln -snf ../../submodules/${submod}-%{lsbrelver}-%{archname} \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/trialuse/${submod}-%{lsbrelver}-%{archname}
  ln -snf ../../submodules/${submod}-%{lsbrelver}-noarch \
$RPM_BUILD_ROOT%{_datadir}/lsb/%{lsbrelver}/modules/trialuse/${submod}-%{lsbrelver}-noarch
done

for LSBVER in %{lsbsover}; do
  ln -snf %{ldso} $RPM_BUILD_ROOT/%{_lib}/%{lsbldso}.$LSBVER
done

mkdir -p $RPM_BUILD_ROOT/bin

# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
# According to the lsb-core documentation provided by 
# http://refspecs.linux-foundation.org/LSB_3.2.0/LSB-Core-generic/LSB-Core-generic.pdf
# it's OK to put non binary in /usr/lib.
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/install_initd
ln -snf ../../../sbin/chkconfig $RPM_BUILD_ROOT/usr/lib/lsb/remove_initd
#ln -snf mail $RPM_BUILD_ROOT/bin/mailx

#mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xserver
#ln -snf /usr/%{_lib}/xserver/SecurityPolicy $RPM_BUILD_ROOT/usr/X11R6/lib/X11/xserver/SecurityPolicy
#ln -snf /usr/share/X11/fonts $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fonts
#ln -snf /usr/share/X11/rgb.txt  $RPM_BUILD_ROOT/usr/X11R6/lib/X11/rgb.txt

# According to https://bugzilla.redhat.com/show_bug.cgi?id=232918 , the '-static' option
# is imported against segfault error while running redhat_lsb_trigger
gcc $RPM_OPT_FLAGS -Os -static -fno-stack-protector -o redhat_lsb_trigger{.%{_target_cpu},.c} -DLSBSOVER='"%{lsbsover}"' \
  -DLDSO='"%{ldso}"' -DLSBLDSO='"/%{_lib}/%{lsbldso}"' -D_GNU_SOURCE
install -p -m 700 redhat_lsb_trigger.%{_target_cpu} \
  $RPM_BUILD_ROOT%{_sbindir}/redhat_lsb_trigger.%{_target_cpu}

cp -p redhat_lsb_init $RPM_BUILD_ROOT/bin/redhat_lsb_init

%triggerpostun -- glibc
if [ -x /usr/sbin/redhat_lsb_trigger.%{_target_cpu} ]; then
  /usr/sbin/redhat_lsb_trigger.%{_target_cpu}
fi

%ifnarch %{ix86}
  /sbin/sln %{ldso} /%{_lib}/%{lsbldso} || :
%else
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  else
    for LSBVER in %{lsbsover}; do
      /sbin/sln %{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif
if ! grep -s -q '^hosts: \+files \+dns *$' /etc/nsswitch.conf;then
    cat /etc/nsswitch.conf >%{_datadir}/lsb/nsswitch.conf.orig
    ed -s /etc/nsswitch.conf <<EOF
/^hosts: \+files \+/s/.*/hosts:      files dns/
w
q
EOF
    cat /etc/nsswitch.conf > %{_datadir}/lsb/nsswitch.conf
fi

%post
%ifarch %{ix86}
# make this softlink again for /emul
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif
if ! grep -s -q '^hosts: \+files \+dns *$' /etc/nsswitch.conf;then
     cat /etc/nsswitch.conf >%{_datadir}/lsb/nsswitch.conf.orig
     ed -s /etc/nsswitch.conf <<EOF
/^hosts: \+files \+/s/.*/hosts:      files dns/
w
q
EOF
cat /etc/nsswitch.conf >%{_datadir}/lsb/nsswitch.conf
fi

%preun
if [ $1 -eq 0 ];then
    if [ -e %{_datadir}/lsb/nsswitch.conf -a -e  %{_datadir}/lsb/nsswitch.conf.orig ];then
        if cmp -s %{_datadir}/lsb/nsswitch.conf /etc/nsswitch.conf;then
            cat %{_datadir}/lsb/nsswitch.conf.orig >/etc/nsswitch.conf
        fi
        rm -f %{_datadir}/lsb/{nsswitch.conf,nsswitch.conf.orig}
    fi
fi

%postun submod-security -p <lua>
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun submod-multimedia -p <lua>
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun core -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun cxx -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun desktop -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun languages -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun printing -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")
%postun trialuse -p <lua> 
os.remove("%{_datadir}/lsb/%{lsbrelver}/submodules")
os.remove("%{_datadir}/lsb/%{lsbrelver}/modules")
os.remove("%{_datadir}/lsb/%{lsbrelver}")
os.remove("%{_datadir}/lsb")

%files
%{_datadir}/lsb/

%files submod-security
%{_datadir}/lsb/%{lsbrelver}/submodules/security-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/security-%{lsbrelver}-noarch

%files submod-multimedia
%{_datadir}/lsb/%{lsbrelver}/submodules/multimedia-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/multimedia-%{lsbrelver}-noarch

%files core
%{_sysconfdir}/redhat-lsb
%dir %{_sysconfdir}/lsb-release.d
%{_mandir}/*/*
%{_bindir}/*
#/bin/mailx
/bin/redhat_lsb_init
/usr/lib/lsb
/%{_lib}/*so*
/lib/lsb*
%{_sbindir}/redhat_lsb_trigger.%{_target_cpu}
%{_datadir}/lsb/%{lsbrelver}/modules/core
%{_sysconfdir}/lsb-release.d/core*
%{_datadir}/lsb/%{lsbrelver}/submodules/core-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/core-%{lsbrelver}-noarch

%files cxx
%{_sysconfdir}/lsb-release.d/cxx*
%{_datadir}/lsb/%{lsbrelver}/modules/cxx
%{_datadir}/lsb/%{lsbrelver}/submodules/cpp-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/cpp-%{lsbrelver}-noarch

%files desktop
%{_sysconfdir}/lsb-release.d/desktop*
%{_datadir}/lsb/%{lsbrelver}/modules/desktop
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-gtk-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-gtk-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-qt-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-qt-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-qt3-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/toolkit-qt3-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/xml-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/xml-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/desktop-misc-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/desktop-misc-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/graphics-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/graphics-%{lsbrelver}-noarch
%{_datadir}/lsb/%{lsbrelver}/submodules/graphics-ext-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/graphics-ext-%{lsbrelver}-noarch

%files languages
%{_sysconfdir}/lsb-release.d/languages*
%{_datadir}/lsb/%{lsbrelver}/modules/languages
%{_datadir}/lsb/%{lsbrelver}/submodules/perl-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/perl-%{lsbrelver}-noarch
%{perl_vendorlib}/Locale/Constants.pm
%{perl_vendorlib}/Locale/Constants.pod
%{_datadir}/lsb/%{lsbrelver}/submodules/python-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/python-%{lsbrelver}-noarch

%files printing
%{_sysconfdir}/lsb-release.d/printing*
%{_datadir}/lsb/%{lsbrelver}/modules/printing
%{_datadir}/lsb/%{lsbrelver}/submodules/printing-%{lsbrelver}-%{archname}
%{_datadir}/lsb/%{lsbrelver}/submodules/printing-%{lsbrelver}-noarch

%files trialuse
%{_sysconfdir}/lsb-release.d/trialuse*
%{_datadir}/lsb/%{lsbrelver}/modules/trialuse


%changelog
* Mon Nov 05 2012 Parag <pnemade AT redhat DOT com> - 4.1-6
- Resolves:rh#873066 - missing dependency /bin/su moved to /usr/bin/su

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 xning <xning AT redhat DOT com> - 4.1-4
- Resolves:rh:#825261: redhat-lsb scripts blow away my /etc/nsswitch.conf

* Wed May 23 2012 Parag <pnemade AT redhat DOT com> - 4.1-3
- Resolves:rh#824305: Dependency glibc-common%{?_isa} should be changed to glibc-common only

* Mon May 14 2012 xning <xning AT redhat DOT com> - 4.1-2
- Resolves:rh:#806190: gethostbyaddr sets h_errno to 3, not HOST_NOT_FOUND
- Resolves:rh:#799284: perl(Pod::Plainer) is required by LSB 4.1
- Resolves:rh:#821308: redhat-lsb 4.1 test libpn12.so.0 failed on fedora 17

* Mon Mar 19 2012 xning <xning AT redhat DOT com> - 4.1-1
- Update to 4.1 release
- Added -core, -cxx, -desktop, -languages, -printing modules as subpackages
- Added submod-security, -submod-multimedia subpackages
- Implements http://refspecs.linux-foundation.org/LSB_4.1.0/ 
- Resolves:rh#800249: new package update review by Parag.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Parag <pnemade AT redhat DOT com> - 4.0-10
- Resolves:rh#758383:- redhat-lsb does not pull in required perl-Pod-Perldoc

* Wed Nov 30 2011 Parag <pnemade AT redhat DOT com> - 4.0-9
- Resolves:rh#738256:- redhat-lsb fails to build on ARM

* Thu Oct 13 2011 Parag <pnemade AT redhat DOT com> - 4.0-8
- Resolves:rh#745100: Add requires: perl-Digest-MD5

* Wed Oct 12 2011 Parag <pnemade AT redhat DOT com> - 4.0-7
- Resolves:rh#654689,rh#736822
- Added dependencies for perl-Locale-Codes and perl-Class-ISA

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Parag <pnemade AT redhat.com> - 4.0-5
- Fix directory ownership issue for %%{_sysconfdir}/lsb-release.d
- Fix duplicate files issue as reported in bodhi testing for 4.0-4

* Fri Jun 25 2010 Parag <pnemade AT redhat.com> - 4.0-4
- Revert license back to GPLv2

* Thu Jun 24 2010 Parag <pnemade AT redhat.com> - 4.0-3
- Resolves:rh#585858:-redhat-lsb-graphics broken

* Fri Jan 15 2010 Lawrence Lim <llim@redhat.com> - 4.0-2
- update spec file to split package into core, desktop and printing (Curtis Doty, #472633)

* Fri Jan 8 2010 Lawrence Lim <llim@redhat.com> - 4.0-1
- update to LSB4.0

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-7
- apply fix from bz514760 (thanks to Jakub Jelinek)

* Wed Oct 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-6
- apply fix from bz485367 (thanks to Jon Thomas)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Jens Petersen <petersen@redhat.com>
- improve url to LSB WG

* Thu Apr 23 2009 Jens Petersen <petersen@redhat.com> - 3.2-4
- use dist tag (Debarshi, #496553)
- update to ix86 (caillon)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Hao Liu <hliu@redhat.com> 3.2-2
- Modify "Requires: /usr/bin/mailx" to "Requires: mailx" (Bug #460249)

* Wed Aug 18 2008 Hao Liu <hliu@redhat.com> 3.2-1
- Port forward to LSB 3.2
- Remove symlink for mailx if user is upgrading from the redhat-lsb of older version 
- Since F10 put mailx under /usr/bin, change the corresponding requires

* Thu Aug 5 2008 Hao Liu <hliu@redhat.com> - 3.1-22
- Remove 2 requires which provided by redhat-lsb
- Add comments explaining why hard-coded path is kept
- Resolve some hard-coded path problems
- Add comments explaining why importing '-static' option while compiling redhat_lsb_trigger
- Replace %{_libdir}/lsb with /usr/lib/lsb
- Replace /%{_lib}/* with /%{_lib}/*so*
- Replace /lib/lsb with /lib/lsb*

* Thu Jul 31 2008 Lawrence Lim <llim@redhat.com> - 3.1-21
- remove symlink for mailx (Bug #457241)

* Wed Apr 16 2008 Mats Wichmann <mats@freestandards.org> 3.2-1
- port forward to LSB 3.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-20
- Autorebuild for GCC 4.3

* Wed Oct 3 2007 Lawrence Lim <llim@redhat.com> - 3.1-19
- fix build issue on ppc - (.opd+0x10): multiple definition of `__libc_start_main'

* Fri Sep 21 2007 Lawrence Lim <llim@redhat.com> - 3.1-18
- fix build issue in minimal build root (Bug #265241)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.1-17
- Rebuild for selinux ppc32 issue.

* Fri Aug 20 2007 Lawrence Lim <llim@redhat.com> - 3.1-16
- update spec file in accordance to feedback provided through merge review - merge-review.patch - #226363

* Wed Jul 18 2007 Lawrence Lim <llim@redhat.com> - 3.1-15.f8
- Resolved: #239842 - /lib/lsb/init-functions shall use aliases but not functions
- forward port the patch from 3.1-12.3.EL which fix #217566, #233530, #240916

* Wed Jul 2 2007 Lawrence Lim <llim@redhat.com> - 3.1-14.fc7
- fixed Bug 232918 for new glibc version

* Tue Jun 26 2007 Lawrence Lim <llim@redhat.com> - 3.1-12.3.EL
- Resolves: #217566 - rewrite /lib/lsb/init-functions file needs to define the commands as true shell functions rather than aliases.
- Resolves: #233530 - LSB pidofproc misspelled as pidofprof.
- Resolves: #240916 - "log_warning_message" replaced with "log_warning_msg" per the LSB 3.1 spec

* Wed Dec 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-12.2.EL
- Resolves: bug 217566
- revise patch

* Wed Nov 29 2006 Lawrence Lim <llim@redhat.com> - 3.1-12
- replaced aliases with functions in /lib/lsb/init-functions; Bug 217566

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.1-11
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.3
- Fix upgrade issue; Bug 202548 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1-10.2.1
- rebuild

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.2
- for some strange reason, ld-lsb-x86-64.so need to be ld-lsb-x86-64.so.3 (LSB3.0) rather than ld-lsb-x86-64.so.3.1 (LSB3.1)

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.1
- generate spec file on RHEL5-Alpha system
- fix vsw4 test suite setup by creating symlink for X11 SecurityPolicy and XFontPath

* Thu Jun 22 2006 Lawrence Lim <llim@redhat.com> - 3.0-10
- Rewrite most part of the mkredhat-lsb to obtain information directly via specdb 
  rather than sniffing through sgml
- remove redundent script and bump up tarball version

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Leon Ho <llch@redhat.com> 3.0-9
- Migrated back to rawhide

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-8.EL
- Added libstdc++.so.6/libGL.so.1 requirement (RH#154605)

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-7.EL
- Fixed multilib problem on lsb_release not to read /etc/lsb-release and solely
  depends on /etc/lsb-release.d/ (Advised by LSB committee)
- Removed /etc/lsb-release (Advised by LSB committee)

* Mon Aug  1 2005 Leon Ho <llch@redhat.com> 3.0-6.EL
- Made the /etc/lsb-release useful (RH#154605)
- Added redhat_lsb_trigger to fix RH#160585 (Jakub Jelinek)
- Fixed AMD64 base libraries requirement parsing (RH#154605)

* Tue Jul 26 2005 Leon Ho <llch@redhat.com> 3.0-5.EL
- Fixed redhat-lsb's mkredhat-lsb on fetching lib and 
  cmd requirements

* Mon Jul 18 2005 Leon Ho <llch@redhat.com> 3.0-4.EL
- Rebuilt

* Tue Jul 05 2005 Leon Ho <llch@redhat.com> 3.0-3.EL
- Disabled support for LSB 1.3 and 2.0

* Mon Jun 20 2005 Leon Ho <llch@redhat.com> 3.0-2.EL
- Upgraded to lsb-release 2.0

* Thu Jun 09 2005 Leon Ho <llch@redhat.com> 3.0-1.EL
- Moved to LSB 3.0

* Wed Apr 13 2005 Leon Ho <llch@redhat.com> 1.3-10
- Fixed ix86 package with ia32 emul support 

* Tue Feb 01 2005 Leon Ho <llch@redhat.com> 1.3-9
- Sync what we have changed on the branches
  Wed Nov 24 2004 Harald Hoyer <harald@redhat.com>
  - added post section to recreate the softlink in emul mode (bug 140739)
  Mon Nov 15 2004 Phil Knirsch <pknirsch@redhat.com>
  Tiny correction of bug in new triggers

* Mon Jan 24 2005 Leon Ho <llch@redhat.com> 1.3-8
- Add support provide on lsb-core-* for each arch

* Fri Jan 21 2005 Leon Ho <llch@redhat.com> 1.3-7
- Add to support multiple LSB test suite version
- Add %endif in trigger postun

* Thu Nov 11 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-6
- Fixed invalid sln call for trigger in postun on ia64 (#137647)

* Mon Aug 09 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-4
- Bump release and rebuilt for RHEL4.

* Thu Jul 24 2003 Matt Wilson <msw@redhat.com> 1.3-3
- fix lsb ld.so name for ia64 (#100613)

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- use /usr/lib/lsb for install_initd, remove_initd

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- add ia64 x86_64 ppc ppc64 s390 s390x

* Tue Feb 18 2003 Matt Wilson <msw@redhat.com> 1.3-1
- 1.3

* Wed Sep  4 2002 Matt Wilson <msw@redhat.com>
- 1.2.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 27 2002 Matt Wilson <msw@redhat.com>
- addeed trigger on glibc to re-establish the ld-lsb.so.1 symlink in the
  forced downgrade case.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com>
- add initscripts support

* Thu Jan 24 2002 Matt Wilson <msw@redhat.com>
- Initial build.
