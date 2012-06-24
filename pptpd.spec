Summary:	Serves out PPTP connections
Summary(pl):	Serwer po��cze� PPTP
Name:		pptpd
Version:	1.1.4
%define	bver	b4
Release:	1.%{bver}.1
License:	GPL
Group:		Applications/System
Vendor:		Matthew Ramsay http://www.moretonbay.com/vpn/pptp.html
Source0:	http://poptop.lineo.com/releases/%{name}-%{version}-%{bver}.tar.gz
# Source0-md5:	3922fef6499b94d4e7f2752f38fe2247
URL:		http://poptop.lineo.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPTPd, Point-to-Point Tunnelling Protocol Daemon, offers out
connections to pptp clients to become virtual members of the IP pool
owned by the pptp server. In effect, these clients become virtual
members of the local subnet, regardless of what their real IP address
is. A tunnel is built between the pptp server and client, and packets
from the subnet are wrapped and passed between server and client
similar to other C/S protocols.

%description -l pl
PPTPd (Point-to-Point Tunnelling Protocol Daemon, czyli demon
obs�uguj�cy protok� tunelowania Point-to-Point) udost�pnia po��czenia
klientom pptp, aby sta�y si� wirtualnymi cz�onkami puli IP
obs�ugiwanej przez serwer pptp. W efekcie ci klienci staj� si�
wirtualnymi cz�onkami podsieci lokalnej, niezale�nie od ich
prawdziwego adresu IP. Tunel jest tworzony mi�dzy serwerem a klientem
pptp, a pakiety z podsieci s� wy�apywane i puszczane pomi�dzy serwerem
a klientem podobnie do innych protoko��w klient-serwer.

%prep
%setup -q -n poptop-%{version}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/pptpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/pptpd.conf

rm -rf html/CVS samples/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO html/* samples/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pptpd.conf
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
