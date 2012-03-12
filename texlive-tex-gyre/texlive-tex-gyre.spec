%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tex-gyre.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/tex-gyre.doc.tar.xz

Name: texlive-tex-gyre
License: GFSL
Summary: TeX Fonts extending freely available URW fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.2.004.svn18651%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(qbookman.sty)
Provides: tex(qcourier.sty)
Provides: tex(qpalatin.sty)
Provides: tex(qswiss.sty)
Provides: tex(qtimes.sty)
Provides: tex(qzapfcha.sty)
Provides: tex(tgadventor.sty)
Provides: tex(tgbonum.sty)
Provides: tex(tgchorus.sty)
Provides: tex(tgcursor.sty)
Provides: tex(tgheros.sty)
Provides: tex(tgpagella.sty)
Provides: tex(tgschola.sty)
Provides: tex(tgtermes.sty)
Requires: tex(kvoptions.sty)
Requires: texlive-tex-gyre-fedora-fonts = %{tl_version}

%description
The TeX-GYRE bundle consists of six font families: TeX Gyre
Adventor is based on the URW Gothic L family of fonts (which is
derived from ITC Avant Garde Gothic, designed by Herb Lubalin
and Tom Carnase). TeX Gyre Bonum is based on the URW Bookman L
family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium
Italic (from ITC Zapf Chancery, designed by Hermann Zapf in
1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX
Gyre Heros is based on URW Nimbus Sans L (from Helvetica,
prepared by Max Miedinger, with Eduard Hoffmann in 1957). TeX
Gyre Pagella is based on URW Palladio L (from Palation,
designed by Hermann Zapf in the 1940s). TeX Gyre Schola is
based on the URW Century Schoolbook L family (which was
designed by Morris Fuller Benton for the American Type
Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9
L family of fonts (whose original, Times, was designed by
Stanley Morison together with Starling Burgess and Victor
Lardent and first offered by Monotype). The constituent
standard faces of each family have been greatly extended, and
contain nearly 1200 glyphs each (though Chorus omits Greek
support, has no small-caps family and has approximately 900
glyphs). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of
encodings) is provided. Vietnamese and Cyrillic characters were
added by Han The Thanh and Valek Filippov, respectively.

date: 2009-11-12 13:33:47 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "Map qag.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qbk.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qcr.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qcs.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qhv.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qpl.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qtm.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "Map qzc.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^Map qag.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qbk.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qcr.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qcs.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qhv.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qpl.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qtm.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^Map qzc.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  %{_bindir}/texhash 2> /dev/null
  %{_bindir}/updmap-sys --nohash --quiet &> /dev/null
else
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
  touch /var/run/texlive/run-updmap
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive/run-updmap ] && %{_bindir}/updmap-sys --nohash --quiet &> /dev/null && rm -f /var/run/texlive/run-updmap
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for tex-gyre
Version: %{tl_version}
Release: %{tl_noarch_release}.2.004.svn18651%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for tex-gyre

%package fedora-fonts
Summary: Fonts for tex-gyre
Version: %{tl_version}
Release: %{tl_noarch_release}.2.004.svn18651%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-tex-gyre = %{tl_version}
BuildArch: noarch

%description fedora-fonts
The TeX-GYRE bundle consists of six font families: TeX Gyre
Adventor is based on the URW Gothic L family of fonts (which is
derived from ITC Avant Garde Gothic, designed by Herb Lubalin
and Tom Carnase). TeX Gyre Bonum is based on the URW Bookman L
family (from Bookman Old Style, designed by Alexander
Phemister). TeX Gyre Chorus is based on URW Chancery L Medium
Italic (from ITC Zapf Chancery, designed by Hermann Zapf in
1979). TeX-Gyre Cursor is based on URW Nimbus Mono L (based on
Courier, designed by Howard G. Kettler in 1955, for IBM). TeX
Gyre Heros is based on URW Nimbus Sans L (from Helvetica,
prepared by Max Miedinger, with Eduard Hoffmann in 1957). TeX
Gyre Pagella is based on URW Palladio L (from Palation,
designed by Hermann Zapf in the 1940s). TeX Gyre Schola is
based on the URW Century Schoolbook L family (which was
designed by Morris Fuller Benton for the American Type
Founders). TeX Gyre Termes is based on the URW Nimbus Roman No9
L family of fonts (whose original, Times, was designed by
Stanley Morison together with Starling Burgess and Victor
Lardent and first offered by Monotype). The constituent
standard faces of each family have been greatly extended, and
contain nearly 1200 glyphs each (though Chorus omits Greek
support, has no small-caps family and has approximately 900
glyphs). Each family is available in Adobe Type 1 and Open Type
formats, and LaTeX support (for use with a variety of
encodings) is provided. Vietnamese and Cyrillic characters were
added by Han The Thanh and Valek Filippov, respectively.

