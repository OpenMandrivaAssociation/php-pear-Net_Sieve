%define		_class		Net
%define		_subclass	Sieve
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.2
Release:	1
Summary:	Handles talking to timsieved
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Sieve/
Source0:	http://download.pear.php.net/package/Net_Sieve-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0
BuildArch:	noarch
BuildRequires:	php-pear

%description
Provides an API to talk to the timsieved server that comes with Cyrus
IMAPd. Can be used to install, remove, mark active etc sieve scripts.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 667633
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 569610
- new version

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.7-2mdv2010.1
+ Revision: 468716
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.7-1mdv2010.0
+ Revision: 400321
- update to new version 1.1.7

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-2mdv2009.1
+ Revision: 321887
- rebuild

* Wed Aug 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-1mdv2009.0
+ Revision: 274173
- fix "build"
- 1.1.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1.5-4mdv2009.0
+ Revision: 224838
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-3mdv2008.1
+ Revision: 178531
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-2mdv2008.0
+ Revision: 33606
- filter out pear(PHPUnit2

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-1mdv2008.0
+ Revision: 15604
- fix build and deps
- 1.1.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdv2007.0
+ Revision: 81180
- Import php-pear-Net_Sieve

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdk
- 1.1.2
- new group (Development/PHP)

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdk
- rebuild

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- 1.1.1
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.1.0-1mdk
- First mdk package


