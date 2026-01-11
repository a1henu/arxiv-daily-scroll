---
layout: default
title: Text as a Universal Interface for Transferable Personalization
---

# Text as a Universal Interface for Transferable Personalization
**arXiv**：[2601.04963v1](https://arxiv.org/abs/2601.04963) · [PDF](https://arxiv.org/pdf/2601.04963.pdf)  
**作者**：Yuting Liu, Jian Guan, Jia-Nan Li, Wei Wu, Jiang-Ming Yang, Jianzhe Zhao, Guibing Guo  

**一句话要点**：提出基于文本的通用偏好表示方法，以解决大语言模型中偏好表示不透明和难以迁移的问题。

**关键词**：大语言模型, 偏好表示, 文本摘要, 迁移学习, 强化学习, 可解释性

## 3 点简述
- 核心问题：现有大语言模型偏好表示为隐式向量，导致不透明且跨模型任务迁移困难。
- 方法要点：采用自然语言作为通用接口，通过两阶段训练框架生成可解释的文本偏好摘要。
- 实验或效果：在九个基准测试中，8B模型达到最优性能，并展示强跨任务和模型迁移能力。

## 摘要（原文）

> We study the problem of personalization in large language models (LLMs). Prior work predominantly represents user preferences as implicit, model-specific vectors or parameters, yielding opaque ``black-box'' profiles that are difficult to interpret and transfer across models and tasks. In contrast, we advocate natural language as a universal, model- and task-agnostic interface for preference representation. The formulation leads to interpretable and reusable preference descriptions, while naturally supporting continual evolution as new interactions are observed. To learn such representations, we introduce a two-stage training framework that combines supervised fine-tuning on high-quality synthesized data with reinforcement learning to optimize long-term utility and cross-task transferability. Based on this framework, we develop AlignXplore+, a universal preference reasoning model that generates textual preference summaries. Experiments on nine benchmarks show that our 8B model achieves state-of-the-art performanc -- outperforming substantially larger open-source models -- while exhibiting strong transferability across tasks, model families, and interaction formats.

