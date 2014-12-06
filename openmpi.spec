# TODO: CUDA (on bcond)
# lsf/lsf.h (Lava/OpenLava?)
# scif.h (MPSS?)
# portals4
# xpmem
# pvfs2
# Intel PSM
# for vt: libf2c clapack papi libcpc cupti ctool bmi?
#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	java		# Java components (VampirTrace and OpenMPI binding)

Summary:	A powerful implementation of MPI
Summary(pl.UTF-8):	Implementacja MPI o dużych możliwościach
Name:		openmpi
Version:	1.8.3
Release:	0.1
License:	BSD
Group:		Development
Source0:	http://www.open-mpi.org/software/ompi/v1.8/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	2067d00853e0c33d498153fc7d268d2b
Patch0:		%{name}-link.patch
Patch1:		%{name}-cc.patch
Patch2:		%{name}-static.patch
Patch3:		%{name}-fmoddir.patch
URL:		http://www.open-mpi.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.12.2
BuildRequires:	gcc-fortran
BuildRequires:	hwloc-devel >= 1.7.2
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libevent-devel >= 2.0.21
BuildRequires:	libgomp-devel
BuildRequires:	libibverbs-devel
BuildRequires:	libltdl-devel
BuildRequires:	librdmacm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	open-mx-devel
BuildRequires:	opensm-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
Provides:	mpi
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
Provides:	mpi-devel
Obsoletes:	libopenmpi-devel < 1.2
Conflicts:	lam-devel
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

%package static
Summary:	Static OpenMPI libraries
Summary(pl.UTF-8):	Statyczne biblioteki OpenMPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	mpi-static

%description static
Static OpenMPI libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OpenMPI.

%package -n java-openmpi
Summary:	Java bindings to OpenMPI libraries
Summary(pl.UTF-8):	Wiązania Javy do bibliotek OpenMPI
Group:		Libraries/Java
Requires:	%{name}-libs = %{version}-%{release}
Requires:	jre

%description -n java-openmpi
Java bindings to OpenMPI libraries.

%description -n java-openmpi -l pl.UTF-8
Wiązania Javy do bibliotek OpenMPI.

%package -n java-openmpi-devel
Summary:	Java bindings to OpenMPI libraries - development files
Summary(pl.UTF-8):	Wiązania Javy do bibliotek OpenMPI - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	java-openmpi-devel = %{version}-%{release}
Requires:	jdk

%description -n java-openmpi-devel
Java bindings to OpenMPI libraries - development files.

%description -n java-openmpi-devel -l pl.UTF-8
Wiązania Javy do bibliotek OpenMPI - pliki programistyczne.

%package -n java-openmpi-static
Summary:	Java bindings to OpenMPI libraries - static library
Summary(pl.UTF-8):	Wiązania Javy do bibliotek OpenMPI - biblioteka statyczna
Group:		Development/Libraries
Requires:	java-openmpi-static = %{version}-%{release}

%description -n java-openmpi-static
Java bindings to OpenMPI libraries - static library.

%description -n java-openmpi-static -l pl.UTF-8
Wiązania Javy do bibliotek OpenMPI - biblioteka statyczna.

%package vt
Summary:	VampirTrace - tool set for instrumentation and tracing of applications
Summary(pl.UTF-8):	VampirTrace - zbiór narzędzi do pomiarów i śledzenia aplikacji
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-vt-libs = %{version}-%{release}

%description vt
VampirTrace consists of a tool set for instrumentation and tracing of
software applications. In particular, it is tailored towards parallel
and distributed High Performance Computing (HPC) applications. 

%description vt -l pl.UTF-8
VampirTrace to zbiór narzędzi do pomiarów i śledzenia aplikacji. Jest
dostosowany szczególnie do aplikacji równoległych i rozproszonych typu
HPC (High Performance Computing).

%package vt-libs
Summary:	VampirTrace libraries
Summary(pl.UTF-8):	Biblioteki VampirTrace
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description vt-libs
VampirTrace libraries.

%description vt-libs -l pl.UTF-8
Biblioteki VampirTrace.

%package vt-devel
Summary:	Header files for VampirTrace libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VampirTrace
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-vt-libs = %{version}-%{release}

%description vt-devel
Header files for VampirTrace libraries.

%description vt-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek VampirTrace.

%package vt-static
Summary:	Static VampirTrace libraries
Summary(pl.UTF-8):	Statyczne biblioteki VampirTrace
Group:		Development/Libraries
Requires:	%{name}-vt-devel = %{version}-%{release}

%description vt-static
Static VampirTrace libraries.

