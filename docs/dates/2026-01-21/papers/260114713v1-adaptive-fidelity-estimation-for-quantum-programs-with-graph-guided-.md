---
layout: default
title: Adaptive Fidelity Estimation for Quantum Programs with Graph-Guided Noise Awareness
---

# Adaptive Fidelity Estimation for Quantum Programs with Graph-Guided Noise Awareness
**arXiv**：[2601.14713v1](https://arxiv.org/abs/2601.14713) · [PDF](https://arxiv.org/pdf/2601.14713.pdf)  
**作者**：Tingting Li, Ziming Zhao, Jianwei Yin  

**一句话要点**：提出QuFid框架，通过图引导噪声感知自适应估计量子程序保真度，以降低NISQ设备测量成本。

**关键词**：量子计算, 保真度估计, 噪声感知, 自适应测量, 图模型, NISQ设备

## 3 点简述
- 核心问题：NISQ设备中保真度估计因噪声、异构性和电路变换导致测量次数难以预定义，资源消耗大。
- 方法要点：将量子程序建模为DAG，利用控制流感知随机游走和编译结构变形指标量化噪声传播，基于谱特征自适应规划测量。
- 实验或效果：在IBM Quantum后端上测试18个基准，相比基线显著减少测量成本，同时保持可接受的保真度偏差。

## 摘要（原文）

> Fidelity estimation is a critical yet resource-intensive step in testing quantum programs on noisy intermediate-scale quantum (NISQ) devices, where the required number of measurements is difficult to predefine due to hardware noise, device heterogeneity, and transpilation-induced circuit transformations. We present QuFid, an adaptive and noise-aware framework that determines measurement budgets online by leveraging circuit structure and runtime statistical feedback. QuFid models a quantum program as a directed acyclic graph (DAG) and employs a control-flow-aware random walk to characterize noise propagation along gate dependencies. Backend-specific effects are captured via transpilation-induced structural deformation metrics, which are integrated into the random-walk formulation to induce a noise-propagation operator. Circuit complexity is then quantified through the spectral characteristics of this operator, providing a principled and lightweight basis for adaptive measurement planning. Experiments on 18 quantum benchmarks executed on IBM Quantum backends show that QuFid significantly reduces measurement cost compared to fixed-shot and learning-based baselines, while consistently maintaining acceptable fidelity bias.

