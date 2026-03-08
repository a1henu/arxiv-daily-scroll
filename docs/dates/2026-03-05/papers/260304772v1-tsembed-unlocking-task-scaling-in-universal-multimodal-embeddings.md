---
layout: default
title: TSEmbed: Unlocking Task Scaling in Universal Multimodal Embeddings
---

# TSEmbed: Unlocking Task Scaling in Universal Multimodal Embeddings
**arXiv**：[2603.04772v1](https://arxiv.org/abs/2603.04772) · [PDF](https://arxiv.org/pdf/2603.04772.pdf)  
**作者**：Yebo Wu, Feng Liu, Ziwei Xie, Zhiyuan Liu, Changwang Zhang, Jun Wang, Li Li  

**一句话要点**：提出TSEmbed框架以解决多模态嵌入中的任务冲突问题

**关键词**：多模态嵌入, 任务冲突, 混合专家, 低秩适应, 负采样策略, 通用嵌入模型

## 3 点简述
- 核心问题：多模态大语言模型作为通用嵌入模型时面临任务冲突阻碍。
- 方法要点：结合MoE与LoRA解耦任务目标，并引入EANS策略优化负采样。
- 实验或效果：在MMEB和工业数据集上实现最先进性能，支持任务级扩展。

## 摘要（原文）

> Despite the exceptional reasoning capabilities of Multimodal Large Language Models (MLLMs), their adaptation into universal embedding models is significantly impeded by task conflict. To address this, we propose TSEmbed, a universal multimodal embedding framework that synergizes Mixture-of-Experts (MoE) with Low-Rank Adaptation (LoRA) to explicitly disentangle conflicting task objectives. Moreover, we introduce Expert-Aware Negative Sampling (EANS), a novel strategy that leverages expert routing distributions as an intrinsic proxy for semantic similarity. By dynamically prioritizing informative hard negatives that share expert activation patterns with the query, EANS effectively sharpens the model's discriminative power and refines embedding boundaries. To ensure training stability, we further devise a two-stage learning paradigm that solidifies expert specialization before optimizing representations via EANS. TSEmbed achieves state-of-the-art performance on both the Massive Multimodal Embedding Benchmark (MMEB) and real-world industrial production datasets, laying a foundation for task-level scaling in universal multimodal embeddings.

