# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:          speech-dispatcher
Version:       0.7.1
Release:       10%{?dist}
Summary:       To provide a high-level device independent layer for speech synthesis
Group:         System Environment/Libraries

# Almost all files are under GPLv2+, however 
# src/c/clients/spdsend/spdsend.h is licensed under GPLv2,
# which makes %%_bindir/spdsend GPLv2.
License:       GPLv2+ and GPLv2
URL:           http://www.freebsoft.org/speechd
Source0:       http://www.freebsoft.org/pub/projects/speechd/%{name}-%{version}.tar.gz
Source1:       speech-dispatcherd.service
BuildRequires: alsa-lib-devel
BuildRequires: dotconf-devel
BuildRequires: espeak-devel
BuildRequires: flite-devel
Buildrequires: glib2-devel
Buildrequires: libao-devel
Buildrequires: pulseaudio-libs-devel
BuildRequires: python-setuptools-devel
BuildRequires: texinfo
BuildRequires: systemd-units
BuildRequires: automake libtool
Patch0: 0001-RPM-Cleanups.patch

Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(post): chkconfig
Requires(preun): systemd-units
Requires(postun): systemd-units

%ifnarch s390 s390x
BuildRequires: libraw1394
%endif

Requires: festival-freebsoft-utils


%description
* Common interface to different TTS engines
* Handling concurrent synthesis requests – requests may come
  asynchronously from multiple sources within an application
  and/or from more different applications.
* Subsequent serialization, resolution of conflicts and
  priorities of incoming requests
* Context switching – state is maintained for each client
  connection independently, event for connections from
  within one application.
* High-level client interfaces for popular programming languages
* Common sound output handling – audio playback is handled by
  Speech Dispatcher rather than the TTS engine, since most engines
  have limited sound output capabilities.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       speech-dispatcher = %{version}-%{release}
License:        GPLv2+

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for speech-dispatcher
License:        GPLv2+
Group:          Documentation
Requires:       speech-dispatcher = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun):/sbin/install-info

%description doc
speechd documentation

%package python
Summary:        Python Client API for speech-dispatcher
License:        GPLv2+
Group:          Development/Libraries
Requires:       speech-dispatcher = %{version}-%{release}

%description python
speechd python module

%prep
%setup -q
%patch0 -p1
autoreconf -i -f

%build
%configure --disable-static --with-alsa --with-pulse --without-nas --with-flite --sysconfdir=%{_sysconfdir}

make %{?_smp_mflags}

%install
for dir in \
 config/ doc/ src/audio/ src/c/ src/modules/ src/tests/ src/server/ src/python/
 do
  pushd $dir
  make install DESTDIR=%{buildroot} INSTALL="install -p"
 popd
done

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %SOURCE1 %{buildroot}%{_unitdir}/

