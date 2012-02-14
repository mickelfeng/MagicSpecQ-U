Name:           telepathy-filesystem
Version:        0.0.2
Release:        2%{?dist}
Summary:        Telepathy filesystem layout
Summary(zh_CN): Telepathy 文件系统布局

Group:          System Environment/Base
Group(zh_CN):	系统环境/基本
License:        Public Domain
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       filesystem


%description
This package provides some directories which are required by other
packages which comprise the Telepathy release.  

%description -l zh_CN
Telepathy 文件系统布局.

%prep


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/managers
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/clients
mkdir -p $RPM_BUILD_ROOT%{_includedir}/telepathy-1.0


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers
%dir %{_datadir}/telepathy/clients
%dir %{_includedir}/telepathy-1.0


%changelog
* Tue Feb 14 2012 Liu Di <liudidi@gmail.com> - 0.0.2-2
- 为 Magic 3.0 重建


