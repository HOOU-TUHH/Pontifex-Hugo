---
title: "Introduction"
description: "Monotonicity Doks is a Hugo theme for building secure, fast, and SEO-ready documentation websites, which you can easily update and customize."
lead: "Monotonicity Doks is a Hugo theme for building secure, fast, and SEO-ready documentation websites, which you can easily update and customize."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "prologue"
weight: 100
toc: true
---

## Get started

Let us test something.

{{< header1 107>}}


There are two main ways to get started with Doks:

### Tutorial

{{< alert icon="👉" text="The Tutorial is intended for novice to intermediate users." />}}

Step-by-step instructions on how to start a new Doks project. [Tutorial →](https://getdoks.org/tutorial/introduction/)

### Quick Start

{{< alert icon="👉" text="The Quick Start is intended for intermediate to advanced users." />}}

One page summary of how to start a new Doks project. [Quick Start →]({{< relref "quick-start" >}})

## Go further

Recipes, Reference Guides, Extensions, and Showcase.

### Recipes

<div class="Theorem">
<p><span>Monotonicity of limits</span><span id="thm:monseq"
label="thm:monseq"></span> Let <span
class="math inline">\((a_n)_{n\in\mathbb{N}}\)</span> and <span
class="math inline">\((b_n)_{n\in\mathbb{N}}\)</span> be two convergent
real sequences with <span
class="math display">\[\lim_{n\to\infty}a_n=a,\qquad
\lim_{n\to\infty}b_n=b.\]</span> Further, assume that for all <span
class="math inline">\(n\in\mathbb{N}\)</span> holds <span
class="math inline">\(a_n\leq b_n\)</span>. Then the following holds
true:</p>
<ol type="i">
<li><p><span class="math inline">\(a\leq b\)</span>;</p></li>
<li><p>If <span class="math inline">\(a=b\)</span> and <span
class="math inline">\((c_n)_{n\in\mathbb{N}}\)</span> is another
sequence with <span class="math inline">\(a_n\leq c_n\leq b_n\)</span>
for all <span class="math inline">\(n \in \mathbb{N}\)</span>, then
<span class="math inline">\((c_n)_{n\in\mathbb{N}}\)</span> is
convergent with <span
class="math display">\[\lim_{n\to\infty}c_n=a=b.\]</span></p></li>
</ol>
</div>
<div class="proof">
<p><em>Proof.</em></p>
<ol type="i">
<li><p>Consider the sequence of differences between <span
class="math inline">\(b_n\)</span> and <span
class="math inline">\(a_n\)</span>, i.e., <span
class="math inline">\((b_n-a_n)_{n\in\mathbb{N}}\)</span>. By Theorem <a
href="#thm:limformnormed" data-reference-type="ref"
data-reference="thm:limformnormed">[thm:limformnormed]</a>, it suffices
to show that <span
class="math display">\[b-a=\lim_{n\To\infty}(b_n-a_n)\geq0.\]</span>
Assume the converse statement, i.e., <span
class="math inline">\(b-a&lt;0\)</span>. Then, we have that both numbers
<span class="math inline">\(a-b\)</span> and <span
class="math inline">\(b_n-a_n\)</span> are positive and thus <span
class="math display">\[|a-b-(a_n-b_n)|=a-b+(b_n-a_n)&gt;a-b.\]</span> In
particular, there exists no <span
class="math inline">\(n\in\mathbb{N}\)</span> such that <span
class="math inline">\(|a-b-(a_n-b_n)|&lt;\varepsilon\)</span> for <span
class="math inline">\(\varepsilon=a-b&gt;0\)</span>. This is
a contradiction to <span
class="math inline">\(\lim_{n\To\infty}(b_n-a_n)=b-a\)</span>.</p></li>
<li><p>Again consider the sequence <span
class="math inline">\((b_n-a_n)_{n\in\mathbb{N}}\)</span> which is
tending to zero according to Theorem <a href="#thm:limformnormed"
data-reference-type="ref"
data-reference="thm:limformnormed">[thm:limformnormed]</a>. Further,
consider the sequence <span
class="math inline">\((c_n-a_n)_{n\in\mathbb{N}}\)</span>. Then we have
for all <span class="math inline">\(n\in\mathbb{N}\)</span> that <span
class="math inline">\(0\leq c_n-a_n\leq b_n-a_n\)</span>. Let <span
class="math inline">\(\varepsilon&gt;0\)</span>. Since <span
class="math inline">\(b_n-a_n\)</span> is tending to zero, there exists
some <span class="math inline">\(N\)</span> such that for all <span
class="math inline">\(n\geq N\)</span> holds <span
class="math inline">\(|b_n-a_n-0|&lt;\varepsilon\)</span>. Due to <span
class="math inline">\(0\leq c_n-a_n\leq b_n-a_n\)</span>, we can
conclude that for <span class="math inline">\(n\geq N\)</span> holds
<span class="math display">\[|c_n-a_n-0|=c_n-a_n\leq b_n-a_n=
|b_n-a_n-0|&lt;\varepsilon.\]</span> This implies that <span
class="math inline">\((c_n-a_n)_{n\in\mathbb{N}}\)</span> is convergent
with <span class="math inline">\(\lim_{n\to\infty}(c_n-a_n)=0\)</span>.
Hence <span class="math inline">\(a=0+a=\lim_{n\rightarrow\infty}
(c_n-a_n) + \lim_{n\rightarrow\infty} a_n = \lim_{n\rightarrow\infty}
c_n\)</span>.</p></li>
</ol>
<p> ◻</p>
</div>
<div class="Remark">
<p><span id="rem:n_0mon" label="rem:n_0mon"></span> Since the
modification of finitely many sequence elements does not change the
limits (take a closer look at Definition <a href="#def:convlim"
data-reference-type="ref"
data-reference="def:convlim">[def:convlim]</a>), the statements of
Theorem <a href="#thm:monseq" data-reference-type="ref"
data-reference="thm:monseq">[thm:monseq]</a> can be slightly generalised
by only claiming that there exists some <span
class="math inline">\(n_0\)</span> such that for all <span
class="math inline">\(n\geq n_0\)</span> holds <span
class="math inline">\(a_n\leq b_n\)</span> (resp. for all <span
class="math inline">\(n\geq n_0\)</span> holds <span
class="math inline">\(a_n\leq c_n\leq b_n\)</span> in (ii)). In the
proof of (i), one has to replace the words “there exists no <span
class="math inline">\(n\in\mathbb{N}\)</span> such that” by “there
exists no <span class="math inline">\(n\geq n_0\)</span> such that” and
in the proof of (ii) the number <span class="math inline">\(N\)</span>
has to be replaced by <span
class="math inline">\(\max\{N,n_0\}\)</span>.</p>
</div>
<div class="Attention">
<p>From the fact that we have the strict inequality <span
class="math inline">\(a_n&lt;b_n\)</span>, we cannot conclude that the
limits satisfy <span class="math inline">\(a&lt;b\)</span>. To see this,
consider the sequences<span
class="math inline">\((a_n)_{n\in\mathbb{N}}=(0,0,0,\ldots)\)</span> and
<span
class="math inline">\((b_n)_{n\in\mathbb{N}}=(\frac1n)_{n\in\mathbb{N}}\)</span>.
In this case, we have <span class="math inline">\(a=b=0\)</span> though
the strict inequality <span
class="math inline">\(a_n=0&lt;\frac1n=b_n\)</span> holds true for all
<span class="math inline">\(n\in\mathbb{N}\)</span>.</p>
</div>
<div class="example">
<ol type="a">
<li><p>Consider <span
class="math inline">\((\frac1{n^k})_{n\in\mathbb{N}}\)</span> for some
<span class="math inline">\(k\in\mathbb{N}\)</span>. We state two
alternative ways to show that this sequence tends to zero. The first
possibility is, of course, an argumentation as in statement (b) in
Remark on page . The second way to treat this problem is making use of
the inequality <span
class="math display">\[\frac1n\geq\frac1{n^k}&gt;0.\]</span> Since we
know from Example <a href="#ex:basicconvseq" data-reference-type="ref"
data-reference="ex:basicconvseq">[ex:basicconvseq]</a> a) that the
sequence <span class="math inline">\((\frac1n)_{n\in\mathbb{N}}\)</span>
tends to zero, statement (ii) of Theorem <a href="#thm:monseq"
data-reference-type="ref" data-reference="thm:monseq">[thm:monseq]</a>
directly leads to the fact that <span
class="math inline">\((\frac1{n^k})_{n\in\mathbb{N}}\)</span> also tends
to zero.</p></li>
<li><p>Consider <span
class="math inline">\((a_n)_{n\in\mathbb{N}}\)</span> with <span
class="math display">\[a_n=\frac{2n^2+5n-1}{-5n^2+n+1}.\]</span>
Rewriting <span
class="math display">\[a_n=\frac{2+\frac5n-\frac1{n^2}}{-5+\frac1n+\frac1{n^2}},\]</span>
and using that both <span
class="math inline">\((\frac1{n})_{n\in\mathbb{N}}\)</span> and <span
class="math inline">\((\frac1{n^2})_{n\in\mathbb{N}}\)</span> tend to
zero, we can apply Theorem <a href="#thm:limformnormed"
data-reference-type="ref"
data-reference="thm:limformnormed">[thm:limformnormed]</a> to obtain
that <span
class="math display">\[\lim_{n\To\infty}a_n=\lim_{n\To\infty}\frac{2n^2+5n-1}{-5n^2+n+1}=\lim_{n\To\infty}\frac{2+\frac5n-\frac1{n^2}}{-5+\frac1n+\frac1{n^2}}=-\frac25.\]</span></p></li>
<li><p>Consider <span
class="math inline">\((a_n)_{n\in\mathbb{N}}\)</span> with <span
class="math inline">\(a_n=\sqrt{n^2+1}-n\)</span>. At first glance, none
of the so far presented results seem to help to analyse convergence of
this sequence. However, we can compute <span
class="math display">\[\begin{aligned}
a_n\,=&amp;\sqrt{n^2+1}-n
=\frac{(\sqrt{n^2+1}-n)(\sqrt{n^2+1}+n)}{\sqrt{n^2+1}+n}\\
=&amp;\frac{n^2+1-n^2}{\sqrt{n^2+1}+n}
=\frac{1}{\sqrt{n^2+1}+n}&lt;\frac1n.
\end{aligned}\]</span> By Theorem <a href="#thm:monseq"
data-reference-type="ref" data-reference="thm:monseq">[thm:monseq]</a>,
we now get that <span
class="math inline">\(\lim_{n\To\infty}a_n=0\)</span>.</p></li>
</ol>
</div>

