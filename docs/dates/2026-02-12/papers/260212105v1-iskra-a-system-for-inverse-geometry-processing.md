---
layout: default
title: Iskra: A System for Inverse Geometry Processing
---

# Iskra: A System for Inverse Geometry Processing
**arXiv**：[2602.12105v1](https://arxiv.org/abs/2602.12105) · [PDF](https://arxiv.org/pdf/2602.12105.pdf)  
**作者**：Ana Dodik, Ahmed H. Mahmoud, Justin Solomon  

**一句话要点**：提出Iskra系统以通过几何处理算法进行微分，支持逆几何处理应用。

**关键词**：逆几何处理, 几何算法微分, 伴随方法, 机器学习框架兼容, 局部-全局求解器, ADMM求解器

## 3 点简述
- 核心问题：如何高效微分几何处理算法，避免重新实现。
- 方法要点：结合散射-聚集方法与张量工作流，利用伴随方法生成高效反向传播。
- 实验效果：在平均曲率流、谱共形参数化等应用中验证低实现成本、快速运行和低内存需求。

## 摘要（原文）

> We propose a system for differentiating through solutions to geometry processing problems. Our system differentiates a broad class of geometric algorithms, exploiting existing fast problem-specific schemes common to geometry processing, including local-global and ADMM solvers. It is compatible with machine learning frameworks, opening doors to new classes of inverse geometry processing applications. We marry the scatter-gather approach to mesh processing with tensor-based workflows and rely on the adjoint method applied to user-specified imperative code to generate an efficient backward pass behind the scenes. We demonstrate our approach by differentiating through mean curvature flow, spectral conformal parameterization, geodesic distance computation, and as-rigid-as-possible deformation, examining usability and performance on these applications. Our system allows practitioners to differentiate through existing geometry processing algorithms without needing to reformulate them, resulting in low implementation effort, fast runtimes, and lower memory requirements than differentiable optimization tools not tailored to geometry processing.

