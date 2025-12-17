---
layout: default
title: Physically consistent model learning for reaction-diffusion systems
---

# Physically consistent model learning for reaction-diffusion systems
**arXiv**：[2512.14240v1](https://arxiv.org/abs/2512.14240) · [PDF](https://arxiv.org/pdf/2512.14240.pdf)  
**作者**：Erion Morina, Martin Holler  

**一句话要点**：提出物理一致的反应-扩散系统模型学习方法，确保质量守恒和准正性

**关键词**：反应-扩散系统, 物理一致性学习, 正则化模型学习, 质量守恒, 准正性, 数据驱动建模

## 3 点简述
- 核心问题：从数据学习反应-扩散系统时，如何保证物理一致性和适定性
- 方法要点：通过正则化框架修改参数化反应项，强制质量守恒和准正性
- 实验或效果：理论证明学习解收敛于正则化最小化解，提供准正函数近似结果

## 摘要（原文）

> This paper addresses the problem of learning reaction-diffusion (RD) systems from data while ensuring physical consistency and well-posedness of the learned models. Building on a regularization-based framework for structured model learning, we focus on learning parameterized reaction terms and investigate how to incorporate key physical properties, such as mass conservation and quasipositivity, directly into the learning process. Our main contributions are twofold: First, we propose techniques to systematically modify a given class of parameterized reaction terms such that the resulting terms inherently satisfy mass conservation and quasipositivity, ensuring that the learned RD systems preserve non-negativity and adhere to physical principles. These modifications also guarantee well-posedness of the resulting PDEs under additional regularity and growth conditions. Second, we extend existing theoretical results on regularization-based model learning to RD systems using these physically consistent reaction terms. Specifically, we prove that solutions to the learning problem converge to a unique, regularization-minimizing solution of a limit system even when conservation laws and quasipositivity are enforced. In addition, we provide approximation results for quasipositive functions, essential for constructing physically consistent parameterizations. These results advance the development of interpretable and reliable data-driven models for RD systems that align with fundamental physical laws.

