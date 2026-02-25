---
layout: default
title: Is Multi-Distribution Learning as Easy as PAC Learning: Sharp Rates with Bounded Label Noise
---

# Is Multi-Distribution Learning as Easy as PAC Learning: Sharp Rates with Bounded Label Noise
**arXiv**：[2602.21039v1](https://arxiv.org/abs/2602.21039) · [PDF](https://arxiv.org/pdf/2602.21039.pdf)  
**作者**：Rafael Hanashiro, Abhishek Shetty, Patrick Jaillet  

**一句话要点**：揭示多分布学习在有限标签噪声下样本复杂度需k/ε²，与单任务学习存在统计分离

**关键词**：多分布学习, 有限标签噪声, 样本复杂度, 统计分离, 假设检验

## 3 点简述
- 研究多分布学习在有限标签噪声下的统计复杂度，探讨样本效率是否可扩展
- 提出结构化假设检验框架，证明多分布下验证近最优性需额外统计成本
- 证明与各分布贝叶斯最优误差竞争时，样本复杂度有k的乘法惩罚

## 摘要（原文）

> Towards understanding the statistical complexity of learning from heterogeneous sources, we study the problem of multi-distribution learning. Given $k$ data sources, the goal is to output a classifier for each source by exploiting shared structure to reduce sample complexity. We focus on the bounded label noise setting to determine whether the fast $1/ε$ rates achievable in single-task learning extend to this regime with minimal dependence on $k$. Surprisingly, we show that this is not the case. We demonstrate that learning across $k$ distributions inherently incurs slow rates scaling with $k/ε^2$, even under constant noise levels, unless each distribution is learned separately. A key technical contribution is a structured hypothesis-testing framework that captures the statistical cost of certifying near-optimality under bounded noise-a cost we show is unavoidable in the multi-distribution setting.
>   Finally, we prove that when competing with the stronger benchmark of each distribution's optimal Bayes error, the sample complexity incurs a \textit{multiplicative} penalty in $k$. This establishes a \textit{statistical} separation between random classification noise and Massart noise, highlighting a fundamental barrier unique to learning from multiple sources.

