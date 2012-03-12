%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/cs.tar.xz

Name: texlive-cs
License: LPPL
Summary: cs package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires: texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-tetex-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-cs-fedora-fonts = %{tl_version}

%description
cs package

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
echo "MixedMap csother.map" >> %{_texdir}/texmf/web2c/updmap.cfg
echo "MixedMap cstext.map" >> %{_texdir}/texmf/web2c/updmap.cfg
touch /var/run/texlive/run-updmap
:

%postun
if [ $1 == 0 ]; then
  sed -i '/^MixedMap csother.map/d' %{_texdir}/texmf/web2c/updmap.cfg
  sed -i '/^MixedMap cstext.map/d' %{_texdir}/texmf/web2c/updmap.cfg
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

%package fedora-fonts
Summary: Fonts for cs
Version: %{tl_version}
Release: %{tl_noarch_release}.svn15878%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-cs = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Fonts for cs package.


%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_texdir}/texmf-dist
xz -dc %{SOURCE0} | tar x -C %{buildroot}%{_texdir}/texmf-dist
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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csb10.pfb .
ln -s %{_fontdir}/csb10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csb10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx10.pfb .
ln -s %{_fontdir}/csbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx12.pfb .
ln -s %{_fontdir}/csbx12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx5.pfb .
ln -s %{_fontdir}/csbx5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx6.pfb .
ln -s %{_fontdir}/csbx6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx7.pfb .
ln -s %{_fontdir}/csbx7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx8.pfb .
ln -s %{_fontdir}/csbx8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx9.pfb .
ln -s %{_fontdir}/csbx9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxsl10.pfb .
ln -s %{_fontdir}/csbxsl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxsl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxti10.pfb .
ln -s %{_fontdir}/csbxti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cscsc10.pfb .
ln -s %{_fontdir}/cscsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cscsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csdunh10.pfb .
ln -s %{_fontdir}/csdunh10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csdunh10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csff10.pfb .
ln -s %{_fontdir}/csff10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csff10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csfi10.pfb .
ln -s %{_fontdir}/csfi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csfi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csfib8.pfb .
ln -s %{_fontdir}/csfib8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csfib8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csinch.pfb .
ln -s %{_fontdir}/csinch.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csinch.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csitt10.pfb .
ln -s %{_fontdir}/csitt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csitt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr10.pfb .
ln -s %{_fontdir}/csr10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr12.pfb .
ln -s %{_fontdir}/csr12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr17.pfb .
ln -s %{_fontdir}/csr17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr5.pfb .
ln -s %{_fontdir}/csr5.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr5.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr6.pfb .
ln -s %{_fontdir}/csr6.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr6.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr7.pfb .
ln -s %{_fontdir}/csr7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr8.pfb .
ln -s %{_fontdir}/csr8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr9.pfb .
ln -s %{_fontdir}/csr9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csr9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl10.pfb .
ln -s %{_fontdir}/cssl10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl12.pfb .
ln -s %{_fontdir}/cssl12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl8.pfb .
ln -s %{_fontdir}/cssl8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl9.pfb .
ln -s %{_fontdir}/cssl9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssltt10.pfb .
ln -s %{_fontdir}/cssltt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cssltt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss10.pfb .
ln -s %{_fontdir}/csss10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss12.pfb .
ln -s %{_fontdir}/csss12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss17.pfb .
ln -s %{_fontdir}/csss17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss8.pfb .
ln -s %{_fontdir}/csss8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss9.pfb .
ln -s %{_fontdir}/csss9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csss9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssbx10.pfb .
ln -s %{_fontdir}/csssbx10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssbx10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssdc10.pfb .
ln -s %{_fontdir}/csssdc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssdc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi10.pfb .
ln -s %{_fontdir}/csssi10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi12.pfb .
ln -s %{_fontdir}/csssi12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi17.pfb .
ln -s %{_fontdir}/csssi17.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi17.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi8.pfb .
ln -s %{_fontdir}/csssi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi9.pfb .
ln -s %{_fontdir}/csssi9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssq8.pfb .
ln -s %{_fontdir}/csssq8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssq8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssqi8.pfb .
ln -s %{_fontdir}/csssqi8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csssqi8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstcsc10.pfb .
ln -s %{_fontdir}/cstcsc10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstcsc10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti10.pfb .
ln -s %{_fontdir}/csti10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti12.pfb .
ln -s %{_fontdir}/csti12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti7.pfb .
ln -s %{_fontdir}/csti7.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti7.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti8.pfb .
ln -s %{_fontdir}/csti8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti9.pfb .
ln -s %{_fontdir}/csti9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csti9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt10.pfb .
ln -s %{_fontdir}/cstt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt12.pfb .
ln -s %{_fontdir}/cstt12.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt12.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt8.pfb .
ln -s %{_fontdir}/cstt8.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt8.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt9.pfb .
ln -s %{_fontdir}/cstt9.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt9.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csu10.pfb .
ln -s %{_fontdir}/csu10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csu10.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csvtt10.pfb .
ln -s %{_fontdir}/csvtt10.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/public/cs/csvtt10.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_texdir}/texmf-dist/dvips/cs/config.cs
%{_texdir}/texmf-dist/fonts/enc/dvips/cs/csin.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cs/csr.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cs/csr1.enc
%{_texdir}/texmf-dist/fonts/enc/dvips/cs/cstt.enc
%{_texdir}/texmf-dist/fonts/map/dvips/cs/csfont-e.map
%{_texdir}/texmf-dist/fonts/map/dvips/cs/csother.map
%{_texdir}/texmf-dist/fonts/map/dvips/cs/cstext.map
%{_texdir}/texmf-dist/fonts/source/public/cs/csaccent.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csacutl.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csacutu.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csadded.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csb9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxsl9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxti10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxti12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csbxti17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscode.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscsc12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscsc17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscsc8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cscsc9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csdunh9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csff10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csfi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csfib10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csfib12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csfib8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csfib9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cshachel.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cshacheu.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cshyph.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csiacutl.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csihachl.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csinch.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csiothrl.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csitt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csitt12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csitt17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csitt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csitt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csotherl.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csotheru.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csr9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl5.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl6.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssl9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssltt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssltt12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssltt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cssltt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csss10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csss12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csss17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csss8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csss9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssbx10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssbx12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssbx17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssbx9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssdc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssi10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssi12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssi17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssi9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssq8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csssqi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstcsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstcsc12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstcsc17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstex10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstex8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstex9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csti9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstt12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/cstt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu17.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu7.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csu9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csvtt10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csvtt12.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csvtt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/csvtt9.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/icscsc10.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/icstt8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/ilcsss8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/ilcsssb8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/ilcsssi8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/kmcsc.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/kmroman.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/kmtexset.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/kmtextit.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/kmtitle.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/lcsss8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/lcsssb8.mf
%{_texdir}/texmf-dist/fonts/source/public/cs/lcsssi8.mf
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csb9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxsl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csbxti17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cscsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cscsc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cscsc17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cscsc8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cscsc9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csdunh9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csff10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csfi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csfib10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csfib12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csfib8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csfib9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csinch.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csitt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csitt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csitt17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csitt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csitt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csr9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl5.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl6.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssl9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssltt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssltt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssltt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cssltt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csss10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csss12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csss17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csss9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssbx10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssbx12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssbx17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssbx9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssdc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssi10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssi12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssi17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssi9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssq8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csssqi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstcsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstcsc12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstcsc17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csti9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/cstt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu17.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu7.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csu9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csvtt10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csvtt12.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csvtt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/csvtt9.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/icscsc10.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/icstt8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/ilcsss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/ilcsssb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/ilcsssi8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/lcsss8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/lcsssb8.tfm
%{_texdir}/texmf-dist/fonts/tfm/public/cs/lcsssi8.tfm
%{_texdir}/texmf-dist/fonts/type1/public/cs/README
%{_texdir}/texmf-dist/fonts/type1/public/cs/csb10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbx9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxsl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csbxti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cscsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csdunh10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csff10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csfi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csfib8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csinch.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csitt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr5.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr6.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csr9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cssl9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cssltt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csss10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csss12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csss17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csss8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csss9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssbx10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssdc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi17.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssi9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssq8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csssqi8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cstcsc10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csti10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csti12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csti7.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csti8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csti9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt12.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt8.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/cstt9.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csu10.pfb
%{_texdir}/texmf-dist/fonts/type1/public/cs/csvtt10.pfb

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/csb10.pfb
%{_fontdir}/csbx10.pfb
%{_fontdir}/csbx12.pfb
%{_fontdir}/csbx5.pfb
%{_fontdir}/csbx6.pfb
%{_fontdir}/csbx7.pfb
%{_fontdir}/csbx8.pfb
%{_fontdir}/csbx9.pfb
%{_fontdir}/csbxsl10.pfb
%{_fontdir}/csbxti10.pfb
%{_fontdir}/cscsc10.pfb
%{_fontdir}/csdunh10.pfb
%{_fontdir}/csff10.pfb
%{_fontdir}/csfi10.pfb
%{_fontdir}/csfib8.pfb
%{_fontdir}/csinch.pfb
%{_fontdir}/csitt10.pfb
%{_fontdir}/csr10.pfb
%{_fontdir}/csr12.pfb
%{_fontdir}/csr17.pfb
%{_fontdir}/csr5.pfb
%{_fontdir}/csr6.pfb
%{_fontdir}/csr7.pfb
%{_fontdir}/csr8.pfb
%{_fontdir}/csr9.pfb
%{_fontdir}/cssl10.pfb
%{_fontdir}/cssl12.pfb
%{_fontdir}/cssl8.pfb
%{_fontdir}/cssl9.pfb
%{_fontdir}/cssltt10.pfb
%{_fontdir}/csss10.pfb
%{_fontdir}/csss12.pfb
%{_fontdir}/csss17.pfb
%{_fontdir}/csss8.pfb
%{_fontdir}/csss9.pfb
%{_fontdir}/csssbx10.pfb
%{_fontdir}/csssdc10.pfb
%{_fontdir}/csssi10.pfb
%{_fontdir}/csssi12.pfb
%{_fontdir}/csssi17.pfb
%{_fontdir}/csssi8.pfb
%{_fontdir}/csssi9.pfb
%{_fontdir}/csssq8.pfb
%{_fontdir}/csssqi8.pfb
%{_fontdir}/cstcsc10.pfb
%{_fontdir}/csti10.pfb
%{_fontdir}/csti12.pfb
%{_fontdir}/csti7.pfb
%{_fontdir}/csti8.pfb
%{_fontdir}/csti9.pfb
%{_fontdir}/cstt10.pfb
%{_fontdir}/cstt12.pfb
%{_fontdir}/cstt8.pfb
%{_fontdir}/cstt9.pfb
%{_fontdir}/csu10.pfb
%{_fontdir}/csvtt10.pfb

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
