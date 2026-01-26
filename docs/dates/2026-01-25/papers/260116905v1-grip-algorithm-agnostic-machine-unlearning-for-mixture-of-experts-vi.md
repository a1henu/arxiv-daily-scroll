---
layout: default
title: GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints
---

# GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints
**arXiv**：[2601.16905v1](https://arxiv.org/abs/2601.16905) · [PDF](https://arxiv.org/pdf/2601.16905.pdf)  
**作者**：Andy Zhu, Rongzhe Wei, Yupu Gu, Pan Li  

**一句话要点**：提出GRIP框架以解决混合专家模型中的机器遗忘问题

**关键词**：机器遗忘, 混合专家模型, 路由约束, 几何优化, 算法无关框架

## 3 点简述
- 核心问题：传统遗忘方法利用MoE路由漏洞，导致模型效用损失和表面遗忘
- 方法要点：通过几何路由不变性约束，将梯度更新投影到专家特定零空间
- 实验或效果：在大型MoE模型中实现超过95%的路由稳定性，保持模型效用

## 摘要（原文）

> Machine unlearning (MU) for large language models has become critical for AI safety, yet existing methods fail to generalize to Mixture-of-Experts (MoE) architectures. We identify that traditional unlearning methods exploit MoE's architectural vulnerability: they manipulate routers to redirect queries away from knowledgeable experts rather than erasing knowledge, causing a loss of model utility and superficial forgetting. We propose Geometric Routing Invariance Preservation (GRIP), an algorithm-agnostic framework for unlearning for MoE. Our core contribution is a geometric constraint, implemented by projecting router gradient updates into an expert-specific null-space. Crucially, this decouples routing stability from parameter rigidity: while discrete expert selections remain stable for retained knowledge, the continuous router parameters remain plastic within the null space, allowing the model to undergo necessary internal reconfiguration to satisfy unlearning objectives. This forces the unlearning optimization to erase knowledge directly from expert parameters rather than exploiting the superficial router manipulation shortcut. GRIP functions as an adapter, constraining router parameter updates without modifying the underlying unlearning algorithm. Extensive experiments on large-scale MoE models demonstrate that our adapter eliminates expert selection shift (achieving over 95% routing stability) across all tested unlearning methods while preserving their utility. By preventing existing algorithms from exploiting MoE model's router vulnerability, GRIP adapts existing unlearning research from dense architectures to MoEs.

