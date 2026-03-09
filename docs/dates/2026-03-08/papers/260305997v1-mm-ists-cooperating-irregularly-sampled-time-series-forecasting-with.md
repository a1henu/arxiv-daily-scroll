---
layout: default
title: MM-ISTS: Cooperating Irregularly Sampled Time Series Forecasting with Multimodal Vision-Text LLMs
---

# MM-ISTS: Cooperating Irregularly Sampled Time Series Forecasting with Multimodal Vision-Text LLMs
**arXiv**：[2603.05997v1](https://arxiv.org/abs/2603.05997) · [PDF](https://arxiv.org/pdf/2603.05997.pdf)  
**作者**：Zhi Lei, Chenxi Liu, Hao Miao, Wanghui Qiu, Bin Yang, Chenjuan Guo  

**一句话要点**：提出MM-ISTS框架，利用多模态视觉-文本大语言模型提升不规则采样时间序列预测性能。

**关键词**：不规则采样时间序列预测, 多模态大语言模型, 视觉-文本编码, 自适应特征提取, 模态对齐

## 3 点简述
- 核心问题：现有方法仅依赖历史观测，难以学习上下文语义和细粒度时间模式。
- 方法要点：设计两阶段编码机制，结合视觉-文本编码和ISTS编码，并引入自适应查询特征提取器。
- 实验或效果：在真实数据上广泛实验验证了框架的有效性。

## 摘要（原文）

> Irregularly sampled time series (ISTS) are widespread in real-world scenarios, exhibiting asynchronous observations on uneven time intervals across variables. Existing ISTS forecasting methods often solely utilize historical observations to predict future ones while falling short in learning contextual semantics and fine-grained temporal patterns. To address these problems, we achieve MM-ISTS, a multimodal framework augmented by vision-text large language models, that bridges temporal, visual, and textual modalities, facilitating ISTS forecasting. MM-ISTS encompasses a novel two-stage encoding mechanism. In particular, a cross-modal vision-text encoding module is proposed to automatically generate informative visual images and textual data, enabling the capture of intricate temporal patterns and comprehensive contextual understanding, in collaboration with multimodal LLMs (MLLMs). In parallel, ISTS encoding extracts complementary yet enriched temporal features from historical ISTS observations, including multi-view embedding fusion and a temporal-variable encoder. Further, we propose an adaptive query-based feature extractor to compress the learned tokens of MLLMs, filtering out small-scale useful knowledge, which in turn reduces computational costs. In addition, a multimodal alignment module with modality-aware gating is designed to alleviate the modality gap across ISTS, images, and text. Extensive experiments on real data offer insight into the effectiveness of the proposed solutions.

