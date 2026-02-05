---
layout: default
title: RexBERT: Context Specialized Bidirectional Encoders for E-commerce
---

# RexBERT: Context Specialized Bidirectional Encoders for E-commerce
**arXiv**：[2602.04605v1](https://arxiv.org/abs/2602.04605) · [PDF](https://arxiv.org/pdf/2602.04605.pdf)  
**作者**：Rahul Bajaj, Anuj Garg  

**一句话要点**：提出RexBERT，一种针对电子商务语义的BERT风格编码器，以解决通用编码器在专业领域覆盖不足的问题。

**关键词**：电子商务语义, 编码器预训练, 专业领域语料库, 长上下文模型, 参数效率

## 3 点简述
- 通用编码器在电子商务等专业领域数据覆盖有限，影响应用性能。
- 通过Ecom-niverse语料库和分阶段预训练方法，专门优化电子商务语义。
- 在电子商务基准测试中，RexBERT以较少参数超越或匹配更大通用模型。

## 摘要（原文）

> Encoder-only transformers remain indispensable in retrieval, classification, and ranking systems where latency, stability, and cost are paramount. Most general purpose encoders, however, are trained on generic corpora with limited coverage of specialized domains. We introduce RexBERT, a family of BERT-style encoders designed specifically for e-commerce semantics. We make three contributions. First, we release Ecom-niverse, a 350 billion token corpus curated from diverse retail and shopping sources. We describe a modular pipeline that isolates and extracts e-commerce content from FineFineWeb and other open web resources, and characterize the resulting domain distribution. Second, we present a reproducible pretraining recipe building on ModernBERT's architectural advances. The recipe consists of three phases: general pre-training, context extension, and annealed domain specialization. Third, we train RexBERT models ranging from 17M to 400M parameters and evaluate them on token classification, semantic similarity, and general natural language understanding tasks using e-commerce datasets. Despite having 2-3x fewer parameters, RexBERT outperforms larger general-purpose encoders and matches or surpasses modern long-context models on domain-specific benchmarks. Our results demonstrate that high quality in-domain data combined with a principled training approach provides a stronger foundation for e-commerce applications than indiscriminate scaling alone.

