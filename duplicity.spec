Summary:	Untrusted/encrypted backup using rsync algorithm
Summary(pl.UTF-8):	Wykonywanie szyfrowanych kopii zapasowych przy użyciu algorytmu rsync
Name:		duplicity
Version:	0.4.11
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz
# Source0-md5:	8891bb4fa2b5d3f053e6f2c4a91782f2
URL:		http://www.nongnu.org/duplicity/
BuildRequires:	librsync-devel
BuildRequires:	python-devel >= 2.2.1
Requires:	gnupg
Requires:	python >= 2.2
Requires:	python-modules
Suggests:	python-gnupg >= 0.3.2
Suggests:	python-pexpect >= 2.1
Suggests:	python-boto >= 0.9d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server. In theory many remote backends are possible; right
now only the local or ssh/scp backend is written. Because duplicity
uses librsync, the incremental archives are space efficient and only
record the parts of files that have changed since the last backup.
Currently duplicity supports deleted files, full Unix permissions,
directories, symbolic links, fifos, etc., but not hard links.

%description -l pl.UTF-8
Duplicity wykonuje przyrostowe kopie zapasowe plików i katalogów
poprzez szyfrowanie archiwów w formacie tar przy pomocy GnuPG i
przesyłanie ich na zdalny (lub lokalny) serwer plików. W teorii można
użyć wiele zdalnych backendów; aktualnie napisane są tylko backendy
lokalny oraz ssh/scp. Ponieważ duplicity używa librsync, przyrostowe
archiwa wydajnie wykorzystują miejsce dzięki zapisywaniu tylko tych
części plików, które zmieniły się od wykonywania poprzedniej kopii.
Aktualnie duplicity obsługuje pliki skasowane, pełny uniksowy system
uprawnień, katalogi, dowiązania symboliczne, nazwane potoki itp. - ale
nie twarde dowiązania.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%dir %{py_sitedir}/duplicity
%{py_sitedir}/duplicity/*.py[co]
%attr(755,root,root) %{py_sitedir}/duplicity/*.so
