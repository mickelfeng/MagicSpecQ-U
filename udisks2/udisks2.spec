%define glib2_version                   2.31.13
%define gobject_introspection_version   1.30.0
%define polkit_version                  0.101
%define udev_version                    173
%define libatasmart_version             0.12
%define dbus_version                    1.4.0

Summary: Disk Manager
Name: udisks2
Version: 1.93.0
Release: 2%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://www.freedesktop.org/wiki/Software/udisks
Source0: http://udisks.freedesktop.org/releases/udisks-%{version}.tar.bz2
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gobject-introspection-devel >= %{gobject_introspection_version}
BuildRequires: polkit-devel >= %{polkit_version}
BuildRequires: intltool
BuildRequires: libatasmart-devel >= %{libatasmart_version}
BuildRequires: libgudev1-devel >= %{udev_version}
BuildRequires: gtk-doc
BuildRequires: systemd-devel
# needed to pull in the system bus daemon
Requires: dbus >= %{dbus_version}
# needed to pull in the udev daemon
Requires: udev >= %{udev_version}
# we need at least this version for bugfixes / features etc.
Requires: libatasmart >= %{libatasmart_version}
# for mount, umount, mkswap
Requires: util-linux
# for mkfs.ext3, mkfs.ext3, e2label
Requires: e2fsprogs
# for mkfs.xfs, xfs_admin
Requires: xfsprogs
# for mkfs.vfat
Requires: dosfstools
# for mlabel
Requires: mtools
# for mkntfs - no ntfsprogs on ppc, though
%ifnarch ppc ppc64
Requires: ntfsprogs
%endif
# for partitioning
Requires: parted
Requires: gdisk
# for LUKS devices
Requires: cryptsetup-luks
Requires: acl

# for /proc/self/mountinfo, only available in 2.6.26 or higher
Conflicts: kernel < 2.6.26

%description
udisks provides a daemon, D-Bus API and command line tools for
managing disks and storage devices. This package is for the udisks 2.x
series.

%package -n libudisks2
Summary: Dynamic library to access the udisks daemon
Group: System Environment/Libraries
License: LGPLv2+

%description -n libudisks2
This package contains the dynamic library libudisks2, which provides
access to the udisks daemon. This package is for the udisks 2.x
series.

%package -n libudisks2-devel
Summary: Development files for libudev
Group: Development/Libraries
Requires: libudisks2 = %{version}-%{release}
Requires: pkgconfig
License: LGPLv2+

%description -n libudisks2-devel
This package contains the development files for the library
libudisks2, a dynamic library, which provides access to the udisks
daemon. This package is for the udisks 2.x series.

%prep
%setup -q -n udisks-%{version}

%build
%configure --enable-gtk-doc
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang %{name}

%post -n libudisks2 -p /sbin/ldconfig

%postun -n libudisks2 -p /sbin/ldconfig

%files -f %{name}.lang
%doc README AUTHORS NEWS COPYING HACKING

%{_sysconfdir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_sysconfdir}/bash_completion.d/udisksctl-bash-completion.sh
%{_prefix}/lib/systemd/system/udisks2.service
%{_prefix}/lib/udev/rules.d/80-udisks2.rules
%{_sbindir}/umount.udisks2

%dir %{_prefix}/lib/udisks2
%{_prefix}/lib/udisks2/udisksd

%{_bindir}/udisksctl

%{_mandir}/man1/*
%{_mandir}/man8/*

%{_datadir}/polkit-1/actions/org.freedesktop.udisks2.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service

# Permissions for local state data are 0700 to avoid leaking information
# about e.g. mounts to unprivileged users
%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks2

%files -n libudisks2
%{_libdir}/libudisks2.so.*
%{_libdir}/girepository-1.0/UDisks-2.0.typelib

%files -n libudisks2-devel
%{_libdir}/libudisks2.so
%dir %{_includedir}/udisks2
%dir %{_includedir}/udisks2/udisks
%{_includedir}/udisks2/udisks/*.h
%{_datadir}/gir-1.0/UDisks-2.0.gir
%dir %{_datadir}/gtk-doc/html/udisks2
%{_datadir}/gtk-doc/html/udisks2/*
%{_libdir}/pkgconfig/udisks2.pc

# Note: please don't forget the %{?dist} in the changelog. Thanks
%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 1.93.0-2
- 为 Magic 3.0 重建

* Mon Mar 05 2012 David Zeuthen <davidz@redhat.com> - 1.93.0-1%{?dist}
- Update to release 1.93.0

* Thu Feb 23 2012 David Zeuthen <davidz@redhat.com> - 1.92.0-2%{?dist}
- Fix build

* Thu Feb 23 2012 David Zeuthen <davidz@redhat.com> - 1.92.0-1%{?dist}
- Update to release 1.92.0

* Wed Feb 22 2012 David Zeuthen <davidz@redhat.com> - 1.91.0-2%{?dist}
- Avoid using $XDG_RUNTIME_DIR/media for now

* Mon Feb 06 2012 David Zeuthen <davidz@redhat.com> - 1.91.0-1%{?dist}
- Update to release 1.91.0

* Fri Jan 21 2012 David Zeuthen <davidz@redhat.com> - 1.90.0-3%{?dist}
- Manually set PATH, if not set

* Fri Jan 20 2012 David Zeuthen <davidz@redhat.com> - 1.90.0-2%{?dist}
- Rebuild

* Fri Jan 20 2012 David Zeuthen <davidz@redhat.com> - 1.90.0-1%{?dist}
- Update to release 1.90.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.0-0.git20111128.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 David Zeuthen <davidz@redhat.com> - 1.90.0-0.git20111128%{?dist}
- Updated for review comments (#756046)

* Mon Nov 22 2011 David Zeuthen <davidz@redhat.com> - 1.90.0-0.git20111122%{?dist}
- Initial packaging of udisks2
