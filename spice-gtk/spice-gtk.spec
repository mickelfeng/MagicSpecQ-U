# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

%define with_gtk3 0
%if 0%{?fedora} >= 15
%define with_gtk3 1
%endif

#define _version_suffix -ab64

Name:           spice-gtk
Version:        0.9
Release:        1%{?dist}
Summary:        A GTK+ widget for SPICE clients

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://spice-space.org/page/Spice-Gtk
Source0:        http://www.spice-space.org/download/gtk/%{name}-%{version}%{?_version_suffix}.tar.bz2

BuildRequires: intltool
BuildRequires: gtk2-devel >= 2.14
BuildRequires: spice-protocol >= 0.10.1
BuildRequires: usbredir-devel >= 0.3.3
BuildRequires: libusb1-devel >= 1.0.9
BuildRequires: libgudev1-devel
BuildRequires: perl-Text-CSV
BuildRequires: pixman-devel openssl-devel libjpeg-turbo-devel
BuildRequires: celt051-devel pulseaudio-libs-devel
BuildRequires: pygtk2-devel python-devel zlib-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libcacard-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libacl-devel
BuildRequires: polkit-devel
BuildRequires: gtk-doc
BuildRequires: vala-tools
%if %{with_gtk3}
BuildRequires: gtk3-devel
%endif
# Hack because of bz #613466
BuildRequires: libtool
Requires: spice-glib%{?_isa} = %{version}-%{release}

ExclusiveArch: %{ix86} x86_64

%description
Client libraries for SPICE desktop servers.

%package devel
Summary: Development files to build GTK2 applications with spice-gtk-2.0
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: spice-glib-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: gtk2-devel

%description devel
spice-client-gtk-2.0 provides a SPICE viewer widget for GTK2.

Libraries, includes, etc. to compile with the spice-gtk2 libraries

%package -n spice-glib
Summary: A GObject for communicating with Spice servers
Group: Development/Libraries

%description -n spice-glib
spice-client-glib-2.0 is a SPICE client library for GLib2.

%package -n spice-glib-devel
Summary: Development files to build Glib2 applications with spice-glib-2.0
Group: Development/Libraries
Requires: spice-glib%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel

%description -n spice-glib-devel
spice-client-glib-2.0 is a SPICE client library for GLib2.

Libraries, includes, etc. to compile with the spice-glib-2.0 libraries


%if %{with_gtk3}
%package -n spice-gtk3
Summary: A GTK3 widget for SPICE clients
Group: Development/Libraries
Requires: spice-glib%{?_isa} = %{version}-%{release}

%description -n spice-gtk3
spice-client-glib-3.0 is a SPICE client library for Gtk3.

%package -n spice-gtk3-devel
Summary: Development files to build GTK3 applications with spice-gtk-3.0
Group: Development/Libraries
Requires: spice-gtk3%{?_isa} = %{version}-%{release}
Requires: spice-glib-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: gtk3-devel

%description -n spice-gtk3-devel
spice-client-gtk-3.0 provides a SPICE viewer widget for GTK3.

Libraries, includes, etc. to compile with the spice-gtk3 libraries

%package -n spice-gtk3-vala
Summary: Vala bindings for the spice-gtk-3.0 library
Group: Development/Libraries
Requires: spice-gtk3%{?_isa} = %{version}-%{release}
Requires: spice-gtk3-devel%{?_isa} = %{version}-%{release}

%description -n spice-gtk3-vala
A module allowing use of the spice-gtk-3.0 widget from vala
%endif

%package python
Summary: Python bindings for the spice-gtk-2.0 library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python
SpiceClientGtk module provides a SPICE viewer widget for GTK2.

A module allowing use of the spice-gtk-2.0 widget from python

%package tools
Summary: Spice-gtk tools
Group: Applications/Internet
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Simple clients for interacting with SPICE servers.
spicy is a client to a SPICE desktop server.
snappy is a tool to capture screen-shots of a SPICE desktop.


%prep
%setup -q -n spice-gtk-%{version}%{?_version_suffix} -c

if [ -n '%{?_version_suffix}' ]; then
  mv spice-gtk-%{version}%{?_version_suffix} spice-gtk-%{version}
fi

%if %{with_gtk3}
cp -a spice-gtk-%{version} spice-gtk3-%{version}
%endif


%build

cd spice-gtk-%{version}
%configure --with-gtk=2.0 --enable-gtk-doc --with-usb-acl-helper-dir=%{_libexecdir}/spice-gtk/
make %{?_smp_mflags}
cd ..