#Remove %{_infodir}/dir file
rm -f %{buildroot}%{_infodir}/dir

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Move the config files from /usr/share to /etc
%{__mkdir} -p %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
%{__mkdir} -p %{buildroot}%{_sysconfdir}/speech-dispatcher/modules
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/speechd.conf %{buildroot}%{_sysconfdir}/speech-dispatcher/
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/clients/* %{buildroot}%{_sysconfdir}/speech-dispatcher/clients
mv %{buildroot}%{_datadir}/speech-dispatcher/conf/modules/* %{buildroot}%{_sysconfdir}/speech-dispatcher/modules

# Create log dir
%{__mkdir} -p -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/

%clean
rm -rf %{buildroot}

%post 
/sbin/ldconfig
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig

/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart speech-dispatcherd.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable speech-dispatcherd.service > /dev/null 2>&1 || :
    /bin/systemctl stop speech-dispatcherd.service > /dev/null 2>&1 || :
fi

%triggerun -- speech-dispatcherd < 0.7.1-6
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save speech-dispatcherd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del speech-dispatcherd >/dev/null 2>&1 || :
/bin/systemctl try-restart speech-dispatcherd.service >/dev/null 2>&1 || :

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README COPYING
%dir %{_sysconfdir}/speech-dispatcher/
%dir %{_sysconfdir}/speech-dispatcher/clients
%dir %{_sysconfdir}/speech-dispatcher/modules
%config(noreplace) %{_sysconfdir}/speech-dispatcher/speechd.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/clients/*.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/*.conf
%{_bindir}/*
%{_libdir}/libspeechd.so.2
%{_libdir}/libspeechd.so.2.3.0
%{_libdir}/speech-dispatcher-modules/
%dir %{_libdir}/speech-dispatcher
%{_libdir}/speech-dispatcher/lib*.so
%{_libdir}/speech-dispatcher/libsdaudio.so.2
%{_libdir}/speech-dispatcher/libsdaudio.so.2.0.4
%{_datadir}/sounds/speech-dispatcher

%dir %attr(0700, root, root) %{_localstatedir}/log/speech-dispatcher/

%{_unitdir}/speech-dispatcherd.service

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/lib*.so

%files doc
%defattr(-,root,root,-)
%{_infodir}/*

%post doc
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/spd-say.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/ssip.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/%{name}-cs.info %{_infodir}/dir || :

%preun doc
if [ $1 = 0 ]; then
 /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
 /sbin/install-info --delete %{_infodir}/spd-say.info %{_infodir}/dir || :
 /sbin/install-info --delete %{_infodir}/ssip.info %{_infodir}/dir || :
 /sbin/install-info --delete %{_infodir}/%{name}-cs.info %{_infodir}/dir || :
fi

%files python
%defattr(-,root,root,-)
%{python_sitearch}/speechd*

%changelog
* Sat Jan 05 2013 Liu Di <liudidi@gmail.com> - 0.7.1-10
- 为 Magic 3.0 重建

* Thu Nov 29 2012 Bastien Nocera <bnocera@redhat.com> 0.7.1-9
- Move RPM hacks to source patches

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 26 2011 Jóhann B. Guðmundsson <johannbg@gmail.com> - 0.7.1-6
- Introduce systemd unit file, drop SysV support

* Tue Mar 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-5
- safer rpath handling (#654585)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Peter Robinson <pbrobinson@gmail.com> - 0.7.1-3
- Bump build for new dotconf

* Thu Oct 14 2010 Peter Robinson <pbrobinson@gmail.com> - 0.7.1-2
- Depend on festival-freebsoft-utils so we work with festival

* Tue Sep 14 2010 Peter Robinson <pbrobinson@gmail.com> - 0.7.1-1
- New upstream 0.7.1 stable release
- Some spec and build cleanups

* Thu Aug  5 2010 Peter Robinson <pbrobinson@gmail.com> - 0.7-2
- Disable NAS support, use PulseAudio by default

* Tue Aug  3 2010 Peter Robinson <pbrobinson@gmail.com> - 0.7-1
- New upstream 0.7 stable release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.7-5.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar 08 2010 Karsten Hopp <karsten@redhat.com> - 0.6.7-4.1
- disable libraw1394 build requirement on s390(x)

* Wed Mar  3 2010 Peter Robinson <pbrobinson@gmail.com> - 0.6.7-4
- Add patch to fix dso linking. Bug 564851

* Sat Jan  9 2010 Peter Robinson <pbrobinson@gmail.com> - 0.6.7-3
- Updated to the new python sysarch spec file reqs

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Peter Robinson <pbrobinson@gmail.com> - 0.6.7-1
- New upstream release, some spec file cleanups.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.6-20
- Rebuild for Python 2.6

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.6.6-19
- Fix Patch0:/%%patch mismatch.

* Wed Jul 16 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-18
- removed suid permission for speech-dispatcher binary.

* Wed Jul 16 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-17
- changing permissions of speech-dispatcher to 6711 (setuid and setguid)
- relocating configuration files in case of OLPC branch.
- excluding init script in case of OLPC branch.

* Wed Jul 16 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-16
- yet another release bump required :-/

* Wed Jul 16 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-15
- release bump

* Mon Jul 13 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-14
- conditional build required for OLPC Branch - Building without nas and 
  pulse-audio support.

* Mon Jun 23 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-13
- changed permission of speech-dispatcherd to 0644 too.

* Fri Jun 20 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-12
- added BuildRequires: texinfo (for makeinfo)
- changed permissions of Sourcex to 0644
- incorporated modified init script by mtasaka
- fixed a few more macros in changelog
- modified location of Source1 and Patch0 to point to online locations

* Wed Jun 18 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-11
- fixed encoding of speech-dispatcher-cs.info file to UTF-8

* Wed Jun 11 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-10
- removed Requires(preun) duplicates
- applied -p option correctly to install command
- fixed macros in changelog to prevent them from exapnding
- fixed the init script
- added patch to change log directory of speech-dispatcher and start only espeak

* Sun Jun 08 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-9
- removed %%{_infodir}/dir file

* Sat Jun 07 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-8
- converted speech-dispatcher-cs.info to UTF-8 encoding
- removed multiple file listings of /usr/lib/python2.5/site-packages/speechd/_test.py
  and fixed its mode
- added init script as a SOURCE instead as a patch
- duplicate Requires have now been removed
- Timestamping of files has now been added
- Install script fixed
- init script fixed

* Tue Jun 03 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-7
- changed license of base package to GPLv2+ and GPL
- changed license of all other packages to GPLv2+
- fixed install sequence using cleaner for loop and pushd and popd commands
- added init script for speech-dispatcher daemon
- added COPYING to doc in base package
- removed comment after /sbin/ldconfig
- resolved rpmlint errors for base package [except UTF-8 encoding error for (cs) documentation file]
- renamed long_message to spd_long_message and run_test to spd_run_test
- reset mode of _test.py to 0755

* Sun Apr 27 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-6
- changed BR to pulseaudio-lib-devel
- removed dotconf BR
- gave ownership of /%%{python_sitelib}/speechd-0.3-py2.5.egg-info to python package if package is built for Fedora 9 or above

* Sun Apr 13 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-5
- Removed conitional building options
- Added BuildRequires for dotconf-devel

* Mon Feb 18 2008    Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-4
- Manually specyfying make install for each src directory to be installed
- Installing python package seprately by by-passing make install

* Sun Feb 17 2008   Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-3
- Added Requires(post), Requires(preun) for -doc package
- Changed scriptlet from postun to preun for -doc package
- Removed Epoch
- Moved %%{_libdir}/lib*.so back to devel pacakge
- Require dependecny on base pacakge is now set to %%{version}-%%{release} instead of %%{version}
- removed --prefix=%{buildroot}/%%{_prefix}  against configure macro.
  -- -python subpackage does not build anymore.
- removed python subpackag rules from SPEC file.

* Sat Feb 16 2008   Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-2
- fixed directory ownerships

* Sat Feb 16 2008   Hemant Goyal <goyal.hemant@gmail.com> 0.6.6-1
- using newest version of speech-dispatcher
- updated %%{_libdir}/libspeechd.so.2.0.4 to %%{_libdir}/libspeechd.so.2.0.5
- python packages are being generated correctly now
- must force prefix=%{buildroot}/%%{_prefix} to enable python packages to get installed correctly.
- finding and deleting .*la files in %{buildroot} to avoid unpackaged files error.

* Sat Feb 16 2008   Hemant Goyal <goyal.hemant@gmail.com> 0.6.5-4
- updated build root

* Sat Feb 16 2008   Hemant Goyal <goyal.hemant@gmail.com> 0.6.5-3
- added macro to prevent error from stopping build for not including *.la files
- added epoch to the SPEC
- conditional build seems to be working correctly the old way only??
- unified changelogs

* Fri Feb 15 2008  Hemant Goyal <goyal.hemant@gmail.com> 0.6.5-2
- Removed .la files
- Removed doc-cs packages and merged it into doc package
- Removed packaging of static files, and tested -without static_libs option for configure script
- Moved symlink .so files from devel package to main package
- Commented /sbin/ldconfig for devel package.
