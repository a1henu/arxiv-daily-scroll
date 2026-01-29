---
layout: default
title: Smoothing the Black-Box: Signed-Distance Supervision for Black-Box Model Copying
---

# Smoothing the Black-Box: Signed-Distance Supervision for Black-Box Model Copying
**arXiv**：[2601.20773v1](https://arxiv.org/abs/2601.20773) · [PDF](https://arxiv.org/pdf/2601.20773.pdf)  
**作者**：Rubén Jiménez, Oriol Pujol  

**一句话要点**：提出基于符号距离监督的黑盒模型复制框架，以平滑回归替代硬标签学习，提升边界几何恢复效率。

**关键词**：黑盒模型复制, 符号距离监督, 平滑回归, 决策边界估计, 模型蒸馏, 不确定性信号

## 3 点简述
- 核心问题：黑盒模型复制中，仅依赖硬标签输出导致不连续表面重建，难以高效恢复决策边界几何。
- 方法要点：引入符号距离监督，将复制转化为平滑回归问题，利用局部几何信息，并设计α控制平滑与正则化方案。
- 实验或效果：在合成问题和UCI基准测试中，相比硬标签基线，在保真度和泛化准确性上表现更优，并提供距离输出作为不确定性信号。

## 摘要（原文）

> Deployed machine learning systems must continuously evolve as data, architectures, and regulations change, often without access to original training data or model internals. In such settings, black-box copying provides a practical refactoring mechanism, i.e. upgrading legacy models by learning replicas from input-output queries alone. When restricted to hard-label outputs, copying turns into a discontinuous surface reconstruction problem from pointwise queries, severely limiting the ability to recover boundary geometry efficiently. We propose a distance-based copying (distillation) framework that replaces hard-label supervision with signed distances to the teacher's decision boundary, converting copying into a smooth regression problem that exploits local geometry. We develop an $α$-governed smoothing and regularization scheme with Hölder/Lipschitz control over the induced target surface, and introduce two model-agnostic algorithms to estimate signed distances under label-only access. Experiments on synthetic problems and UCI benchmarks show consistent improvements in fidelity and generalization accuracy over hard-label baselines, while enabling distance outputs as uncertainty-related signals for black-box replicas.

