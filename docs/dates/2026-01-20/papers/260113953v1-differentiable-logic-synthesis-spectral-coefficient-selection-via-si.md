---
layout: default
title: Differentiable Logic Synthesis: Spectral Coefficient Selection via Sinkhorn-Constrained Composition
---

# Differentiable Logic Synthesis: Spectral Coefficient Selection via Sinkhorn-Constrained Composition
**arXiv**：[2601.13953v1](https://arxiv.org/abs/2601.13953) · [PDF](https://arxiv.org/pdf/2601.13953.pdf)  
**作者**：Gorgi Pavlov  

**一句话要点**：提出可微分逻辑合成方法，通过Sinkhorn约束组合选择谱系数以解决布尔逻辑学习中的量化退化问题。

**关键词**：可微分逻辑合成, 谱系数选择, Sinkhorn约束, 布尔逻辑学习, 神经符号合成, 硬件效率

## 3 点简述
- 核心问题：神经网络学习布尔逻辑时易收敛到模糊近似，量化后性能下降。
- 方法要点：采用分层谱组合架构，从冻结布尔傅里叶基选择谱系数，通过Sinkhorn约束路由和列符号调制进行组合。
- 实验效果：在n=2至4变量操作中验证，梯度下降和谱合成方法实现高精度，支持硬件高效神经符号逻辑合成。

## 摘要（原文）

> Learning precise Boolean logic via gradient descent remains challenging: neural networks typically converge to "fuzzy" approximations that degrade under quantization. We introduce Hierarchical Spectral Composition, a differentiable architecture that selects spectral coefficients from a frozen Boolean Fourier basis and composes them via Sinkhorn-constrained routing with column-sign modulation. Our approach draws on recent insights from Manifold-Constrained Hyper-Connections (mHC), which demonstrated that projecting routing matrices onto the Birkhoff polytope preserves identity mappings and stabilizes large-scale training. We adapt this framework to logic synthesis, adding column-sign modulation to enable Boolean negation -- a capability absent in standard doubly stochastic routing.
>   We validate our approach across four phases of increasing complexity: (1) For n=2 (16 Boolean operations over 4-dim basis), gradient descent achieves 100% accuracy with zero routing drift and zero-loss quantization to ternary masks. (2) For n=3 (10 three-variable operations), gradient descent achieves 76% accuracy, but exhaustive enumeration over 3^8 = 6561 configurations proves that optimal ternary masks exist for all operations (100% accuracy, 39% sparsity). (3) For n=4 (10 four-variable operations over 16-dim basis), spectral synthesis -- combining exact Walsh-Hadamard coefficients, ternary quantization, and MCMC refinement with parallel tempering -- achieves 100% accuracy on all operations. This progression establishes (a) that ternary polynomial threshold representations exist for all tested functions, and (b) that finding them requires methods beyond pure gradient descent as dimensionality grows. All operations enable single-cycle combinational logic inference at 10,959 MOps/s on GPU, demonstrating viability for hardware-efficient neuro-symbolic logic synthesis.

