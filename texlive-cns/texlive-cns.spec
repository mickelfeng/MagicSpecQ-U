%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cns.tar.xz
Source1: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cns.doc.tar.xz

Name: texlive-cns
License: LPPL
Summary: cns package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}

%description
cns package

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
Summary: Documentation for cns
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: texlive-base = %{tl_version}
BuildArch: noarch

%description doc
Documentation for cns


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
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
%{_texdir}/texmf-dist/fonts/misc/cns/4040w0.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w1.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w2.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w3.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w4.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w5.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w6.bin
%{_texdir}/texmf-dist/fonts/misc/cns/4040w7.bin
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-1.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-2.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-3.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-4.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-5.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-6.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-7.hbf
%{_texdir}/texmf-dist/fonts/misc/cns/cns40-b5.hbf
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1226.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1227.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1228.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1229.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1230.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1231.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1232.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1233.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1234.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1235.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1236.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1237.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1238.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1239.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1240.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1241.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1242.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1243.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1244.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1245.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1246.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1247.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1248.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1249.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1250.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1251.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1252.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1253.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1254.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c0so12/c0so1255.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1226.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1227.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1228.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1229.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1230.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1231.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1232.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1233.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c1so12/c1so1234.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1226.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1227.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1228.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1229.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c2so12/c2so1230.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c3so12/c3so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1226.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1227.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1228.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c4so12/c4so1229.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1226.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1227.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1228.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1229.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1230.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1231.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1232.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1233.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c5so12/c5so1234.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c6so12/c6so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1201.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1202.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1203.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1204.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1205.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1206.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1207.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1208.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1209.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1210.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1211.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1212.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1213.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1214.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1215.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1216.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1217.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1218.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1219.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1220.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1221.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1222.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1223.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1224.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1225.tfm
%{_texdir}/texmf-dist/fonts/tfm/cns/c7so12/c7so1226.tfm

%files doc
%defattr(-,root,root)
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-1/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-2/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-3/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-4/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-5/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-6/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-7/README
%{_texdir}/texmf-dist/doc/fonts/cns/cns40-b5/README


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
