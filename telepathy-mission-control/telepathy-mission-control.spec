%define tp_glib_ver 0.17.5

Name:           telepathy-mission-control
Version:        5.12.0
Release:        1%{?dist}
Epoch:          1
Summary:        Central control for Telepathy connection manager

Group:          System Environment/Libraries
License:        LGPLv2
URL:            http://telepathy.freedesktop.org/wiki/Mission_Control
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel 
BuildRequires:  libxslt-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  telepathy-glib-devel >= %{tp_glib_ver}
BuildRequires:  upower-devel
BuildRequires:  gtk-doc


%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       telepathy-glib-devel >= %{tp_glib_ver}


%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-gnome-keyring --enable-gtk-doc --enable-mcd-plugins --with-connectivity=nm --enable-upower

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
magic_rpm_clean.sh

%post -p /usr/sbin/ldconfig

%postun
/usr/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_libdir}/libmission-control-plugins.so.*
%{_libdir}/libmissioncontrol-server-%{version}.so
%{_libexecdir}/mission-control-5
%{_mandir}/man*/*.gz


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmission-control-plugins.so
%{_libdir}/libmissioncontrol-server.so
%doc %{_datadir}/gtk-doc/html/mission-control-plugins


%changelog
* Mon Apr  2 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.12.0-1
- Update to 5.12.0.

* Wed Feb 22 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.11.0-1
- Update to 5.11.0
- Bump minimum version of tp-glib.

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:5.10.1-2
- Rebuild for new gcc.

* Tue Nov  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.10.1-1
- Update to the 5.10.1 stable release

* Wed Oct  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.9.3-1
- Update to 5.9.3
- Enable NetworkManager and upower support so t-m-c can detect network and suspend events and deal with them

* Thu Sep  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.9.2-1
- Update to 5.9.2

* Thu Jul 21 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:5.9.1-1
- Update to 5.9.1.

* Fri Jun 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.9.0-1
- Update to 5.9.0

* Thu May 12 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.11-1
- Update to 5.7.11

* Sat May  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.10-1
- Update to 5.7.10

* Wed Apr  6 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.9-1
- Update to 5.7.9

* Wed Mar 23 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.7-1
- Update to 5.7.7

* Mon Mar 07 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:5.7.6-1
- Update to 5.7.6

* Thu Mar  3 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:5.7.5-1
- Update to 5.7.5.

* Thu Feb 24 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:5.7.4-1
- Update to 5.7.4

* Tue Feb 15 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:5.7.3-1
- Update to 5.7.3.
- Add minimum version of tp-glib needed.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.2-1
- Update to 5.7.2

* Sat Dec 11 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.7.1-1
- Update to 5.7.1

* Wed Nov 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.6.1-1
- Update to 5.6.1

* Wed Sep 29 2010 jkeating - 1:5.6.0-2
- Rebuilt for gcc bug 634757
- Add missing buildreq on gtk-doc

* Wed Sep 22 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.6.0-1
- Update to 5.6.0.

* Tue Sep 14 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:5.5.4-1
- Update to 5.5.4.
- Drop explicit linking patch. Fixed upstream.

* Mon Aug 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.5.3-2
- Update to 5.5.3.

* Thu Aug 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.4.3-2
- Fix 617832

* Thu Jun 17 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:5.4.3-1
- Update to 5.4.3.

* Tue Jun  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.4.2-2
- enable gnome keyring so passwords are encrypted.

* Wed May 26 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:5.4.2-1
- Update to 5.4.2.

* Wed Apr 28 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:5.4.0-1
- Update to new stable 5.4.0 release

* Sat Feb 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 1:5.3.2-1
- Update to 5.3.2.

* Mon Nov 23 2009 Brian Pepple <bpepple@fedoraproject.org> - 1:5.2.6-1
- Update to 5.2.6.

* Fri Sep 25 2009 Brian Pepple <bpepple@fedoraproject.org> - 1:5.2.5-2
- Add the epoch to the devel requires.

* Thu Sep 24 2009 Brian Pepple <bpepple@fedoraproject.org> - 1:5.2.5-1
- Update to 5.2.5.
- Add epoch so we don't ship the devel branch of mission control for F12.

* Mon Sep 14 2009 Brian Pepple <bpepple@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0.

* Thu Sep 10 2009 Brian Pepple <bpepple@fedoraproject.org> - 5.2.3-1
- Update to 5.2.3.
- Drop mission-control directory since it's no longer needed.

* Fri Aug 28 2009 Brian Pepple <bpepple@fedoraproject.org> - 5.2.1-2
- Let's not pull have the main package depend on the devel sub.

* Wed Aug 26 2009 Brian Pepple <bpepple@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1.

* Tue Aug 25 2009 Brian Pepple <bpepple@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0.
- Drop BR on libtelepathy.
- Update url & source links.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 4.67-2
- Include /usr/share/mission-control directory.

* Sat Sep 27 2008 Brian Pepple <bpepple@fedoraproject.org> - 4.67-1
- Update to 4.67.

* Fri Sep 26 2008 Brian Pepple <bpepple@fedoraproject.org> - 4.65-3
- Enable gnome-keyring support.

* Tue May 29 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 4.65-2
- Update to new upstream release (4.65)

* Mon Mar 17 2008 Matej Cepl <mcepl@redhat.com> 4.64-1
- Upgrade to the current upstream release (4.64) (Resolves: #437766)
- Fix building on x86_64 (upstream libtool is not aware of /usr/lib64 and
  produces rpaths)
- Fix invalid License tag.

* Mon Mar 10 2008 Peter Gordon <peter@thecodergeek.com> - 4.63-1
- Update to new upstream release (4.63)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.55-2
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Peter Gordon <peter@thecodergeek.com> - 4.55-1
- Update to new upstream release (4.55)
- Drop obsolete 64-bit patch.
  - size_t_vs_guint.patch

* Sat Dec 15 2007 Peter Gordon <peter@thecodergeek.com> - 4.51-1
- Update to new upstream release (4.51)

* Mon Nov 12 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> - 4.49-1
- Bump to latest release

* Sun Aug 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 4.35-1
- Bump to latest release

* Thu Jun 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 4.24-3
- New release
- Remove patch, applied upstream

* Sat Jun 02 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 4.22-2
- Add missing requires on -devel package

* Sat May 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 4.22-1
- Initial build
