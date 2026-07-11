%global tl_name punk
%global tl_revision 27388

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Donald Knuths punk font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/punk
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/punk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/punk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A response to the assertion in a lecture that "typography tends to lag
behind other stylistic changes by about 10 years". Knuth felt it was (in
1988) time to design a replacement for his designs of the 1970s, and
came up with this font! The fonts are distributed as Metafont source.
The package offers LaTeX support by Rohit Grover, from an original by
Sebastian Rahtz, which is slightly odd in claiming that the fonts are
T1-encoded. A (possibly) more rational support package is to be found in
punk-latex

