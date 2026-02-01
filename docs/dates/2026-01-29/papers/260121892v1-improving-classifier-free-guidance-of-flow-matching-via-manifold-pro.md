---
layout: default
title: Improving Classifier-Free Guidance of Flow Matching via Manifold Projection
---

# Improving Classifier-Free Guidance of Flow Matching via Manifold Projection
**arXiv**：[2601.21892v1](https://arxiv.org/abs/2601.21892) · [PDF](https://arxiv.org/pdf/2601.21892.pdf)  
**作者**：Jian-Feng Cai, Haixia Liu, Zhengyi Su, Chao Wang  

**一句话要点**：提出基于流形投影的优化方法以改进流匹配中的无分类器引导

**关键词**：流匹配, 无分类器引导, 流形投影, 优化理论, 可控生成, Anderson加速

## 3 点简述
- 核心问题：无分类器引导依赖启发式线性外推，对引导尺度敏感，缺乏理论依据
- 方法要点：从优化视角解释引导，将采样重构为带流形约束的同伦优化，引入增量梯度下降和Anderson加速
- 实验或效果：训练无关方法，在DiT-XL-2-256等模型上验证，提升生成保真度、提示对齐和鲁棒性

## 摘要（原文）

> Classifier-free guidance (CFG) is a widely used technique for controllable generation in diffusion and flow-based models. Despite its empirical success, CFG relies on a heuristic linear extrapolation that is often sensitive to the guidance scale. In this work, we provide a principled interpretation of CFG through the lens of optimization. We demonstrate that the velocity field in flow matching corresponds to the gradient of a sequence of smoothed distance functions, which guides latent variables toward the scaled target image set. This perspective reveals that the standard CFG formulation is an approximation of this gradient, where the prediction gap, the discrepancy between conditional and unconditional outputs, governs guidance sensitivity. Leveraging this insight, we reformulate the CFG sampling as a homotopy optimization with a manifold constraint. This formulation necessitates a manifold projection step, which we implement via an incremental gradient descent scheme during sampling. To improve computational efficiency and stability, we further enhance this iterative process with Anderson Acceleration without requiring additional model evaluations. Our proposed methods are training-free and consistently refine generation fidelity, prompt alignment, and robustness to the guidance scale. We validate their effectiveness across diverse benchmarks, demonstrating significant improvements on large-scale models such as DiT-XL-2-256, Flux, and Stable Diffusion 3.5.

