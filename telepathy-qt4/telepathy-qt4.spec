Name:    telepathy-qt4
Version: 0.9.1
Release: 3%{?dist}
Summary: High-level bindings for Telepathy

License: LGPLv2+
URL:     http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
Source0: http://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-%{version}.tar.gz

## upstreamable patches
# fix for error: 'intptr_t' was not declared in this scope
Patch50:  telepathy-qt-0.9.0-gcc47.patch

Provides: telepathy-qt = %{version}-%{release} 
Provides: telepathy-qt%{?_isa} = %{version}-%{release}

BuildRequires: cmake
BuildRequires: dbus-python python2-devel
BuildRequires: doxygen
BuildRequires: pkgconfig(gstreamer-interfaces-0.10) 
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtNetwork) pkgconfig(QtXml)
%define farstream 1
BuildRequires: pkgconfig(telepathy-farstream)
# unit tests
BuildRequires: pkgconfig(telepathy-glib) >= 0.17.2
BuildRequires: pkgconfig(gio-2.0)

Requires: telepathy-mission-control

%description
Telepathy-qt4 are high level bindings for Telepathy and provides both
the low level 1:1 auto generated API, and a high-level API build
on top of that, in the same library.

%package devel
Summary: Development files for %{name}
Provides: telepathy-qt-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: telepathy-filesystem
Requires: %{name}-farstream%{?_isa} = %{version}-%{release}
Obsoletes: telepathy-qt4-farstream-devel < 0.9.1-2
Provides:  telepathy-qt4-farstream-devel = %{version}-%{release} 
Provides:  telepathy-qt-farstream-devel = %{version}-%{release}

%description devel
%{summary}.

%package farsight
Summary: Farsight %{name} bindings
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:  telepathy-qt-farsight = %{version}-%{release}
%description farsight
%{summary}.

%package farstream
Summary: Farstream %{name} bindings
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: telepathy-qt4-farsight < %{version}-%{release}
Provides:  telepathy-qt-farstream = %{version}-%{release}
%description farstream 
%{summary}.



%prep
%setup -q -n telepathy-qt-%{version}

%patch50 -p1 -b .gcc47


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
magic_rpm_clean.sh

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS NEWS README ChangeLog
%{_libdir}/libtelepathy-qt4.so.2*

%post farstream -p /sbin/ldconfig
%postun farstream -p /sbin/ldconfig

%files farstream
%{_libdir}/libtelepathy-qt4-farstream.so.2*

%files devel
%doc HACKING
%dir %{_includedir}/telepathy-qt4/
%{_includedir}/telepathy-qt4/TelepathyQt/
%{_libdir}/libtelepathy-qt4.so
%{_libdir}/pkgconfig/TelepathyQt4.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/TelepathyQt4/
%{_libdir}/libtelepathy-qt4-farstream.so
%{_libdir}/pkgconfig/TelepathyQt4Farstream.pc
%{_libdir}/cmake/TelepathyQt4Farstream/


%changelog
* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-3
- -farsight subpkg (f16)

* Mon Apr 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-2
- drop -farstream-devel subpkg

* Sat Mar 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-1
- 0.9.1
- -farstream(-devel) subpkgs

* Tue Mar 06 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-3
- drop telepathy-farsight support (awaiting upstream -farstream love)

* Fri Feb 17 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2
- Requires: telepathy-mission-control

* Wed Jan 25 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- telepathy-qt-0.9.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-2
- drop Requires: gnome-keyring

* Sat Nov 19 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.3-1
- 0.7.3
- pkgconfig-style deps

* Wed Aug 10 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-1
- 0.7.2
- Requires: gnome-keyring

* Fri Jul 15 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.7.1-1
- initial package
