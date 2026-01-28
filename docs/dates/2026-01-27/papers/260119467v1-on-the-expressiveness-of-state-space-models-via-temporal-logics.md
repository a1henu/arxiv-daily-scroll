---
layout: default
title: On the Expressiveness of State Space Models via Temporal Logics
---

# On the Expressiveness of State Space Models via Temporal Logics
**arXiv**：[2601.19467v1](https://arxiv.org/abs/2601.19467) · [PDF](https://arxiv.org/pdf/2601.19467.pdf)  
**作者**：Eric Alsmann, Lowejatan Noori, Martin Lange  

**一句话要点**：分析状态空间模型在有限迹线性时序逻辑下的表达能力，区分不同门控机制和精度的影响。

**关键词**：状态空间模型, 线性时序逻辑, 表达能力分析, 门控机制, 量化模型, 非正则语言

## 3 点简述
- 核心问题：状态空间模型作为Transformer替代架构的表达能力，基于有限迹线性时序逻辑片段和扩展进行分析。
- 方法要点：区分固定宽度算术（量化模型）和无界精度SSM，前者限于正则语言，后者能捕获计数属性和非正则语言。
- 实验或效果：系统比较不同SSM变体与Transformer的表达能力，阐明两者关系，门控机制显著影响表达力。

## 摘要（原文）

> We investigate the expressive power of state space models (SSM), which have recently emerged as a potential alternative to transformer architectures in large language models. Building on recent work, we analyse SSM expressiveness through fragments and extensions of linear temporal logic over finite traces. Our results show that the expressive capabilities of SSM vary substantially depending on the underlying gating mechanism. We further distinguish between SSM operating over fixed-width arithmetic (quantised models), whose expressive power remains within regular languages, and SSM with unbounded precision, which can capture counting properties and non-regular languages. In addition, we provide a systematic comparison between these different SSM variants and known results on transformers, thereby clarifying how the two architectures relate in terms of expressive power.

