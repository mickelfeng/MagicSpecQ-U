%define tex_texinfo %{_datadir}/texmf/tex/texinfo

Summary: Tools needed to create Texinfo format documentation files
Summary(zh_CN.GB18030): ½¨Á¢ Texinfo ¸ñÊ½ÎÄµµÎÄ¼şËùĞèÒªµÄ¹¤¾ß
Name: texinfo
Version: 4.13a
Release: 11%{?dist}
License: GPLv3+
Group: Applications/Publishing
Group(zh_CN.GB18030): Ó¦ÓÃ³ÌĞò/³ö°æ
Url: http://www.gnu.org/software/texinfo/
Source0: ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.lzma
Source1: info-dir
Source2: texi2pdf.man
Patch0: texinfo-4.12-zlib.patch
Patch1: texinfo-4.13a-data_types.patch
# Patch2: is already upstream
Patch2: texinfo-4.13a-mosdo-crash.patch
Patch3: texinfo-4.13a-powerpc.patch
# Patch4: accepted by upstream, bz579263
Patch4: texinfo-4.13a-help-index-segfault.patch
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: zlib-devel, ncurses-devel

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.

%description -l zh_CN.GB18030
Texinfo ÊÇÒ»¸öÎÄµµÏµÍ³£¬Ëü¿ÉÒÔ´ÓÒ»¸öÀ´Ô´ÎÄ¼şÍ¬Ê±²úÉúÔÚÏßĞÅÏ¢ºÍ¿É´òÓ¡Êä³ö¡£
GNU ÏîÄ¿´ó²¿·ÖÊ¹ÓÃ Texinfo ¸ñÊ½×öËüÃÇµÄÎÄµµ¡£

%package -n info
Summary: A stand-alone TTY-based reader for GNU texinfo documentation
Summary(zh_CN.GB18030): Ò»¸ö¶ÀÁ¢µÄÓÃÓÚ GNU texinfo ÎÄµµµÄ»ùÓÚ TTY µÄÔÄ¶ÁÆ÷
Group: System Environment/Base
Group(zh_CN.GB18030): ÏµÍ³»·¾³/»ù±¾

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. The info package provides a standalone TTY-based
browser program for viewing texinfo files.

%description -n info -l zh_CN.GB18030
GNU ¼Æ»®ÔÚ¶àÊıÎÄµµÖĞÊ¹ÓÃ texinfo ÎÄ¼ş¸ñÊ½¡£info Èí¼ş°üÌá¹©ÁËÒ»¸öµ¥¶ÀµÄ
»ùÓÚ TTY µÄä¯ÀÀÆ÷³ÌĞòÀ´²é¿´ texinfo ÎÄ¼ş¡£

%package tex
Summary: Tools for formatting Texinfo documentation files using TeX
Summary(zh_CN.GB18030): Ê¹ÓÃ TeX ¸ñÊ½»¯ Texinfo ÎÄµµÎÄ¼şµÄ¹¤¾ß
Group: Applications/Publishing
Group(zh_CN.GB18030): Ó¦ÓÃ³ÌĞò/³ö°æ
Requires: texinfo = %{version}-%{release}
Requires: tetex
Requires(post): %{_bindir}/texconfig-sys
Requires(postun): %{_bindir}/texconfig-sys

%description tex
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

The texinfo-tex package provides tools to format Texinfo documents
for printing using TeX.

%description tex -l zh_CN.GB18030
Texinfo ÊÇÒ»¸öÎÄµµÏµÍ³£¬Ëü¿ÉÒÔ´ÓÒ»¸öÀ´Ô´ÎÄ¼şÍ¬Ê±²úÉúÔÚÏßĞÅÏ¢ºÍ¿É´òÓ¡Êä³ö¡£
GNU ÏîÄ¿´ó²¿·ÖÊ¹ÓÃ Texinfo ¸ñÊ½×öËüÃÇµÄÎÄµµ¡£

texinfo-tex °üÌá¹©ÁËÊ¹ÓÃ Tex ´òÓ¡¸ñÊ½ Texinfo ÎÄµµµÄ¹¤¾ß¡£

%prep
%setup -q -n %{name}-4.13
%patch0 -p1 -b .zlib
%patch1 -p1 -b .data_types
%patch2 -p1 -b .mosdo-crash
%patch3 -p1 -b .powerpc
%patch4 -p1 -b .help-index-segfault

%build
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/sbin

make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

mkdir -p $RPM_BUILD_ROOT%{tex_texinfo}
install -p -m644 doc/texinfo.tex doc/txi-??.tex $RPM_BUILD_ROOT%{tex_texinfo}

install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/texi2pdf.1
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_infodir}/dir
mv $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT/sbin

# Convert ChangeLog to UTF-8
/usr/bin/iconv -f iso-8859-2 -t utf-8 < ChangeLog > ChangeLog_utf8
touch -r ChangeLog ChangeLog_utf8
mv ChangeLog_utf8 ChangeLog

magic_rpm_clean.sh
%find_lang %name

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
if [ -f %{_infodir}/texinfo ]; then # --excludedocs?
    /sbin/install-info %{_infodir}/texinfo %{_infodir}/dir || :
fi

%preun
if [ $1 = 0 ]; then
    if [ -f %{_infodir}/texinfo ]; then # --excludedocs?
        /sbin/install-info --delete %{_infodir}/texinfo %{_infodir}/dir || :
    fi
fi

%post -n info
if [ -f %{_infodir}/info-stnd.info ]; then # --excludedocs?
    /sbin/install-info %{_infodir}/info-stnd.info %{_infodir}/dir
fi
if [ -x /bin/sed ]; then
    /bin/sed -i '/^This is.*produced by makeinfo.*from/d' %{_infodir}/dir || :
fi

%preun -n info
if [ $1 = 0 ]; then
    if [ -f %{_infodir}/info-stnd.info ]; then # --excludedocs?
        /sbin/install-info --delete %{_infodir}/info-stnd.info %{_infodir}/dir \
        || :
    fi
fi

%post tex
%{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun tex
%{_bindir}/texconfig-sys rehash 2> /dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS INTRODUCTION README COPYING
%{_bindir}/makeinfo
%{_datadir}/texinfo
%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man5/texinfo.5*

%files -n info
%defattr(-,root,root,-)
%config(noreplace) %verify(not md5 size mtime) %{_infodir}/dir
%{_bindir}/info
%{_bindir}/infokey
%{_infodir}/info.info*
%{_infodir}/info-stnd.info*
/sbin/install-info
%{_mandir}/man1/info.1*
%{_mandir}/man1/infokey.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*

%files tex
%defattr(-,root,root)
%{_bindir}/texindex
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%{_bindir}/pdftexi2dvi
%{tex_texinfo}/
%{_mandir}/man1/texindex.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man1/pdftexi2dvi.1*

%changelog
* Tue Feb 14 2012 Liu Di <liudidi@gmail.com> - 4.13a-11
- ä¸º Magic 3.0 é‡å»º

* Mon Oct 09 2006 Liu Di <liudidi@gmail.com> - 4.8-1mgc
- rebuild for Magic
