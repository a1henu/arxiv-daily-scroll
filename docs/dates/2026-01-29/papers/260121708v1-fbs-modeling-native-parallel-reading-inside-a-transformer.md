---
layout: default
title: FBS: Modeling Native Parallel Reading inside a Transformer
---

# FBS: Modeling Native Parallel Reading inside a Transformer
**arXiv**：[2601.21708v1](https://arxiv.org/abs/2601.21708) · [PDF](https://arxiv.org/pdf/2601.21708.pdf)  
**作者**：Tongxi Wang  

**一句话要点**：提出FBS Transformer以解决大语言模型推理中缺乏人类阅读式并行处理的问题。

**关键词**：Transformer加速, 并行推理, 注意力机制, 大语言模型, 效率优化

## 3 点简述
- 核心问题：大语言模型推理依赖逐词自回归，效率低，缺乏人类阅读的适应性前瞻和分块处理。
- 方法要点：引入Parafovea-Attention Window、Chunk-Head和Skip-Gate模块，在Transformer中注入可训练的因果循环。
- 实验或效果：在多样基准测试中提升质量-效率权衡，无需增加参数，模块互补性得到验证。

## 摘要（原文）

> Large language models (LLMs) excel across many tasks, yet inference is still dominated by strictly token-by-token autoregression. Existing acceleration methods largely patch this pipeline and miss core human-reading ingredients: content-adaptive foresight, chunk-structure-aware compute allocation, and train--test consistency for preview/skimming. We propose the \textbf{Fovea-Block-Skip Transformer} (FBS), which injects a causal, trainable loop into Transformers via Parafovea-Attention Window (PAW), Chunk-Head (CH), and Skip-Gate (SG). Across diverse benchmarks, FBS improves the quality-efficiency trade-off without increasing parameters, and ablations show the three modules are complementary.

