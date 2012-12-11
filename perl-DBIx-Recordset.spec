%define upstream_name	 DBIx-Recordset
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl extension for DBI recordsets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:  perl(DBD::Pg)
BuildArch:	noarch
Requires:	perl(DBI)

%description
DBIx::Recordset is a perl module for abstraction and simplification of database
access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention is
made on web applications to make it possible to handle the state-less access
and to process the posted data of formfields, but DBIx::Recordset is not
limited to web applications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 Changes Recordset.pm
perl -pi -e 's/\cM//' Changes
perl Makefile.PL INSTALLDIRS=vendor << EOF




EOF
make

%install
%makeinstall_std

%files
%doc Changes README TODO
%{_mandir}/*/*
%{perl_vendorlib}/DBIx


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.260.0-2mdv2011.0
+ Revision: 681361
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 406978
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.26-5mdv2009.0
+ Revision: 256588
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.26-3mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.26-3mdv2007.0
+ Revision: 108544
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-DBIx-Recordset

* Wed Nov 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.26-2mdk
- Fix URL, summary, description, build, install, line endings and permissions
- Require DBI and perl-base by hand since perl.req doesn't seem to find it

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.26-1mdk
- 0.26

* Thu Apr 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25a-1mdk
- 0.25a

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.24-8mdk
- rebuild
- own dir

