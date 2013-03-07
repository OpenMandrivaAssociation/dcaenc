%define libmajor 0
%define pluginname %{mklibname alsa-plugins}-dca
%define libname %mklibname %name %libmajor
%define devellibname %mklibname -d %name
%define debug_package	%{nil}
%define distsuffix mrb

Summary: DTS Coherent Acoustics encoder
Name:    dcaenc
Version: 2
Release: 1
Source0: http://aepatrakov.narod.ru/dcaenc/%{name}-%{version}.tar.gz
License: LGPLv2.1+
Group:   Sound
URL:     http://aepatrakov.narod.ru/dcaenc/
BuildRequires: kernel-headers >= 2.4.0
BuildRequires: pkgconfig(alsa)

%description
DTS Coherent Acoustics encoder

It may be useful if you want to create a DTS CD or a DTS soundtrack for a DVD
from a 6-channel PCM wav file using linux. Another use case is related to
real-time encoding of multichannel PCM audio output from arbitrary linux
applications for transmission over SPDIF (see %{pluginname} package)


%package -n %{libname}
Summary:   Libraries for DTS Coherent Acoustics encoder
Group:     Sound

%description -n %{libname}
Libraries for DTS Coherent Acoustics encoder


%package -n %{devellibname}
Summary:   Development sources for DTS Coherent Acoustics encoder
Group:     Development/C
Requires:  %{libname} = %{version}-%{release}

%description -n %{devellibname}
Development sources for DTS Coherent Acoustics encoder


%package -n %{pluginname}
Summary:   DTS Coherent Acoustics encoder plugin for ALSA
Group:     Sound
Requires:  alsa-lib

%description -n %{pluginname}
DTS Coherent Acoustics encoder plugin for ALSA

Provides real-time encoding of multichannel PCM audio output from arbitrary
linux applications for transmission over SPDIF.


%prep
%setup -q -n %name-%version
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

mv %{buildroot}%{_datadir}/alsa/pcm %{buildroot}%{_datadir}/alsa/alsa.conf.d

find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/dcaenc

%files -n %{libname}
%{_libdir}/libdcaenc.so.%{libmajor}*

%files -n %{devellibname}
%{_includedir}/dcaenc.h
%{_libdir}/libdcaenc.so
%{_libdir}/pkgconfig/dcaenc.pc

%files -n %{pluginname}
%{_datadir}/alsa/alsa.conf.d/dca.conf
%{_libdir}/alsa-lib/*




