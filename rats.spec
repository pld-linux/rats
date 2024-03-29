Summary:	Rough Auditing Tool for Security
Summary(pl.UTF-8):	Narzędzie do pobieżnych audytów bezpieczeństwa
Name:		rats
Version:	2.1
Release:	0.1
License:	GPL v2
Vendor:		Secure Software Solutions
Group:		Development/Tools
Source0:	http://www.securesw.com/rats/%{name}-%{version}.tar.gz
# Source0-md5:	adf31806f1eff0c353abcfd57653ecb3
URL:		http://www.securesw.com/rats/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RATS scans through code, finding potentially dangerous function calls.
The goal of this tool is not to definitively find bugs (yet). The
current goal is to provide a reasonable starting point for performing
manual security audits.

The initial vulnerability database is taken directly from things that
could be easily found when starting with the forthcoming book,
"Building Secure Software" by Viega and McGraw.

%description -l pl.UTF-8
RATS skanuje kod, znajdując wywołania potencjalnie niebezpiecznych
funkcji. Celem tego narzędzia nie jest (jeszcze) definitywne
znajdowanie błędów. Aktualnym celem jest dostarczenie sensownego
punktu startowego do przeprowadzania ręcznych audytów bezpieczeństwa.

Początkowa baza dziur jest brana bezpośrednio z rzeczy, które mogą być
łatwo znalezione przy lekturze nadchodzącej książki "Building Secure
Software" napisanaj przez Viegę i McGrawa.

%prep
%setup -q

%build
%configure \
	--datadir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rats
%{_datadir}/%{name}
%{_mandir}/man1/*
