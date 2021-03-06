%if 0%{?rhel}
%global run_tests 0
%else
%global run_tests 1
%endif

Name:           telepathy-idle
Version:        0.1.12
Release:        3%{?dist}
Summary:        IRC connection manager for Telepathy

Group:          Applications/Communications
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         make-j-fix.patch

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	telepathy-glib-devel >= 0.13.10
BuildRequires:  libxslt
%if %{run_tests}
# Build Requires needed for tests.
BuildRequires:	python
BuildRequires:	python-twisted
BuildRequires:	dbus-python
BuildRequires:	pygobject2
%endif

Requires:	telepathy-filesystem
   

%description
A full-featured IRC connection manager for the Telepathy project.


%prep
%setup -q
%patch0 -p1 -b .make-j-fix

%if %{run_tests}
%check
#make check
%endif

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz


%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.1.12-3
- 为 Magic 3.0 重建

* Tue Oct  2 2012 Dan Winship <danw@redhat.com> - 0.1.12-2
- Add a patch from upstream for "make -j" reliability

* Fri Aug  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-3
- Make tests conditional. (#831344)

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-2
- Rebuild for new gcc.

* Sun Oct 30 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11.

* Wed May 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10.

* Mon Apr 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9.

* Fri Feb 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8.
- Bump min version of tp-glib needed.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-2
- Bump.

* Tue Dec  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7.
- Bump min version of tp-glib needed.
- Add BR on python-twisted, dbus-python, and pygobject2 for tests.
- Drop buildroot & clean section. No longer needed.

* Fri Feb 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6.

* Mon Sep 14 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5.
- Drop glibc patch.  Fixed upstream.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.4-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4.
- Add patch to fix glibc compilation bug.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3.
- Bump minimum version of tp-glib-devel needed.

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.2-4
- rebuild with new openssl

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-3
- Rebuild for gcc-4.3.

* Wed Dec  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-2
- rebuild for new libssl.so.6/libcrypto.so.6

* Sat Nov 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2.
- Add BR for telepathy-glib-devel, libxslt, & python.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-2
- Update license tag.

* Tue Jun 19 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1.
- Add check section for tests.
- Add BR on telepathy-glib-unstable-static.

* Mon Apr 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-1
- Initial spec file.

