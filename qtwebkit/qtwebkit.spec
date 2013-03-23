
Name: qtwebkit
Version: 2.2.2
Release: 8%{?dist}
Summary: Qt WebKit bindings
Group: System Environment/Libraries
License: LGPLv2 with exceptions or GPLv3 with exceptions
URL: http://trac.webkit.org/wiki/QtWebKit
# get make-package.py:
# $ git clone git://qt.gitorious.org/qtwebkit/tools.git
# get Qt WebKit source code:
# $ git clone git://gitorious.org/+qtwebkit-developers/webkit/qtwebkit.git
# create a branch from a tag (e.g. qtwebkit-2.2.2):
# $ git checkout -b qtwebkit-2.2.2 qtwebkit-2.2.2
# generate the tarball (requires: bison flex gperf):
# $ make-package.py
# fix/repack the generated tarball:
# $ tar xzf qtwebkit-2.2.2-source.tar.gz
# $ mv qtwebkit-2.2.2-source/include qtwebkit-2.2.2-source/Source/
# $ tar cJf qtwebkit-2.2.2-source.tar.xz qtwebkit-2.2.2-source/
Source0: qtwebkit-%{version}-source.tar.xz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# search /usr/lib{,64}/mozilla/plugins-wrapped for browser plugins too
Patch1: webkit-qtwebkit-2.2-tp1-pluginpath.patch

# include -debuginfo except on s390(x) during linking of libQtWebKit
Patch3: webkit-qtwebkit-2.2-debuginfo.patch

# fix for qt-4.6.x 
Patch5: webkit-qtwebkit-2.2tp1-qt46.patch

# gcc doesn't support flag -fuse-ld=gold
Patch7: webkit-qtwebkit-ld.gold.patch

# svg infinite loop 
# https://projects.kde.org/news/177
# https://bugs.webkit.org/show_bug.cgi?id=97258
Patch8: qtwebkit-svg_infinite_loop.patch

# fix 64k pagesize issue
Patch9: qtwebkit-64k-pagesize.patch

# use SYSTEM_MALLOC on ppc/ppc64
Patch10: qtwebkit-ppc.patch

## upstream patches
# https://bugzilla.redhat.com/891464
# https://bugs.webkit.org/show_bug.cgi?id=72285
Patch100: qtwebkit-webkit72285.patch
Patch102: 0002-JSString-resolveRope-should-report-extra-memory-cost.patch
Patch103: 0003-Fix-build-with-GLib-2.31.patch
Patch105: 0005-Fix-build-on-linux-i386-where-gcc-would-produce-warn.patch

BuildRequires: chrpath
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(gio-2.0) pkgconfig(glib-2.0)
# gstreamer media support
BuildRequires: pkgconfig(gstreamer-0.10) pkgconfig(gstreamer-app-0.10)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(QtCore) pkgconfig(QtNetwork) 
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrender)
%if 0%{?fedora}
# for QtLocation, QtSensors 
BuildRequires: qt-mobility-devel >= 1.2
%endif
Obsoletes: qt-webkit < 1:4.9.0
Provides: qt-webkit = 2:%{version}-%{release}
Provides: qt4-webkit = 2:%{version}-%{release}
Provides: qt4-webkit%{?_isa} = 2:%{version}-%{release}

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
%{summary}

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
# when qt_webkit_version.pri was moved from qt-devel => qt-webkit-devel
Conflicts: qt-devel < 1:4.7.2-9
Obsoletes: qt-webkit-devel < 1:4.9.0
Provides:  qt-webkit-devel = 2:%{version}-%{release}
Provides:  qt4-webkit-devel = 2:%{version}-%{release}
Provides:  qt4-webkit-devel%{?_isa} = 2:%{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n qtwebkit-%{version}-source

%patch1 -p1 -b .pluginpath
%patch3 -p1 -b .debuginfo
## don't unconditionally apply this anymore
## it has side-effects ( like http://bugzilla.redhat.com/761337 )
#patch5 -p1 -b .qt46
%patch7 -p1 -b .ld.gold
%patch8 -p1 -b .svn_infinite_loop
%patch9 -p1 -b .64kpagesize
%ifarch ppc ppc64
%patch10 -p1 -b .system-malloc
%endif
%patch100 -p1 -b .webkit72285
%patch102 -p1 -b .0002
%patch103 -p1 -b .0003
%patch105 -p1 -b .0005


%build 

PATH=%{_qt4_bindir}:$PATH; export PATH
QTDIR=%{_qt4_prefix}; export QTDIR

pushd Source
%{_qt4_qmake} 
popd

make %{?_smp_mflags} -C Source

  
%install
rm -rf %{buildroot} 

make install INSTALL_ROOT=%{buildroot} -C Source 

## HACK, there has to be a better way
chrpath --list   %{buildroot}%{_qt4_libdir}/libQtWebKit.so.4.9.?
chrpath --delete %{buildroot}%{_qt4_libdir}/libQtWebKit.so.4.9.? ||:

mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_qt4_libdir}/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_qt4_libdir}/pkgconfig/

%clean
rm -rf %{buildroot} 


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_qt4_libdir}/libQtWebKit.so.4*
%if 0%{?_qt4_importdir:1}
%{_qt4_importdir}/QtWebKit/
%endif

