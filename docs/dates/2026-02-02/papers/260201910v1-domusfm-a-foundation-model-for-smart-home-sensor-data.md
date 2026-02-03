---
layout: default
title: DomusFM: A Foundation Model for Smart-Home Sensor Data
---

# DomusFM: A Foundation Model for Smart-Home Sensor Data
**arXiv**：[2602.01910v1](https://arxiv.org/abs/2602.01910) · [PDF](https://arxiv.org/pdf/2602.01910.pdf)  
**作者**：Michele Fiori, Gabriele Civitarese, Flora D. Salim, Claudio Bettini  

**一句话要点**：提出DomusFM基础模型以解决智能家居传感器数据稀疏与标注稀缺问题

**关键词**：智能家居传感器, 基础模型, 自监督学习, 对比学习, 活动识别, 事件分析

## 3 点简述
- 现有方法依赖标注数据或惯性传感器，难以处理智能家居二进制传感器事件的稀疏离散特性
- 采用自监督双对比学习，结合语义嵌入与时间编码，学习可迁移的通用表示
- 在七个公开数据集上通过留一评估，仅用5%标注数据微调即超越基线

## 摘要（原文）

> Smart-home sensor data holds significant potential for several applications, including healthcare monitoring and assistive technologies. Existing approaches, however, face critical limitations. Supervised models require impractical amounts of labeled data. Foundation models for activity recognition focus only on inertial sensors, failing to address the unique characteristics of smart-home binary sensor events: their sparse, discrete nature combined with rich semantic associations. LLM-based approaches, while tested in this domain, still raise several issues regarding the need for natural language descriptions or prompting, and reliance on either external services or expensive hardware, making them infeasible in real-life scenarios due to privacy and cost concerns. We introduce DomusFM, the first foundation model specifically designed and pretrained for smart-home sensor data. DomusFM employs a self-supervised dual contrastive learning paradigm to capture both token-level semantic attributes and sequence-level temporal dependencies. By integrating semantic embeddings from a lightweight language model and specialized encoders for temporal patterns and binary states, DomusFM learns generalizable representations that transfer across environments and tasks related to activity and event analysis. Through leave-one-dataset-out evaluation across seven public smart-home datasets, we demonstrate that DomusFM outperforms state-of-the-art baselines on different downstream tasks, achieving superior performance even with only 5% of labeled training data available for fine-tuning. Our approach addresses data scarcity while maintaining practical deployability for real-world smart-home systems.

