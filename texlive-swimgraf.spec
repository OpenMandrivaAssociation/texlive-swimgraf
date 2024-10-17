Name:		texlive-swimgraf
Version:	25446
Release:	2
Summary:	Graphical/textual representations of swimming performances
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/swimgraf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swimgraf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swimgraf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two macros that produce representations of
a swimmer's performances. The user records data in a text file
and specifies as arguments of the macros the date range of
interest. The macros extract the relevant information from the
file and process it: \swimgraph produces a graph of the times
in a single swimming event (specified as an argument), plotting
long course and short course times in separate lines. Records
and qualifying times, stored in text files, may optionally be
included on the graph. \swimtext produces a written record of
the times in all events. Files of current world and Canadian
records are included. The package requires the PSTricks and
keyval packages. For attractive output it also requires a
colour output device.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/swimgraf
%doc %{_texmfdistdir}/doc/latex/swimgraf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
