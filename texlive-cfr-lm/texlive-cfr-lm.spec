%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cfr-lm.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cfr-lm.doc.tar.xz
Source2: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cfr-lm.source.tar.xz

Name: texlive-cfr-lm
License: LPPL
Summary: Enhanced support for the Latin Modern fonts
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn19489%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Provides: tex(cfr-lm.sty)
Requires: tex(xkeyval.sty)
Requires: tex(fontenc.sty)
Requires: tex(textcomp.sty)
Requires: tex(nfssext-cfr.sty)

%description
The package supports a number of features of the Latin Modern
fonts which are not easily accessible via the default (La)TeX
support provided in the official distribution. In particular,
the package supports the use of the various styles of digits
available, small-caps and upright italic shapes, and
alternative weights and widths. It also supports variable width
typewriter and the "quotation" font. Version 2.004 of the Latin
Modern fonts is supported. By default, the package uses
proportional oldstyle digits and variable width typewriter but
this can be changed by passing appropriate options to the
package. The package also supports using e.g. different styles
of digits within a document so it is possible to use
proportional oldstyle digits by default, say, but tabular
lining digits within a particular table. See the README for
details. The package requires the official Latin Modern
distribution, including its (La)TeX support. The package relies
on the availability of both the fonts themselves and the
official font support files. The package also makes use of the
nfssext-cfr package. Only the T1 and TS1 encodings are
supported for text fonts. The set up of fonts for mathematics
is identical to that provided by Latin Modern.

