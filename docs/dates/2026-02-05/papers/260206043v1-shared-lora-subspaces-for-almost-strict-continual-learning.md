---
layout: default
title: Shared LoRA Subspaces for almost Strict Continual Learning
---

# Shared LoRA Subspaces for almost Strict Continual Learning
**arXiv**：[2602.06043v1](https://arxiv.org/abs/2602.06043) · [PDF](https://arxiv.org/pdf/2602.06043.pdf)  
**作者**：Prakhar Kaushik, Ankit Vaidya, Shravan Chaudhari, Rama Chellappa, Alan Yuille  

**一句话要点**：提出Share方法，通过共享低秩子空间实现参数高效持续学习，解决灾难性遗忘与高计算成本问题。

**关键词**：持续学习, 参数高效微调, 低秩适应, 灾难性遗忘, 知识整合, 多模态适应

## 3 点简述
- 核心问题：大型预训练模型在持续学习中面临灾难性遗忘和高昂重训练成本，现有参数高效方法如LoRA缺乏严格持续学习机制。
- 方法要点：Share构建并动态更新单一共享低秩子空间，从过去任务提取核心知识并增量整合新信息，促进前向知识转移。
- 实验或效果：在图像分类、自然语言理解等任务中验证，实现高达100倍参数减少和281倍内存节省，性能接近联合训练模型。

## 摘要（原文）

> Adapting large pretrained models to new tasks efficiently and continually is crucial for real-world deployment but remains challenging due to catastrophic forgetting and the high cost of retraining. While parameter-efficient tuning methods like low rank adaptation (LoRA) reduce computational demands, they lack mechanisms for strict continual learning and knowledge integration, without relying on data replay, or multiple adapters. We propose Share, a novel approach to parameter efficient continual finetuning that learns and dynamically updates a single, shared low-rank subspace, enabling seamless adaptation across multiple tasks and modalities. Share constructs a foundational subspace that extracts core knowledge from past tasks and incrementally integrates new information by identifying essential subspace directions. Knowledge from each new task is incorporated into this evolving subspace, facilitating forward knowledge transfer, while minimizing catastrophic interference. This approach achieves up to 100x parameter reduction and 281x memory savings over traditional LoRA methods, maintaining performance comparable to jointly trained models. A single Share model can replace hundreds of task-specific LoRA adapters, supporting scalable, asynchronous continual learning. Experiments across image classification, natural language understanding, 3D pose estimation, and text-to-image generation validate its effectiveness, making Share a practical and scalable solution for lifelong learning in large-scale AI systems.

