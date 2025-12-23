---
layout: default
title: Finite-sample guarantees for data-driven forward-backward operator methods
---

# Finite-sample guarantees for data-driven forward-backward operator methods
**arXiv**：[2512.19172v1](https://arxiv.org/abs/2512.19172) · [PDF](https://arxiv.org/pdf/2512.19172.pdf)  
**作者**：Filippo Fabiani, Barbara Franci  

**一句话要点**：提出基于数据的前向后向算子分裂方法的有限样本保证，用于随机环境下算子求零问题

**关键词**：算子分裂方法, 有限样本保证, 算法稳定性, 随机优化, 纳什均衡, 智能电网控制

## 3 点简述
- 核心问题：在随机环境中，当算子之一无法闭式表达或计算昂贵时，如何利用有限噪声样本近似求解算子零点的质量保证
- 方法要点：基于算法稳定性理论，推导真实零点与前向后向输出距离的概率界，无需特定数据分布假设
- 实验或效果：将结果应用于随机纳什均衡寻求算法，并在智能电网控制问题中验证理论界

## 摘要（原文）

> We establish finite sample certificates on the quality of solutions produced by data-based forward-backward (FB) operator splitting schemes. As frequently happens in stochastic regimes, we consider the problem of finding a zero of the sum of two operators, where one is either unavailable in closed form or computationally expensive to evaluate, and shall therefore be approximated using a finite number of noisy oracle samples. Under the lens of algorithmic stability, we then derive probabilistic bounds on the distance between a true zero and the FB output without making specific assumptions about the underlying data distribution. We show that under weaker conditions ensuring the convergence of FB schemes, stability bounds grow proportionally to the number of iterations. Conversely, stronger assumptions yield stability guarantees that are independent of the iteration count. We then specialize our results to a popular FB stochastic Nash equilibrium seeking algorithm and validate our theoretical bounds on a control problem for smart grids, where the energy price uncertainty is approximated by means of historical data.