%if %{with_gtk3}
cd spice-gtk3-%{version}
%configure --with-gtk=3.0 --enable-vala --with-usb-acl-helper-dir=%{_libexecdir}/spice-gtk/
make %{?_smp_mflags}
cd ..
%endif


%install

%if %{with_gtk3}
cd spice-gtk3-%{version}
make install DESTDIR=%{buildroot}
cd ..
%endif

cd spice-gtk-%{version}
make install DESTDIR=%{buildroot}
cd ..

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/python*/site-packages/*.a
rm -f %{buildroot}%{_libdir}/python*/site-packages/*.la
%find_lang %{name}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n spice-glib -p /sbin/ldconfig
%postun -n spice-glib -p /sbin/ldconfig

%if %{with_gtk3}
%post -n spice-gtk3 -p /sbin/ldconfig
%postun -n spice-gtk3 -p /sbin/ldconfig
%endif


%files
%doc spice-gtk-%{version}/AUTHORS
%doc spice-gtk-%{version}/COPYING
%doc spice-gtk-%{version}/README
%doc spice-gtk-%{version}/NEWS
%{_libdir}/libspice-client-gtk-2.0.so.*
%{_libdir}/girepository-1.0/SpiceClientGtk-2.0.typelib

%files devel
%{_libdir}/libspice-client-gtk-2.0.so
%{_includedir}/spice-client-gtk-2.0
%{_libdir}/pkgconfig/spice-client-gtk-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-2.0.gir

%files -n spice-glib -f %{name}.lang
%{_libdir}/libspice-client-glib-2.0.so.*
%{_libdir}/libspice-controller.so.*
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib
%{_libexecdir}/spice-gtk/spice-client-glib-usb-acl-helper
%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy

%files -n spice-glib-devel
%{_libdir}/libspice-client-glib-2.0.so
%{_libdir}/libspice-controller.so
%{_includedir}/spice-client-glib-2.0
%{_includedir}/spice-controller/*
%{_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{_libdir}/pkgconfig/spice-controller.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir
%{_datadir}/vala/vapi/spice-protocol.vapi
%doc %{_datadir}/gtk-doc/html/*

%if %{with_gtk3}
%files -n spice-gtk3
%{_libdir}/libspice-client-gtk-3.0.so.*
%{_libdir}/girepository-1.0/SpiceClientGtk-3.0.typelib

%files -n spice-gtk3-devel
%{_libdir}/libspice-client-gtk-3.0.so
%{_includedir}/spice-client-gtk-3.0
%{_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-3.0.gir

%files -n spice-gtk3-vala
%{_datadir}/vala/vapi/spice-client-glib-2.0.deps
%{_datadir}/vala/vapi/spice-client-glib-2.0.vapi
%{_datadir}/vala/vapi/spice-client-gtk-3.0.deps
%{_datadir}/vala/vapi/spice-client-gtk-3.0.vapi
%endif

%files python
%{_libdir}/python*/site-packages/SpiceClientGtk.so

%files tools
%{_bindir}/snappy
%{_bindir}/spicy
%{_bindir}/spicy-stats

%changelog
* Mon Jan 30 2012 Hans de Goede <hdegoede@redhat.com> - 0.9-1
- New upstream release 0.9

* Mon Jan 16 2012 Hans de Goede <hdegoede@redhat.com> - 0.8-1
- New upstream release 0.8
- Various small specfile improvements
- Enable vala bindings

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> 0.7.39-2
- Rebuild to break bogus libpng dependency
- Fix summaries for gtk3 subpackages to not talk about gtk2

* Fri Sep  2 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.39-1
- Update to git snapshot 0.7.39-ab64, to add usbredir support

* Tue Jul 26 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.7.1-1
- Upstream version 0.7.1-d5a8 (fix libtool versionning)

* Tue Jul 19 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.7-1
- Upstream release 0.7

* Wed May 25 2011 Christophe Fergeau <cfergeau@redhat.com> - 0.6-1
- Upstream release 0.6

* Tue Mar  1 2011 Hans de Goede <hdegoede@redhat.com> - 0.5-6
- Fix spice-glib requires in .pc file (#680314)

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 0.5-5
- Fix build against glib 2.28

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> - 0.5-4
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 0.5-2
- Rebuild against newer gtk

* Thu Jan 27 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5-1
- Upstream release 0.5

* Fri Jan 14 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4-2
- Add support for parallel GTK3 build

* Mon Jan 10 2011 Dan Horák <dan[at]danny.cz> - 0.4-2
- add ExclusiveArch as only x86 is supported

* Sun Jan 09 2011 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4-1
- Upstream release 0.4
- Initial release (#657403)

* Thu Nov 25 2010 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.1.0-1
- Initial packaging
