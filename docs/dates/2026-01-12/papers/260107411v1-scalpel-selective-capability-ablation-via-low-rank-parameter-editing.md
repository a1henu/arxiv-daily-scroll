---
layout: default
title: SCALPEL: Selective Capability Ablation via Low-rank Parameter Editing for Large Language Model Interpretability Analysis
---

# SCALPEL: Selective Capability Ablation via Low-rank Parameter Editing for Large Language Model Interpretability Analysis
**arXiv**：[2601.07411v1](https://arxiv.org/abs/2601.07411) · [PDF](https://arxiv.org/pdf/2601.07411.pdf)  
**作者**：Zihao Fu, Xufeng Duan, Zhenguang G. Cai  

**一句话要点**：提出SCALPEL框架，通过低秩参数编辑实现大语言模型能力的选择性消融以提升可解释性分析

**关键词**：大语言模型可解释性, 能力消融, 低秩参数编辑, LoRA适配器, 参数空间分析

## 3 点简述
- 核心问题：传统方法将能力映射到离散模块，无法捕捉细粒度、分布式的编码，限制了对大语言模型内部机制的理解。
- 方法要点：将能力表示为跨层和模块分布的低秩参数子空间，通过训练LoRA适配器实现精确能力移除而不影响其他能力。
- 实验或效果：在BLiMP任务上验证，SCALPEL能成功移除目标能力并保留通用能力，揭示能力在参数空间中的低秩结构分布。

## 摘要（原文）

> Large language models excel across diverse domains, yet their deployment in healthcare, legal systems, and autonomous decision-making remains limited by incomplete understanding of their internal mechanisms. As these models integrate into high-stakes systems, understanding how they encode capabilities has become fundamental to interpretability research. Traditional approaches identify important modules through gradient attribution or activation analysis, assuming specific capabilities map to specific components. However, this oversimplifies neural computation: modules may contribute to multiple capabilities simultaneously, while single capabilities may distribute across multiple modules. These coarse-grained analyses fail to capture fine-grained, distributed capability encoding. We present SCALPEL (Selective Capability Ablation via Low-rank Parameter Editing for Large language models), a framework representing capabilities as low-rank parameter subspaces rather than discrete modules. Our key insight is that capabilities can be characterized by low-rank modifications distributed across layers and modules, enabling precise capability removal without affecting others. By training LoRA adapters to reduce distinguishing correct from incorrect answers while preserving general language modeling quality, SCALPEL identifies low-rank representations responsible for particular capabilities while remaining disentangled from others. Experiments across diverse capability and linguistic tasks from BLiMP demonstrate that SCALPEL successfully removes target capabilities while preserving general capabilities, providing fine-grained insights into capability distribution across parameter space. Results reveal that capabilities exhibit low-rank structure and can be selectively ablated through targeted parameter-space interventions, offering nuanced understanding of capability encoding in LLMs.

