---
layout: default
title: Toward Generative Quantum Utility via Correlation-Complexity Map
---

# Toward Generative Quantum Utility via Correlation-Complexity Map
**arXiv**：[2603.06440v1](https://arxiv.org/abs/2603.06440) · [PDF](https://arxiv.org/pdf/2603.06440.pdf)  
**作者**：Chen-Yu Liu, Leonardo Placidi, Eric Brunner, Enrico Rinaldi  

**一句话要点**：提出相关性-复杂度图作为诊断工具，以识别数据分布与IQP量子生成模型的结构对齐性。

**关键词**：量子生成模型, 相关性分析, 复杂度指标, 湍流数据建模, IQP电路, 分布对齐

## 3 点简述
- 核心问题：如何判断真实世界数据分布是否适合IQP型量子生成模型。
- 方法要点：定义量子相关性指标和经典相关性复杂度指标，构建相关性-复杂度图进行诊断。
- 实验或效果：在湍流数据上验证IQP模型，相比经典模型实现竞争性分布对齐，使用更少训练快照。

## 摘要（原文）

> We propose a Correlation-Complexity Map as a practical diagnostic tool for determining when real-world data distributions are structurally aligned with IQP-type quantum generative models. Characterized by two complementary indicators: (i) a Quantum Correlation-Likeness Indicator (QCLI), computed from the dataset's correlation-order (Walsh-Hadamard/Fourier) power spectrum aggregated by interaction order and quantified via Jensen-Shannon divergence from an i.i.d. binomial reference; and (ii) a Classical Correlation-Complexity Indicator (CCI), defined as the fraction of total correlation not captured by the optimal Chow-Liu tree approximation, normalized by total correlation. We provide theoretical support by relating QCLI to a support-mismatch mechanism, for fixed-architecture IQP families trained with an MMD objective, higher QCLI implies a smaller irreducible approximation floor. Using the map, we identify the classical turbulence data as both IQP-compatible and classically complex (high QCLI/high CCI). Guided by this placement, we use an invertible float-to-bitstring representation and a latent-parameter adaptation scheme that reuses a compact IQP circuit over a temporal sequence by learning and interpolating a low-dimensional latent trajectory. In comparative evaluations against classical models such as Restricted Boltzmann Machine (RBM) and Deep Convolutional Generative Adversarial Networks (DCGAN), the IQP approach achieves competitive distributional alignment while using substantially fewer training snapshots and a small latent block, supporting the use of QCLI/CCI as practical indicators for locating IQP-aligned domains and advancing generative quantum utility.

