---
layout: default
title: Parallel Context-of-Experts Decoding for Retrieval Augmented Generation
---

# Parallel Context-of-Experts Decoding for Retrieval Augmented Generation
**arXiv**：[2601.08670v1](https://arxiv.org/abs/2601.08670) · [PDF](https://arxiv.org/pdf/2601.08670.pdf)  
**作者**：Giulio Corallo, Paolo Papotti  

**一句话要点**：提出并行上下文专家解码框架，以解决检索增强生成中多文档推理与速度的权衡问题。

**关键词**：检索增强生成, 并行解码, 对比解码, 多文档推理, 训练无关框架

## 3 点简述
- 核心问题：检索增强生成面临长提示拼接导致预填充瓶颈与单独编码文档KV缓存破坏跨文档交互的权衡。
- 方法要点：通过训练无关框架，将证据聚合从注意力机制转移到解码，使用检索感知对比解码规则同步专家预测。
- 实验或效果：恢复跨文档推理能力，无需构建跨文档共享注意力，具体效果未知。

## 摘要（原文）

> Retrieval Augmented Generation faces a trade-off: concatenating documents in a long prompt enables multi-document reasoning but creates prefill bottlenecks, while encoding document KV caches separately offers speed but breaks cross-document interaction. We propose Parallel Context-of-Experts Decoding (Pced), a training-free framework that shifts evidence aggregation from the attention mechanism to the decoding. Pced treats retrieved documents as isolated "experts", synchronizing their predictions via a novel retrieval-aware contrastive decoding rule that weighs expert logits against the model prior. This approach recovers cross-document reasoning capabilities without constructing a shared attention across documents.

