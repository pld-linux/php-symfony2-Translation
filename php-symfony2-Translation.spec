%define		package	Translation
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Translation Component
Name:		php-symfony2-Translation
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	d2ded9d18907c55ebf1fb743af55f901
URL:		http://symfony.com/doc/2.7/book/translation.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Yaml
Conflicts:	php-symfony2-Config < 2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translation provides tools for loading translation files and
generating translated strings from these including support for
pluralization.

%prep
%setup -q -n %{package}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Translation
%{php_pear_dir}/Symfony/Component/Translation/*.php
%{php_pear_dir}/Symfony/Component/Translation/Catalogue
%{php_pear_dir}/Symfony/Component/Translation/Dumper
%{php_pear_dir}/Symfony/Component/Translation/Exception
%{php_pear_dir}/Symfony/Component/Translation/Extractor
%{php_pear_dir}/Symfony/Component/Translation/Loader
%{php_pear_dir}/Symfony/Component/Translation/Writer
