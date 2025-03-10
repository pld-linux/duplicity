Summary:	Untrusted/encrypted backup using rsync algorithm
Summary(pl.UTF-8):	Wykonywanie szyfrowanych kopii zapasowych przy użyciu algorytmu rsync
Name:		duplicity
Version:	2.1.1
Release:	3
License:	GPL v2
Group:		Applications/Archiving
Source0:	https://gitlab.com/duplicity/duplicity/-/archive/rel.%{version}/%{name}-rel.%{version}.tar.bz2
# Source0-md5:	7064f8a6b176a8d095406509ddf5451a
URL:		http://www.nongnu.org/duplicity/
BuildRequires:	librsync-devel >= 0.9.6
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	gnupg
Requires:	python3
Requires:	python3-lockfile
Requires:	python3-modules
Requires:	python3-pexpect >= 2.1
Suggests:	lftp
Suggests:	ncftp
Suggests:	python3-boto >= 0.9d
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
%setup -q -n %{name}-rel.%{version}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      bin/duplicity

%{__rm} po/{en_PR,es_EM,es_US,nl_SR,ru_BY,ru_MD,ru_UA,zh_MO,zh_SG}.po

cd po
for f in *.po ; do
	case $(basename $f .po) in
	de_AT|en_AU|en_GB|es_MX|es_PR|nl_BE|pt_BR|zh_CN|zh_HK|zh_TW) continue
	;;
	*) %{__mv} $f ${f%%_*}.po
	;;
	esac
done

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.md README*.md
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%dir %{py3_sitedir}/duplicity
%dir %{py3_sitedir}/duplicity/backends
%dir %{py3_sitedir}/duplicity/backends/pyrax_identity
%{py3_sitedir}/duplicity/__pycache__
%{py3_sitedir}/duplicity/*.py
%{py3_sitedir}/duplicity/backends/__pycache__
%{py3_sitedir}/duplicity/backends/*.py
%{py3_sitedir}/duplicity/backends/pyrax_identity/__pycache__
%{py3_sitedir}/duplicity/backends/pyrax_identity/*.py
%attr(755,root,root) %{py3_sitedir}/duplicity/*.so
%{py3_sitedir}/duplicity-*.egg-info