date: 2009-11-12 13:33:47 +0100


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/gfsl.txt gfsl.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE1} | tar x -C %{buildroot}%{_texdir}/texmf-dist
# nuke useless tlmgr packaging stuff and doc droppings
rm -rf %{buildroot}%{_texdir}/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf-dist/tlpkg/tlpobj/
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/man/man*/Makefile
rm -rf %{buildroot}%{_texdir}/texmf/doc/info/dir

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_fontdir}
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bold.otf .
ln -s %{_fontdir}/texgyreadventor-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bolditalic.otf .
ln -s %{_fontdir}/texgyreadventor-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-italic.otf .
ln -s %{_fontdir}/texgyreadventor-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf .
ln -s %{_fontdir}/texgyreadventor-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf .
ln -s %{_fontdir}/texgyrebonum-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bolditalic.otf .
ln -s %{_fontdir}/texgyrebonum-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-italic.otf .
ln -s %{_fontdir}/texgyrebonum-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-regular.otf .
ln -s %{_fontdir}/texgyrebonum-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrechorus-mediumitalic.otf .
ln -s %{_fontdir}/texgyrechorus-mediumitalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrechorus-mediumitalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bold.otf .
ln -s %{_fontdir}/texgyrecursor-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bolditalic.otf .
ln -s %{_fontdir}/texgyrecursor-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-italic.otf .
ln -s %{_fontdir}/texgyrecursor-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-regular.otf .
ln -s %{_fontdir}/texgyrecursor-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf .
ln -s %{_fontdir}/texgyreheros-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bolditalic.otf .
ln -s %{_fontdir}/texgyreheros-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf .
ln -s %{_fontdir}/texgyreheros-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf .
ln -s %{_fontdir}/texgyreheros-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bold.otf .
ln -s %{_fontdir}/texgyreheroscn-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bolditalic.otf .
ln -s %{_fontdir}/texgyreheroscn-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-italic.otf .
ln -s %{_fontdir}/texgyreheroscn-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf .
ln -s %{_fontdir}/texgyreheroscn-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf .
ln -s %{_fontdir}/texgyrepagella-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bolditalic.otf .
ln -s %{_fontdir}/texgyrepagella-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf .
ln -s %{_fontdir}/texgyrepagella-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf .
ln -s %{_fontdir}/texgyrepagella-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf .
ln -s %{_fontdir}/texgyreschola-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bolditalic.otf .
ln -s %{_fontdir}/texgyreschola-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-italic.otf .
ln -s %{_fontdir}/texgyreschola-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf .
ln -s %{_fontdir}/texgyreschola-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bold.otf .
ln -s %{_fontdir}/texgyretermes-bold.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bold.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bolditalic.otf .
ln -s %{_fontdir}/texgyretermes-bolditalic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bolditalic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-italic.otf .
ln -s %{_fontdir}/texgyretermes-italic.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-italic.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf .
ln -s %{_fontdir}/texgyretermes-regular.otf %{buildroot}%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfb .
ln -s %{_fontdir}/qagb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfb .
ln -s %{_fontdir}/qagbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfb .
ln -s %{_fontdir}/qagr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfb .
ln -s %{_fontdir}/qagri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfb .
ln -s %{_fontdir}/qbkb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfb .
ln -s %{_fontdir}/qbkbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfb .
ln -s %{_fontdir}/qbkr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfb .
ln -s %{_fontdir}/qbkri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfb .
ln -s %{_fontdir}/qcrb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfb .
ln -s %{_fontdir}/qcrbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfb .
ln -s %{_fontdir}/qcrr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfb .
ln -s %{_fontdir}/qcrri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfb .
ln -s %{_fontdir}/qcsb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfb .
ln -s %{_fontdir}/qcsbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfb .
ln -s %{_fontdir}/qcsr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfb .
ln -s %{_fontdir}/qcsri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfb .
ln -s %{_fontdir}/qhvb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfb .
ln -s %{_fontdir}/qhvbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfb .
ln -s %{_fontdir}/qhvcb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfb .
ln -s %{_fontdir}/qhvcbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfb .
ln -s %{_fontdir}/qhvcr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfb .
ln -s %{_fontdir}/qhvcri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfb .
ln -s %{_fontdir}/qhvr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfb .
ln -s %{_fontdir}/qhvri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfb .
ln -s %{_fontdir}/qplb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfb .
ln -s %{_fontdir}/qplbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfb .
ln -s %{_fontdir}/qplr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfb .
ln -s %{_fontdir}/qplri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfb .
ln -s %{_fontdir}/qtmb.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfb .
ln -s %{_fontdir}/qtmbi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfb .
ln -s %{_fontdir}/qtmr.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfb .
ln -s %{_fontdir}/qtmri.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfb .
ln -s %{_fontdir}/qzcmi.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc gfsl.txt
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qagri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qbkri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcrri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qcsri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvcri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qhvri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qplri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmb.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmbi.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmr.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qtmri.afm
%{_texdir}/texmf-dist/fonts/afm/public/tex-gyre/qzcmi.afm
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cs-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cs.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-csm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-csm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-cszc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ec-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ec.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7x-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7x.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-l7xzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qx-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qx.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-qxzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmm-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-rmzc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-t5-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-t5.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansi-sc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansi.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-texnansizc.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/tex-gyre/q-ts1.enc
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qag.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qbk.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcr.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qcs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qhv.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qpl.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qtm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-cs.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-ec.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-l7x.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-qx.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-rm.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-t5.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-texnansi.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc-ts1.map
%{_texdir}/texmf-dist/fonts/map/dvips/tex-gyre/qzc.map
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreadventor-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrebonum-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrechorus-mediumitalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrecursor-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreheroscn-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyreschola-regular.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bold.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-bolditalic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-italic.otf
%{_texdir}/texmf-dist/fonts/opentype/public/tex-gyre/texgyretermes-regular.otf
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/cs-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ec-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/l7x-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/qx-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/rm-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/t5-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmb-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmbi-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmr-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmri-sc.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/texnansi-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qagri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qbkri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcrri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qcsri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvcri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qplri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmb.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmr.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qtmri.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/tex-gyre/ts1-qzcmi.tfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qagri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qbkri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcrri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qcsri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvcri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qhvri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qplri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmb.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmbi.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmr.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qtmri.pfm
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfb
%{_texdir}/texmf-dist/fonts/type1/public/tex-gyre/qzcmi.pfm
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/il2qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/l7xqzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ly1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ot4qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qbookman.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qcourier.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qpalatin.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qswiss.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qtimes.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qxqzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/qzapfcha.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t1qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/t5qzc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgadventor.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgbonum.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgchorus.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgcursor.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgheros.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgpagella.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgschola.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/tgtermes.sty
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qag.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qbk.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qcr.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qcs.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qhv.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qhvc.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qpl.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qtm.fd
%{_texdir}/texmf-dist/tex/latex/tex-gyre/ts1qzc.fd

