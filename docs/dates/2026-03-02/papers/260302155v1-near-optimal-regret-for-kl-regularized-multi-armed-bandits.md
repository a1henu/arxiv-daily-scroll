---
layout: default
title: Near-Optimal Regret for KL-Regularized Multi-Armed Bandits
---

# Near-Optimal Regret for KL-Regularized Multi-Armed Bandits
**arXiv**：[2603.02155v1](https://arxiv.org/abs/2603.02155) · [PDF](https://arxiv.org/pdf/2603.02155.pdf)  
**作者**：Kaixuan Ji, Qingyue Zhao, Heyang Zhao, Qiwei Di, Quanquan Gu  

**一句话要点**：提出KL-UCB的尖锐分析，为KL正则化多臂老虎机提供近最优遗憾界

**关键词**：多臂老虎机, KL正则化, 遗憾界, 在线学习, 统计效率

## 3 点简述
- 研究KL正则化多臂老虎机的统计效率，填补理论空白
- 使用新颖剥离论证分析KL-UCB，获得线性依赖K的高概率遗憾上界
- 通过硬实例构造和贝叶斯先验分解，证明下界，验证分析的紧致性

## 摘要（原文）

> Recent studies have shown that reinforcement learning with KL-regularized objectives can enjoy faster rates of convergence or logarithmic regret, in contrast to the classical $\sqrt{T}$-type regret in the unregularized setting. However, the statistical efficiency of online learning with respect to KL-regularized objectives remains far from completely characterized, even when specialized to multi-armed bandits (MABs). We address this problem for MABs via a sharp analysis of KL-UCB using a novel peeling argument, which yields a $\tilde{O}(ηK\log^2T)$ upper bound: the first high-probability regret bound with linear dependence on $K$. Here, $T$ is the time horizon, $K$ is the number of arms, $η^{-1}$ is the regularization intensity, and $\tilde{O}$ hides all logarithmic factors except those involving $\log T$. The near-tightness of our analysis is certified by the first non-constant lower bound $Ω(ηK \log T)$, which follows from subtle hard-instance constructions and a tailored decomposition of the Bayes prior. Moreover, in the low-regularization regime (i.e., large $η$), we show that the KL-regularized regret for MABs is $η$-independent and scales as $\tildeΘ(\sqrt{KT})$. Overall, our results provide a thorough understanding of KL-regularized MABs across all regimes of $η$ and yield nearly optimal bounds in terms of $K$, $η$, and $T$.

