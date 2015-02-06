%define major	5
%define api	1.0
%define libname %mklibname aal- %{api} %{major}
%define libname_basic %mklibname aal-%{api}
%define minimal_libname	%mklibname aal-minimal 0

Summary:	Library for Reiser4 filesystem
Name:		libaal
Version:	1.0.5
Release:	7
License:	GPLv2
Group:		System/Libraries
Source0:	http://www.kernel.org/pub/linux/utils/fs/reiser4/libaal/%{name}-%{version}.tar.bz2
Patch0:		libaal-1.0.5-rpmoptflags.patch
Patch1:		libaal.castint.patch
URL:		http://www.kernel.org/pub/linux/utils/fs/reiser4/

%description
libaal library - needed for Reiser4 filesystem utilities.

%package -n	%{libname}
Summary:	Library for Reiser4 filesystem
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{_lib}aal-%{api} = %{version}-%{release}

%description -n	%{libname}
libaal library - needed for Reiser4 filesystem utilities.

%package	devel
Summary:	Development related files for libaal library
Group:		Development/C
Requires: 	%{libname} = %{version}
Requires: 	%{minimal_libname} = %{version}
# Don't provide! This is just temporary
Obsoletes:	libaal3-devel libaal2-devel

%description	devel
Development related files for libaal library.

%package	static-devel
Summary:	Static libaal library
Group:		Development/C
Requires: 	%{name}-devel = %{version}
# Don't provide! This is just temporary
Obsoletes:	libaal3-static-devel libaal2-static-devel

%description	static-devel
The static libaal library.

%package -n	%{minimal_libname}
Summary:	%{name} library with miminal footprint
Group:		System/Libraries

%description -n %{minimal_libname}
%{name} library with miminal memory foorprint. This is
useful when you need to build grub with Reiser4 support.

%prep
%setup -q
%patch0 -p1 -b .cflags
%patch1 -p1 -b .castint

%build
# be very pedantic
# needed for patch0
autoreconf -f
libtoolize
%configure2_5x \
	--libdir=/%{_lib}\
	--libexecdir=/%{_lib}\
	--enable-Werror \
	%{?debug:--enable-debug}

%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root,-)
# COPYING contains information other than GPL text
%doc AUTHORS BUGS COPYING CREDITS ChangeLog README THANKS TODO
/%{_lib}/libaal-%{api}.so.%{major}*

%files -n %{minimal_libname}
%defattr(-,root,root,-)
/%{_lib}/libaal-minimal.so.*

%files devel
%defattr(-,root,root,-)
/%{_lib}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files static-devel
%defattr(-,root,root,-)
/%{_lib}/lib*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-5mdv2011.0
+ Revision: 620075
- the mass rebuild of 2010.0 packages

* Fri May 01 2009 Thomas Backlund <tmb@mandriva.org> 1.0.5-4mdv2010.0
+ Revision: 369983
- libs should be in /lib instead of /usr/lib (#50451)

* Sun Feb 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.5-3mdv2009.1
+ Revision: 340485
- Fix castint patch with correct version by upstream

* Wed Feb 11 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.5-2mdv2009.1
+ Revision: 339594
- Re-add a rediffed castint patch: it is needed for compilation
  on x86_64 with --WError
- Update to new version 1.0.5, new major
- Protect major in file list
- Update URL and Source URL
- Remove unneeded patch
- Add patch to use Mandriva cflags, but still use -Os for the minimal library
- Fix license

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 248375
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2008.1
+ Revision: 128417
- kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - bunzip2 the patch

  + Emmanuel Andry <eandry@mandriva.org>
    - Import libaal



* Tue Apr 05 2005 Olivier Thauvin <nanardon@mandrake.org> 1.0.4-3mdk
- reupload cause kenobi crash

* Mon Apr 04 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.4-2mdk
- patch0: fix int/ptr casting on 64bits arch

* Thu Mar 10 2005 Abel Cheung <deaddog@mandrake.org> 1.0.4-1mdk
- Fix mklibname
- Remove all patches (debug option not necessary, automake18 is upstream)

* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.3-2mdk
- bump major

* Fri Jan 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.3-1mdk
- 1.0.3

* Tue Jun 18 2004 Svetoslav Slavtchev <svetljo@gmx.de> 0.5.2-1mdk
- 0.5.2
- re-add static package

* Sat Jun 12 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.5.1-1thac
- Built for Mandrake 10.0 official