%files doc
%defattr(-,root,root)
%doc gfsl.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/GUST-FONT-LICENSE.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Adventor.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Bonum.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Chorus.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Cursor.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Heros.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Pagella.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Schola.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/MANIFEST-TeX-Gyre-Termes.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Adventor.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Bonum.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Chorus.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Cursor.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Heros.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Pagella.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Schola.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/README-TeX-Gyre-Termes.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/goadb999.nam
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qag-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qag-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qag-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qag-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qagb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qagbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qagr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qagri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbk-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbk-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbk-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbk-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbkb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbkbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbkr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qbkri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcr-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcr-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcr-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcr-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcrb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcrbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcrr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcrri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcs-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcs-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcs-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcs-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcsb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcsbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcsr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qcsri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhv-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhv-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhv-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhv-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvcb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvcbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvcr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvcri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qhvri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qpl-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qpl-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qpl-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qpl-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qplb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qplbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qplr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qplri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtm-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtm-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtm-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtm-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtmb.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtmbi.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtmr.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qtmri.fea
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qzc-hist.txt
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qzc-info.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qzc-test.pdf
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qzc-test.tex
%{_texdir}/texmf-dist/doc/fonts/tex-gyre/qzcmi.fea

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/texgyreadventor-bold.otf
%{_fontdir}/texgyreadventor-bolditalic.otf
%{_fontdir}/texgyreadventor-italic.otf
%{_fontdir}/texgyreadventor-regular.otf
%{_fontdir}/texgyrebonum-bold.otf
%{_fontdir}/texgyrebonum-bolditalic.otf
%{_fontdir}/texgyrebonum-italic.otf
%{_fontdir}/texgyrebonum-regular.otf
%{_fontdir}/texgyrechorus-mediumitalic.otf
%{_fontdir}/texgyrecursor-bold.otf
%{_fontdir}/texgyrecursor-bolditalic.otf
%{_fontdir}/texgyrecursor-italic.otf
%{_fontdir}/texgyrecursor-regular.otf
%{_fontdir}/texgyreheros-bold.otf
%{_fontdir}/texgyreheros-bolditalic.otf
%{_fontdir}/texgyreheros-italic.otf
%{_fontdir}/texgyreheros-regular.otf
%{_fontdir}/texgyreheroscn-bold.otf
%{_fontdir}/texgyreheroscn-bolditalic.otf
%{_fontdir}/texgyreheroscn-italic.otf
%{_fontdir}/texgyreheroscn-regular.otf
%{_fontdir}/texgyrepagella-bold.otf
%{_fontdir}/texgyrepagella-bolditalic.otf
%{_fontdir}/texgyrepagella-italic.otf
%{_fontdir}/texgyrepagella-regular.otf
%{_fontdir}/texgyreschola-bold.otf
%{_fontdir}/texgyreschola-bolditalic.otf
%{_fontdir}/texgyreschola-italic.otf
%{_fontdir}/texgyreschola-regular.otf
%{_fontdir}/texgyretermes-bold.otf
%{_fontdir}/texgyretermes-bolditalic.otf
%{_fontdir}/texgyretermes-italic.otf
%{_fontdir}/texgyretermes-regular.otf
%{_fontdir}/qagb.pfb
%{_fontdir}/qagbi.pfb
%{_fontdir}/qagr.pfb
%{_fontdir}/qagri.pfb
%{_fontdir}/qbkb.pfb
%{_fontdir}/qbkbi.pfb
%{_fontdir}/qbkr.pfb
%{_fontdir}/qbkri.pfb
%{_fontdir}/qcrb.pfb
%{_fontdir}/qcrbi.pfb
%{_fontdir}/qcrr.pfb
%{_fontdir}/qcrri.pfb
%{_fontdir}/qcsb.pfb
%{_fontdir}/qcsbi.pfb
%{_fontdir}/qcsr.pfb
%{_fontdir}/qcsri.pfb
%{_fontdir}/qhvb.pfb
%{_fontdir}/qhvbi.pfb
%{_fontdir}/qhvcb.pfb
%{_fontdir}/qhvcbi.pfb
%{_fontdir}/qhvcr.pfb
%{_fontdir}/qhvcri.pfb
%{_fontdir}/qhvr.pfb
%{_fontdir}/qhvri.pfb
%{_fontdir}/qplb.pfb
%{_fontdir}/qplbi.pfb
%{_fontdir}/qplr.pfb
%{_fontdir}/qplri.pfb
%{_fontdir}/qtmb.pfb
%{_fontdir}/qtmbi.pfb
%{_fontdir}/qtmr.pfb
%{_fontdir}/qtmri.pfb
%{_fontdir}/qzcmi.pfb

