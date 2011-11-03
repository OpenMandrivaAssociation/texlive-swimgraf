# revision 18780
# category Package
# catalog-ctan /macros/latex/contrib/swimgraf
# catalog-date 2007-01-15 14:17:51 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-swimgraf
Version:	20070115
Release:	1
Summary:	Graphical/textual representations of swimming performances
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/swimgraf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swimgraf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swimgraf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/swimgraf/100BR1.TEX
%doc %{_texmfdistdir}/doc/latex/swimgraf/100BR2.TEX
%doc %{_texmfdistdir}/doc/latex/swimgraf/100br1.pdf
%doc %{_texmfdistdir}/doc/latex/swimgraf/100br2.pdf
%doc %{_texmfdistdir}/doc/latex/swimgraf/README.TXT
%doc %{_texmfdistdir}/doc/latex/swimgraf/SAMPLE1.DAT
%doc %{_texmfdistdir}/doc/latex/swimgraf/SAMPLE2.DAT
%doc %{_texmfdistdir}/doc/latex/swimgraf/SWIMGRAF.CFG
%doc %{_texmfdistdir}/doc/latex/swimgraf/SWIMGRAF.STY
%doc %{_texmfdistdir}/doc/latex/swimgraf/TEXT1.TEX
%doc %{_texmfdistdir}/doc/latex/swimgraf/TEXT2.TEX
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada11.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada12.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada13.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada14.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada15.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada16.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fcanada17.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario10.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario11.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario12.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario13.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario14.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario15.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario16.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario17.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario8.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fontario9.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/fworld.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/mcanada.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/mworld.dat
%doc %{_texmfdistdir}/doc/latex/swimgraf/swimgraf.pdf
%doc %{_texmfdistdir}/doc/latex/swimgraf/text1.pdf
%doc %{_texmfdistdir}/doc/latex/swimgraf/text2.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
