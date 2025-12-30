---
layout: default
title: FRoD: Full-Rank Efficient Fine-Tuning with Rotational Degrees for Fast Convergence
---

# FRoD: Full-Rank Efficient Fine-Tuning with Rotational Degrees for Fast Convergence
**arXiv**：[2512.23485v1](https://arxiv.org/abs/2512.23485) · [PDF](https://arxiv.org/pdf/2512.23485.pdf)  
**作者**：Guoan Wan, Tianyu Chen, Fangzheng Feng, Haoyi Zhou, Runhua Xu  

**一句话要点**：提出FRoD方法，结合分层联合分解与旋转自由度，以解决参数高效微调中收敛慢和表达能力受限的问题。

**关键词**：参数高效微调, 全秩更新, 旋转自由度, 分层联合分解, 快速收敛

## 3 点简述
- 核心问题：参数高效微调方法如LoRA因低秩约束导致收敛慢和适应能力有限。
- 方法要点：通过全局共享基和稀疏可学习扰动实现灵活的全秩更新，提升表达效率。
- 实验或效果：在20个基准测试中，仅用1.72%可训练参数即匹配全模型微调精度。

## 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) methods have emerged as a practical solution for adapting large foundation models to downstream tasks, reducing computational and memory costs by updating only a small subset of parameters. Among them, approaches like LoRA aim to strike a balance between efficiency and expressiveness, but often suffer from slow convergence and limited adaptation capacity due to their inherent low-rank constraints. This trade-off hampers the ability of PEFT methods to capture complex patterns needed for diverse tasks. To address these challenges, we propose FRoD, a novel fine-tuning method that combines hierarchical joint decomposition with rotational degrees of freedom. By extracting a globally shared basis across layers and injecting sparse, learnable perturbations into scaling factors for flexible full-rank updates, FRoD enhances expressiveness and efficiency, leading to faster and more robust convergence. On 20 benchmarks spanning vision, reasoning, and language understanding, FRoD matches full model fine-tuning in accuracy, while using only 1.72% of trainable parameters under identical training budgets.