### Reference Guides

\[chapter\] \[theorem\] Lemma \[theorem\] Folgerung

\[theorem\] Frage \[theorem\] Question \[theorem\] Aufgabe \[theorem\]
Exercise

\[theorem\] Proposition \[theorem\] Satz \[theorem\] Definition

\[theorem\] Bemerkung \[theorem\] Beispiel \[theorem\] Example
\[theorem\] Notation \[theorem\]Rule of Thumb \[theorem\]Concept

Subsequences and accumulation values
====================================

Subsequence Let $(a_n)_{n\in\mathbb{N}}$ be a sequence in $\mathbb{K}$.
Let $(n_k)_{k\in\mathbb{N}}$ be a strongly monotonically increasing
sequence with $n_k\in\mathbb{N}$ for all $k\in\mathbb{N}$. Then
$(a_{n_k})_{k\in\mathbb{N}}$ is called a *subsequence*.

Consider the sequence
$(a_n)_{n\in\mathbb{N}}=(\frac1n)_{n\in\mathbb{N}}$. Then some
subsequences are given by

-   $(a_{n_k})_{k\in\mathbb{N}}=(a_{2k})_{k\in\mathbb{N}}=(\frac12,\frac14,\frac16,\frac18,\ldots)$;

-   $(a_{n_k})_{k\in\mathbb{N}}=(a_{k^2})_{k\in\mathbb{N}}=(1,\frac14,\frac19,\frac1{16},\frac1{25},\ldots)$;

