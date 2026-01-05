---
layout: default
title: ECR: Manifold-Guided Semantic Cues for Compact Language Models
---

# ECR: Manifold-Guided Semantic Cues for Compact Language Models
**arXiv**：[2601.00543v1](https://arxiv.org/abs/2601.00543) · [PDF](https://arxiv.org/pdf/2601.00543.pdf)  
**作者**：Chung-Wei Victor Yuan  

**一句话要点**：提出嵌入一致性调控框架以解决紧凑模型语义漂移问题

**关键词**：紧凑语言模型, 嵌入空间结构, 语义漂移, 多语言处理, 模型压缩, 几何一致性

## 3 点简述
- 紧凑模型在容量受限或多语言数据下易丢失嵌入空间结构，导致语义漂移
- ECR框架利用离线计算的教师嵌入语义锚点，引导紧凑模型保持几何一致性
- 实验表明ECR能稳定训练，在多语言任务中保留语义结构，提升表示质量

## 摘要（原文）

> Compact models often lose the structure of their embedding space. The issue shows up when the capacity is tight or the data spans several languages. Such collapse makes it difficult for downstream tasks to build on the resulting representation. Existing compression methods focus on aligning model outputs at a superficial level but fail to preserve the underlying manifold structure. This mismatch often leads to semantic drift in the compact model, causing both task behavior and linguistic properties to deviate from the reference model.
>   To address those issues, we provide a new framework called Embedding Consistency Regulation (ECR). This framework first derives a set of semantic anchors from teacher embeddings (computed once offline). Then, the compact model learns to maintain consistent geometry around these anchors, without relying on matching logits or internal features. ECR adds only a small projection step at inference, without altering the decoding architecture or its runtime behavior.
>   In experiments on a 100K multilingual corpus, ECR consistently stabilizes training and preserves semantic structure across tasks and languages. It also produces a more compact and task-aligned representation space, enabling low-capacity models to learn cleaner manifolds than conventional baselines. ECR works without teacher outputs and is compatible with, but independent of, distillation. Taken together, our results show that ECR helps compact models better follow task requirements and makes them easier to deploy under strict efficiency or privacy limits.

