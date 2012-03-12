%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/adobemapping.tar.xz

Name: texlive-adobemapping
License: Freely redistributable without restriction
Summary: Adobe cmap and pdfmapping files
Version: %{tl_version}
Release: %{tl_noarch_release}.svn19169%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
The package comprises the collection of CMap and PDF mapping
files now made available for distribution by Adobe systems
incorporated.

date: 2010-06-01 09:42:37 +0200

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


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
ln -s %{_texdir}/licenses/other-free.txt other-free.txt
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/LICENSE
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/README
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/cmap-current-versions.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/cmap-readme.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/mapping-readme.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/90ms-RKSJ-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/90pv-RKSJ-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/90pv-RKSJ-UCS2C
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-B5pc
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-ETen-B5
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-CID
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-Host
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-CNS1-H-Mac
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-GBK-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-GBpc-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-CID
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-Host
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-GB1-H-Mac
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-90ms-RKSJ
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-90pv-RKSJ
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-CID
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-Host
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-H-Mac
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-PS-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Japan1-PS-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-CID
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-Host
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-H-Mac
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-KSCms-UHC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/Adobe-Korea1-KSCpc-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/B5pc-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/B5pc-UCS2C
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/ETen-B5-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/GBK-EUC-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/GBpc-EUC-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/GBpc-EUC-UCS2C
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/KSCms-UHC-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/KSCpc-EUC-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/KSCpc-EUC-UCS2C
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-90ms-RKSJ
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-90pv-RKSJ
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-B5pc
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-ETen-B5
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-GBK-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-GBpc-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-KSCms-UHC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/MappingOther/UCS2-KSCpc-EUC
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode/Adobe-CNS1-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode/Adobe-GB1-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode/Adobe-Japan1-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ToUnicode/Adobe-Korea1-UCS2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-0
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-1
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-3
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-4
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-5
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/Adobe-CNS1-6
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/B5pc-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/B5pc-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS1-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS1-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS2-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/CNS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETHK-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETHK-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETen-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETen-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETenms-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/ETenms-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKdla-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKdla-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKdlb-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKdlb-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKgccs-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKgccs-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKm314-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKm314-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKm471-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKm471-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKscs-B5-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/HKscs-B5-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UCS2-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UCS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF16-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF16-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF8-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/CMap/UniCNS-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ac16/cid2code.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-0
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-1
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-3
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-4
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/Adobe-GB1-5
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GB-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GB-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GB-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GB-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBK-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBK-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBK2K-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBK2K-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBKp-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBKp-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBT-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBT-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBT-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBT-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBTpc-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBTpc-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBpc-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/GBpc-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UCS2-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UCS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF16-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF16-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF8-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/CMap/UniGB-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ag15/cid2code.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ai0/CMap/Identity-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ai0/CMap/Identity-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78ms-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/78ms-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/83pv-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90ms-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90ms-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90msp-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90msp-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90pv-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/90pv-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Add-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Add-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Add-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Add-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-0
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-1
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-3
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-4
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-5
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Adobe-Japan1-6
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Ext-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Ext-RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Ext-RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Ext-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Hankaku
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Hiragana
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Katakana
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/NWP-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/NWP-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/RKSJ-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/RKSJ-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/Roman
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-HW-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-HW-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UCS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF16-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF16-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF8-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF16-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF16-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF8-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJIS2004-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UCS2-HW-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UCS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISPro-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISX0213-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISX0213-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISX02132004-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/UniJISX02132004-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/CMap/WP-Symbol
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/aj16/cid2code.txt
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-0
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-1
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/Adobe-Korea1-2
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-Johab-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-Johab-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-HW-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-HW-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCms-UHC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCpc-EUC-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/KSCpc-EUC-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UCS2-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UCS2-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF16-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF16-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF32-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF32-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF8-H
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/CMap/UniKS-UTF8-V
%{_texdir}/texmf-dist/fonts/cmap/adobemapping/ak12/cid2code.txt


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
