---
layout: default
title: Mario: Multimodal Graph Reasoning with Large Language Models
---

# Mario: Multimodal Graph Reasoning with Large Language Models
**arXiv**：[2603.05181v1](https://arxiv.org/abs/2603.05181) · [PDF](https://arxiv.org/pdf/2603.05181.pdf)  
**作者**：Yuanfu Sun, Kang Li, Pengkang Guo, Jiajin Liu, Qiaoyu Tan  

**一句话要点**：提出Mario框架以解决多模态图推理中的跨模态一致性和异质模态偏好问题

**关键词**：多模态图推理, 大型语言模型, 跨模态对比学习, 图指令调优, 节点分类, 链接预测

## 3 点简述
- 核心问题：现有方法忽略多模态数据的图结构，导致跨模态一致性弱和模态偏好异质。
- 方法要点：采用图条件视觉语言模型和模态自适应图指令调优，联合优化特征并适配LLM推理。
- 实验或效果：在多个多模态图基准上，监督和零样本场景下节点分类与链接预测均优于先进模型。

## 摘要（原文）

> Recent advances in large language models (LLMs) have opened new avenues for multimodal reasoning. Yet, most existing methods still rely on pretrained vision-language models (VLMs) to encode image-text pairs in isolation, ignoring the relational structure that real-world multimodal data naturally form. This motivates reasoning on multimodal graphs (MMGs), where each node has textual and visual attributes and edges provide structural cues. Enabling LLM-based reasoning on such heterogeneous multimodal signals while preserving graph topology introduces two key challenges: resolving weak cross-modal consistency and handling heterogeneous modality preference. To address this, we propose Mario, a unified framework that simultaneously resolves the two above challenges and enables effective LLM-based reasoning over MMGs. Mario consists of two innovative stages. Firstly, a graph-conditioned VLM design that jointly refines textual and visual features through fine-grained cross-modal contrastive learning guided by graph topology. Secondly, a modality-adaptive graph instruction tuning mechanism that organizes aligned multimodal features into graph-aware instruction views and employs a learnable router to surface, for each node and its neighborhood, the most informative modality configuration to the LLM. Extensive experiments across diverse MMG benchmarks demonstrate that Mario consistently outperforms state-of-the-art graph models in both supervised and zero-shot scenarios for node classification and link prediction. The code will be made available at https://github.com/sunyuanfu/Mario.

