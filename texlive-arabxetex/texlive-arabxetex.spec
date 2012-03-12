%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabxetex.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabxetex.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/arabxetex.source.tar.xz

Name: texlive-arabxetex
License: LPPL
Summary: An ArabTeX-like interface for XeLaTeX
Version: %{tl_version}
Release: %{tl_noarch_release}.v1.1.4.svn17470%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(arabxetex.sty)
Requires: tex(amsmath.sty)
Requires: tex(fontspec.sty)
Requires: tex(bidi.sty)

%description
ArabXeTeX provides a convenient ArabTeX-like user-interface for
typesetting languages using the Arabic script in XeLaTeX, with
flexible access to font features. Input in ArabTeX notation can
be set in three different vocalization modes or in roman
transliteration. Direct UTF-8 input is also supported. The
parsing and converting of ArabTeX input to Unicode is done by
means of TECkit mappings. Version 1.0 provides support for
Arabic, Maghribi Arabic, Farsi (Persian), Urdu, Sindhi,
Kashmiri, Ottoman Turkish, Kurdish, Jawi (Malay) and Uighur.
The documentation (not yet complete) covers topics such as
typesetting the Holy Quran, typesetting bidirectional critical
editions (with ednotes), and information on various recommended
OpenType fonts for the Arabic script and for transliterating
Oriental languages.

date: 2010-03-06 08:51:23 +0100

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
:

%postun
if [ $1 == 1 ]; then
  mkdir -p /var/run/texlive
  touch /var/run/run-texhash
else
  %{_bindir}/texhash 2> /dev/null
fi
:

%posttrans
[ -e /var/run/texlive/run-texhash ] && %{_bindir}/texhash 2> /dev/null && rm -f /var/run/texlive/run-texhash
[ -e /var/run/texlive ] && rm -rf /var/run/texlive
:

%package doc
Summary: Documentation for arabxetex
Version: %{tl_version}
Release: %{tl_noarch_release}.v1.1.4.svn17470%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for arabxetex


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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabicdigits.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabicdigits.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-farsi-trans-loc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-farsi-trans-loc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-farsi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kashmiri-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kurdish.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-kurdish.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-maghribi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-malay-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-pashto-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-sindhi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-turk-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-uighur.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-uighur.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-urdu-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2alif-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-farsi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kashmiri-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kurdish.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-kurdish.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-maghribi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-malay-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-pashto-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-sindhi-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-turk-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-uighur.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-uighur.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-fullvoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-fullvoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-novoc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-novoc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-urdu-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-voc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-fdf2noalif-voc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-pashto-trans-loc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-pashto-trans-loc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-sindhi-trans-loc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-sindhi-trans-loc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-dmg.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-dmg.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-loc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-trans-loc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-urdu-trans-loc.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/arabtex-urdu-trans-loc.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/farsidigits.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/farsidigits.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/fixlamalif.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/fixlamalif.tec
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/mirrorpunct.map
%{_texdir}/texmf-dist/fonts/misc/xetex/fontmapping/arabxetex/mirrorpunct.tec
%{_texdir}/texmf-dist/tex/xelatex/arabxetex/arabxetex.sty

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/README
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/arabxetex.pdf
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/examples/ednotes_example.pdf
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/examples/ednotes_example.tex
%{_texdir}/texmf-dist/doc/xelatex/arabxetex/examples/minimal.tex


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