%description vt-static -l pl.UTF-8
Statyczne biblioteki VampirTrace.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_java:--disable-java} \
	%{?with_java:--enable-mpi-java} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-hwloc=/usr \
	--with-libevent=external \
	--with-libltdl=external \
	--with-sqlite3 \
	--with-verbs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	fmoddir=%{_includedir} \
	javadir=%{_javadir} \
	vtbindatadir=%{_javadir}

%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/openmpi-totalview.tcl $RPM_BUILD_ROOT%{_datadir}/openmpi/doc

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a
%endif
%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/openmpi/javadoc-openmpi $RPM_BUILD_ROOT%{_javadocdir}/openmpi
%{__sed} -i -e 's,%{_libdir}/mpi\.jar,%{_javadir}/mpi.jar,' $RPM_BUILD_ROOT%{_bindir}/mpijavac.pl
%{__sed} -i -e 's,\$bindir/vtsetup\.jar,%{_javadir}/vtsetup.jar,' $RPM_BUILD_ROOT%{_bindir}/vtsetup
%else
# still installed even if java disabled
%{__rm} $RPM_BUILD_ROOT{%{_bindir}/vtsetup,%{_sysconfdir}/vtsetup-config.*,%{_javadir}/vtsetup.jar}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n java-openmpi -p /sbin/ldconfig
%postun	-n java-openmpi -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE NEWS AUTHORS examples/
%attr(755,root,root) %{_bindir}/mpiexec
%attr(755,root,root) %{_bindir}/mpirun
%attr(755,root,root) %{_bindir}/ompi-clean
%attr(755,root,root) %{_bindir}/ompi-ps
%attr(755,root,root) %{_bindir}/ompi-server
%attr(755,root,root) %{_bindir}/ompi-top
%attr(755,root,root) %{_bindir}/ompi_info
%attr(755,root,root) %{_bindir}/opari
%attr(755,root,root) %{_bindir}/orte-clean
%attr(755,root,root) %{_bindir}/orte-info
%attr(755,root,root) %{_bindir}/orte-ps
%attr(755,root,root) %{_bindir}/orte-server
%attr(755,root,root) %{_bindir}/orte-top
%attr(755,root,root) %{_bindir}/orted
%attr(755,root,root) %{_bindir}/orterun
%attr(755,root,root) %{_bindir}/oshmem_info
%attr(755,root,root) %{_bindir}/oshrun
%attr(755,root,root) %{_bindir}/otfaux
%attr(755,root,root) %{_bindir}/otfcompress
%attr(755,root,root) %{_bindir}/otfconfig
%attr(755,root,root) %{_bindir}/otfdecompress
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otfmerge
%attr(755,root,root) %{_bindir}/otfmerge-mpi
%attr(755,root,root) %{_bindir}/otfprint
%attr(755,root,root) %{_bindir}/otfprofile
%attr(755,root,root) %{_bindir}/otfprofile-mpi
%attr(755,root,root) %{_bindir}/otfshrink
%attr(755,root,root) %{_bindir}/shmemrun
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openmpi-default-hostfile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openmpi-mca-params.conf
%{_datadir}/openmpi
%{_mandir}/man1/mpiexec.1*
%{_mandir}/man1/mpirun.1*
%{_mandir}/man1/ompi-clean.1*
%{_mandir}/man1/ompi-ps.1*
%{_mandir}/man1/ompi-server.1*
%{_mandir}/man1/ompi-top.1*
%{_mandir}/man1/ompi_info.1*
%{_mandir}/man1/orte-clean.1*
%{_mandir}/man1/orte-info.1*
%{_mandir}/man1/orte-ps.1*
%{_mandir}/man1/orte-server.1*
%{_mandir}/man1/orte-top.1*
%{_mandir}/man1/orted.1*
%{_mandir}/man1/orterun.1*
%{_mandir}/man1/oshmem_info.1*
%{_mandir}/man7/ompi_crcp.7*
%{_mandir}/man7/opal_crs.7*
%{_mandir}/man7/orte_filem.7*
%{_mandir}/man7/orte_hosts.7*
%{_mandir}/man7/orte_snapc.7*
%{_mandir}/man7/orte_sstore.7*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmca_common_mx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmca_common_mx.so.2
%attr(755,root,root) %{_libdir}/libmca_common_sm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmca_common_sm.so.4
%attr(755,root,root) %{_libdir}/libmca_common_verbs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmca_common_verbs.so.0
%attr(755,root,root) %{_libdir}/libmpi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi.so.1
%attr(755,root,root) %{_libdir}/libmpi_cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_cxx.so.1
%attr(755,root,root) %{_libdir}/libmpi_mpifh.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_mpifh.so.2
%attr(755,root,root) %{_libdir}/libmpi_usempi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_usempi.so.1
%attr(755,root,root) %{_libdir}/libompitrace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libompitrace.so.0
%attr(755,root,root) %{_libdir}/libopen-pal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopen-pal.so.6
%attr(755,root,root) %{_libdir}/libopen-rte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopen-rte.so.7
%attr(755,root,root) %{_libdir}/libopen-trace-format.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopen-trace-format.so.1
%attr(755,root,root) %{_libdir}/liboshmem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboshmem.so.3
%attr(755,root,root) %{_libdir}/libotfaux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libotfaux.so.0
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libompi_dbg_msgq.so
%{_libdir}/%{name}/mca_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/opal_wrapper
%attr(755,root,root) %{_bindir}/mpiCC
%attr(755,root,root) %{_bindir}/mpic++
%attr(755,root,root) %{_bindir}/mpicc
%attr(755,root,root) %{_bindir}/mpicxx
%attr(755,root,root) %{_bindir}/mpif77
%attr(755,root,root) %{_bindir}/mpif90
%attr(755,root,root) %{_bindir}/mpifort
%attr(755,root,root) %{_bindir}/ortecc
%attr(755,root,root) %{_bindir}/oshcc
%attr(755,root,root) %{_bindir}/oshfort
%attr(755,root,root) %{_bindir}/shmemcc
%attr(755,root,root) %{_bindir}/shmemfort
%attr(755,root,root) %{_libdir}/libmca_common_mx.so
%attr(755,root,root) %{_libdir}/libmca_common_sm.so
%attr(755,root,root) %{_libdir}/libmca_common_verbs.so
%attr(755,root,root) %{_libdir}/libmpi.so
%attr(755,root,root) %{_libdir}/libmpi_cxx.so
%attr(755,root,root) %{_libdir}/libmpi_mpifh.so
%attr(755,root,root) %{_libdir}/libmpi_usempi.so
%attr(755,root,root) %{_libdir}/libompitrace.so
%attr(755,root,root) %{_libdir}/libopen-pal.so
%attr(755,root,root) %{_libdir}/libopen-rte.so
%attr(755,root,root) %{_libdir}/libopen-trace-format.so
%attr(755,root,root) %{_libdir}/liboshmem.so
%attr(755,root,root) %{_libdir}/libotfaux.so
%{_libdir}/libmca_common_mx.la
%{_libdir}/libmca_common_sm.la
%{_libdir}/libmca_common_verbs.la
%{_libdir}/libmpi.la
%{_libdir}/libmpi_cxx.la
%{_libdir}/libmpi_mpifh.la
%{_libdir}/libmpi_usempi.la
%{_libdir}/libompitrace.la
%{_libdir}/libopen-pal.la
%{_libdir}/libopen-rte.la
%{_libdir}/libopen-trace-format.la
%{_libdir}/liboshmem.la
%{_libdir}/libotfaux.la
%{_includedir}/mpi.h
%{_includedir}/mpi-ext.h
%{_includedir}/mpi_portable_platform.h
%{_includedir}/mpif*.h
%{_includedir}/pshmem.h
%{_includedir}/pshmemx.h
%{_includedir}/shmem.h
%{_includedir}/shmem-compat.h
%{_includedir}/shmemx.h
%{_includedir}/mpp
# Fortran
%{_includedir}/mpi.mod
%{_includedir}/shmem.fh
%dir %{_includedir}/openmpi
%dir %{_includedir}/openmpi/ompi
%dir %{_includedir}/openmpi/ompi/mpi
%{_includedir}/openmpi/ompi/mpi/cxx
%{_pkgconfigdir}/ompi.pc
%{_pkgconfigdir}/ompi-c.pc
%{_pkgconfigdir}/ompi-cxx.pc
%{_pkgconfigdir}/ompi-f77.pc
%{_pkgconfigdir}/ompi-f90.pc
%{_pkgconfigdir}/ompi-fort.pc
%{_pkgconfigdir}/orte.pc
%{_mandir}/man1/mpiCC.1*
%{_mandir}/man1/mpic++.1*
%{_mandir}/man1/mpicc.1*
%{_mandir}/man1/mpicxx.1*
%{_mandir}/man1/mpif77.1*
%{_mandir}/man1/mpif90.1*
%{_mandir}/man1/mpifort.1*
%{_mandir}/man1/opal_wrapper.1*
%{_mandir}/man3/MPI*.3*
%{_mandir}/man3/OpenMPI.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmca_common_mx.a
%{_libdir}/libmca_common_sm.a
%{_libdir}/libmca_common_verbs.a
%{_libdir}/libmpi.a
%{_libdir}/libmpi_cxx.a
%{_libdir}/libmpi_mpifh.a
%{_libdir}/libmpi_usempi.a
%{_libdir}/libompitrace.a
%{_libdir}/libopen-pal.a
%{_libdir}/libopen-rte.a
%{_libdir}/libopen-trace-format.a
%{_libdir}/liboshmem.a
%{_libdir}/libotfaux.a
%endif