-   $(a_{n_k})_{k\in\mathbb{N}}=(a_{2^k})_{k\in\mathbb{N}}=(\frac12,\frac14,\frac18,\frac1{16},\frac1{32},\ldots)$;

-   $(a_{n_k})_{k\in\mathbb{N}}=(a_{k!})_{k\in\mathbb{N}}=(1,\frac12,\frac16,\frac1{24},\frac1{120},\frac1{720},\ldots)$.

Convergence of subsequences[\[thm:convsubseq\]]{#thm:convsubseq
label="thm:convsubseq"} Let $(a_n)_{n\in\mathbb{N}}$ be a convergent
sequence in $\mathbb{K}$ with $\lim_{n\to\infty}a_n=a$. Then all
subsequences $(a_{n_k})_{k\in\mathbb{N}}$ of $(a_n)_{n\in\mathbb{N}}$
are also convergent with $$\lim_{k\to\infty}a_{n_k}=a.$$

The existence of a convergent subsequence $(a_{n_k})_{k\in\mathbb{N}}$
does in general imply the convergence of $(a_n)_{n\in\mathbb{N}}$. For
instance, consider $(a_n)_{n\in\mathbb{N}}=((-1)^n)_{n\in\mathbb{N}}$.
Both subsequences $$\begin{aligned}
(a_{2k})_{k\in\mathbb{N}}\,&=((-1)^{2k})_{k\in\mathbb{N}}&&=(1,1,1,1,\ldots)\\
(a_{2k+1})_{k\in\mathbb{N}}\,&=((-1)^{2k+1})_{k\in\mathbb{N}}\!\!\!\!\!\!&&=(-1,-1,-1,-1,\ldots)
  \end{aligned}$$ are convergent though
