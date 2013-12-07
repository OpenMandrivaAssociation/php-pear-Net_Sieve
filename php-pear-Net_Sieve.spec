%define	_class	Net
%define	_subclass	Sieve
%define	modname	%{_class}_%{_subclass}

Summary:	Handles talking to timsieved
Name:		php-pear-%{modname}
Version:	1.3.2
Release:	3
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_Sieve/
Source0:	http://download.pear.php.net/package/Net_Sieve-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

