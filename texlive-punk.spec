# revision 13293
# category Package
# catalog-ctan /fonts/punk
# catalog-date 2008-11-30 13:31:17 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-punk
Version:	20081130
Release:	3
Summary:	Donald Knuth's punk font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/punk
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/punk.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A response to the assertion in a lecture that "typography tends
to lag behind other stylistic changes by about 10 years". Knuth
felt it was (in 1988) time to design a replacement for his
designs of the 1970s, and came up with this font! The fonts are
distributed as MetaFont source. The package offers LaTeX
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
%{_texmfdistdir}/fonts/source/public/punk/punk.mf
%{_texmfdistdir}/fonts/source/public/punk/punk10.mf
%{_texmfdistdir}/fonts/source/public/punk/punk12.mf
%{_texmfdistdir}/fonts/source/public/punk/punk20.mf
%{_texmfdistdir}/fonts/source/public/punk/punka.mf
%{_texmfdistdir}/fonts/source/public/punk/punkae.mf
%{_texmfdistdir}/fonts/source/public/punk/punkbx20.mf
%{_texmfdistdir}/fonts/source/public/punk/punkd.mf
%{_texmfdistdir}/fonts/source/public/punk/punkg.mf
%{_texmfdistdir}/fonts/source/public/punk/punkl.mf
%{_texmfdistdir}/fonts/source/public/punk/punkp.mf
%{_texmfdistdir}/fonts/source/public/punk/punksl.mf
%{_texmfdistdir}/fonts/source/public/punk/punksl20.mf
%{_texmfdistdir}/fonts/tfm/public/punk/punk10.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punk12.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punk20.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punkbx20.tfm
%{_texmfdistdir}/fonts/tfm/public/punk/punksl20.tfm

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081130-2
+ Revision: 755525
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081130-1
+ Revision: 719413
- texlive-punk
- texlive-punk
- texlive-punk
- texlive-punk

