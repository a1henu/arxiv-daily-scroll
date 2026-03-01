---
layout: default
title: Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement
---

# Accelerating LLM Pre-Training through Flat-Direction Dynamics Enhancement
**arXiv**：[2602.22681v1](https://arxiv.org/abs/2602.22681) · [PDF](https://arxiv.org/pdf/2602.22681.pdf)  
**作者**：Shuchen Zhu, Rizhen Hu, Mingze Wang, Mou Sun, Xue Wang, Kun Yuan, Zaiwen Wen  

**一句话要点**：提出LITE策略以加速大语言模型预训练，通过增强平坦方向动态提升优化器效率。

**关键词**：大语言模型预训练, 优化器加速, 黎曼几何, 各向异性优化, Hessian阻尼, 平坦方向动态

## 3 点简述
- 核心问题：大语言模型预训练计算成本高，优化器需高效处理高度各向异性的损失景观。
- 方法要点：基于黎曼ODE框架，LITE通过增大平坦方向的Hessian阻尼系数和学习率来加速训练动态。
- 实验或效果：LITE显著加速Muon和SOAP优化器，在多种架构、参数规模和数据集上验证了其有效性。

## 摘要（原文）

> Pre-training Large Language Models requires immense computational resources, making optimizer efficiency essential. The optimization landscape is highly anisotropic, with loss reduction driven predominantly by progress along flat directions. While matrix-based optimizers such as Muon and SOAP leverage fine-grained curvature information to outperform AdamW, their updates tend toward isotropy -- relatively conservative along flat directions yet potentially aggressive along sharp ones. To address this limitation, we first establish a unified Riemannian Ordinary Differential Equation (ODE) framework that elucidates how common adaptive algorithms operate synergistically: the preconditioner induces a Riemannian geometry that mitigates ill-conditioning, while momentum serves as a Riemannian damping term that promotes convergence. Guided by these insights, we propose LITE, a generalized acceleration strategy that enhances training dynamics by applying larger Hessian damping coefficients and learning rates along flat trajectories. Extensive experiments demonstrate that LITE significantly accelerates both Muon and SOAP across diverse architectures (Dense, MoE), parameter scales (130M--1.3B), datasets (C4, Pile), and learning-rate schedules (cosine, warmup-stable-decay). Theoretical analysis confirms that LITE facilitates faster convergence along flat directions in anisotropic landscapes, providing a principled approach to efficient LLM pre-training. The code is available at https://github.com/SHUCHENZHU/LITE.

