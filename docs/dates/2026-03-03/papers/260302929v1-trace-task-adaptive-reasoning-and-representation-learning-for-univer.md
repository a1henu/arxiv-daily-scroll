---
layout: default
title: TRACE: Task-Adaptive Reasoning and Representation Learning for Universal Multimodal Retrieval
---

# TRACE: Task-Adaptive Reasoning and Representation Learning for Universal Multimodal Retrieval
**arXiv**：[2603.02929v1](https://arxiv.org/abs/2603.02929) · [PDF](https://arxiv.org/pdf/2603.02929.pdf)  
**作者**：Xiangzhao Hao, Shijie Wang, Tianyu Yang, Tianyue Wang, Haiyun Guo, JinQiao Wang  

**一句话要点**：提出TRACE框架，通过任务自适应推理与表示学习解决通用多模态检索中复杂意图理解问题。

**关键词**：通用多模态检索, 任务自适应推理, 思维链压缩, 表示学习, 零样本迁移

## 3 点简述
- 核心问题：通用多模态检索需处理从简单到复杂的用户意图，现有编码器范式难以应对需逻辑推理的复杂查询。
- 方法要点：TRACE结合生成式推理与判别式表示学习，先生成结构化思维链推理查询，再压缩为紧凑嵌入。
- 实验或效果：在M-BEIR基准上达到新SOTA，展示自适应推理行为，平衡检索精度与推理吞吐，并具零样本迁移能力。

## 摘要（原文）

> Universal Multimodal Retrieval requires unified embedding models capable of interpreting diverse user intents, ranging from simple keywords to complex compositional instructions. While Multimodal Large Language Models (MLLMs) possess strong reasoning capabilities, prevailing adaptations confine them to static encoders, underutilizing their generative potential. This encoder-only paradigm struggles with complex intents that demand logical deduction rather than superficial pattern matching. To address this, we introduce TRACE (Task-adaptive Reasoning And Compressing Embeddings). TRACE unifies generative reasoning with discriminative representation learning. It first generates a structured Chain-of-Thought (CoT) to explicitly reason about the query, and subsequently compresses this reasoning trace into a compact embedding via a dedicated token. To train this framework, we construct M-BEIR-CoT, a large-scale dataset featuring a difficulty-aware routing strategy. Experiments on the M-BEIR benchmark establish TRACE as the new state-of-the-art. Crucially, TRACE demonstrates a learned implicit routing behavior. It autonomously activates reasoning for complex queries while bypassing it for simpler ones, achieving an optimal balance between retrieval accuracy and inference throughput. Furthermore, by internalizing the deductive process, TRACE exhibits remarkable zero-shot transferability to unseen domains and novel constraints.

