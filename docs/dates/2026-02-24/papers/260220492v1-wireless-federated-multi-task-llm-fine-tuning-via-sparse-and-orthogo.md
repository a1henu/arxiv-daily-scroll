---
layout: default
title: Wireless Federated Multi-Task LLM Fine-Tuning via Sparse-and-Orthogonal LoRA
---

# Wireless Federated Multi-Task LLM Fine-Tuning via Sparse-and-Orthogonal LoRA
**arXiv**：[2602.20492v1](https://arxiv.org/abs/2602.20492) · [PDF](https://arxiv.org/pdf/2602.20492.pdf)  
**作者**：Nuocheng Yang, Sihua Wang, Ouwen Huan, Mingzhe Chen, Tony Q. S. Quek, Changchuan Yin  

**一句话要点**：提出稀疏正交LoRA与聚类拓扑设计，以解决无线联邦多任务LLM微调中的知识遗忘与通信效率问题。

**关键词**：联邦学习, 低秩适应, 多任务学习, 无线通信, 模型聚合, 知识干扰

## 3 点简述
- 核心问题：异构数据导致更新冲突、通信冗余和知识干扰，影响联邦学习性能。
- 方法要点：采用稀疏正交LoRA消除方向冲突，聚类拓扑优化聚合，隐式MoE避免推理干扰。
- 实验或效果：相比传统LoRA，通信资源消耗减少73%，平均性能提升5%。

## 摘要（原文）

> Decentralized federated learning (DFL) based on low-rank adaptation (LoRA) enables mobile devices with multi-task datasets to collaboratively fine-tune a large language model (LLM) by exchanging locally updated parameters with a subset of neighboring devices via wireless connections for knowledge integration.However, directly aggregating parameters fine-tuned on heterogeneous datasets induces three primary issues across the DFL life-cycle: (i) \textit{catastrophic knowledge forgetting during fine-tuning process}, arising from conflicting update directions caused by data heterogeneity; (ii) \textit{inefficient communication and convergence during model aggregation process}, due to bandwidth-intensive redundant model transmissions; and (iii) \textit{multi-task knowledge interference during inference process}, resulting from incompatible knowledge representations coexistence during inference. To address these issues in a fully decentralized scenario, we first propose a sparse-and-orthogonal LoRA that ensures orthogonality between model updates to eliminate direction conflicts during fine-tuning.Then, we analyze how device connection topology affects multi-task performance, prompting a cluster-based topology design during aggregation.Finally, we propose an implicit mixture of experts (MoE) mechanism to avoid the coexistence of incompatible knowledge during inference. Simulation results demonstrate that the proposed approach effectively reduces communication resource consumption by up to $73\%$ and enhances average performance by $5\%$ compared with the traditional LoRA method.