$(a_n)_{n\in\mathbb{N}}=((-1)^n)_{n\in\mathbb{N}}$ is divergent (see
Example [\[ex:basicconvseq\]](#ex:basicconvseq){reference-type="ref"
reference="ex:basicconvseq"} b)).

However, we can "rescue" this statement by additionally claiming that
$(a_n)_{n\in\mathbb{N}}$ is monotonic.

Subsequences of monotonic sequences [\[thm:submon\]]{#thm:submon
label="thm:submon"} Let $(a_n)_{n\in\mathbb{N}}$ be a sequence in
$\mathbb{R}$. If $(a_n)_{n\in\mathbb{N}}$ is monotonic and there exists
a convergent subsequence $(a_{n_k})_{k\in\mathbb{N}}$, then
$(a_n)_{n\in\mathbb{N}}$ is convergent with
$$\lim_{n\to\infty}a_n=\lim_{k\to\infty}a_{n_k}.$$

*Proof:* Denote $a=\lim_{k\to\infty}a_{n_k}$. We just consider the case
where $(a_n)_{n\in\mathbb{N}}$ is monotonically increasing (the
remaining part can be done analogously to the argumentations at the end
of the proof of
Theorem [\[thm:bndmonseq\]](#thm:bndmonseq){reference-type="ref"
reference="thm:bndmonseq"}). Since $(a_{n_k})_{k\in\mathbb{N}}$ is also
monotonically increasing, we have that
$a=\sup\{a_{n_k}\,:\,k\in\mathbb{N}\}$.\
Let $\varepsilon>0$. Due to the convergence and monotonicity of
$(a_{n_k})_{k\in\mathbb{N}}$, there exists some $K\in\mathbb{N}$ such
that for all $k\geq K$ holds $$a-\varepsilon<a_{n_k}\leq a.$$ Now assume
that $n\geq N=n_K$. Monotonicity then implies that
$a-\varepsilon<a_{n_K}\leq a_n\leq a_{n_n}\leq a$. In particular, we
have that $$|a- a_n|=a-a_n<\varepsilon.$$$\Box$

Accumulation value
[\[def:accuPointNormedSpace\]]{#def:accuPointNormedSpace
label="def:accuPointNormedSpace"} Let $(a_n)_{n\in\mathbb{N}}$ be
a sequence in $\mathbb{K}$. Then $a\in \mathbb{K}$ is called if there
exists some subsequence $(a_{n_k})_{k\in\mathbb{N}}$ with
$$a=\lim_{k\to\infty}a_{n_k}.$$

Names Accumulation values are often called by other names, like , or .

$a\in \mathbb{K}$ is an accumulation value if and only if in every
$\varepsilon$-neighbourhood of $a$, there are infinitely many elements
of the sequence $(a_{n})_{n\in\mathbb{N}}$.

Accumulation values $\pm\infty$[\[accinf\]]{#accinf label="accinf"} A
real sequence $(a_n)_{n\in\mathbb{N}}$ is said to have the if it is not
bounded from above. Analogously, we define the if it is not bounded from
below.


Learn how to customize Doks to fully make it your own. [Reference Guides →](https://getdoks.org/docs/reference-guides/security/)

### Extensions

Get instructions on how to add even more to Doks. [Extensions →](https://getdoks.org/docs/extensions/breadcrumb-navigation/)

### Showcase

See what others have build with Doks. [Showcase →](https://getdoks.org/showcase/electric-blocks/)

## Contributing

Find out how to contribute to Doks. [Contributing →](https://getdoks.org/docs/contributing/how-to-contribute/)

## Help

Get help on Doks. [Help →]({{< relref "how-to-update" >}})
