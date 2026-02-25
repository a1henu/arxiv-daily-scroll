---
layout: default
title: Characterizing Online and Private Learnability under Distributional Constraints via Generalized Smoothness
---

# Characterizing Online and Private Learnability under Distributional Constraints via Generalized Smoothness
**arXiv**：[2602.20585v1](https://arxiv.org/abs/2602.20585) · [PDF](https://arxiv.org/pdf/2602.20585.pdf)  
**作者**：Moïse Blanchard, Abhishek Shetty, Alexander Rakhlin  

**一句话要点**：提出广义平滑性以刻画分布约束下的在线与私有学习可学习性

**关键词**：在线学习, 分布对抗, 广义平滑性, 私有学习, VC维, 遗憾界

## 3 点简述
- 研究分布对抗下的序列决策学习，核心问题为确定允许样本复杂度接近独立数据情况的条件
- 引入广义平滑性概念，证明分布族允许有限VC维假设类获得VC维依赖的遗憾界当且仅当该族广义平滑
- 基于广义平滑性提供通用算法，无需显式知识即可实现低遗憾，并给出已知分布族时的细化界限

## 摘要（原文）

> Understanding minimal assumptions that enable learning and generalization is perhaps the central question of learning theory. Several celebrated results in statistical learning theory, such as the VC theorem and Littlestone's characterization of online learnability, establish conditions on the hypothesis class that allow for learning under independent data and adversarial data, respectively. Building upon recent work bridging these extremes, we study sequential decision making under distributional adversaries that can adaptively choose data-generating distributions from a fixed family $U$ and ask when such problems are learnable with sample complexity that behaves like the favorable independent case. We provide a near complete characterization of families $U$ that admit learnability in terms of a notion known as generalized smoothness i.e. a distribution family admits VC-dimension-dependent regret bounds for every finite-VC hypothesis class if and only if it is generalized smooth. Further, we give universal algorithms that achieve low regret under any generalized smooth adversary without explicit knowledge of $U$. Finally, when $U$ is known, we provide refined bounds in terms of a combinatorial parameter, the fragmentation number, that captures how many disjoint regions can carry nontrivial mass under $U$. These results provide a nearly complete understanding of learnability under distributional adversaries. In addition, building upon the surprising connection between online learning and differential privacy, we show that the generalized smoothness also characterizes private learnability under distributional constraints.

