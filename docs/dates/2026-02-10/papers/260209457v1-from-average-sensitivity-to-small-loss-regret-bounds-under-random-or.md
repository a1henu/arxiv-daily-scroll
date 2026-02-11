---
layout: default
title: From Average Sensitivity to Small-Loss Regret Bounds under Random-Order Model
---

# From Average Sensitivity to Small-Loss Regret Bounds under Random-Order Model
**arXiv**：[2602.09457v1](https://arxiv.org/abs/2602.09457) · [PDF](https://arxiv.org/pdf/2602.09457.pdf)  
**作者**：Shinsaku Sakaue, Yuichi Yoshida  

**一句话要点**：提出基于平均敏感性的自适应方法，在随机顺序模型中实现小损失遗憾界

**关键词**：随机顺序模型, 在线学习, 平均敏感性, 小损失遗憾界, 自适应算法, 近似算法

## 3 点简述
- 研究随机顺序模型中的在线学习，损失函数集对抗选择但随机顺序揭示
- 利用离线算法的平均敏感性，自适应调整近似参数，推导小损失遗憾界
- 应用于在线k均值聚类、低秩逼近和回归，无需损失函数光滑性假设

## 摘要（原文）

> We study online learning in the random-order model, where the multiset of loss functions is chosen adversarially but revealed in a uniformly random order. Building on the batch-to-online conversion by Dong and Yoshida (2023), we show that if an offline algorithm admits a $(1+\varepsilon)$-approximation guarantee and the effect of $\varepsilon$ on its average sensitivity is characterized by a function $\varphi(\varepsilon)$, then an adaptive choice of $\varepsilon$ yields a small-loss regret bound of $\tilde O(\varphi^{\star}(\mathrm{OPT}_T))$, where $\varphi^{\star}$ is the concave conjugate of $\varphi$, $\mathrm{OPT}_T$ is the offline optimum over $T$ rounds, and $\tilde O$ hides polylogarithmic factors in $T$. Our method requires no regularity assumptions on loss functions, such as smoothness, and can be viewed as a generalization of the AdaGrad-style tuning applied to the approximation parameter $\varepsilon$. Our result recovers and strengthens the $(1+\varepsilon)$-approximate regret bounds of Dong and Yoshida (2023) and yields small-loss regret bounds for online $k$-means clustering, low-rank approximation, and regression. We further apply our framework to online submodular function minimization using $(1\pm\varepsilon)$-cut sparsifiers of submodular hypergraphs, obtaining a small-loss regret bound of $\tilde O(n^{3/4}(1 + \mathrm{OPT}_T^{3/4}))$, where $n$ is the ground-set size. Our approach sheds light on the power of sparsification and related techniques in establishing small-loss regret bounds in the random-order model.

