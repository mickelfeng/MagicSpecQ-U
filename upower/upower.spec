Summary:        Power Management Service
Name:           upower
Version:        0.9.15
Release:        4%{?dist}
License:        GPLv2+
Group:          System Environment/Libraries
URL:            http://hal.freedesktop.org/releases/
Source0:        http://hal.freedesktop.org/releases/upower-%{version}.tar.xz
BuildRequires:  sqlite-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  libgudev1-devel
%ifnarch s390 s390x
BuildRequires:  libusb1-devel
BuildRequires:  libimobiledevice-devel
%endif
BuildRequires:  glib2-devel >= 2.6.0
BuildRequires:  dbus-devel  >= 1.2
BuildRequires:  dbus-glib-devel >= 0.82
BuildRequires:  polkit-devel >= 0.92
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
Requires:       polkit >= 0.92
Requires:       udev
Requires:       pm-utils >= 1.2.2.1
Requires:       gobject-introspection

%description
UPower (formerly DeviceKit-power) provides a daemon, API and command
line tools for managing power devices attached to the system.

%package devel
Summary: Headers and libraries for UPower
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: DeviceKit-power-devel < 1:0.9.0-2

%description devel
Headers and libraries for UPower.

%prep
%setup -q

%build
%configure \
        --enable-gtk-doc \
        --disable-static \
        --enable-introspection \
%ifarch s390 s390x
	--with-backend=dummy
%endif

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

mkdir  -p %{buildroot}%{_prefix}/lib/udev/
mv %{buildroot}/lib/udev/rules.d %{buildroot}%{_prefix}/lib/udev/

magic_rpm_clean.sh
%find_lang upower || touch upower.lang

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f upower.lang
%defattr(-,root,root,-)
%doc NEWS COPYING AUTHORS HACKING README
%{_libdir}/libupower-glib.so.*
%{_sysconfdir}/dbus-1/system.d/*.conf
%ifnarch s390 s390x
%{_prefix}/lib/udev/rules.d/*.rules
%endif
%dir %{_localstatedir}/lib/upower
%dir %{_sysconfdir}/UPower
%config %{_sysconfdir}/UPower/UPower.conf
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/girepository-1.0/*.typelib
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/dbus-1/system-services/*.service

%files devel
%defattr(-,root,root,-)
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/UPower
%{_datadir}/gtk-doc/html/UPower/*
%{_libdir}/libupower-glib.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_includedir}/libupower-glib
%{_includedir}/libupower-glib/up-*.h
%{_includedir}/libupower-glib/upower.h

%changelog
* Mon Apr 23 2012 Liu Di <liudidi@gmail.com> - 0.9.15-4
- 为 Magic 3.0 重建

* Sun Apr 22 2012 Liu Di <liudidi@gmail.com> - 0.9.15-3
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Richard Hughes <rhughes@redhat.com> - 0.9.15-1
- Use linear regression to get better predicted battery times.
- Don't spam the log when we're saving history when on low power.
- Don't assert when the power_supply device type is usb.

* Mon Oct 03 2011 Richard Hughes <rhughes@redhat.com> - 0.9.14-1
- New upstream release.
- Fix a bug when detecting if suspend and hibernate are supported.

* Mon Sep 05 2011 Richard Hughes <rhughes@redhat.com> - 0.9.13-1
- New upstream release.
- Blacklist wacom battery devices as not power-supply devices.

* Mon Jul 04 2011 Richard Hughes <rhughes@redhat.com> - 0.9.12-1
- New upstream release.
- Fix how we estimate the device rate for batteries that do not provide
  this data.

* Wed May 25 2011 Richard Hughes <rhughes@redhat.com> - 0.9.11-1
- New upstream release.
- Only include glib-unix.h if the GLib version is >= 2.29.4

* Tue May 03 2011 Richard Hughes <rhughes@redhat.com> - 0.9.10-1
- New upstream release.
- Add a config option 'IgnoreLid' for users with broken lid switches
- Consider a discharging UPS as "on battery"
- Support batteries that report both energy and charge
- Use the new threadsafe signal handling support in GLib

* Tue Mar 23 2011 Colin Walters <walters@verbum.org> - 0.9.9-2
- Move typelib file to main package; it should go along with the .so;
  i.e. gnome-shell shouldn't require upower-devel.

* Mon Mar 21 2011 Richard Hughes <rhughes@redhat.com> - 0.9.9-1
- New upstream release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Richard Hughes <rhughes@redhat.com> - 0.9.8-1
- New upstream release.

* Sun Dec 26 2010 Bastien Nocera <bnocera@redhat.com> 0.9.7-2
- Rebuild for new libimobiledevice

* Mon Nov 01 2010 Richard Hughes <rhughes@redhat.com> - 0.9.7-1
- New upstream release.
- Add support for controlling leds keyboard backlight
- Fix building with gobject-introspection 0.9.10

* Mon Oct 04 2010 Richard Hughes <rhughes@redhat.com> - 0.9.6-1
- New upstream release.
- Fix compile with the latest PolicyKit release.
- Only save by default 7 days data to stop the log files becoming huge.
- Do not continue to poll the serial port if there is no Watts Up Pro adaptor.
- Fix the build with new versions of gobject-introspection.
- Resolves #634228

* Wed Sep 29 2010 jkeating - 0.9.5-10
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.5-9
- Rebuild against newer gobject-introspection

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.5-8
- Co-own /usr/share/gtk-doc

* Tue Aug 17 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.5-7
- Some fixes for dbus error handling

* Tue Aug 10 2010 Richard Hughes <rhughes@redhat.com> - 0.9.5-5
- Ensure we've initialized errors when calling into PolicyKit.
- Resolves: #622830

* Mon Jul 26 2010 Bastien Nocera <bnocera@redhat.com> 0.9.5-4
- Add support for iDevice battery checking

* Sat Jul 17 2010 Dan Horák <dan[at]danny.cz> - 0.9.5-3
- use dummy backend on s390(x) because the Linux backend requires USB

* Mon Jul 12 2010 Colin Walters <walters@verbum.org> - 0.9.5-2
- Rebuild against new gobject-introspection

* Mon Jul 12 2010 Richard Hughes <rhughes@redhat.com> - 0.9.5-1
- New upstream release.

* Mon May 17 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.4-1
- Make my laptop suspend again when I close the lid

* Thu May 06 2010 Richard Hughes <rhughes@redhat.com> - 0.9.3-1
- New upstream release.

* Tue Apr 06 2010 Richard Hughes <rhughes@redhat.com> - 0.9.2-1
- New upstream release.

* Wed Mar 17 2010 Richard Hughes <rhughes@redhat.com> - 0.9.1-4
- It seems people don't like pain.

* Mon Mar 15 2010 Richard Hughes <rhughes@redhat.com> - 0.9.1-3
- Obsolete DeviceKit-power.

* Mon Mar 15 2010 Richard Hughes <rhughes@redhat.com> - 0.9.1-2
- Actually enable the introspection support.

* Wed Mar 03 2010 Richard Hughes <rhughes@redhat.com> - 0.9.1-1
- Initial release of 0.9.1

