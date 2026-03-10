---
layout: default
title: Fibration Policy Optimization
---

# Fibration Policy Optimization
**arXiv**：[2603.08239v1](https://arxiv.org/abs/2603.08239) · [PDF](https://arxiv.org/pdf/2603.08239.pdf)  
**作者**：Chang Li, Tshihao Tsu, Yaren Zhang, Chao Xue, Xiaodong He  

**一句话要点**：提出FiberPO框架，通过纤维束门控和聚合策略审查目标，解决LLM多尺度稳定性控制问题。

**关键词**：大语言模型优化, 多尺度稳定性控制, 纤维束门控, 聚合策略审查, 信任区域理论, 层次门控

## 3 点简述
- 核心问题：现有近端目标缺乏多尺度耦合机制，无法统一控制令牌级、轨迹级和高层次稳定性。
- 方法要点：基于APC-Obj和FBG，推导FiberPO目标，其雅可比矩阵块对角化，在策略上简化为恒等映射。
- 实验或效果：FiberPO提供更好的更新方向，提高令牌效率，并通过FGH扩展到任意层次深度，如四层实例FiberPO-Domain。

## 摘要（原文）

> Large language models are increasingly trained as heterogeneous systems spanning multiple domains, expert partitions, and agentic pipelines, yet prevalent proximal objectives operate at a single scale and lack a principled mechanism for coupling token-level, trajectory-level, and higher-level hierarchical stability control. To bridge this gap, we derive the Aggregational Policy Censoring Objective (APC-Obj), the first exact unconstrained reformulation of sample-based TV-TRPO, establishing that clipping-based surrogate design and trust-region optimization are dual formulations of the same problem. Building on this foundation, we develop Fiber Bundle Gating (FBG), an algebraic framework that organizes sampled RL data as a fiber bundle and decomposes ratio gating into a base-level gate on trajectory aggregates and a fiber-level gate on per-token residuals, with provable first-order agreement with the true RL objective near on-policy. From APC-Obj and FBG we derive Fibration Policy Optimization (or simply, FiberPO), a concrete objective whose Jacobian is block-diagonal over trajectories, reduces to identity at on-policy, and provides better update direction thus improving token efficiency. The compositional nature of the framework extends beyond the trajectory-token case: fibrations compose algebraically into a Fibration Gating Hierarchy (FGH) that scales the same gating mechanism to arbitrary hierarchical depth without new primitives, as demonstrated by FiberPO-Domain, a four-level instantiation with independent trust-region budgets at the domain, prompt group, trajectory, and token levels. Together, these results connect the trust-region theory, a compositional algebraic structure, and practical multi-scale stability control into a unified framework for LLM policy optimization.

