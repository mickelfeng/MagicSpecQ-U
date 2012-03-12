%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabtex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabtex.doc.tar.xz

Name: texlive-arabtex
License: LPPL
Summary: Macros and fonts for typesetting Arabic
Version: %{tl_version}
Release: %{tl_noarch_release}.3.11s.svn17095%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(abidir.sty)
Provides: tex(abjad.sty)
Provides: tex(aboxes.sty)
Provides: tex(acjk.sty)
Provides: tex(acmd.sty)
Provides: tex(aconfig.sty)
Provides: tex(aedpatch.sty)
Provides: tex(afonts.sty)
Provides: tex(afonts0.sty)
Provides: tex(afonts1.sty)
Provides: tex(afonts2.sty)
Provides: tex(afoot.sty)
Provides: tex(alatex.sty)
Provides: tex(aligs.sty)
Provides: tex(alists.sty)
Provides: tex(alocal.sty)
Provides: tex(altxext.sty)
Provides: tex(amac.sty)
Provides: tex(aoutput.sty)
Provides: tex(aparse.sty)
Provides: tex(apatch.sty)
Provides: tex(arababel.sty)
Provides: tex(arabart.sty)
Provides: tex(arabaux.sty)
Provides: tex(arabbook.sty)
Provides: tex(arabchrs.sty)
Provides: tex(arabext.sty)
Provides: tex(arabrep.sty)
Provides: tex(arabrep1.sty)
Provides: tex(arabskel.sty)
Provides: tex(arabsymb.sty)
Provides: tex(arabtex.sty)
Provides: tex(arabtoks.sty)
Provides: tex(ascan.sty)
Provides: tex(asect.sty)
Provides: tex(asmo449.sty)
Provides: tex(asmo449a.sty)
Provides: tex(atabg.sty)
Provides: tex(atrans.sty)
Provides: tex(awrite.sty)
Provides: tex(bhs.sty)
Provides: tex(bhslabel.sty)
Provides: tex(buck.sty)
Provides: tex(cp1256.sty)
Provides: tex(etrans.sty)
Provides: tex(gedalin.sty)
Provides: tex(hebchrs.sty)
Provides: tex(hebsymb.sty)
Provides: tex(hebtex.sty)
Provides: tex(hecmd.sty)
Provides: tex(hefonts.sty)
Provides: tex(hefonts0.sty)
Provides: tex(hefonts1.sty)
Provides: tex(hefonts2.sty)
Provides: tex(heparse.sty)
Provides: tex(hepatch.sty)
Provides: tex(hescan.sty)
Provides: tex(hetrans.sty)
Provides: tex(hewrite.sty)
Provides: tex(hmac.sty)
Provides: tex(isiri.sty)
Provides: tex(iso88596.sty)
Provides: tex(nashbf.sty)
Provides: tex(raw.sty)
Provides: tex(saw.sty)
Provides: tex(sotoku.sty)
Provides: tex(twoblks.sty)
Provides: tex(utf8.sty)
Provides: tex(utfcode.sty)
Provides: tex(verses.sty)
Provides: tex(witbhs.sty)
Provides: tex(xarbskel.sty)
Provides: tex(xarbsymb.sty)
Provides: tex(yiddish.sty)
Requires: texlive-arabtex-fedora-fonts = %{tl_version}

%description
ArabTeX is a package extending the capabilities of TeX/LaTeX to
generate Arabic and Hebrew text. Input may be in ASCII
transliteration or other encodings (including UTF-8); output
may be Arabic, Hebrew, or any of several languages that use the
Arabic script. ArabTeX consists of a TeX macro package and
Arabic and Hebrew fonts (provided both in Metafont format and
Adobe Type 1). The Arabic font is presently only available in
the Naskhi style. ArabTeX will run with Plain TeX and also with
LaTeX.

date: 2007-05-24 10:59:21 +0200

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap arabtex.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap arabtex.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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
Summary: Documentation for arabtex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.11s.svn17095%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for arabtex

%package fedora-fonts
Summary: Fonts for arabtex
Version: %{tl_version}
Release: %{tl_noarch_release}.3.11s.svn17095%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-arabtex = %{tl_version}
BuildArch: noarch

%description fedora-fonts
ArabTeX is a package extending the capabilities of TeX/LaTeX to
generate Arabic and Hebrew text. Input may be in ASCII
transliteration or other encodings (including UTF-8); output
may be Arabic, Hebrew, or any of several languages that use the
Arabic script. ArabTeX consists of a TeX macro package and
Arabic and Hebrew fonts (provided both in Metafont format and
Adobe Type 1). The Arabic font is presently only available in
the Naskhi style. ArabTeX will run with Plain TeX and also with
LaTeX.

