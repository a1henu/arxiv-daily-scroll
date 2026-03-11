---
layout: default
title: On Catastrophic Forgetting in Low-Rank Decomposition-Based Parameter-Efficient Fine-Tuning
---

# On Catastrophic Forgetting in Low-Rank Decomposition-Based Parameter-Efficient Fine-Tuning
**arXiv**：[2603.09684v1](https://arxiv.org/abs/2603.09684) · [PDF](https://arxiv.org/pdf/2603.09684.pdf)  
**作者**：Muhammad Ahmad, Jingjing Zheng, Yankai Cao  

**一句话要点**：研究低秩分解参数高效微调在序列学习中的灾难性遗忘问题

**关键词**：参数高效微调, 灾难性遗忘, 低秩分解, 序列学习, 更新子空间设计

## 3 点简述
- 核心问题：低秩分解参数高效微调在序列学习中灾难性遗忘的行为机制尚不明确
- 方法要点：通过更新子空间的几何和参数化设计，如张量分解和结构对齐，来减轻遗忘
- 实验或效果：实证表明张量分解方法在超紧凑预算下能捕获更丰富结构信息，减少任务干扰

## 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) based on low-rank decomposition, such as LoRA, has become a standard for adapting large pretrained models. However, its behavior in sequential learning -- specifically regarding catastrophic forgetting -- remains insufficiently understood. In this work, we present an empirical study showing that forgetting is strongly influenced by the geometry and parameterization of the update subspace. While methods that restrict updates to small, shared matrix subspaces often suffer from task interference, tensor-based decompositions (e.g., LoRETTA) mitigate forgetting by capturing richer structural information within ultra-compact budgets, and structurally aligned parameterizations (e.g., WeGeFT) preserve pretrained representations. Our findings highlight update subspace design as a key factor in continual learning and offer practical guidance for selecting efficient adaptation strategies in sequential settings.

