---
layout: default
title: Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
---

# Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
**arXiv**：[2601.20796v1](https://arxiv.org/abs/2601.20796) · [PDF](https://arxiv.org/pdf/2601.20796.pdf)  
**作者**：Yiran Huang, Karsten Roth, Quentin Bouniot, Wenjia Xu, Zeynep Akata  

**一句话要点**：通过合成任务分析现代Transformer中多模态上下文学习的不对称性与电路机制

**关键词**：多模态上下文学习, Transformer机制分析, 模态不对称性, 合成任务实验, RoPE影响

## 3 点简述
- 核心问题：Transformer如何从上下文示例中跨模态关联信息，探究多模态上下文学习机制
- 方法要点：在合成分类任务上训练小型Transformer，精确控制数据统计和模型架构，包括使用RoPE
- 实验或效果：发现多模态学习不对称性，主模态高多样性预训练下，次模态低复杂度数据即可实现多模态上下文学习

## 摘要（原文）

> Transformer-based multimodal large language models often exhibit in-context learning (ICL) abilities. Motivated by this phenomenon, we ask: how do transformers learn to associate information across modalities from in-context examples? We investigate this question through controlled experiments on small transformers trained on synthetic classification tasks, enabling precise manipulation of data statistics and model architecture. We begin by revisiting core principles of unimodal ICL in modern transformers. While several prior findings replicate, we find that Rotary Position Embeddings (RoPE) increases the data complexity threshold for ICL. Extending to the multimodal setting reveals a fundamental learning asymmetry: when pretrained on high-diversity data from a primary modality, surprisingly low data complexity in the secondary modality suffices for multimodal ICL to emerge. Mechanistic analysis shows that both settings rely on an induction-style mechanism that copies labels from matching in-context exemplars; multimodal training refines and extends these circuits across modalities. Our findings provide a mechanistic foundation for understanding multimodal ICL in modern transformers and introduce a controlled testbed for future investigation.