%changelog
* Mon Aug 23 2010 Jindrich Novy <jnovy@redhat.com> 2010-9
- rpmlint fixes

* Sat Jul 17 2010 Jindrich Novy <jnovy@redhat.com> 2010-8
- depend on the new texlive-base noarch package
- ship licenses with documentation
- sync with upstream

* Mon May 31 2010 Jindrich Novy <jnovy@redhat.com> 2010-7
- switch to "tlpretest" source tree
- add lua and ruby dependencies to packages requiring them
- generate global package database "texlive.tlpdb" directly from
tlpobj files shipped with each package

* Wed May 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-6
- update to the latest frozen development TeX Live
- add svn to noarch versions according to guildelines

* Fri Apr 30 2010 Jindrich Novy <jnovy@redhat.com> 2010-5
- add dependencies resolution among biblatex files
- another %%postun scriplets fix

* Wed Apr 21 2010 Jindrich Novy <jnovy@redhat.com> 2010-4
- fix and tighten dependencies in %%post* scriptlets
- extract dependencies also from .cls and .ldf files
- speed up build by skipping some bits in __os_install_post

* Mon Apr 19 2010 Jindrich Novy <jnovy@redhat.com> 2010-3
- speed up installation/updating by running updmap/fmtutil
and texhash post-transaction once

* Sat Apr 03 2010 Jindrich Novy <jnovy@redhat.com> 2010-0.1
- bump version to 2010
- reduce total number of packages from 3580 to 3440 by removal
of dummy ones not shipping actually anything
- add style dependencies from packages reecently added
(were previously blacklisted)
- do not ship koma-script sources

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-4
- info and man pages are now part of main packages, not -doc
- use fedora-compliant license codes for License in spec
- fix fedora-fonts packages generation
- add dummy description if packages misses any
- package bdf fonts

* Tue Nov 10 2009 Jindrich Novy <jnovy@redhat.com> 2009-2
- install man and info pages into proper locations visible
by man and info
- update scriptlets
- remove xindy bits

* Mon Nov 09 2009 Jindrich Novy <jnovy@redhat.com> 2009-1
- official TeX Live 2009 release

* Tue Aug 25 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.3
- make TeX Live TrueType and OpenType fonts accessible by
other Fedora apps

* Thu Aug 20 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.2
- don't package generated pdfs from man pages

* Wed Aug 12 2009 Jindrich Novy <jnovy@redhat.com> 2009-0.1
- initial packaging for TeX Live 2009
