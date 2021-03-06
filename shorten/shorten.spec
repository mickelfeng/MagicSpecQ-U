%define version 3.6.0
%define release 3%{dist}

Name: shorten
Summary: Audio file lossless compress/uncompress utility
Summary(zh_CN.UTF-8): 音频文件无损压缩/解压缩工具
Version: %{version}
Release: %{release}
License: shorten license
Group: Applications/Multimedia
Group(zh_CN.UTF-8): 应用程序/多媒体
Url: http://www.hornig.net/shorten.html
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Packager: kde <athena_star@163.com>
#Requires: 

%description
Shorten is a utility developed by Tony Robinson and SoftSound Limited at www.softsound.com to convert audio files to and from a compressed format. Compression of about 50% is typical. MP3 compression is usually much greater, but unlike MP3 files, shortened files result in no loss of fidelity. Shorten can operate in both lossy and lossless modes.

%description -l zh_CN.UTF-8
Shorten 是由 SoftSound 有限公司（www.softsound.com）的 Tony Robinson 开发的一款音频文件
压缩/解压缩工具。典型情况下压缩率可达 50%。MP3 压缩率通常更高，但是与 MP3 文件不同，
Shorten 文件（扩展名 .shn）可获得无损的保真度。Shorten 可以使用有损和无损模式。

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags} CFLAGS="-O3  -pipe"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}


%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING doc/LICENSE doc/TODO doc/tr156.ps NEWS README
%{_bindir}
%{_mandir}

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 3.6.0-3
- 为 Magic 3.0 重建

* Sat Sep 22 2007 kde <athena_star@163.com> - 3.6.0-1mgc
- init the spec file
