%define tl_version 2011
%define tl_noarch_release 9
%define _binary_payload w6.xzdio

%{!?_texdir: %global _texdir %{_datadir}/texlive}

%define __perl_requires %{nil}
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __debug_install_post %{nil}

Source0: ftp://ftp.ctex.org/mirrors/texlive/tlpretest/archive/helvetic.tar.xz

Name: texlive-helvetic
License: LPPL
Summary: helvetic package
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16767%{?dist}
BuildArch: noarch
Requires: texlive-base = %{tl_version}
Requires: texlive-kpathsea-bin = %{tl_version}
Requires(post,postun): texlive-kpathsea-bin = %{tl_version}
Requires: texlive-helvetic-fedora-fonts = %{tl_version}

%description
helvetic package

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

%package fedora-fonts
Summary: Fonts for helvetic
Version: %{tl_version}
Release: %{tl_noarch_release}.svn16767%{?dist}
Requires: fontpackages-filesystem
BuildRequires: fontpackages-devel
Requires: texlive-helvetic = %{tl_version}
BuildArch: noarch

%description fedora-fonts
Fonts for helvetic package.


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
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb .
ln -s %{_fontdir}/uhvb8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8ac.pfb .
ln -s %{_fontdir}/uhvb8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8a.pfb .
ln -s %{_fontdir}/uhvbo8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8ac.pfb .
ln -s %{_fontdir}/uhvbo8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvboc8a.pfb .
ln -s %{_fontdir}/uhvboc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvboc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbrc8a.pfb .
ln -s %{_fontdir}/uhvbrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbrc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a-105.pfb .
ln -s %{_fontdir}/uhvr8a-105.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a-105.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb .
ln -s %{_fontdir}/uhvr8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8ac.pfb .
ln -s %{_fontdir}/uhvr8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a-105.pfb .
ln -s %{_fontdir}/uhvro8a-105.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a-105.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfb .
ln -s %{_fontdir}/uhvro8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8ac.pfb .
ln -s %{_fontdir}/uhvro8ac.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8ac.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvroc8a.pfb .
ln -s %{_fontdir}/uhvroc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvroc8a.pfb
mv %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvrrc8a.pfb .
ln -s %{_fontdir}/uhvrrc8a.pfb %{buildroot}%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvrrc8a.pfb
popd
%_font_pkg -n fedora *

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_texdir}/texmf-dist/dvips/helvetic/config.uhv
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvb8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvb8an.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvbo8an.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvr8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvr8an.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvro8a.afm
%{_texdir}/texmf-dist/fonts/afm/adobe/helvetic/phvro8an.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvb8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvb8ac.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvbo8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvbo8ac.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvr8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvr8ac.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvro8a.afm
%{_texdir}/texmf-dist/fonts/afm/urw/helvetic/uhvro8ac.afm
%{_texdir}/texmf-dist/fonts/map/dvips/helvetic/uhv.map
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvb8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbc7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbc8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbo8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbon.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvbrn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvr8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrc.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrc7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrc8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvro8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvron.tfm
%{_texdir}/texmf-dist/fonts/tfm/adobe/helvetic/phvrrn.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvb8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvbc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvbn8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvbnc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvbo8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvbon8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvr8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvrc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvrn8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvrnc8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvro8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/phvron8z.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvbo.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvbon.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvbrn.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvro.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvron.tfm
%{_texdir}/texmf-dist/fonts/tfm/cspsfonts-adobe/helvetic/rphvrrn.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arb10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arb2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arb7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arb8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arb9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/ari10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/ari2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/ari7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/ari8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/ari9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arj10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arj2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arj7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arj8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arj9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arr10u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arr2n.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arr7j.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arr8u.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/arr9t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvb.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvbi.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvr.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvri.tfm
%{_texdir}/texmf-dist/fonts/tfm/monotype/helvetic/mhvri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvb8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbc7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbc8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbi7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbi8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbi8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbi8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvbo8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvr8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvrc7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvrc7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvrc8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvrc8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvri8tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro7t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro7tn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8c.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8cn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8r.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8rn.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8t.tfm
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/helvetic/uhvro8tn.tfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvb8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbo8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvboc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvbrc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a-105.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvr8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a-105.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8ac.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvro8ac.pfm
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvroc8a.pfb
%{_texdir}/texmf-dist/fonts/type1/urw/helvetic/uhvrrc8a.pfb
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb8cn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvb8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbc7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbc8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo8cn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbo8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbon.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvbrn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr8cn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvr8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrc.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrc7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrc8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro7t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro7tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro8c.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro8cn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro8t.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvro8tn.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvron.vf
%{_texdir}/texmf-dist/fonts/vf/adobe/helvetic/phvrrn.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvb8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvbc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvbn8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvbnc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvbo8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvbon8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvr8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvrc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvrn8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvrnc8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvro8z.vf
%{_texdir}/texmf-dist/fonts/vf/cspsfonts-adobe/helvetic/phvron8z.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvb.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvb8t.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvbi.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvr.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvr8t.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvri.vf
%{_texdir}/texmf-dist/fonts/vf/monotype/helvetic/mhvri8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb8cn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvb8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbc7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbc8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbi7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbi8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbi8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo8cn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvbo8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr8cn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvr8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvrc7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvrc7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvrc8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvrc8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri8cn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvri8tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro7t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro7tn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro8c.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro8cn.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro8t.vf
%{_texdir}/texmf-dist/fonts/vf/urw35vf/helvetic/uhvro8tn.vf
%{_texdir}/texmf-dist/tex/latex/helvetic/8ruhv.fd
%{_texdir}/texmf-dist/tex/latex/helvetic/omluhv.fd
%{_texdir}/texmf-dist/tex/latex/helvetic/omsuhv.fd
%{_texdir}/texmf-dist/tex/latex/helvetic/ot1uhv.fd
%{_texdir}/texmf-dist/tex/latex/helvetic/t1uhv.fd
%{_texdir}/texmf-dist/tex/latex/helvetic/ts1uhv.fd

%files fedora-fonts
%defattr(-,root,root)
%dir %{_fontdir}
%{_fontdir}/uhvb8a.pfb
%{_fontdir}/uhvb8ac.pfb
%{_fontdir}/uhvbo8a.pfb
%{_fontdir}/uhvbo8ac.pfb
%{_fontdir}/uhvboc8a.pfb
%{_fontdir}/uhvbrc8a.pfb
%{_fontdir}/uhvr8a-105.pfb
%{_fontdir}/uhvr8a.pfb
%{_fontdir}/uhvr8ac.pfb
%{_fontdir}/uhvro8a-105.pfb
%{_fontdir}/uhvro8a.pfb
%{_fontdir}/uhvro8ac.pfb
%{_fontdir}/uhvroc8a.pfb
%{_fontdir}/uhvrrc8a.pfb

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
