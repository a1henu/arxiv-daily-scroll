---
layout: default
title: Thermodynamic Isomorphism of Transformers: A Lagrangian Approach to Attention Dynamics
---

# Thermodynamic Isomorphism of Transformers: A Lagrangian Approach to Attention Dynamics
**arXiv**：[2602.08216v1](https://arxiv.org/abs/2602.08216) · [PDF](https://arxiv.org/pdf/2602.08216.pdf)  
**作者**：Gunn Kim  

**一句话要点**：提出基于拉格朗日方法的Transformer热力学同构理论，以物理原理统一解释注意力机制。

**关键词**：Transformer理论, 注意力机制, 信息热力学, 拉格朗日方法, 统计物理, 深度学习

## 3 点简述
- 核心问题：Transformer机制缺乏统一物理理论，依赖启发式设计。
- 方法要点：将信息状态映射到黎曼流形，推导智能拉格朗日量，建立信息热力学第一定律。
- 实验或效果：理论解释缩放定律、涌现现象和RoPE，连接统计物理与深度学习。

## 摘要（原文）

> Although the Transformer architecture has revolutionized artificial intelligence, its underlying mechanisms remain largely heuristic and lack a unified physical theory. In this work, we propose a first-principles framework for information dynamics, treating the attention mechanism as a physical system governed by the principle of least action rather than as an algorithmic optimization. By mapping information states to a Riemannian manifold with the Fisher information metric, we derive the intelligence Lagrangian. We show that the softmax function corresponds to the unique thermodynamic equilibrium state that minimizes the Helmholtz free energy of the information gas. In addition, we identify the query-key interaction as an electrodynamic coupling between an external field and an intrinsic dipole moment. This theory establishes the first law of information thermodynamics, unifying inference (mechanical work) and learning (chemical evolution). It also explains emergent phenomena, such as scaling laws and grokking, as phase transitions characterized by the divergence of specific heat. Finally, we discuss how rotational symmetry breaking in the attention manifold generates massless Goldstone bosons, providing a field-theoretic perspective on rotary positional embeddings (RoPE). Our work connects Statistical Physics and Deep Learning, laying the groundwork for a general theory of physics-based intelligence.

