Name:          qmmp
Version:        0.5.3
Release:        2%{?dist}
Summary:        A qt4 based media player similar to xmms
Summary(zh_CN): 基于 qt4 的类似 xmms 的媒体播放器

Group:         Applications/Multimedia
Group(zh_CN):	应用程序/多媒体
License:       GPLv2
URL:             http://audacious-media-player.org/

Source0:       qmmp-%{version}.tar.bz2
Source1:	     skins.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  qt4-devel

%description
beep-media-player  is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.

%description -l zh_CN
基于 qt4 的类似 xmms 的媒体播放器。

%prep
%setup -q -n  qmmp-%{version}
%build

install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	..

make

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/qmmp
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
tar xvf %{SOURCE1} -C $RPM_BUILD_ROOT/usr/share/qmmp

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}/*.so*
%{_libdir}/qmmp/*

%changelog
