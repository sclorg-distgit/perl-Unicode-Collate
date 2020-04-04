%{?scl:%scl_package perl-Unicode-Collate}

Name:           %{?scl_prefix}perl-Unicode-Collate
Version:        1.27
Release:        451%{?dist}
Summary:        Unicode Collation Algorithm
# Collate/allkeys.txt:  Unicode (the file contains a link to
#                       <http://www.unicode.org/terms_of_use.html>)
# other files:          GPL+ or Artistic
License:        (GPL+ or Artistic) and Unicode
URL:            https://metacpan.org/release/Unicode-Collate
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SADAHIRO/Unicode-Collate-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Unicode::Normalize)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Unicode::Normalize)
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

%description
This package is Perl implementation of Unicode Technical Standard #10 (Unicode
Collation Algorithm).

%prep
%setup -q -n Unicode-Collate-%{version}

# Remove pregenerated files
rm Collate/Locale/*
# Collate/CJK/Korean.pm is an input for the mklocale script, do not remove it

%build
# Regenerate code from Collate/allkeys.txt whose authority is
# <http://www.unicode.org/Public/UCA/latest/allkeys.txt>
perl mklocale
mv Locale/*.pl Collate/Locale
mv Korean.pm Collate/CJK

%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode*
%{_mandir}/man3/*

%changelog
* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 1.27-1
- 1.27 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Tue Nov 21 2017 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Fri Nov 03 2017 Petr Pisar <ppisar@redhat.com> - 1.20-1
- 1.20 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-393
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-3
- Fixes for removal '.' from @INC in Perl 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Tue Nov 08 2016 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Mon Oct 31 2016 Petr Pisar <ppisar@redhat.com> - 1.17-1
- 1.17 bump

* Wed Oct 26 2016 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump

* Mon Oct 24 2016 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Mon Sep 19 2016 Petr Pisar <ppisar@redhat.com> - 1.14-366
- License corrected to ((GPL+ or Artistic) and Unicode)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Thu Jul 02 2015 Petr Pisar <ppisar@redhat.com> 1.12-348
- Specfile autogenerated by cpanspec 1.78.
- Run mklocale only if not bootstrapping
