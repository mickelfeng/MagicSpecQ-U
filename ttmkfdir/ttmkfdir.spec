Summary: Utility to create fonts.scale files for truetype fonts
Summary(zh_CN.UTF-8): 为 truetype 字体创建 fonts.scale 文件的工具。
Name: ttmkfdir
Version: 3.0.9
Release: 27%{?dist}
Source0: %{name}-%{version}.tar.bz2
Patch: ttmkfdir-3.0.9-cpp.patch
Patch1: ttmkfdir-3.0.9-zlib.patch
Patch2: ttmkfdir-3.0.9-fix-freetype217.patch
Patch3: ttmkfdir-3.0.9-namespace.patch
Patch4: ttmkfdir-3.0.9-fix-crash.patch
Patch5: ttmkfdir-3.0.9-warnings.patch
Patch6: ttmkfdir-3.0.9-segfaults.patch
Patch7: ttmkfdir-3.0.9-encoding-dir.patch
Patch8: ttmkfdir-3.0.9-font-scale.patch
Patch9:	ttmkfdir-3.0.9-gcc44.patch
License: GPL
Group: Applications/System
Group(zh_CN.UTF-8): 应用程序/系统
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel flex
BuildRequires: libtool

# ttmkfdir used to be in the following packages at one point
Conflicts: XFree86-font-utils < 4.2.99.2-0.20021126.3
Conflicts: freetype < 2.0.6-3

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%description -l zh_CN.UTF-8
ttmkfdir 是一个用来在全是 TrueType 字体的目录中创建 fonts.scale 
文件以便为字体服务器做准备的工具。

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/ttmkfdir

%changelog
* Fri Feb 17 2012 Liu Di <liudidi@gmail.com> - 3.0.9-27
- 为 Magic 3.0 重建

* Wed Jan 10 2007 Liu Di <liudidi@gmail.com> - 3.0.9-24mgc
- rebuild for magic

* Thu Nov 30 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-24.fc7
- add ttmkfdir-3.0.9-font-scale.patch to fix bug #209102.
- Patch from Akira TAGOH.

* Wed Oct 18 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-23
- rebuild

* Fri Sep 29 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-22
- delete "%post" and "Requires(post)" in ttmkfdir.spec

* Thu Sep 28 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-21
- modify release

* Wed Sep 27 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.4
- modify "%post" and add "Requires(post)" in ttmkfdir.spec for fixing bug173591, bug207279, bug208122

* Wed Sep 06 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.3
- add "%post" in ttmkfdir.spec for fixing bug173591

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-20.2.1
- rebuild

* Tue Jun 20 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.2
- add "BuildRequires: libtool" in ttmkfdir.spec

* Mon Jun 19 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.1
- remove the modifying part of ttmkfdir-3.0.9/Makefile, recover the old Makefile
- modify ttmkfdir-3.0.9-encoding-dir.patch about Makefile

* Thu Jun 15 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20
- add ttmkfdir-3.0.9-encoding-dir.patch to fix bug #173705
- modify ttmkfdir-3.0.9/Makefile to delete the compiling flag of "ggdb"

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-19.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-19.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 8 2005 LingNing Zhang <lizhang@redhat.com> -3.0.9-19
- add ttmkfdir-3.0.9-segfaults.patch to fix bug #164969

* Wed Aug  3 2005 Jens Petersen <petersen@redhat.com> - 3.0.9-17
- replace ttmkfdir-3.0.9-defautl_enc_size.patch and
  ttmkfdir-3.0.9-crashplus.patch with ttmkfdir-3.0.9-fix-crash.patch
  to fix missing native encodings of fonts
  (Akira Tagoh, #143941)
- buildrequire flex
- add ttmkfdir-3.0.9-warnings.patch to silence most of compiler warnings

* Sun Mar 20 2005 Yu Shao <yshao@redhat.com> 3.0.9-16
- rebuild with GCC 4

* Fri Sep 10 2004 Yu Shao <yshao@redhat.com> 3.0.9-14
- bug #100560, requires zlib-devel rather than zlib

* Tue Aug 17 2004 Elliot Lee <sopwith@redhat.com> 3.0.9-13
- Follow-on fix for the issue detailed in #118713
- Improve performance when checking if a font has a mapping present
- Base font file selection on the magic at the start of the file, rather than the filename

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 19 2004 Yu Shao <yshao@redhat.com> 3.0.9-11
- set default encoding size to DEFAULT_SIZE, bug #118713

* Fri Mar 12 2004 Yu Shao <yshao@redhat.com> 3.0.9-10
- patch suggested from law@redhat.com not to use semicolon in GCC3.4, 3.5

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 12 2004 Yu Shao <yshao@redhat.com> 3.0.9-8
- patch for building package against freetype-2.1.7
- from kanagawa jigorou (jigorou3@mail.goo.ne.jp) #114682

* Mon Sep 15 2003 Yu Shao <yshao@redhat.com> 3.0.9-6
- updated zlib patch from Nalin Dahyabhai #104331

* Thu Aug 21 2003 Yu Shao <yshao@redhat.com> 3.0.9-4
- added zlib build requirement, partly releated to #100560
- other fixes

* Thu Aug  7 2003 Elliot Lee <sopwith@redhat.com>
- Fix compile error (cpp.patch)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 23 2003 Yu Shao <yshao@redhat.com> 3.0.9-1
- added freetype-devel build requirement #82468

* Mon Jan 20 2003 Yu Shao <yshao@redhat.com> 3.0.8-1
- revert additional-entries to 0 #82125

* Wed Jan 15 2003 Yu Shao <yshao@redhat.com> 3.0.7-1
- set default value of additional-entries to 1

* Mon Jan 13 2003 Yu Shao <yshao@redhat.com> 3.0.6-1
- added iso8859-13 support from Nerijus Baliunas #77289
- added README 

* Wed Jan 8 2003 Yu Shao <yshao@redhat.com> 3.0.5-1
- encoding.l fix and ttc support patch 
- default read system encodings.dir instead of the one
- in current directory

* Wed Dec 18 2002 Yu Shao <yshao@redhat.com> 3.0.4-1
- make ttmkfdir keep silent with FIRSTINDEX. #61769

* Wed Dec 18 2002 Yu Shao <yshao@redhat.com> 3.0.3-1
- Applied new patches to make ttmkfdir provide more infomation when meets 
- bad fonts

* Mon Dec  9 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.2-1
- Changed the nonstandard RPM Group from System/Utilities to Applications/System
- Added a new Makefile install target, and changed specfile to use makeinstall

* Mon Dec  9 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.1-1
- Imported ttmkfdir into CVS on cvs.devel and applied all patches to CVS
- Removed patches from spec file
- Rewrote Makefile, now uses freetype-config to autodetect CFLAGS and libs,
  allowing a lot of spec file cleanups.  Added new targets for tagging CVS,
  making tarball, and making srpm.

* Mon Dec  2 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.0-2
- Added Conflicts for prior packages which contained ttmkfdir

* Fri Nov 29 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.0-1
- Initial build.  Basically just renamed our existing ttmkfdir to version
  3.0.0 to differentiate it.  It's the same old thing as before, but is
  likely going to move to CVS for easier development.
