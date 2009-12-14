Summary:	A powerful implementation of MPI
Summary(pl.UTF-8):	Implementacja MPI o dużych możliwościach
Name:		openmpi
Version:	1.2.5
Release:	0.1
License:	BSD
Group:		Development
Source0:	http://www.open-mpi.org/software/ompi/v1.2/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	c6e82aab6cdcd425bf29217e8317d7dc
Patch0:		%{name}-ksh.patch
Patch1:		%{name}-cc.patch
URL:		http://www.open-mpi.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-fortran
#BuildRequires:	libtool >= 2.2
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	lam
Conflicts:	mpich
Conflicts:	mpich2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMPI is a project combining technologies and resources from several
other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in order to
build the best MPI library available.

This package contains all of the tools necessary to compile, link, and
run OpenMPI jobs.

%description -l pl.UTF-8
OpenMPI to projekt łączący technologie i zasoby z kilku innych
projektów (FT-MPI, LA-MPI, LAM/MPI i PACX-MPI) w celu stworzenia
najlepszej dostępnej biblioteki MPI.

Ten pakiet zawiera wszystkie narzędzia potrzebne do kompilacji,
linkowania i uruchamiania zadań OpenMPI.

%package libs
Summary:	Shared libraries for OpenMPI
Summary(pl.UTF-8):	Biblioteki współdzielone OpenMPI
Group:		Libraries

%description libs
OpenMPI is a project combining technologies and resources from several
other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in order to
build the best MPI library available.

This package contains the shared libraries needed by programs linked
against OpenMPI.

%description libs -l pl.UTF-8
OpenMPI to projekt łączący technologie i zasoby z kilku innych
projektów (FT-MPI, LA-MPI, LAM/MPI i PACX-MPI) w celu stworzenia
najlepszej dostępnej biblioteki MPI.

Ten pakiet zawiera biblioteki współdzielone wymagane przez programy
zlinkowane z OpenMPI.

%package devel
Summary:	Development files for OpenMPI
Summary(pl.UTF-8):	Pliki programistyczne OpenMPI
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	lam-devel
Conflicts:	libopenmpi-devel < 1.2
Conflicts:	mpich1-devel
Conflicts:	mpich2-devel

%description devel
OpenMPI is a project combining technologies and resources from several
other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in order to
build the best MPI library available.

This package contains the header files needed to compile applications
against OpenMPI.

%description devel -l pl.UTF-8
OpenMPI to projekt łączący technologie i zasoby z kilku innych
projektów (FT-MPI, LA-MPI, LAM/MPI i PACX-MPI) w celu stworzenia
najlepszej dostępnej biblioteki MPI.

Ten pakiet zawiera pliki nagłówkowe potrzebne przy kompilacji
aplikacji korzystających z OpenMPI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f configure{,.orig}

%build
if [ ! -f configure -o configure.ac -nt configure ]; then
	# libltdl comes from libtool 2.1x, so libtoolize fails with libtool <2.1
	%{__aclocal} -I config -I opal/libltdl/m4
	%{__autoconf}
	%{__autoheader}
	%{__automake}
fi
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/openmpi-totalview.tcl $RPM_BUILD_ROOT%{_datadir}/openmpi/doc

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE NEWS AUTHORS examples/
%attr(755,root,root) %{_bindir}/mpi*
%attr(755,root,root) %{_bindir}/ompi_info
%attr(755,root,root) %{_bindir}/opal_wrapper
%attr(755,root,root) %{_bindir}/orted
%attr(755,root,root) %{_bindir}/orterun
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openmpi-default-hostfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openmpi-mca-params.conf
%{_datadir}/openmpi
%{_mandir}/man1/mpi*.1*
%{_mandir}/man1/orterun.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmca_common_sm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmca_common_sm.so.0
%attr(755,root,root) %{_libdir}/libmpi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi.so.0
%attr(755,root,root) %{_libdir}/libmpi_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_cxx.so.0
%attr(755,root,root) %{_libdir}/libmpi_f77.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_f77.so.0
%attr(755,root,root) %{_libdir}/libmpi_f90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_f90.so.0
%attr(755,root,root) %{_libdir}/libopen-pal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopen-pal.so.0
%attr(755,root,root) %{_libdir}/libopen-rte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopen-rte.so.0
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libompitv.so
%{_libdir}/%{name}/mca_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmca_common_sm.so
%attr(755,root,root) %{_libdir}/libmpi.so
%attr(755,root,root) %{_libdir}/libmpi_cxx.so
%attr(755,root,root) %{_libdir}/libmpi_f77.so
%attr(755,root,root) %{_libdir}/libmpi_f90.so
%attr(755,root,root) %{_libdir}/libopen-pal.so
%attr(755,root,root) %{_libdir}/libopen-rte.so
%{_libdir}/libmca_common_sm.la
%{_libdir}/libmpi.la
%{_libdir}/libmpi_cxx.la
%{_libdir}/libmpi_f77.la
%{_libdir}/libmpi_f90.la
%{_libdir}/libopen-pal.la
%{_libdir}/libopen-rte.la
%{_libdir}/mpi.mod
%{_includedir}/mpi*.h
%{_includedir}/openmpi
%{_mandir}/man3/MPI*.3*
%{_mandir}/man3/OpenMPI.3*
