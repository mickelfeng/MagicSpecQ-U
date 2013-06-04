Name: smokekde
Version: 4.10.3
Release: 1%{?dist}
Summary: Bindings for KDE libraries

License: LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdebindings/smoke 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kde4-kate-devel >= %{version}
BuildRequires: kdepimlibs4-devel >= %{version}
BuildRequires: kde4-okular-devel >= %{version}
BuildRequires: pkgconfig(akonadi)
BuildRequires: smokegen-devel >= %{version}
BuildRequires: smokeqt-devel >= %{version}

Obsoletes: kdebindings < 4.7.0 

# versioned core/runtime deps
# shouldn't we be using %%_kde4_version here?  -- rex
Requires: kde4-kate%{?_isa} >= %{version}
Requires: kde4-okular%{?_isa} >= %{version}
Requires: smokegen%{?_isa} >= %{version}
Requires: smokeqt%{?_isa} >= %{version}

%description
This package includes bindings for KDE libraries.

%package akonadi
Summary: Akonadi runtime support for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdepimlibs4-akonadi%{?_isa} >= %{version}
%description akonadi
%{summary}.

%package devel
Summary: Development files for %{name} 
Obsoletes: kdebindings-devel < 4.7.0
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-akonadi%{?_isa} = %{version}-%{release}
Requires: smokegen-devel
Requires: smokeqt-devel
%description devel
%{summary}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} -DOKULAR_INCLUDE_DIR=%{kde4_includedir}/okular ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING.LIB
%{_kde4_libdir}/libsmokeattica.so.3*
%{_kde4_libdir}/libsmokekate.so.3*
%{_kde4_libdir}/libsmokekdecore.so.3*
%{_kde4_libdir}/libsmokekdeui.so.3*
%{_kde4_libdir}/libsmokekfile.so.3*
%{_kde4_libdir}/libsmokekhtml.so.3*
%{_kde4_libdir}/libsmokekio.so.3*
%{_kde4_libdir}/libsmokeknewstuff2.so.3*
%{_kde4_libdir}/libsmokeknewstuff3.so.3*
%{_kde4_libdir}/libsmokekparts.so.3*
%{_kde4_libdir}/libsmokektexteditor.so.3*
%{_kde4_libdir}/libsmokekutils.so.3*
%{_kde4_libdir}/libsmokenepomuk.so.3*
%{_kde4_libdir}/libsmokenepomukquery.so.3*
%{_kde4_libdir}/libsmokeokular.so.3*
%{_kde4_libdir}/libsmokeplasma.so.3*
%{_kde4_libdir}/libsmokesolid.so.3*
%{_kde4_libdir}/libsmokesoprano.so.3*
%{_kde4_libdir}/libsmokesopranoclient.so.3*
%{_kde4_libdir}/libsmokesopranoserver.so.3*

%files akonadi
%{_kde4_libdir}/libsmokeakonadi.so.3*

%files devel
%{_libdir}/libsmoke*.so
%{_includedir}/smoke/*
%{_datadir}/smokegen/*


%changelog
* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Mon Feb 25 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-2
- don't override CXXFLAGS (#884839, kde#315774)

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.95-2
- drop BR: nepomuk-core-devel hack

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.95-1
- 4.8.95

* Wed Jun 20 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-3
- rebuild (attica)

* Sun Jun 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-2
- rebuild (smokegen)

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Thu May 31 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- 4.8.2

* Fri Mar 23 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-2
- -akonadi subpkg

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.7.97-1
- 4.7.97

* Sat Dec 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- rebuild (attica)

* Thu Dec 22 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Thu Nov 24 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Sat Oct 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-2
- Requires: kate-part

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Thu Sep 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-3
- s/Conflicts/Obsoletes/ kdebindings
- update URL
- remove deprecated tags from .spec

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-2
- BR: qt4-webkit-devel kate-devel

* Tue Sep 06 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Wed Aug 03 2011 Than Ngo <than@redhat.com> - 4.7.0-2
- BR: okula-devel

* Tue Jul 26 2011 Than Ngo <than@redhat.com> - 4.7.0-1
- 4.7.0

* Fri Jul 22 2011 Than Ngo <than@redhat.com> - 4.6.95-1
- 4.7 rc1

* Wed Jul 06 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- first Fedora RPM
