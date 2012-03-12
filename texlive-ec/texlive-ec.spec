%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ec.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/ec.doc.tar.xz

Name: texlive-ec
License: Freely redistributable without restriction
Summary: Computer modern fonts in T1 and TS1 encodings
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
The EC fonts are European Computer Modern Fonts, supporting the
complete LaTeX T1 encoding defined at the 1990 TUG conference
hold at Cork/Ireland. These fonts are intended to be stable
with no changes being made to the tfm files. The set also
contains a Text Companion Symbol font, called tc, featuring
many useful characters needed in text typesetting, for example
oldstyle digits, currency symbols (including the newly created
Euro symbol), the permille sign, copyright, trade mark and
servicemark as well as a copyleft sign, and many others. Recent
releases of LaTeX2e support the EC fonts. The EC fonts
supersede the preliminary version released as the DC fonts. The
fonts are available in (traced) Adobe Type 1 format, as part of
the cm-super bundle. The other Computer Modern-style T1-encoded
Type 1 set, Latin Modern, is not actually a direct development
of the EC set, and differs from the EC in a number of
particulars.

date: 2009-08-27 17:24:27 +0200

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
Summary: Documentation for ec
Version: %{tl_version}
Release: %{tl_noarch_release}.1.0.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for ec


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
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
%doc other-free.txt
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbl3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbm.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecbx3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eccc3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecci3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecdh3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecfb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecff.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecfi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecfs.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecit3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eclb8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecli8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eclo8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/eclq8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecltt8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecoc3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecqi8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrb3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecrm3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsc3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsl3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecso3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsq8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecss3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecssdc10.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecst3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecsx3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectc3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecti3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ectt3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecui3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecvt3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ecxc3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exbase.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/excligtb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/excsc.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/excspl.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exidigit.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exileast.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exilig.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exillett.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exilwest.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exisixts.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exitalp.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/expunct.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exroman.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exromp.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exsign.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/exsixtst.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/extextit.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ieclb8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/iecli8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ieclo8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/ieclq8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/iecltt8.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbl3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbm.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcbx3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcci3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcdh.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcfb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcff.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcfi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcfs.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcit3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrb3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcrm3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsl3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcso3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcss3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcst3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcsx3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcti3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tctt3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui0500.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui0600.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui0700.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcui3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvi3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt0800.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt0900.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt1000.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt1095.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt1200.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt1440.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt1728.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt2074.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt2488.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt2986.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/tcvt3583.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txgen.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txifract.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txisuper.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txitlod.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txromod.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecbx3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eccc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecci3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecdh3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecit3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eclb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecli8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eclo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/eclq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecltt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecoc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrb3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecrm3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecso3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecss3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecst3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecsx3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecti3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ectt3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecui3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecvt3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ecxc3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ieclb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/iecli8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ieclo8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/ieclq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/iecltt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcbx3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcci3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcit3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrb3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcrm3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsl3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcso3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcss3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcst3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcsx3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcti3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tctt3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui0500.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui0600.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui0700.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcui3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvi3583.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt0800.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt0900.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt1000.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt1095.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt1200.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt1440.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt1728.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt2074.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt2488.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt2986.tfm
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/tcvt3583.tfm

%files doc
%defattr(-,root,root)
%doc other-free.txt
%{_texdir}/texmf-dist/doc/fonts/ec/00bugs.txt
%{_texdir}/texmf-dist/doc/fonts/ec/00error.txt
%{_texdir}/texmf-dist/doc/fonts/ec/00files.txt
%{_texdir}/texmf-dist/doc/fonts/ec/00inst.txt
%{_texdir}/texmf-dist/doc/fonts/ec/00readme.txt
%{_texdir}/texmf-dist/doc/fonts/ec/copyrite.txt
%{_texdir}/texmf-dist/doc/fonts/ec/dc-chg.txt
%{_texdir}/texmf-dist/doc/fonts/ec/dcdoc.tex
%{_texdir}/texmf-dist/doc/fonts/ec/ec-chg.txt
%{_texdir}/texmf-dist/doc/fonts/ec/ecstdedt.tex
%{_texdir}/texmf-dist/doc/fonts/ec/tc-chg.txt
%{_texdir}/texmf-dist/doc/fonts/ec/tcstdedt.tex


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
