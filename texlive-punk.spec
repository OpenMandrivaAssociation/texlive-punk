Name:		texlive-punk
Version:	27388
Release:	2
Summary:	Donald Knuth's punk font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/punk
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A response to the assertion in a lecture that "typography tends
to lag behind other stylistic changes by about 10 years". Knuth
felt it was (in 1988) time to design a replacement for his
designs of the 1970s, and came up with this font! The fonts are
distributed as Metafont source. The package offers LaTeX
support by Rohit Grover, from an original by Sebastian Rahtz,
which is slightly odd in claiming that the fonts are T1-
encoded. A (possibly) more rational support package is to be
found in punk-latex.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/punk
%{_texmfdistdir}/fonts/tfm/public/punk
%doc %{_texmfdistdir}/doc/fonts/punk

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
