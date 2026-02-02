---
layout: default
title: Solving Inverse Problems with Flow-based Models via Model Predictive Control
---

# Solving Inverse Problems with Flow-based Models via Model Predictive Control
**arXiv**：[2601.23231v1](https://arxiv.org/abs/2601.23231) · [PDF](https://arxiv.org/pdf/2601.23231.pdf)  
**作者**：George Webber, Alexander Denker, Riccardo Barbano, Andrew J Reader  

**一句话要点**：提出MPC-Flow框架，通过模型预测控制解决基于流模型的逆问题

**关键词**：流模型, 逆问题求解, 模型预测控制, 条件生成, 图像修复, 无训练引导

## 3 点简述
- 核心问题：流模型在逆问题中无条件先验强，但条件生成引导困难且计算成本高
- 方法要点：将逆问题转化为序列控制子问题，避免轨迹优化中的反向传播或伴随求解
- 实验或效果：在图像修复任务中表现优异，可无训练引导大规模模型如FLUX.2

## 摘要（原文）

> Flow-based generative models provide strong unconditional priors for inverse problems, but guiding their dynamics for conditional generation remains challenging. Recent work casts training-free conditional generation in flow models as an optimal control problem; however, solving the resulting trajectory optimisation is computationally and memory intensive, requiring differentiation through the flow dynamics or adjoint solves. We propose MPC-Flow, a model predictive control framework that formulates inverse problem solving with flow-based generative models as a sequence of control sub-problems, enabling practical optimal control-based guidance at inference time. We provide theoretical guarantees linking MPC-Flow to the underlying optimal control objective and show how different algorithmic choices yield a spectrum of guidance algorithms, including regimes that avoid backpropagation through the generative model trajectory. We evaluate MPC-Flow on benchmark image restoration tasks, spanning linear and non-linear settings such as in-painting, deblurring, and super-resolution, and demonstrate strong performance and scalability to massive state-of-the-art architectures via training-free guidance of FLUX.2 (32B) in a quantised setting on consumer hardware.

