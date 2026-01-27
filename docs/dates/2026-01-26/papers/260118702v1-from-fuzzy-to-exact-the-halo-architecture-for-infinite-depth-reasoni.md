---
layout: default
title: From Fuzzy to Exact: The Halo Architecture for Infinite-Depth Reasoning via Rational Arithmetic
---

# From Fuzzy to Exact: The Halo Architecture for Infinite-Depth Reasoning via Rational Arithmetic
**arXiv**：[2601.18702v1](https://arxiv.org/abs/2601.18702) · [PDF](https://arxiv.org/pdf/2601.18702.pdf)  
**作者**：Hansheng Ren  

**一句话要点**：提出Halo架构，通过有理数算术实现无限深度推理，以解决大语言模型中的数值误差累积问题。

**关键词**：有理数算术, 精确推理单元, 无限深度推理, 大语言模型, 数值误差, AGI

## 3 点简述
- 核心问题：当前深度学习依赖浮点近似，导致大语言模型在深度推理中出现幻觉和逻辑不一致。
- 方法要点：引入Halo架构，基于有理数算术和精确推理单元，支持任意精度计算。
- 实验或效果：在Huginn-0125原型上验证，Halo在混沌系统中保持零数值发散，而BF16基线崩溃。

## 摘要（原文）

> Current paradigms in Deep Learning prioritize computational throughput over numerical precision, relying on the assumption that intelligence emerges from statistical correlation at scale. In this paper, we challenge this orthodoxy. We propose the Exactness Hypothesis: that General Intelligence (AGI), specifically high-order causal inference, requires a computational substrate capable of Arbitrary Precision Arithmetic. We argue that the "hallucinations" and logical incoherence seen in current Large Language Models (LLMs) are artifacts of IEEE 754 floating-point approximation errors accumulating over deep compositional functions. To mitigate this, we introduce the Halo Architecture, a paradigm shift to Rational Arithmetic ($\mathbb{Q}$) supported by a novel Exact Inference Unit (EIU). Empirical validation on the Huginn-0125 prototype demonstrates that while 600B-parameter scale BF16 baselines collapse in chaotic systems, Halo maintains zero numerical divergence indefinitely. This work establishes exact arithmetic as a prerequisite for reducing logical uncertainty in System 2 AGI.

