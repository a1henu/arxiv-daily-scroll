---
layout: default
title: Why Smooth Stability Assumptions Fail for ReLU Learning
---

# Why Smooth Stability Assumptions Fail for ReLU Learning
**arXiv**：[2512.22055v1](https://arxiv.org/abs/2512.22055) · [PDF](https://arxiv.org/pdf/2512.22055.pdf)  
**作者**：Ronald Katende  

**一句话要点**：揭示平滑稳定性假设在ReLU学习中的全局失效，并提出非光滑感知框架

**关键词**：ReLU网络, 稳定性分析, 非光滑优化, 梯度Lipschitzness, 广义导数, 学习系统

## 3 点简述
- 核心问题：平滑稳定性假设（如梯度Lipschitzness）在ReLU非线性下全局不成立，导致经典稳定性分析失效
- 方法要点：通过具体反例证明失效，并识别最小广义导数条件以恢复稳定性陈述
- 实验或效果：在简单设置中展示训练轨迹经验稳定，但平滑近似可能误导，需非光滑感知方法

## 摘要（原文）

> Stability analyses of modern learning systems are frequently derived under smoothness assumptions that are violated by ReLU-type nonlinearities. In this note, we isolate a minimal obstruction by showing that no uniform smoothness-based stability proxy such as gradient Lipschitzness or Hessian control can hold globally for ReLU networks, even in simple settings where training trajectories appear empirically stable. We give a concrete counterexample demonstrating the failure of classical stability bounds and identify a minimal generalized derivative condition under which stability statements can be meaningfully restored. The result clarifies why smooth approximations of ReLU can be misleading and motivates nonsmooth-aware stability frameworks.

