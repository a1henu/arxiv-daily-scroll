---
layout: default
title: Correction of Transformer-Based Models with Smoothing Pseudo-Projector
---

# Correction of Transformer-Based Models with Smoothing Pseudo-Projector
**arXiv**：[2603.09815v1](https://arxiv.org/abs/2603.09815) · [PDF](https://arxiv.org/pdf/2603.09815.pdf)  
**作者**：Vitaly Bulgakov  

**一句话要点**：提出伪投影器以提升基于Transformer模型的鲁棒性和训练动态

**关键词**：伪投影器, Transformer模型, 鲁棒性增强, 训练动态优化, 代数多重网格, 文本分类

## 3 点简述
- 核心问题：模型对标签无关输入噪声敏感，影响训练稳定性和泛化能力。
- 方法要点：引入轻量级伪投影器，基于代数多重网格思想，抑制噪声诱导方向，无需改变核心架构。
- 实验或效果：在文本分类和合成基准测试中，有效改善训练行为，未观察到负面影响。

## 摘要（原文）

> The pseudo-projector is a lightweight modification that can be integrated into existing language models and other neural networks without altering their core architecture. It can be viewed as a hidden-representation corrector that reduces sensitivity to noise by suppressing directions induced by label-irrelevant input content. The design is inspired by the multigrid (MG) paradigm, originally developed to accelerate the convergence of iterative solvers for partial differential equations and boundary value problems, and later extended to more general linear systems through algebraic multigrid methods. We refer to the method as a pseudo-projector because its linear prototype corresponds to a strictly idempotent orthogonal projector, whereas the practical formulation employs learnable restriction and prolongation operators and therefore does not, in general, satisfy the properties of an exact orthogonal projection. We evaluate the proposed approach on transformer-based text classification tasks, as well as controlled synthetic benchmarks, demonstrating its effectiveness in improving training dynamics and robustness. Experimental results, together with supporting theoretical heuristics, indicate consistent improvements in training behavior across a range of settings, with no adverse effects observed otherwise. Our next step will be to extend this approach to language models.

