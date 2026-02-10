---
layout: default
title: Discrete Adjoint Schrödinger Bridge Sampler
---

# Discrete Adjoint Schrödinger Bridge Sampler
**arXiv**：[2602.08243v1](https://arxiv.org/abs/2602.08243) · [PDF](https://arxiv.org/pdf/2602.08243.pdf)  
**作者**：Wei Guo, Yuchen Zhu, Xiaochen Du, Juno Nam, Yongxin Chen, Rafael Gómez-Bombarelli, Guan-Horng Liu, Molei Tao, Jaemoo Choi  

**一句话要点**：提出离散ASBS框架，将伴随匹配方法扩展至离散空间以高效学习神经采样器。

**关键词**：离散神经采样器, 伴随匹配, 薛定谔桥, 随机最优控制, 训练效率

## 3 点简述
- 核心问题：离散神经采样器学习因梯度缺失和组合复杂性而具挑战性。
- 方法要点：揭示伴随匹配机制与状态空间无关，引入离散ASBS统一框架。
- 实验效果：在样本质量上具竞争力，训练效率和可扩展性优势显著。

## 摘要（原文）

> Learning discrete neural samplers is challenging due to the lack of gradients and combinatorial complexity. While stochastic optimal control (SOC) and Schrödinger bridge (SB) provide principled solutions, efficient SOC solvers like adjoint matching (AM), which excel in continuous domains, remain unexplored for discrete spaces. We bridge this gap by revealing that the core mechanism of AM is $\mathit{state}\text{-}\mathit{space~agnostic}$, and introduce $\mathbf{discrete~ASBS}$, a unified framework that extends AM and adjoint Schrödinger bridge sampler (ASBS) to discrete spaces. Theoretically, we analyze the optimality conditions of the discrete SB problem and its connection to SOC, identifying a necessary cyclic group structure on the state space to enable this extension. Empirically, discrete ASBS achieves competitive sample quality with significant advantages in training efficiency and scalability.

