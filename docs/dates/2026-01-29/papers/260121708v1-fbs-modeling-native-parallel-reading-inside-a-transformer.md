---
layout: default
title: FBS: Modeling Native Parallel Reading inside a Transformer
---

# FBS: Modeling Native Parallel Reading inside a Transformer
**arXiv**：[2601.21708v1](https://arxiv.org/abs/2601.21708) · [PDF](https://arxiv.org/pdf/2601.21708.pdf)  
**作者**：Tongxi Wang  

**一句话要点**：提出FBS Transformer以解决LLM推理中缺乏人类阅读式并行处理的问题

**关键词**：Transformer加速, 并行推理, 自回归模型, 计算效率, 注意力机制

## 3 点简述
- 核心问题：LLM推理依赖逐token自回归，缺乏内容自适应前瞻和块结构感知计算分配
- 方法要点：通过PAW、CH和SG模块注入可训练因果循环，实现并行阅读建模
- 实验或效果：在多样基准上提升质量-效率权衡，无需增加参数，模块互补

## 摘要（原文）

> Large language models (LLMs) excel across many tasks, yet inference is still dominated by strictly token-by-token autoregression. Existing acceleration methods largely patch this pipeline and miss core human-reading ingredients: content-adaptive foresight, chunk-structure-aware compute allocation, and train--test consistency for preview/skimming. We propose the \textbf{Fovea-Block-Skip Transformer} (FBS), which injects a causal, trainable loop into Transformers via Parafovea-Attention Window (PAW), Chunk-Head (CH), and Skip-Gate (SG). Across diverse benchmarks, FBS improves the quality-efficiency trade-off without increasing parameters, and ablations show the three modules are complementary.

