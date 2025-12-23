---
layout: default
title: Helios: A Foundational Language Model for Smart Energy Knowledge Reasoning and Application
---

# Helios: A Foundational Language Model for Smart Energy Knowledge Reasoning and Application
**arXiv**：[2512.19299v1](https://arxiv.org/abs/2512.19299) · [PDF](https://arxiv.org/pdf/2512.19299.pdf)  
**作者**：Haoyu Jiang, Fanjie Zeng, Boan Qu, Xiaojie Lin, Wei Zhong  

**一句话要点**：提出Helios领域大语言模型以解决智能能源中通用LLMs缺乏专业知识与物理约束的问题

**关键词**：智能能源大语言模型, 领域知识推理, 多智能体数据集构建, 指令微调, 强化学习人类反馈, 能源基准评估

## 3 点简述
- 核心问题：通用LLMs在智能能源领域因跨学科、碎片化知识而推理不精确
- 方法要点：构建Enersys框架及数据集，通过预训练、SFT和RLHF定制Helios模型
- 实验或效果：发布EnerBench基准，Helios在知识掌握、任务准确性和对齐方面显著提升

## 摘要（原文）

> In the global drive toward carbon neutrality, deeply coordinated smart energy systems underpin industrial transformation. However, the interdisciplinary, fragmented, and fast-evolving expertise in this domain prevents general-purpose LLMs, which lack domain knowledge and physical-constraint awareness, from delivering precise engineering-aligned inference and generation. To address these challenges, we introduce Helios, a large language model tailored to the smart energy domain, together with a comprehensive suite of resources to advance LLM research in this field. Specifically, we develop Enersys, a multi-agent collaborative framework for end-to-end dataset construction, through which we produce: (1) a smart energy knowledge base, EnerBase, to enrich the model's foundational expertise; (2) an instruction fine-tuning dataset, EnerInstruct, to strengthen performance on domain-specific downstream tasks; and (3) an RLHF dataset, EnerReinforce, to align the model with human preferences and industry standards. Leveraging these resources, Helios undergoes large-scale pretraining, SFT, and RLHF. We also release EnerBench, a benchmark for evaluating LLMs in smart energy scenarios, and demonstrate that our approach significantly enhances domain knowledge mastery, task execution accuracy, and alignment with human preferences.