%if %{with java}
%files -n java-openmpi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpi_java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpi_java.so.1
%{_javadir}/mpi.jar

%files -n java-openmpi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpijavac
%attr(755,root,root) %{_bindir}/mpijavac.pl
%attr(755,root,root) %{_libdir}/libmpi_java.so
%{_libdir}/libmpi_java.la
%{_includedir}/openmpi/ompi/mpi/java
%{_mandir}/man1/mpijavac.1*
%{_javadocdir}/openmpi

%if %{with static_libs}
%files -n java-openmpi-static
%defattr(644,root,root,755)
%{_libdir}/libmpi_java.a
%endif
%endif

%files vt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtfilter
%attr(755,root,root) %{_bindir}/vtfilter-mpi
%attr(755,root,root) %{_bindir}/vtfiltergen
%attr(755,root,root) %{_bindir}/vtfiltergen-mpi
%attr(755,root,root) %{_bindir}/vtrun
%attr(755,root,root) %{_bindir}/vtunify
%attr(755,root,root) %{_bindir}/vtunify-mpi
%{_datadir}/vampirtrace
%if %{with java}
%attr(755,root,root) %{_bindir}/vtjava
%attr(755,root,root) %{_bindir}/vtsetup
%{_javadir}/vtsetup.jar
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vt-java-default-filter.spec
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vtsetup-config.dtd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vtsetup-config.xml
%endif

