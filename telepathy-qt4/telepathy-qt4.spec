Name:    telepathy-qt4
Version: 0.9.0
Release: 1%{?dist}
Summary: A high-level bindings for Telepathy

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
BuildRequires: pkgconfig(telepathy-farsight) 
%if 0%{?fedora} > 16
# unit tests
BuildRequires: pkgconfig(telepathy-glib) >= 0.17.2
BuildRequires: pkgconfig(gio-2.0)
%endif

%description
Telepathy-qt4 are high level bindings for Telepathy and provides both
the low level 1:1 auto generated API, and a high-level API build
on top of that, in the same library.

%package devel
Summary: Development files for %{name}
Provides: telepathy-qt-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: telepathy-filesystem
%description devel
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


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS NEWS README ChangeLog
%{_libdir}/libtelepathy-qt4.so.2*
%{_libdir}/libtelepathy-qt4-farsight.so.2*

%files devel
%doc HACKING
%{_includedir}/telepathy-qt4/
%{_libdir}/libtelepathy-qt4.so
%{_libdir}/libtelepathy-qt4-farsight.so
%{_libdir}/pkgconfig/TelepathyQt4.pc
%{_libdir}/pkgconfig/TelepathyQt4Farsight.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/TelepathyQt4/
%{_libdir}/cmake/TelepathyQt4Farsight/


%changelog
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
