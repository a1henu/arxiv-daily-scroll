---
layout: default
title: REASON: Accelerating Probabilistic Logical Reasoning for Scalable Neuro-Symbolic Intelligence
---

# REASON: Accelerating Probabilistic Logical Reasoning for Scalable Neuro-Symbolic Intelligence
**arXiv**：[2601.20784v1](https://arxiv.org/abs/2601.20784) · [PDF](https://arxiv.org/pdf/2601.20784.pdf)  
**作者**：Zishen Wan, Che-Kai Liu, Jiayi Qian, Hanchen Yang, Arijit Raychowdhury, Tushar Krishna  

**一句话要点**：提出REASON加速框架以解决神经符号AI中概率逻辑推理的效率瓶颈

**关键词**：神经符号AI, 概率逻辑推理, 硬件加速, 能效优化, 可重构架构, 推理加速

## 3 点简述
- 核心问题：概率逻辑推理在CPU和GPU上存在控制流不规则、算术强度低等效率瓶颈
- 方法要点：采用统一有向无环图表示，结合自适应剪枝和可重构树基处理架构
- 实验或效果：在TSMC 28 nm节点下，相比GPU实现12-50倍加速和310-681倍能效提升

## 摘要（原文）

> Neuro-symbolic AI systems integrate neural perception with symbolic reasoning to enable data-efficient, interpretable, and robust intelligence beyond purely neural models. Although this compositional paradigm has shown superior performance in domains such as reasoning, planning, and verification, its deployment remains challenging due to severe inefficiencies in symbolic and probabilistic inference. Through systematic analysis of representative neuro-symbolic workloads, we identify probabilistic logical reasoning as the inefficiency bottleneck, characterized by irregular control flow, low arithmetic intensity, uncoalesced memory accesses, and poor hardware utilization on CPUs and GPUs.
>   This paper presents REASON, an integrated acceleration framework for probabilistic logical reasoning in neuro-symbolic AI. REASON introduces a unified directed acyclic graph representation that captures common structure across symbolic and probabilistic models, coupled with adaptive pruning and regularization. At the architecture level, REASON features a reconfigurable, tree-based processing fabric optimized for irregular traversal, symbolic deduction, and probabilistic aggregation. At the system level, REASON is tightly integrated with GPU streaming multiprocessors through a programmable interface and multi-level pipeline that efficiently orchestrates compositional execution. Evaluated across six neuro-symbolic workloads, REASON achieves 12-50x speedup and 310-681x energy efficiency over desktop and edge GPUs under TSMC 28 nm node. REASON enables real-time probabilistic logical reasoning, completing end-to-end tasks in 0.8 s with 6 mm2 area and 2.12 W power, demonstrating that targeted acceleration of probabilistic logical reasoning is critical for practical and scalable neuro-symbolic AI and positioning REASON as a foundational system architecture for next-generation cognitive intelligence.