%files devel
%defattr(-,root,root,-)
%{_qt4_datadir}/mkspecs/modules/qt_webkit_version.pri
%{_qt4_headerdir}/QtWebKit/
%{_qt4_libdir}/libQtWebKit.prl
%{_qt4_libdir}/libQtWebKit.so
%{_libdir}/pkgconfig/QtWebKit.pc


%changelog
* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> 2.2.2-8
- fix rpath (#902571)

* Tue Jan 15 2013 Than Ngo <than@redhat.com> - 2.2.2-7
- use SYSTEM_MALLOC on ppc/ppc64

* Fri Jan 11 2013 Than Ngo <than@redhat.com> 2.2.2-6
- bz#893447, fix 64k pagesize issue

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> 2.2.2-5
- segfault in requiresLineBox at rendering/RenderBlockLineLayout.cpp (#891464)

* Mon Dec 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.2.2-4
- switch to upstream versions of some patches

* Tue Nov 13 2012 Rex Dieter <rdieter@fedoraproject.org> 2.2.2-3
- Certain SVG content freezes QtWebKit (webkit#97258)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Rex Dieter <rdieter@fedoraproject.org> 2.2.2-1
- qtwebkit-2.2.2

* Fri May 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-6
- can't render Complex Text Layout (Hindi, Arabic) (#761337)

* Fri May 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-5
- respin tarball using upstream make-package.py tool

* Tue Jan 24 2012 Than Ngo <than@redhat.com> - 2.2.1-4
- gcc doesn't support flag -fuse-ld=gold yet
- fix build failure with gcc-4.7 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Than Ngo <than@redhat.com> - 2.2.1-2
- backport the correct patch from trunk to fix glib-2.31 issue

* Mon Dec 19 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-1
- qtwebkit-2.2.1
- add explicit BR: pkgconfig(xext) pkgconfig(xrender)

* Sun Nov 27 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-3
- add explicit BR: libjpeg-devel libpng-devel

* Fri Nov 18 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-2
- fix FTBFS against newer glib

* Thu Sep 29 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-1
- qtwebkit-2.2.0 (final)
- more pkgconfig-style deps

* Wed Sep 14 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-0.1.rc1
- qtwebkit-2.2.0-rc1

* Tue Sep 06 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-16.week35
- qtwebkit-2.2-week35 snapshot

* Thu Sep 01 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-15.week34
- qtwebkit-2.2-week34 snapshot

* Sat Aug 27 2011 Than Ngo <than@redhat.com> - 2.2-14.week32
- drop conditional

* Thu Aug 18 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-13.week32
- qtwebkit-2.2-week32 snapshot

* Wed Aug 10 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-12.week31
- BR: gstreamer-devel bits

* Tue Aug 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-11.week31
- qtwebkit-2.2-week31 snapshot

* Sat Jul 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-10.week28
- rebuild

* Wed Jul 20 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-9.week28
- qtwebkit-2.2-week28 snapshot

* Wed Jul 20 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-8.20110621
- rebuild (qt48)

* Wed Jun 22 2011 Dan Horák <dan[at]danny.cz> 2.2-7.20110621
- bump release for the s390 build fix

* Tue Jun 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-6.20110621
- 20110621 snapshot
- s390: respin javascriptcore_debuginfo.patch to omit -g from CXXFLAGS too

* Fri Jun 03 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-5.20110603
- 20110603 snapshot
- drop unused/deprecated phonon/gstreamer support snippets
- add minimal qt4 dep

* Tue May 24 2011 Than Ngo <than@redhat.com> - 2.2-4.20110513
- fix for qt-4.6.x
- add condition for rhel
- enable shared for qtwebkit build

* Thu May 19 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-3.20110513
- bump up Obsoletes: qt-webkit a bit, to be on the safe side

* Fri May 13 2011 Rex Dieter <rdieter@fedoraproject.org> 2.2-2.20110513
- 20110513 qtwebkit-2.2 branch snapshot
- cleanup deps
- drop -Werror

* Thu May 12 2011 Than Ngo <than@redhat.com> - 2.2-1
- 2.2-tp1
- gstreamer is now default, drop unneeded phonon patch

* Fri Apr 22 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1-4
- javascriptcore -debuginfo too (#667175)

* Fri Apr 22 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1-3
- Provides: qt(4)-webkit(-devel) = 2:%%version...

* Thu Apr 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1-2
- -devel: Conflicts: qt-devel < 1:4.7.2-9 (qt_webkit_version.pri)
- drop old/deprecated Obsoletes/Provides: WebKit-qt
- use modified, less gigantic tarball
- patch to use phonon instead of QtMultimediaKit
- patch pluginpath for /usr/lib{,64}/mozilla/plugins-wrapped

* Tue Apr 19 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1-1
- 2.1

* Mon Nov 08 2010 Than Ngo <than@redhat.com> - 2.0-2
- fix webkit to export symbol correctly

* Tue Nov 02 2010 Rex Dieter <rdieter@fedoraproject.org> 2.0-1
- 2.0 (as released with qt-4.7.0)

* Thu Sep 09 2010 Rex Dieter <rdieter@fedoraproject.org> 2.0-0.1.week32
- first try, borrowing a lot from debian/kubuntu packaging
