---
layout: default
title: Best of Both Worlds: Multimodal Reasoning and Generation via Unified Discrete Flow Matching
---

# Best of Both Worlds: Multimodal Reasoning and Generation via Unified Discrete Flow Matching
**arXiv**：[2602.12221v1](https://arxiv.org/abs/2602.12221) · [PDF](https://arxiv.org/pdf/2602.12221.pdf)  
**作者**：Onkar Susladkar, Tushar Prakash, Gayatri Deshmukh, Kiet A. Nguyen, Jiaxun Zhang, Adheesh Juvekar, Tianshu Bao, Lin Chai, Sparsh Mittal, Inderjit S Dhillon, Ismini Lourentzou  

**一句话要点**：提出UniDFlow统一离散流匹配框架，用于多模态理解、生成与编辑。

**关键词**：多模态理解, 多模态生成, 离散流匹配, 低秩适配器, 偏好对齐, 零样本泛化

## 3 点简述
- 核心问题：多模态任务中理解与生成目标干扰和表示纠缠。
- 方法要点：通过任务特定低秩适配器解耦理解与生成，并引入基于参考的多模态偏好对齐优化结果。
- 实验或效果：在八个基准测试中达到SOTA，零样本泛化能力强，支持修复、上下文图像生成等任务。

## 摘要（原文）

> We propose UniDFlow, a unified discrete flow-matching framework for multimodal understanding, generation, and editing. It decouples understanding and generation via task-specific low-rank adapters, avoiding objective interference and representation entanglement, while a novel reference-based multimodal preference alignment optimizes relative outcomes under identical conditioning, improving faithfulness and controllability without large-scale retraining. UniDFlpw achieves SOTA performance across eight benchmarks and exhibits strong zero-shot generalization to tasks including inpainting, in-context image generation, reference-based editing, and compositional generation, despite no explicit task-specific training.

