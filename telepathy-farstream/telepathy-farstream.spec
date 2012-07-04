%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           telepathy-farstream
Version:        0.4.0
Release:        2%{?dist}
Summary:        Telepathy client library to handle Call channels

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Telepathy-Farsight
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  telepathy-glib-devel >= 0.17.5
BuildRequires:  farstream-devel >= 0.1.0
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  python-devel
BuildRequires:  gstreamer-python-devel
BuildRequires:  pygobject2-devel

## Obsolete telepathy-farsight with Fedora 17
Provides:       telepathy-farsight = %{version}
Obsoletes:      telepathy-farsight < 0.0.20


%description
%{name} is a Telepathy client library that uses Farstream to handle
Call channels.


%package        python
Summary:        Python binding for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

## Obsolete telepathy-farsight with Fedora 17
Provides:       telepathy-farsight-python = %{version}
Obsoletes:      telepathy-farsight-python < 0.0.20


%description    python
Python bindings for %{name}.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-python = %{version}-%{release}
Requires:       telepathy-glib-devel >= 0.17.5
Requires:       farstream-devel >= 0.1.0
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       pkgconfig

## Obsolete telepathy-farsight with Fedora 17
Provides:       telepathy-farsight-devel = %{version}
Obsoletes:      telepathy-farsight-devel < 0.0.20


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure --enable-static=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
magic_rpm_clean.sh

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc NEWS README COPYING
%{_libdir}/libtelepathy-farstream*.so.*


%files python
%{python_sitearch}/tpfarstream.so


%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/telepathy-1.0/%{name}/


%changelog
* Thu Apr 05 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-2
- Rebuild against farstream

* Thu Apr  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Tue Apr 03 2012 Brian Pepple <bpepple@fedoraproject.org. - 0.2.3-2
- Rebuild against new tp-glib.

* Tue Mar 20 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3.

* Tue Mar 13 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-2
- Add obsolete/provides on python subpackage.

* Fri Mar  9 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-1
- Update 0.2.2.

* Wed Mar  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-3
- Enable python bindings.

* Mon Mar  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-2
- Use macro for version in provides.
- Change reference Farsight in description to Farstream.

* Sun Mar  4 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1.
- Add BR on farstream-devel.
- Bump minimum version of tp-glib.
- Add obsolete/provide on telepathy-farsight.

* Mon Nov 21 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-1
- Initial Fedora spec file.
- Disable the python bindings for now.

