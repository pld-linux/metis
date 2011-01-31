Summary:	METIS - Serial Graph Partitioning and Fill-reducing Matrix Ordering
Summary(pl.UTF-8):	METIS - szeregowy podział grafu i tworzenie porządków redukujący macierzy
Name:		metis
# see VERSION file for real version number
Version:	4.0.1
%define	fver	4.0
Release:	1
License:	free, distribution restricted (http://glaros.dtc.umn.edu/gkhome/metis/metis/faq?q=metis/metis/faq#distribute)
Group:		Libraries
#Source0Download: http://glaros.dtc.umn.edu/gkhome/metis/metis/download
Source0:	http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/%{name}-%{fver}.tar.gz
# NoSource0-md5:	0aa546419ff7ef50bd86ce1ec7f727c7
NoSource:	0
Patch0:		%{name}-shared.patch
Patch1:		%{name}-libc.patch
URL:		http://glaros.dtc.umn.edu/gkhome/views/metis
BuildRequires:	libtool
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
%setup -q -n %{name}-%{fver}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDOPTIONS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/metis
install Lib/*.h $RPM_BUILD_ROOT%{_includedir}/metis

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES VERSION
%attr(755,root,root) %{_bindir}/graphchk
%attr(755,root,root) %{_bindir}/kmetis
%attr(755,root,root) %{_bindir}/mesh2dual
%attr(755,root,root) %{_bindir}/mesh2nodal
%attr(755,root,root) %{_bindir}/oemetis
%attr(755,root,root) %{_bindir}/onmetis
%attr(755,root,root) %{_bindir}/partdmesh
%attr(755,root,root) %{_bindir}/partnmesh
%attr(755,root,root) %{_bindir}/pmetis
%attr(755,root,root) %{_libdir}/libmetis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetis.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/manual.ps
%attr(755,root,root) %{_libdir}/libmetis.so
%{_libdir}/libmetis.la
%{_includedir}/metis

%files static
%defattr(644,root,root,755)
%{_libdir}/libmetis.a
