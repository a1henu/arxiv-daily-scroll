---
layout: default
title: The Implicit Bias of Steepest Descent with Mini-batch Stochastic Gradient
---

# The Implicit Bias of Steepest Descent with Mini-batch Stochastic Gradient
**arXiv**：[2602.11557v1](https://arxiv.org/abs/2602.11557) · [PDF](https://arxiv.org/pdf/2602.11557.pdf)  
**作者**：Jichu Li, Xuan Tang, Difan Zou  

**一句话要点**：分析小批量随机最速下降的隐式偏差，揭示动量与方差缩减对极限最大间隔行为的影响

**关键词**：随机优化, 隐式偏差, 最速下降, 动量方法, 方差缩减, 最大间隔分类

## 3 点简述
- 研究多类分类中小批量随机最速下降的隐式偏差，关注批量大小、动量和方差缩减的作用
- 证明无动量时仅大批量收敛，动量通过批量-动量权衡实现小批量收敛但减慢速度
- 方差缩减可恢复全批量隐式偏差但收敛更慢，并通过数据示例揭示无动量单批量更新的不同偏差

## 摘要（原文）

> A variety of widely used optimization methods like SignSGD and Muon can be interpreted as instances of steepest descent under different norm-induced geometries. In this work, we study the implicit bias of mini-batch stochastic steepest descent in multi-class classification, characterizing how batch size, momentum, and variance reduction shape the limiting max-margin behavior and convergence rates under general entry-wise and Schatten-$p$ norms. We show that without momentum, convergence only occurs with large batches, yielding a batch-dependent margin gap but the full-batch convergence rate. In contrast, momentum enables small-batch convergence through a batch-momentum trade-off, though it slows convergence. This approach provides fully explicit, dimension-free rates that improve upon prior results. Moreover, we prove that variance reduction can recover the exact full-batch implicit bias for any batch size, albeit at a slower convergence rate. Finally, we further investigate the batch-size-one steepest descent without momentum, and reveal its convergence to a fundamentally different bias via a concrete data example, which reveals a key limitation of purely stochastic updates. Overall, our unified analysis clarifies when stochastic optimization aligns with full-batch behavior, and paves the way for perform deeper explorations of the training behavior of stochastic gradient steepest descent algorithms.

