---
layout: default
title: Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithm on Stochastic Smooth Functions
---

# Explicit and Non-asymptotic Query Complexities of Rank-Based Zeroth-order Algorithm on Stochastic Smooth Functions
**arXiv**：[2512.19104v1](https://arxiv.org/abs/2512.19104) · [PDF](https://arxiv.org/pdf/2512.19104.pdf)  
**作者**：Haishan Ye  

**一句话要点**：提出基于排序的零阶算法，在随机平滑函数上实现最优查询复杂度

**关键词**：零阶优化, 排序反馈, 随机函数, 查询复杂度, 非渐近分析, 人类偏好优化

## 3 点简述
- 研究随机函数下仅基于排序反馈的零阶优化问题，理论理解有限
- 提出简单高效的排序零阶算法，在标准假设下建立显式非渐近查询复杂度界
- 结果匹配基于值的零阶算法最优查询复杂度，证明排序信息在随机设置中足够

## 摘要（原文）

> Zeroth-order (ZO) optimization with ordinal feedback has emerged as a fundamental problem in modern machine learning systems, particularly in human-in-the-loop settings such as reinforcement learning from human feedback, preference learning, and evolutionary strategies. While rank-based ZO algorithms enjoy strong empirical success and robustness properties, their theoretical understanding, especially under stochastic objectives and standard smoothness assumptions, remains limited. In this paper, we study rank-based zeroth-order optimization for stochastic functions where only ordinal feedback of the stochastic function is available. We propose a simple and computationally efficient rank-based ZO algorithm. Under standard assumptions including smoothness, strong convexity, and bounded second moments of stochastic gradients, we establish explicit non-asymptotic query complexity bounds for both convex and nonconvex objectives. Notably, our results match the best-known query complexities of value-based ZO algorithms, demonstrating that ordinal information alone is sufficient for optimal query efficiency in stochastic settings. Our analysis departs from existing drift-based and information-geometric techniques, offering new tools for the study of rank-based optimization under noise. These findings narrow the gap between theory and practice and provide a principled foundation for optimization driven by human preferences.

