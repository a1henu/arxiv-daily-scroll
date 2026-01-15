---
layout: default
title: Linear Complexity Self-Supervised Learning for Music Understanding with Random Quantizer
---

# Linear Complexity Self-Supervised Learning for Music Understanding with Random Quantizer
**arXiv**：[2601.09603v1](https://arxiv.org/abs/2601.09603) · [PDF](https://arxiv.org/pdf/2601.09603.pdf)  
**作者**：Petros Vavaroutsos, Theodoros Palamas, Pantelis Vikatos  

**一句话要点**：提出结合Branchformer、SummaryMixing与随机量化的线性复杂度自监督学习模型，用于音乐信息检索任务以减小模型规模。

**关键词**：音乐信息检索, 自监督学习, 模型压缩, 随机量化, Branchformer架构, SummaryMixing

## 3 点简述
- 核心问题：基础模型在音乐信息检索中参数过多导致资源消耗大、成本高。
- 方法要点：采用Branchformer架构与SummaryMixing，结合随机量化过程以降低模型复杂度。
- 实验或效果：在公开与私有数据集上预训练，下游任务评估显示模型规模减少8.5%至12.3%，性能保持竞争力。

## 摘要（原文）

> In recent years, foundation models have become very popular due to their exceptional performance, mainly in natural language (NLP) tasks where they were first introduced. These models usually consist of hundreds of millions, or even billions, of parameters, making them resource-intensive during training and in production systems, leading to increased costs. This paper focuses on the reduction of a foundation's model size when applied to music information retrieval (MIR) tasks. Our research combines the Branchformer architecture with SummaryMixing, which were first applied in speech recognition, along with a random quantization process. To facilitate reproducibility, we conduct pre-training on publicly available datasets, complemented by a proprietary dataset comparable in scale to other private datasets reported in the literature. We ensure robust evaluation by using a framework consisting of a variety of downstream MIR tasks. Our results show that our architecture achieves competitive performance when compared with other state-of-the-art models that use multi-head self-attention, while reducing the model size from 8.5% up to 12.3%.

