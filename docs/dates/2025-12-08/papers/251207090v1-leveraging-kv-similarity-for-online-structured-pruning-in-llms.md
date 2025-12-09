---
layout: default
title: Leveraging KV Similarity for Online Structured Pruning in LLMs
---

# Leveraging KV Similarity for Online Structured Pruning in LLMs
**arXiv**：[2512.07090v1](https://arxiv.org/abs/2512.07090) · [PDF](https://arxiv.org/pdf/2512.07090.pdf)  
**作者**：Jungmin Lee, Gwangeun Byeon, Yulhwa Kim, Seokin Hong  

**一句话要点**：提出Token Filtering在线结构化剪枝方法，利用KV相似性在LLM推理中跳过冗余计算以加速。

**关键词**：大语言模型剪枝, 在线推理加速, 键值相似性, 结构化剪枝, 注意力机制优化

## 3 点简述
- 现有LLM剪枝方法依赖离线校准数据，导致跨输入不稳定。
- 基于键值相似性在线评估token冗余，自适应融合策略增强稳定性，无额外内存开销。
- 在LLaMA和Mistral模型上实验，50%剪枝下保持MMLU等任务性能，优于先前方法。

## 摘要（原文）

> Pruning has emerged as a promising direction for accelerating large language model (LLM) inference, yet existing approaches often suffer from instability because they rely on offline calibration data that may not generalize across inputs. In this work, we introduce Token Filtering, a lightweight online structured pruning technique that makes pruning decisions directly during inference without any calibration data. The key idea is to measure token redundancy via joint key-value similarity and skip redundant attention computations, thereby reducing inference cost while preserving critical information. To further enhance stability, we design a variance-aware fusion strategy that adaptively weights key and value similarity across heads, ensuring that informative tokens are retained even under high pruning ratios. This design introduces no additional memory overhead and provides a more reliable criterion for token importance. Extensive experiments on LLaMA-2 (7B/13B), LLaMA-3 (8B), and Mistral (7B) demonstrate that Token Filtering consistently outperforms prior structured pruning methods, preserving accuracy on commonsense reasoning benchmarks and maintaining strong performance on challenging tasks such as MMLU, even with 50% pruning.

