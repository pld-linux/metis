Summary:	METIS - Serial Graph Partitioning and Fill-reducing Matrix Ordering
Summary(pl.UTF-8):	METIS - szeregowy podział grafu i tworzenie porządków redukujący macierzy
Name:		metis
Version:	5.1.0
Release:	2
License:	Apache v2.0
Group:		Libraries
#Source0Download: http://glaros.dtc.umn.edu/gkhome/metis/metis/download
Source0:	http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/%{name}-%{version}.tar.gz
# Source0-md5:	5465e67079419a69e0116de24fce58fe
Patch0:		%{name}-cmake.patch
URL:		http://glaros.dtc.umn.edu/gkhome/views/metis
BuildRequires:	cmake >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
METIS is a set of serial routines for partitioning graphs,
partitioning finite element meshes, and producing fill reducing
orderings for sparse matrices. The algorithms implemented in METIS are
based on the multilevel recursive-bisection, multilevel k-way, and
multi-constraint partitioning schemes developed at the Department of
Computer Science and Engineering at the University of Minnesota.

%description -l pl.UTF-8
METIS to zbiór szeregowych procedur do podziału grafów, podziału
siatek elementów skończonych oraz tworzenia porządków redukujących dla
macierzy rzadkich. Algorytmy zaimplementowane w METIS są oparte na
wielopoziomowej bisekcji rekurencyjnej oraz schematach podziałów
wielopoziomowych z wieloma ograniczeniami opracowanych na wydziale
informatyki (Depratment of Computer Science and Engineering)
Uniwersytetu w Minnesocie.

%package devel
Summary:	Header files for METIS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki METIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for METIS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki METIS.

%package static
Summary:	Static METIS library
Summary(pl.UTF-8):	Statyczna biblioteka METIS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static METIS library.

%description static -l pl.UTF-8
Statyczna biblioteka METIS.

%prep
%setup -q
%patch0 -p1

%build
mkdir -p build-shared build-static
cd build-static
%cmake ..
%{__make}
cd ../build-shared
%cmake .. \
	-DSHARED=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build-shared install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog LICENSE.txt
%attr(755,root,root) %{_bindir}/cmpfillin
%attr(755,root,root) %{_bindir}/gpmetis
%attr(755,root,root) %{_bindir}/graphchk
%attr(755,root,root) %{_bindir}/m2gmetis
%attr(755,root,root) %{_bindir}/mpmetis
%attr(755,root,root) %{_bindir}/ndmetis
%attr(755,root,root) %{_libdir}/libmetis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetis.so.0

%files devel
%defattr(644,root,root,755)
%doc manual/manual.pdf
%attr(755,root,root) %{_libdir}/libmetis.so
%{_includedir}/metis.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmetis.a
