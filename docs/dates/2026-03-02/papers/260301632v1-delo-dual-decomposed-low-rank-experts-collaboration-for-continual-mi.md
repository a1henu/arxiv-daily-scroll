---
layout: default
title: DeLo: Dual Decomposed Low-Rank Experts Collaboration for Continual Missing Modality Learning
---

# DeLo: Dual Decomposed Low-Rank Experts Collaboration for Continual Missing Modality Learning
**arXiv**：[2603.01632v1](https://arxiv.org/abs/2603.01632) · [PDF](https://arxiv.org/pdf/2603.01632.pdf)  
**作者**：Xiwei Liu, Yulong Li, Feilong Tang, Imran Razzak  

**一句话要点**：提出DeLo框架，通过双分解低秩专家架构解决持续缺失模态学习中的模态干扰问题。

**关键词**：持续缺失模态学习, 低秩适应, 模态干扰, 任务分区, 多模态模型, 专家系统

## 3 点简述
- 核心问题：持续缺失模态学习中，现有方法因共享嵌入空间中的跨任务干扰或模态干扰而性能受限。
- 方法要点：采用双分解低秩专家架构，动态组合解耦的模态特定因子池中的秩一因子，结合任务分区框架防止灾难性遗忘。
- 实验或效果：在标准基准测试中显著优于最先进方法，验证了架构感知的LoRA设计价值。

## 摘要（原文）

> Adapting Large Multimodal Models (LMMs) to real-world scenarios poses the dual challenges of learning from sequential data streams while handling frequent modality incompleteness, a task known as Continual Missing Modality Learning (CMML). However, existing works on CMML have predominantly relied on prompt tuning, a technique that struggles with this task due to cross-task interference between its learnable prompts in their shared embedding space. A naive application of Low-Rank Adaptation (LoRA) with modality-shared module will also suffer modality interference from competing gradients. To this end, we propose DeLo, the first framework to leverage a novel dual-decomposed low-rank expert architecture for CMML. Specifically, this architecture resolves modality interference through decomposed LoRA expert, dynamically composing LoRA update matrix with rank-one factors from disentangled modality-specific factor pools. Embedded within a task-partitioned framework that structurally prevents catastrophic forgetting, this expert system is supported by two key mechanisms: a Cross-Modal Guided Routing strategy to handle incomplete data and a Task-Key Memory for efficient, task-agnostic inference. Extensive experiments on established CMML benchmarks demonstrate that our method significantly outperforms state-of-the-art approaches. This highlights the value of a principled, architecturally-aware LoRA design for real-world multimodal challenges.