date: 2007-05-24 10:59:21 +0200


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/lppl.txt lppl.txt
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hcaption-4.pfb .
ln -s %{_fontdir}/hcaption-4.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hcaption-4.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hclassic-4.pfb .
ln -s %{_fontdir}/hclassic-4.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hclassic-4.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14.pfb .
ln -s %{_fontdir}/xnsh14.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14bf.pfb .
ln -s %{_fontdir}/xnsh14bf.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14bf.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/arabtex/arabtex.map
%{_texdir}/texmf-dist/fonts/source/public/arabtex/arabsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/hcaption.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/hcbase.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/hclassic.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nash.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nash14.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nash14bf.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashbase.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashchar.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashdia.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashdig.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashlig.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/nashspec.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xarbsymb.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnsh.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnsh14.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnsh14bf.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshbase.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshchar.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshdia.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshdig.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshlig.mf
%{_texdir}/texmf-dist/fonts/source/public/arabtex/xnshspec.mf
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/hcaption.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/hclassic.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/nash14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/nash14bf.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/xnsh14.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/xnsh14bf.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/arabtex/yarborn.tfm
%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hcaption-4.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arabtex/hclassic-4.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14.pfb
%{_texdir}/texmf-dist/fonts/type1/public/arabtex/xnsh14bf.pfb
%{_texdir}/texmf-dist/tex/latex/arabtex/Uxnsh.fd
%{_texdir}/texmf-dist/tex/latex/arabtex/abidir.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/abjad.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aboxes.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/acjk.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/acmd.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aconfig.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aedpatch.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/afonts.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/afonts0.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/afonts1.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/afonts2.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/afoot.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/alatex.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aligs.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/alists.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/alocal.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/altxext.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/amac.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aoutput.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/aparse.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/apatch.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arababel.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabart.cls
%{_texdir}/texmf-dist/tex/latex/arabtex/arabaux.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabbook.cls
%{_texdir}/texmf-dist/tex/latex/arabtex/arabchrs.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabext.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabrep.cls
%{_texdir}/texmf-dist/tex/latex/arabtex/arabrep1.cls
%{_texdir}/texmf-dist/tex/latex/arabtex/arabskel.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabsymb.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabtex-doc.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/arabtex.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arabtex.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/arabtoks.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/arwindoc.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/ascan.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/asect.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/asize10.clo
%{_texdir}/texmf-dist/tex/latex/arabtex/asize11.clo
%{_texdir}/texmf-dist/tex/latex/arabtex/asize12.clo
%{_texdir}/texmf-dist/tex/latex/arabtex/asmo449.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/asmo449a.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/atabg.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/atrans.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/awrite.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/bhs.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/bhslabel.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/buck.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/captions.def
%{_texdir}/texmf-dist/tex/latex/arabtex/cp1256.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/etrans.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/gedalin.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/guha.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/hebchrs.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hebsymb.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hebtex.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hebtex.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/hecmd.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hefonts.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hefonts0.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hefonts1.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hefonts2.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/heparse.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hepatch.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hescan.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hetrans.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hewrite.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/hmac.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/isiri.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/iso88596.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/kashmiri.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/ligtable.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/malay.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/nashbf.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/omar.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/raw.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/saw.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/sindhi.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/sotoku.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/twoblks.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/uheb.fd
%{_texdir}/texmf-dist/tex/latex/arabtex/uighur.tex
%{_texdir}/texmf-dist/tex/latex/arabtex/unash.fd
%{_texdir}/texmf-dist/tex/latex/arabtex/utf8.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/utfcode.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/verses.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/witbhs.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/xarbskel.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/xarbsymb.sty
%{_texdir}/texmf-dist/tex/latex/arabtex/yiddish.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/announce.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex-doc.pdf
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex.doc
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex.faq
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex.gif
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex1.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/arabtex2.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/changes.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/changes.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/changes2.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/chg311.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/chg311a.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/chg311b.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/chg311c.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/chg311d.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/guha.ps
%{_texdir}/texmf-dist/doc/latex/arabtex/hebrew.305
%{_texdir}/texmf-dist/doc/latex/arabtex/install.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/lppl.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/malay.ps
%{_texdir}/texmf-dist/doc/latex/arabtex/manifest.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/miktex.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/miktex.mai
%{_texdir}/texmf-dist/doc/latex/arabtex/new1.gif
%{_texdir}/texmf-dist/doc/latex/arabtex/new2.gif
%{_texdir}/texmf-dist/doc/latex/arabtex/readme.305
%{_texdir}/texmf-dist/doc/latex/arabtex/readme.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/refer.htm
%{_texdir}/texmf-dist/doc/latex/arabtex/sindhi.ps
%{_texdir}/texmf-dist/doc/latex/arabtex/tetex.txt
%{_texdir}/texmf-dist/doc/latex/arabtex/uighur.ps
%{_texdir}/texmf-dist/doc/latex/arabtex/xarbsymb.dat

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/hcaption-4.pfb
%{_fontdir}/hclassic-4.pfb
%{_fontdir}/xnsh14.pfb
%{_fontdir}/xnsh14bf.pfb

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
