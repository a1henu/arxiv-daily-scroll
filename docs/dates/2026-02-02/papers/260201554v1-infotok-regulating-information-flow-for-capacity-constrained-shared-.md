---
layout: default
title: InfoTok: Regulating Information Flow for Capacity-Constrained Shared Visual Tokenization in Unified MLLMs
---

# InfoTok: Regulating Information Flow for Capacity-Constrained Shared Visual Tokenization in Unified MLLMs
**arXiv**：[2602.01554v1](https://arxiv.org/abs/2602.01554) · [PDF](https://arxiv.org/pdf/2602.01554.pdf)  
**作者**：Lv Tang, Tianyi Zheng, Bo Li, Xingyu Li  

**一句话要点**：提出InfoTok信息正则化视觉分词机制，以解决统一多模态大模型中共享分词的信息流调控问题。

**关键词**：统一多模态大模型, 视觉分词, 信息瓶颈, 信息正则化, 共享令牌空间, 容量约束

## 3 点简述
- 核心问题：统一多模态大模型中共享视觉分词缺乏明确信息保留准则，影响理解与生成任务。
- 方法要点：基于信息瓶颈原理，通过互信息正则化控制图像到共享令牌的信息流，平衡压缩与任务相关性。
- 实验或效果：在三个代表性统一多模态大模型中集成InfoTok，无需额外数据，理解与生成任务均获提升。

## 摘要（原文）

> Unified multimodal large language models (MLLMs) integrate image understanding and generation in a single framework, with the visual tokenizer acting as the sole interface that maps visual inputs into tokens for downstream tasks. However, existing shared-token designs are mostly architecture-driven and lack an explicit criterion for what information tokens should preserve to support both understanding and generation. Therefore, we introduce a capacity-constrained perspective, highlighting that in shared-token unified MLLMs the visual tokenizer behaves as a compute-bounded learner, so the token budget should prioritize reusable structure over hard-to-exploit high-entropy variations and redundancy. Motivated by this perspective, we propose InfoTok, an information-regularized visual tokenization mechanism grounded in the Information Bottleneck (IB) principle. InfoTok formulates tokenization as controlling information flow from images to shared tokens to multimodal outputs, yielding a principled trade-off between compression and task relevance via mutual-information regularization. We integrate InfoTok into three representative unified MLLMs without introducing any additional training data. Experiments show consistent improvements on both understanding and generation, supporting information-regularized tokenization as a principled foundation for learning a shared token space in unified MLLMs.

