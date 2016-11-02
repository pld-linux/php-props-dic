%define		pkgname props-dic
%define		php_min_version 5.3.3
Summary:	An IDE and static analysis friendly PHP DI container
Name:		php-%{pkgname}
Version:	2.2.0
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/mrclay/Props/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b33eb3f60a41a7caa5ea0794a357ab92
URL:		https://packagist.org/packages/mrclay/props-dic
Requires:	php(core) >= %{php_min_version}
Requires:	php-container-interop >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Props is a simple DI container that allows retrieving values via
custom property and method names.

%prep
%setup -qn Props-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE composer.json
%{php_data_dir}/Props
