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
	%{__aclocal}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE NEWS LICENSE AUTHORS examples/
%{_sysconfdir}/*
%{_datadir}/openmpi
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*
%{_libdir}/%{name}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.mod
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.la
%{_mandir}/man3/*
