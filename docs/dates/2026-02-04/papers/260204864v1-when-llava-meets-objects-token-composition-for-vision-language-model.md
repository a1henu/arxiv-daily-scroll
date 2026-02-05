---
layout: default
title: When LLaVA Meets Objects: Token Composition for Vision-Language-Models
---

# When LLaVA Meets Objects: Token Composition for Vision-Language-Models
**arXiv**：[2602.04864v1](https://arxiv.org/abs/2602.04864) · [PDF](https://arxiv.org/pdf/2602.04864.pdf)  
**作者**：Soumya Jahagirdar, Walid Bousselham, Anna Kukleva, Hilde Kuehne  

**一句话要点**：提出Mask-LLaVA框架，结合多级视觉特征以解决自回归视觉语言模型推理时计算开销大的问题。

**关键词**：视觉语言模型, 令牌组合, 推理效率, 多级特征融合, 动态令牌选择

## 3 点简述
- 当前自回归视觉语言模型依赖大量视觉令牌，导致推理计算需求高。
- 方法结合掩码对象表示、全局令牌和局部补丁令牌，创建紧凑且信息丰富的视觉表示。
- 实验显示，模型在测试时可灵活减少令牌数量，性能接近基线，仅需少量视觉令牌。

## 摘要（原文）

> Current autoregressive Vision Language Models (VLMs) usually rely on a large number of visual tokens to represent images, resulting in a need for more compute especially at inference time. To address this problem, we propose Mask-LLaVA, a framework that leverages different levels of visual features to create a compact yet information-rich visual representation for autoregressive VLMs. Namely, we combine mask-based object representations together with global tokens and local patch tokens. While all tokens are used during training, it shows that the resulting model can flexibly drop especially the number of mask-based object-tokens at test time, allowing to adapt the number of tokens during inference without the need to retrain the model and without a significant drop in performance. We evaluate the proposed approach on a suite of standard benchmarks showing results competitive to current token efficient methods and comparable to the original LLaVA baseline using only a fraction of visual tokens. Our analysis demonstrates that combining multi-level features enables efficient learning with fewer tokens while allowing dynamic token selection at test time for good performance.

