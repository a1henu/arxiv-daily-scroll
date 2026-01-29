---
layout: default
title: A scalable flow-based approach to mitigate topological freezing
---

# A scalable flow-based approach to mitigate topological freezing
**arXiv**：[2601.20708v1](https://arxiv.org/abs/2601.20708) · [PDF](https://arxiv.org/pdf/2601.20708.pdf)  
**作者**：Claudio Bonanno, Andrea Bulgarelli, Elia Cellini, Alessandro Nada, Dario Panfalone, Davide Vadacchino, Lorenzo Verzichelli  

**一句话要点**：提出基于随机归一化流的可扩展方法，以缓解非平衡蒙特卡洛模拟中的拓扑冻结问题。

**关键词**：拓扑冻结, 随机归一化流, 晶格规范理论, 蒙特卡洛模拟, 边界条件处理

## 3 点简述
- 核心问题：晶格规范理论在连续极限下，标准蒙特卡洛模拟因拓扑冻结导致拓扑可观测量自相关急剧增长。
- 方法要点：使用随机归一化流，通过掩码参数化stout平滑层，将开放边界条件配置传输到周期性系综，以消除边界伪影。
- 实验或效果：在4d SU(3) Yang-Mills理论中验证，重现拓扑磁化率参考结果，显示优于纯随机非平衡方法。

## 摘要（原文）

> As lattice gauge theories with non-trivial topological features are driven towards the continuum limit, standard Markov Chain Monte Carlo simulations suffer for topological freezing, i.e., a dramatic growth of autocorrelations in topological observables. A widely used strategy is the adoption of Open Boundary Conditions (OBC), which restores ergodic sampling of topology but at the price of breaking translation invariance and introducing unphysical boundary artifacts. In this contribution we summarize a scalable, exact flow-based strategy to remove them by transporting configurations from a prior with a OBC defect to a fully periodic ensemble, and apply it to 4d SU(3) Yang--Mills theory. The method is based on a Stochastic Normalizing Flow (SNF) that alternates non-equilibrium Monte Carlo updates with localized, gauge-equivariant defect coupling layers implemented via masked parametric stout smearing. Training is performed by minimizing the average dissipated work, equivalent to a Kullback--Leibler divergence between forward and reverse non-equilibrium path measures, to achieve more reversible trajectories and improved efficiency. We discuss the scaling with the number of degrees of freedom affected by the defect and show that defect SNFs achieve better performances than purely stochastic non-equilibrium methods at comparable cost. Finally, we validate the approach by reproducing reference results for the topological susceptibility.

