Name:           bytelist
Version:        0.1
Release:        %mkrel 2.2.svn6558.3
Summary:        A java library for lists of bytes

Group:          Development/Java
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://jruby.codehaus.org/
# The source for this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
#   svn export http://svn.codehaus.org/jruby/bytelist/trunk/ bytelist
#   tar -cjf bytelist-svn6558.tar.bz2 bytelist/
Source0:        %{name}-svn6558.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       java >= 1.5
Requires:       jpackage-utils


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{name}


%build
export CLASSPATH=$(build-classpath junit)
%ant


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/%{name}-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


%check
%ant test


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/%{name}.jar


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-2.2.svn6558.3mdv2011.0
+ Revision: 616906
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.1-2.2.svn6558.2mdv2010.0
+ Revision: 424701
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.1-2.2.svn6558.1mdv2009.0
+ Revision: 266434
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 28 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.1-0.2.svn6558.1mdv2009.0
+ Revision: 198008
- fix Group
- import bytelist


