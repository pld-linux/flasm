Summary:	Flasm - assembler/disassembler of Flash ActionScript bytecode
Summary(pl.UTF-8):   Flasm - asembler/disasembler bajtkodu Flash ActionScript
Name:		flasm
Version:	1.61
Release:	0.1
License:	freeware
Group:		Development
Source0:	http://www.nowrap.de/download/%{name}16linux.tgz
# Source0-md5:	57940311b5d55e48757fcd63f86d9243
Source1:	%{name}.sh
URL:		http://www.nowrap.de/flasm.html
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flasm disassembles your entire SWF including all the timelines and
events. Looking at disassembly, you learn how the Flash compiler
works, which improves your ActionScript skills. You can also do some
optimizations on the disassembled code by hand or adjust the code as
you wish. Flasm then applies your changes to the original SWF,
replacing original actions.

%description -l pl.UTF-8
Flasm disasembluje cały SWF wraz ze znacznikami czasu i zdarzeniami.
Patrząc na wynik można nauczyć się jak działa kompilator Flasha,
poprawiając swoją znajomość ActionScriptu. Można także dokonywać
ręcznie pewnych optymalizacji w zdisasemblowanym kodzie lub
modyfikować kod. Flasm następnie aplikuje zmiany w oryginalnym SWF-ie,
zastępując oryginalne działania.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install flasm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT CHANGES.TXT flasm.html classic.css
%doc flasm.ini
%attr(755,root,root) %{_bindir}/flasm
