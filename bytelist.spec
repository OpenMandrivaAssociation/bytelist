%{?_javapackages_macros:%_javapackages_macros}
%global  git_commit d0ec879
%global  cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           bytelist
Version:        1.0.8
Release:        9.3
Group:		Development/Java
Summary:        A java library for lists of bytes


License:        CPL or GPLv2+ or LGPLv2+
URL:            https://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  jcodings
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       java
Requires:       jcodings
Requires:       jpackage-utils


%description
A small java library for manipulating lists of bytes.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -delete
find -name '*.jar' -delete


%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
mkdir -p lib
%ant


%install
mkdir -p %{buildroot}%{_javadir}

cp -p lib/%{name}-1.0.2.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%check
export CLASSPATH=$(build-classpath junit jcodings)
%ant test

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml
%doc README.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> - 1.0.8-4
- add maven pom
- adapt to current guideline

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.8-1
- Bumped version to latest upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 25 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.0.5-1
- Bumped version to latest upstream release

* Tue Feb 09 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.3-2
- Fix the clean up code in the prep section
- Fix typo
- Save changelog

* Thu Jan 28 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> - 1.0.3-1
- 1.0.3
- Remove gcj bits
- New URL
- Use macros in all sections of the spec
- Add README.txt generated on the fly

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.svn9177
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.1-0.1.svn9177
- Bump to SVN HEAD.

* Sun Feb 15 2009 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Bump to 1.0 release.

* Tue Apr 22 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-0.2.svn6558
- Do not include version in jar filename.
- Run tests in check section.

* Tue Apr 22 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-0.1.svn6558
- Initial RPM.
