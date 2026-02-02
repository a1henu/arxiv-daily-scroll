---
layout: default
title: Value-at-Risk Constrained Policy Optimization
---

# Value-at-Risk Constrained Policy Optimization
**arXiv**：[2601.22993v1](https://arxiv.org/abs/2601.22993) · [PDF](https://arxiv.org/pdf/2601.22993.pdf)  
**作者**：Rohan Tangri, Jan-Peter Calliess  

**一句话要点**：提出VaR-CPO算法以直接优化风险价值约束，实现安全探索

**关键词**：风险价值约束, 安全强化学习, 约束策略优化, 切比雪夫不等式, 信任域方法

## 3 点简述
- 核心问题：风险价值约束在强化学习中非可微，难以直接优化
- 方法要点：利用切比雪夫不等式构建可处理代理，扩展CPO信任域框架
- 实验或效果：在可行环境中训练时实现零约束违反，优于基线方法

## 摘要（原文）

> We introduce the Value-at-Risk Constrained Policy Optimization algorithm (VaR-CPO), a sample efficient and conservative method designed to optimize Value-at-Risk (VaR) constraints directly. Empirically, we demonstrate that VaR-CPO is capable of safe exploration, achieving zero constraint violations during training in feasible environments, a critical property that baseline methods fail to uphold. To overcome the inherent non-differentiability of the VaR constraint, we employ the one-sided Chebyshev inequality to obtain a tractable surrogate based on the first two moments of the cost return. Additionally, by extending the trust-region framework of the Constrained Policy Optimization (CPO) method, we provide rigorous worst-case bounds for both policy improvement and constraint violation during the training process.

