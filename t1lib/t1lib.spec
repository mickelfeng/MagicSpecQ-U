Name:           t1lib
Version:        5.1.2
Release:        4%{?dist}

Summary:        PostScript Type 1 font rasterizer
Summary(zh_CN.GB18030): PostScript Type 1 ×ÖÌåÕ¤¸ñ´¦ÀíÆ÷

Group:          Applications/Publishing
Group(zh_CN.GB18030):	Ó¦ÓÃ³ÌĞò/³ö°æ
License:        LGPLv2+
URL:            ftp://sunsite.unc.edu/pub/Linux/libs/graphics/t1lib-%{version}.lsm
Source0:        ftp://sunsite.unc.edu/pub/Linux/libs/graphics/t1lib-%{version}.tar.gz
Patch0:         http://ftp.de.debian.org/debian/pool/main/t/t1lib/t1lib_5.1.1-3.diff.gz
Patch1:         t1lib-5.1.2-segf.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libXaw-devel

Requires(post): coreutils, findutils

%description
T1lib is a rasterizer library for Adobe Type 1 Fonts. It supports
rotation and transformation, kerning underlining and antialiasing. It
does not depend on X11, but does provides some special functions for
X11.

AFM-files can be generated from Type 1 font files and font subsetting
is possible.

%description -l zh_CN.GB18030
T1lib ÊÇÒ»¸ö Adobe Type 1 ×ÖÌåµÄÕ¤¸ñ´¦ÀíÆ÷¿â¡£ËüÖ§³ÖĞı×ª¡¢±äĞÎ¡¢×Ö¾à
µ÷Õû¡¢¼ÓÏÂ»®ÏßºÍ·´¾â³İµÈ¡£Ëü²»ÒÀÀµÓÚ X11£¬µ«Ìá¹©ÁËÒ»Ğ© X11 ÌØ¶¨µÄº¯Êı¡£

%package        devel
Summary:        Header files and development files for %{name}
Summary(zh_CN.GB18030):	%{name} µÄ¿ª·¢°ü
Group:          Development/Libraries
Group(zh_CN.GB18030): 	¿ª·¢/¿â
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and development files for %{name}.

%description devel -l zh_CN.GB18030
%{name} µÄ¿ª·¢°ü¡£

%package        static
Summary:        Static libraries for %{name}
Summary(zh_CN.GB18030):	%{name} µÄ¾²Ì¬¿â
Group:          Development/Libraries
Group(zh_CN.GB18030):   ¿ª·¢/¿â
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This package contains static libraries for %{name}.

%description static -l zh_CN.GB18030
%{name} µÄ¾²Ì¬¿â¡£

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .segf

# use debian patches directly instead of duplicating them
#patch -p1 < debian/patches/segfault.diff -b -z .segf
patch -p1 < debian/patches/no-config.diff
patch -p1 < debian/patches/no-docs.diff
patch -p1 < debian/patches/lib-cleanup.diff

iconv -f latin1 -t utf8 < Changes > Changes.utf8
touch -r Changes Changes.utf8
mv Changes.utf8 Changes


%build
%configure
make %{?_smp_mflags} without_doc
touch -r lib/t1lib/t1lib.h.in lib/t1lib.h
touch -r lib/t1lib/t1libx.h lib/t1libx.h
ln README.t1lib-%{version} README
sed -e 's;/usr/share/X11/fonts;%{_datadir}/X11/fonts;' \
  -e 's;/usr/share/fonts/type1;%{_datadir}/fonts %{_datadir}/texmf/fonts;' \
  -e 's;/etc/t1lib/;%{_datadir}/t1lib/;' \
 debian/t1libconfig > t1libconfig
touch -r README.t1lib-%{version} t1libconfig

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/libt1*.la
chmod a+x $RPM_BUILD_ROOT%{_libdir}/libt1*.so.*

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}
install -p -m 644 debian/FontDatabase.5 $RPM_BUILD_ROOT%{_mandir}/man5/
install -p -m 644 debian/t1libconfig.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install -p -m 644 debian/type1afm.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 debian/xglyph.1 $RPM_BUILD_ROOT%{_mandir}/man1/
touch -r README.t1lib-%{version} $RPM_BUILD_ROOT%{_mandir}/man?/*.* 

mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -p -m 755 t1libconfig $RPM_BUILD_ROOT%{_sbindir}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/t1lib/
touch $RPM_BUILD_ROOT%{_datadir}/t1lib/{FontDatabase,t1lib.config}

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
%{_sbindir}/t1libconfig --force > /dev/null

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc Changes LGPL LICENSE README
%dir %{_datadir}/t1lib
%ghost %verify(not size mtime md5) %{_datadir}/t1lib/t1lib.config
%ghost %verify(not size mtime md5) %{_datadir}/t1lib/FontDatabase
%{_bindir}/type1afm
%{_bindir}/xglyph
%{_libdir}/libt1.so.*
%{_libdir}/libt1x.so.*
%{_mandir}/man*/*
%{_sbindir}/t1libconfig

%files devel
%defattr(-,root,root,-)
%doc doc/t1lib_doc.pdf
%{_includedir}/t1lib*.h
%{_libdir}/libt1.so
%{_libdir}/libt1x.so

%files static
%defattr(-,root,root,-)
%{_libdir}/libt1.a
%{_libdir}/libt1x.a


%changelog
* Mon Feb 13 2012 Liu Di <liudidi@gmail.com> - 5.1.2-4
- ä¸º Magic 3.0 é‡å»º

* Thu Jan 08 2008 Liu Di <liudidi@gmail.com> - %{version}-%{release}
- ÖØ½¨
