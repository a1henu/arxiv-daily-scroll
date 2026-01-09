---
layout: default
title: On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions
---

# On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions
**arXiv**：[2601.04600v1](https://arxiv.org/abs/2601.04600) · [PDF](https://arxiv.org/pdf/2601.04600.pdf)  
**作者**：Zhiyuan He, Binghan Chen, Tianxiang Xiong, Ziyang Sun, Mozhao Zhu, Xi Chen  

**一句话要点**：提出冗余编辑策略以缓解知识编辑在多跳推理中的局限性

**关键词**：知识编辑, 多跳推理, 模型编辑, Transformer模型, 泛化能力

## 3 点简述
- 研究ROME知识编辑在多跳推理中的失败模式，如跳转过晚和泛化能力下降
- 提出冗余编辑策略，通过增强中间表示来提升多跳推理准确性
- 实验显示在2跳问题上准确率提升至少15.5个百分点，但牺牲部分特异性和语言自然性

## 摘要（原文）

> Recent advances in Knowledge Editing (KE), particularly Rank-One Model Editing (ROME), show superior efficiency over fine-tuning and in-context learning for updating single-hop facts in transformers. However, these methods face significant challenges when applied to multi-hop reasoning tasks requiring knowledge chaining. In this work, we study the effect of editing knowledge with ROME on different layer depths and identify three key failure modes. First, the "hopping-too-late" problem occurs as later layers lack access to necessary intermediate representations. Second, generalization ability deteriorates sharply when editing later layers. Third, the model overfits to edited knowledge, incorrectly prioritizing edited-hop answers regardless of context. To mitigate the issues of "hopping-too-late" and generalisation decay, we propose Redundant Editing, a simple yet effective strategy that enhances multi-hop reasoning. Our experiments demonstrate that this approach can improve accuracy on 2-hop questions by at least 15.5 percentage points, representing a 96% increase over the previous single-edit strategy, while trading off some specificity and language naturalness.

