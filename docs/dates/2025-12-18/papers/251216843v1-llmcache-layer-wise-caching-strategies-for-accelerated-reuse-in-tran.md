---
layout: default
title: LLMCache: Layer-Wise Caching Strategies for Accelerated Reuse in Transformer Inference
---

# LLMCache: Layer-Wise Caching Strategies for Accelerated Reuse in Transformer Inference
**arXiv**：[2512.16843v1](https://arxiv.org/abs/2512.16843) · [PDF](https://arxiv.org/pdf/2512.16843.pdf)  
**作者**：Harsh Vardhan Bansal  

**一句话要点**：提出LLMCache层缓存框架以加速Transformer推理，通过语义相似性重用中间激活

**关键词**：Transformer推理加速, 层缓存策略, 语义相似性匹配, 模型无关缓存, 自适应淘汰策略

## 3 点简述
- Transformer推理延迟高，现有缓存机制如token级KV缓存适用范围有限
- LLMCache为模型无关层缓存框架，支持任意层缓存和轻量指纹匹配语义相似输入
- 实验在BERT和GPT-2上实现最高3.1倍加速，精度下降<0.5%

## 摘要（原文）

> Transformer-based language models have achieved remarkable performance across a wide range of tasks, yet their high inference latency poses a significant challenge for real-timeand large-scale deployment. While existing caching mechanisms,such as token-level key-value caches, offer speedups in autore-gressive decoding, they are limited in scope and applicability. In this paper, we present LLMCache, a novel layer-wise caching framework that accelerates transformer inference by reusing intermediate activations based on semantic similarity of input sequences. Unlike prior work, LLMCache is model-agnostic,operates across both encoder and decoder architectures, and supports caching at arbitrary transformer layers. We introduce a lightweight fingerprinting mechanism for matching seman-tically similar inputs and propose adaptive eviction strategies to manage cache staleness. Experiments on BERT and GPT-2 across SQuAD, WikiText-103, and OpenBookQA show up to 3.1 X speedup in inference time with <0.5% accuracy degradation. Our results highlight LLMCache as a practical and general-purpose solution for optimizing transformer inference in real-world applications

