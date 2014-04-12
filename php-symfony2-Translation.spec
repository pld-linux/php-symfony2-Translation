%define		pearname	Translation
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Translation Component
Name:		php-symfony2-Translation
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	9835ea141e8a225e37e3cf747f35386b
URL:		http://symfony.com/doc/2.4/book/translation.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translation provides tools for loading translation files and
generating translated strings from these including support for
pluralization.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Translation
%{php_pear_dir}/Symfony/Component/Translation/*.php
%{php_pear_dir}/Symfony/Component/Translation/Catalogue
%{php_pear_dir}/Symfony/Component/Translation/Dumper
%{php_pear_dir}/Symfony/Component/Translation/Exception
%{php_pear_dir}/Symfony/Component/Translation/Extractor
%{php_pear_dir}/Symfony/Component/Translation/Loader
%{php_pear_dir}/Symfony/Component/Translation/Writer
