%global	gemdir		%{gem_dir}
%global	majorver	2.11.3
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	fedorarel	1

%global	gemname	rspec-expectations
%global	gem_name %gemname
%global	geminstdir	%{gem_instdir}

%global	rubyabi	1.9.1

# %%check section needs rspec-core, however rspec-core depends on rspec-expectations
# runtime part of rspec-expectaions does not depend on rspec-core
%global	need_bootstrap_set	1

%{!?need_bootstrap:	%global	need_bootstrap	%{need_bootstrap_set}}

Summary:	Rspec-2 expectations (should and matchers) 
Name:		rubygem-%{gemname}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{fedorarel}%{?preminorver:%{rpmminorver}}%{?dist}.1

Group:		Development/Languages
License:	MIT
URL:		http://github.com/rspec/rspec-expectations
Source0:	http://rubygems.org/gems/%{gemname}-%{fullver}.gem

BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	rubygems-devel
%if 0%{?need_bootstrap} < 1
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(minitest)
%endif
Requires:	ruby(abi) = %{rubyabi}
Requires:	rubygem(diff-lcs)
Provides:	rubygem(%{gemname}) = %{version}-%{release}
BuildArch:	noarch

%description
rspec-expectations adds `should` and `should_not` to every object and includes
RSpec::Matchers, a library of standard matchers.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install \
	-V \
	--local \
	--install-dir .%{gemdir} \
	--force \
	--rdoc \
	%{SOURCE0}

chmod 0644 .%{gemdir}/cache/%{gemname}-%{fullver}.gem

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/

# cleanups
rm -f %{buildroot}%{geminstdir}/{.document,.gitignore,.travis.yml,.yardopts}

%if 0%{?need_bootstrap} < 1
%check
pushd .%{geminstdir}
ruby -rubygems -Ilib/ -S rspec spec/
popd
%endif

%files
%defattr(-,root,root,-)
%dir	%{geminstdir}

%doc	%{geminstdir}/License.txt
%doc	%{geminstdir}/*.md
%{geminstdir}/lib/

%{gemdir}/cache/%{gemname}-%{fullver}.gem
%{gemdir}/specifications/%{gemname}-%{fullver}.gemspec


%files	doc
%defattr(-,root,root,-)
%{gemdir}/doc/%{gemname}-%{fullver}
%{geminstdir}/features/
%{geminstdir}/spec/

%changelog
* Sat Dec 08 2012 Liu Di <liudidi@gmail.com> - 2.11.3-1.1
- 为 Magic 3.0 重建

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.11.3-1
- 2.11.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.0-2
- Require (diff-lcs) again

* Sun Jan 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.0-1
- 2.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-1
- 2.6.0

* Tue May 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.3.rc6
- 2.6.0 rc6

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And enable check on rawhide

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.1.rc4
- 2.6.0 rc4

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And enable check on rawhide

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.5.0-2
- Cleanups

* Thu Feb 17 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-1
- 2.5.0

* Fri Nov 05 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- Initial package
