---
layout: default
title: Improved Approximate Regret for Decentralized Online Continuous Submodular Maximization via Reductions
---

# Improved Approximate Regret for Decentralized Online Continuous Submodular Maximization via Reductions
**arXiv**：[2602.09502v1](https://arxiv.org/abs/2602.09502) · [PDF](https://arxiv.org/pdf/2602.09502.pdf)  
**作者**：Yuanyu Wan, Yu Shen, Dingzhi Yu, Bo Xue, Mingli Song  

**一句话要点**：提出两种归约方法以改进去中心化在线连续子模最大化的近似遗憾界

**关键词**：去中心化在线学习, 连续子模最大化, 近似遗憾界, 归约方法, 无投影算法

## 3 点简述
- 核心问题：去中心化在线连续子模最大化中近似遗憾界与凸设置差距大，且无投影算法无法恢复集中式设置界
- 方法要点：通过归约到去中心化在线凸优化，利用其算法提升近似遗憾界
- 实验或效果：在一般凸决策集上同时解决两个问题，在下闭决策集上显著缓解第一个问题

## 摘要（原文）

> To expand the applicability of decentralized online learning, previous studies have proposed several algorithms for decentralized online continuous submodular maximization (D-OCSM) -- a non-convex/non-concave setting with continuous DR-submodular reward functions. However, there exist large gaps between their approximate regret bounds and the regret bounds achieved in the convex setting. Moreover, if focusing on projection-free algorithms, which can efficiently handle complex decision sets, they cannot even recover the approximate regret bounds achieved in the centralized setting. In this paper, we first demonstrate that for D-OCSM over general convex decision sets, these two issues can be addressed simultaneously. Furthermore, for D-OCSM over downward-closed decision sets, we show that the second issue can be addressed while significantly alleviating the first issue. Our key techniques are two reductions from D-OCSM to decentralized online convex optimization (D-OCO), which can exploit D-OCO algorithms to improve the approximate regret of D-OCSM in these two cases, respectively.

