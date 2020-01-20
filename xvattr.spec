%if 0%{?rhel}
%global gxvattr 0
%else
%global gxvattr 1
%endif

Summary: Utility for getting and setting Xv attributes
Name: xvattr
Version: 1.3
Release: 27%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://www.dtek.chalmers.se/groups/dvd/
Source: http://ajax.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
Patch0: encoding.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{gxvattr}
BuildRequires: gtk+-devel
%endif
BuildRequires: perl-podlators
BuildRequires: libXt-devel, libXv-devel

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY, ...

%package -n gxvattr
Summary: GTK1-based GUI for Xv attributes
Group: User Interface/X

%description -n gxvattr
GTK1-based GUI for inspecting and setting Xv attributes.

%prep
%setup -q
# Append GTK CFLAGS to CFLAGS instead of overwriting CFLAGS (optflags get used)
%{__perl} -pi -e 's|^CFLAGS = (.*)|CFLAGS += $1|g' Makefile*
# Convert man page to UTF-8
%patch0
iconv -f iso8859-1 -t utf-8 -o tmp xvattr.pod.in
%{__mv} -f tmp xvattr.pod.in
rm xvattr.pod xvattr.1 xvattr.html


%build
%configure
%if ! %{gxvattr}
sed -i 's|bin_PROGRAMS = xvattr gxvattr|bin_PROGRAMS = xvattr|g' Makefile
sed -i 's|bin_PROGRAMS = xvattr$(EXEEXT) gxvattr$(EXEEXT)|bin_PROGRAMS = xvattr$(EXEEXT)|g' Makefile
%endif
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/xvattr
%{_mandir}/man1/*

%if %{gxvattr}
%files -n gxvattr
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/gxvattr
%endif

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.3-27
- Mass rebuild 2014-01-24

* Mon Aug 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.3-26
- Fix pod encoding, rhbz #993161

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Adam Jackson <ajax@redhat.com> 1.3-24
- BuildRequires: perl-podlators for pod2man

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Adam Jackson <ajax@redhat.com> 1.3-22
- Move Source0 to fedorapeople since upstream went away
- Don't built (gtk1-based) gxvattr in RHEL

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 18 2011 Adam Jackson <ajax@redhat.com> 1.3-19
- Split the GTK1 (!) version to a subpackage

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-15
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.3-14
- Rebuild for new BuildID feature.
- Remove dist tag, since the package will seldom change.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 1.3-13
- Update License field.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 1.3-12
- Switch to using DESTDIR install method.
- Convert man page to UTF-8... not?

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.3-11
- FC6 rebuild.

* Tue May 23 2006 Matthias Saou <http://freshrpms.net/> 1.3-10
- Fix CFLAGS so that our optflags get used too (Ville, #192611).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.3-9
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.3-8
- Rebuild for new gcc/glibc and modular X.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3-7
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.3-5
- Bump release to provide Extras upgrade path.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 1.3-4
- Remove explicit XFree86 dependency for the binary package.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Oct 4 2002 Matthias Saou <http://freshrpms.net/>
- Initial rpm release.

