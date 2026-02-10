---
layout: default
title: ARO: A New Lens On Matrix Optimization For Large Models
---

# ARO: A New Lens On Matrix Optimization For Large Models
**arXiv**：[2602.09006v1](https://arxiv.org/abs/2602.09006) · [PDF](https://arxiv.org/pdf/2602.09006.pdf)  
**作者**：Wenbo Gong, Javier Zazo, Qijun Luo, Puqian Wang, James Hensman, Chao Ma  

**一句话要点**：提出自适应旋转优化框架ARO，通过梯度旋转提升大语言模型训练效率

**关键词**：矩阵优化, 大语言模型训练, 梯度旋转, 自适应优化, 训练效率, 对称性优化

## 3 点简述
- 核心问题：现有基于正交化/白化的矩阵优化方法是否可被超越，以进一步推动大模型训练效率前沿
- 方法要点：ARO将梯度旋转作为核心设计原则，在旋转坐标系中执行范数最速下降，基于新范数策略确定旋转
- 实验或效果：在严格基准协议下，ARO在8B参数规模预训练中优于AdamW和正交化方法，未见收益递减

## 摘要（原文）

> Matrix-based optimizers have attracted growing interest for improving LLM training efficiency, with significant progress centered on orthogonalization/whitening based methods. While yielding substantial performance gains, a fundamental question arises: can we develop new paradigms beyond orthogonalization, pushing the efficiency frontier further? We present \textbf{Adaptively Rotated Optimization (ARO}, a new matrix optimization framework that treats gradient rotation as a first class design principle. ARO accelerates LLM training by performing normed steepest descent in a rotated coordinate system, where the rotation is determined by a novel norm-informed policy. This perspective yields update rules that go beyond existing orthogonalization and whitening optimizers, improving sample efficiency in practice. To make comparisons reliable, we propose a rigorously controlled benchmarking protocol that reduces confounding and bias. Under this protocol, ARO consistently outperforms AdamW (by 1.3 $\sim$1.35$\times$) and orthogonalization methods (by 1.1$\sim$1.15$\times$) in LLM pretraining at up to 8B activated parameters, and up to $8\times$ overtrain budget, without evidence of diminishing returns. Finally, we discuss how ARO can be reformulated as a symmetry-aware optimizer grounded in rotational symmetries of residual streams, motivating advanced designs that enable computationally efficient exploitation of cross-layer/cross module couplings.