%files vt-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt.so.0
%attr(755,root,root) %{_libdir}/libvt-hyb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt-hyb.so.0
%attr(755,root,root) %{_libdir}/libvt-mpi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt-mpi.so.0
%attr(755,root,root) %{_libdir}/libvt-mpi-unify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt-mpi-unify.so.0
%attr(755,root,root) %{_libdir}/libvt-mt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt-mt.so.0
%if %{with java}
%attr(755,root,root) %{_libdir}/libvt-java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvt-java.so.0
%endif

%files vt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpiCC-vt
%attr(755,root,root) %{_bindir}/mpic++-vt
%attr(755,root,root) %{_bindir}/mpicc-vt
%attr(755,root,root) %{_bindir}/mpicxx-vt
%attr(755,root,root) %{_bindir}/mpif77-vt
%attr(755,root,root) %{_bindir}/mpif90-vt
%attr(755,root,root) %{_bindir}/mpifort-vt
%attr(755,root,root) %{_bindir}/vtwrapper
%attr(755,root,root) %{_bindir}/vtCC
%attr(755,root,root) %{_bindir}/vtc++
%attr(755,root,root) %{_bindir}/vtcc
%attr(755,root,root) %{_bindir}/vtcxx
%attr(755,root,root) %{_bindir}/vtf77
%attr(755,root,root) %{_bindir}/vtf90
%attr(755,root,root) %{_bindir}/vtfort
%attr(755,root,root) %{_libdir}/libvt.so
%attr(755,root,root) %{_libdir}/libvt-hyb.so
%attr(755,root,root) %{_libdir}/libvt-mpi.so
%attr(755,root,root) %{_libdir}/libvt-mpi-unify.so
%attr(755,root,root) %{_libdir}/libvt-mt.so
%{_libdir}/libvt.la
%{_libdir}/libvt-hyb.la
%{_libdir}/libvt-mpi.la
%{_libdir}/libvt-mpi-unify.la
%{_libdir}/libvt-mt.la
%{_libdir}/libvt-pomp.la
%{_libdir}/libvt-pomp.a
%{_includedir}/vampirtrace
%if %{with java}
%attr(755,root,root) %{_libdir}/libvt-java.so
%{_libdir}/libvt-java.la
%endif

%files vt-static
%defattr(644,root,root,755)
%{_libdir}/libvt.a
%{_libdir}/libvt-hyb.a
%{_libdir}/libvt-mpi.a
%{_libdir}/libvt-mpi-unify.a
%{_libdir}/libvt-mt.a
