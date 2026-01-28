---
layout: default
title: Analysis of Shuffling Beyond Pure Local Differential Privacy
---

# Analysis of Shuffling Beyond Pure Local Differential Privacy
**arXiv**：[2601.19154v1](https://arxiv.org/abs/2601.19154) · [PDF](https://arxiv.org/pdf/2601.19154.pdf)  
**作者**：Shun Takagi, Seng Pei Liew  

**一句话要点**：提出基于洗牌指数的渐近分析，以精确量化洗牌在非纯本地差分隐私下的隐私放大效果。

**关键词**：洗牌差分隐私, 渐近分析, 洗牌指数, 隐私放大, 高斯机制, 数值算法

## 3 点简述
- 核心问题：现有洗牌隐私分析依赖纯本地差分隐私参数，导致上界宽松且无法准确描述高斯机制等基本机制的隐私放大。
- 方法要点：通过渐近分析洗牌覆盖散度，引入洗牌指数作为关键参数，推导出洗牌机制的紧致隐私保证带。
- 实验或效果：开发基于FFT的算法，在有限样本下计算覆盖散度，提供可控误差和近线性运行时间的实用数值分析。

## 摘要（原文）

> Shuffling is a powerful way to amplify privacy of a local randomizer in private distributed data analysis, but existing analyses mostly treat the local differential privacy (DP) parameter $\varepsilon_0$ as the only knob and give generic upper bounds that can be loose and do not even characterize how shuffling amplifies privacy for basic mechanisms such as the Gaussian mechanism. We revisit the privacy blanket bound of Balle et al. (the blanket divergence) and develop an asymptotic analysis that applies to a broad class of local randomizers under mild regularity assumptions, without requiring pure local DP. Our key finding is that the leading term of the blanket divergence depends on the local mechanism only through a single scalar parameter $χ$, which we call the shuffle index. By applying this asymptotic analysis to both upper and lower bounds, we obtain a tight band for $δ_n$ in the shuffled mechanism's $(\varepsilon_n,δ_n)$-DP guarantee. Moreover, we derive a simple structural necessary and sufficient condition on the local randomizer under which the blanket-divergence-based upper and lower bounds coincide asymptotically. $k$-RR families with $k\ge3$ satisfy this condition, while for generalized Gaussian mechanisms the condition may not hold but the resulting band remains tight. Finally, we complement the asymptotic theory with an FFT-based algorithm for computing the blanket divergence at finite $n$, which offers rigorously controlled relative error and near-linear running time in $n$, providing a practical numerical analysis for shuffle DP.

