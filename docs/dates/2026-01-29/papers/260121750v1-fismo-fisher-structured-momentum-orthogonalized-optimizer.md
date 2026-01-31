---
layout: default
title: FISMO: Fisher-Structured Momentum-Orthogonalized Optimizer
---

# FISMO: Fisher-Structured Momentum-Orthogonalized Optimizer
**arXiv**：[2601.21750v1](https://arxiv.org/abs/2601.21750) · [PDF](https://arxiv.org/pdf/2601.21750.pdf)  
**作者**：Chenrui Xu, Wenjing Yan, Ying-Jun Angela Zhang  

**一句话要点**：提出FISMO优化器，通过Fisher信息几何平衡各向同性与曲率信息，提升大规模神经网络训练效率。

**关键词**：优化器设计, Fisher信息几何, 结构化预条件, 非凸优化, 神经网络训练

## 3 点简述
- 核心问题：现有优化器如Muon强制各向同性更新，可能忽略梯度谱中的曲率信息，影响训练性能。
- 方法要点：FISMO基于Kronecker分解的Fisher度量，将更新重构为信任域问题，实现结构化预条件，适应局部损失几何。
- 实验或效果：在图像分类和语言建模基准测试中，FISMO相比基线方法展现出更优的训练效率和最终性能。

## 摘要（原文）

> Training large-scale neural networks requires solving nonconvex optimization where the choice of optimizer fundamentally determines both convergence behavior and computational efficiency. While adaptive methods like Adam have long dominated practice, the recently proposed Muon optimizer achieves superior performance through orthogonalized momentum updates that enforce isotropic geometry with uniform singular values. However, this strict isotropy discards potentially valuable curvature information encoded in gradient spectra, motivating optimization methods that balance geometric structure with adaptivity. We introduce FISMO (Fisher-Structured Momentum-Orthogonalized) optimizer, which generalizes isotropic updates to incorporate anisotropic curvature information through Fisher information geometry. By reformulating the optimizer update as a trust-region problem constrained by a Kronecker-factored Fisher metric, FISMO achieves structured preconditioning that adapts to local loss landscape geometry while maintaining computational tractability. We establish convergence guarantees for FISMO in stochastic nonconvex settings, proving an $\mathcal{O}(1/\sqrt{T})$ rate for the expected squared gradient norm with explicit characterization of variance reduction through mini-batching. Empirical evaluation on image classification and language modeling benchmarks demonstrates that FISMO achieves superior training efficiency and final performance compared to established baselines.

