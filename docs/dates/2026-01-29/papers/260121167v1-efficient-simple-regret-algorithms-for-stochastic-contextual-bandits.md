---
layout: default
title: Efficient Simple Regret Algorithms for Stochastic Contextual Bandits
---

# Efficient Simple Regret Algorithms for Stochastic Contextual Bandits
**arXiv**：[2601.21167v1](https://arxiv.org/abs/2601.21167) · [PDF](https://arxiv.org/pdf/2601.21167.pdf)  
**作者**：Shuai Liu, Alireza Bakhtiari, Alex Ayoub, Botao Hao, Csaba Szepesvári  

## 摘要（原文）

> We study stochastic contextual logistic bandits under the simple regret objective. While simple regret guarantees have been established for the linear case, no such results were previously known for the logistic setting. Building on ideas from contextual linear bandits and self-concordant analysis, we propose the first algorithm that achieves simple regret $\tilde{\mathcal{O}}(d/\sqrt{T})$. Notably, the leading term of our regret bound is free of the constant $κ= \mathcal O(\exp(S))$, where $S$ is a bound on the magnitude of the unknown parameter vector. The algorithm is shown to be fully tractable when the action set is finite. We also introduce a new variant of Thompson Sampling tailored to the simple-regret setting. This yields the first simple regret guarantee for randomized algorithms in stochastic contextual linear bandits, with regret $\tilde{\mathcal{O}}(d^{3/2}/\sqrt{T})$. Extending this method to the logistic case, we obtain a similarly structured Thompson Sampling algorithm that achieves the same regret bound -- $\tilde{\mathcal{O}}(d^{3/2}/\sqrt{T})$ -- again with no dependence on $κ$ in the leading term. The randomized algorithms, as expected, are cheaper to run than their deterministic counterparts. Finally, we conducted a series of experiments to empirically validate these theoretical guarantees.