date: 2010-07-12 01:19:39 +0200

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
Summary: Documentation for cfr-lm
Version: %{tl_version}
Release: %{tl_noarch_release}.1.3.svn19489%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cfr-lm


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
%{_texdir}/texmf-dist/fonts/enc/dvips/cfr-lm/dotdigits-clm.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cfr-lm/t1-clm.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cfr-lm/clm.map
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmb28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmb2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmb2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmb2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmb8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx28t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2i8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2ij8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2j8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbx8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxi8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxj8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxji8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmbxo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsc28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsc2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsc2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsc2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsc8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcscj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcscjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmcsco8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdun2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdun2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdunh28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdunh2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdunh8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdunhj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmdunjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmduno8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr28t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2i8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2i8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2i8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2i8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2i8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2ij8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2ij8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2ij8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2ij8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2ij8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2j8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2jo8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2jo8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2jo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2jo8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2o8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2o8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2o8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr2o8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmr8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmri8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmri8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmri8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmri8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmri8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrj8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrji8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrji8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrji8t7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrji8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrji8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrjo8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrjo8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrjo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmrjo8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmro8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmro8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmro8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmro8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmro8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss28t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss28t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss28t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2j8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2j8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2j8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2j8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2jo8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2jo8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2jo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss2jo8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmss8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssb2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssb2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbx28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbx2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbx8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssbxj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssd2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssd2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdc28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdc2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdc8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdcj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssdo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssj8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssj8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssj8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssjo8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssjo8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssjo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssjo8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso28t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso28t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso28t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso8t17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmsso8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssq28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssq2j8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssq2jo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssq2o8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssq8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqb2jo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqb2o8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbjo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbx28t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbx2j8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbx8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqbxj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqjo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmssqo8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtcsc8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtcscj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtcsjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtcso8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtk8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtkj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtkjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtko8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtl8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlc8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlcj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlcjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlco8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtljo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtlo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtt8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtt8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtt8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtt8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtti8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttij8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttj8t12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttj8t8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttj8t9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmttjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmtto8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmu28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmu2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmu8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmuj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtk28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtk2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtk2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtk2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtk8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtkj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtkjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtko8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtl28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtl2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtl2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtl2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtl8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtlj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtljo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtlo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtt28t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtt2j8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtt2jo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtt2o8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtt8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvttj8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvttjo8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/clmvtto8t10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbxi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmbxo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmcsco10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmdunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmduno10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmri10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmri12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmri7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmri8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmri9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmro10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmro12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmro17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmro8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmro9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssbo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssdo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmsso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmsso12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmsso17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmsso8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmsso9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssqbo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssqbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmssqo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtcso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtk10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtko10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtlc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtlco10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtlo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmtto10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtk10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtko10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtlo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/dd-lmvtto10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmb8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbx8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbxi8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmbxo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmcsc8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmcsco8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmdunh8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmduno8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmr8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmri8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmri8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmri8ttl7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmri8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmri8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmro8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmro8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmro8ttl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmro8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmro8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmss8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmss8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmss8ttl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmss8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmss8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssbo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssbx8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssdc8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssdo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmsso8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmsso8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmsso8ttl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmsso8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmsso8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssq8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssqbo8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssqbx8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmssqo8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtcsc8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtcso8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtk8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtko8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtl8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtlc8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtlco8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtlo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtt8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtt8ttl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtt8ttl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtt8ttl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtti8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmtto8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmu8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtk8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtko8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtl8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtlo8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtt8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/lmvtto8ttl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbxi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmbxo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmcsco10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmdunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmduno10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmri10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmri12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmri7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmri8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmri9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmro10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmro12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmro17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmro8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmro9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssbo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssdo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmsso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmsso12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmsso17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmsso8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmsso9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssqbo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssqbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmssqo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtcso10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtk10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtko10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtlc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtlco10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtlo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmtto10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtk10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtko10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtlo10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/u-clmvtto10.tfm
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmb28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmb2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmb2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmb2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmb8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx28t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2i8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2ij8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2j8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbx8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxi8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxj8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxji8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmbxo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsc28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsc2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsc2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsc2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsc8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcscj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcscjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmcsco8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdun2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdun2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdunh28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdunh2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdunh8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdunhj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmdunjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmduno8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr28t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2i8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2i8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2i8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2i8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2i8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2ij8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2ij8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2ij8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2ij8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2ij8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2j8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2jo8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2jo8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2jo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2jo8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2o8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2o8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2o8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr2o8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmr8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmri8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmri8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmri8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmri8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmri8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrj8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrji8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrji8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrji8t7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrji8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrji8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrjo8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrjo8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrjo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmrjo8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmro8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmro8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmro8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmro8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmro8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss28t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss28t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss28t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2j8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2j8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2j8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2j8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2jo8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2jo8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2jo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss2jo8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmss8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssb2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssb2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbx28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbx2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbx8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssbxj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssd2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssd2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdc28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdc2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdc8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdcj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssdo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssj8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssj8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssj8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssjo8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssjo8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssjo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssjo8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso28t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso28t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso28t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso8t17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmsso8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssq28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssq2j8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssq2jo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssq2o8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssq8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqb2jo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqb2o8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbjo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbx28t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbx2j8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbx8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqbxj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqjo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmssqo8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtcsc8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtcscj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtcsjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtcso8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtk8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtkj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtkjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtko8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtl8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlc8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlcj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlcjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlco8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtljo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtlo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtt8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtt8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtt8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtt8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtti8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttij8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttj8t12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttj8t8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttj8t9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmttjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmtto8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmu28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmu2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmu8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmuj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtk28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtk2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtk2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtk2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtk8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtkj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtkjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtko8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtl28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtl2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtl2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtl2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtl8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtlj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtljo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtlo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtt28t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtt2j8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtt2jo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtt2o8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtt8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvttj8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvttjo8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/clmvtto8t10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmb10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbx9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbxi10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmbxo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmcsc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmcsco10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmdunh10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmduno10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr5.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr6.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmr9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmri10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmri12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmri7.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmri8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmri9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmro10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmro12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmro17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmro8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmro9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmss10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmss12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmss17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmss8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmss9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssbo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssbx10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssdc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssdo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmsso10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmsso12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmsso17.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmsso8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmsso9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssq8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssqbo8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssqbx8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmssqo8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtcsc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtcso10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtk10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtko10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtl10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtlc10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtlco10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtlo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtt10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtt12.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtt8.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtt9.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtti10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmtto10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmu10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtk10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtko10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtl10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtlo10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtt10.vf
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/u-clmvtto10.vf
%{_texdir}/texmf-dist/tex/latex/cfr-lm/cfr-lm.sty
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2d.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2dj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2j.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2jqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2js.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2jt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2jv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2qs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2s.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2t.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clm2v.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmd.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmdj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmjqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmjs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmjt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmjv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clms.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/t1clmv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2d.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2dj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2j.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2jqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2js.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2jt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2jv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2qs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2s.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2t.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clm2v.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmd.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmdj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmjqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmjs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmjt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmjv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clms.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/ts1clmv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2d.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2dj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2j.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2jqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2js.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2jt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2jv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2qs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2s.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2t.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclm2v.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmd.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmdj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmj.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmjqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmjs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmjt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmjv.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmqs.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclms.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmt.fd
%{_texdir}/texmf-dist/tex/latex/cfr-lm/uclmv.fd

%files doc
%defattr(-,root,root)
%doc lppl.txt
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/README
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/cfr-lm.pdf
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/cfr-lm.tex
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/clm-test.pdf
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/clm-test.tex
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/manifest.txt


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
