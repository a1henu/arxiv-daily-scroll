---
layout: default
title: Avoiding Premature Collapse: Adaptive Annealing for Entropy-Regularized Structural Inference
---

# Avoiding Premature Collapse: Adaptive Annealing for Entropy-Regularized Structural Inference
**arXiv**：[2601.23039v1](https://arxiv.org/abs/2601.23039) · [PDF](https://arxiv.org/pdf/2601.23039.pdf)  
**作者**：Yizhi Liu  

**一句话要点**：提出自适应退火算法以解决熵正则化结构推断中的早熟模式崩溃问题

**关键词**：熵正则化最优传输, 结构推断, 自适应退火, 早熟模式崩溃, Sinkhorn算法, 热力学速度限制

## 3 点简述
- 核心问题：熵正则化最优传输在退火过程中因热力学速度限制导致早熟模式崩溃，使推断不稳定
- 方法要点：提出Efficient PH-ASC算法，通过监控推断稳定性并实施线性稳定性定律，自适应调整退火计划
- 实验或效果：算法将开销从O(N^3)降低到摊销O(1)，提供开源实现和交互演示验证有效性

## 摘要（原文）

> Differentiable matching layers, often implemented via entropy-regularized Optimal Transport, serve as a critical approximate inference mechanism in structural prediction. However, recovering discrete permutations via annealing $ε\to 0$ is notoriously unstable. We identify a fundamental mechanism for this failure: \textbf{Premature Mode Collapse}. By analyzing the non-normal dynamics of the Sinkhorn fixed-point map, we reveal a theoretical \textbf{thermodynamic speed limit}. Under standard exponential cooling, the shift in the target posterior ($O(1)$) outpaces the contraction rate of the inference operator, which degrades as $O(1/ε)$. This mismatch inevitably forces the inference trajectory into spurious local basins. To address this, we propose \textbf{Efficient PH-ASC}, an adaptive scheduling algorithm that monitors the stability of the inference process. By enforcing a linear stability law, we decouple expensive spectral diagnostics from the training loop, reducing overhead from $O(N^3)$ to amortized $O(1)$. Our implementation and interactive demo are available at https://github.com/xxx0438/torch-sinkhorn-asc and https://huggingface.co/spaces/leon0923/torch-sinkhorn-asc-demo. bounded away from zero in generic training dynamics unless the feature extractor converges unrealistically fast.

