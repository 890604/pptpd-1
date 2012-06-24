Summary:	Serves out PPTP connections
Summary(pl):	Serwer po��cze� PPTP
Name:		pptpd
Version:	1.2.1
Release:	0.1
License:	GPL
Group:		Applications/System
Vendor:		Matthew Ramsay http://www.moretonbay.com/vpn/pptp.html
Source0:	http://dl.sourceforge.net/poptop/%{name}-%{version}.tar.gz
# Source0-md5:	067e9474998345485ba1e92cc5ff59c6
Source1:	%{name}.init
Patch0:		%{name}-install.patch
URL:		http://www.poptop.org/
BuildRequires:	autoconf
BuildRequires:	automake
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
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
%setup -q 
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/rc.d/init.d}

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

install samples/pptpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/pptpd.conf
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

rm -rf html/CVS samples/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add pptpd
if [ -f /var/lock/subsys/pptpd ]; then
	/etc/rc.d/init.d/pptpd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/pptpd start\" to start pptpd." 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/pptpd ]; then
		/etc/rc.d/init.d/pptpd stop 1>&2
	fi
	/sbin/chkconfig --del pptpd
fi


%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO samples/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pptpd.conf
%attr(755,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%{_libdir}/%{name}
