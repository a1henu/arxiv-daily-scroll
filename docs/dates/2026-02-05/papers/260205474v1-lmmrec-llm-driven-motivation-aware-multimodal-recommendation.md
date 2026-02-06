---
layout: default
title: LMMRec: LLM-driven Motivation-aware Multimodal Recommendation
---

# LMMRec: LLM-driven Motivation-aware Multimodal Recommendation
**arXiv**：[2602.05474v1](https://arxiv.org/abs/2602.05474) · [PDF](https://arxiv.org/pdf/2602.05474.pdf)  
**作者**：Yicheng Di, Zhanjie Zhang, Yun Wangc, Jinren Liue, Jiaqi Yanf, Jiyu Wei, Xiangyu Chend, Yuan Liu  

**一句话要点**：提出LMMRec框架，利用大语言模型解决多模态推荐中动机建模的跨模态对齐与噪声问题。

**关键词**：多模态推荐, 动机建模, 大语言模型, 跨模态对齐, 对比学习

## 3 点简述
- 核心问题：多模态动机融合面临跨模态对齐不稳定和特征识别困难，现有方法忽略文本等异构信息。
- 方法要点：使用链式思维提示提取细粒度动机，双编码器架构结合对比学习和动量更新实现跨模态对齐与噪声缓解。
- 实验或效果：在三个数据集上实验，性能提升最高达4.98%。

## 摘要（原文）

> Motivation-based recommendation systems uncover user behavior drivers. Motivation modeling, crucial for decision-making and content preference, explains recommendation generation. Existing methods often treat motivation as latent variables from interaction data, neglecting heterogeneous information like review text. In multimodal motivation fusion, two challenges arise: 1) achieving stable cross-modal alignment amid noise, and 2) identifying features reflecting the same underlying motivation across modalities. To address these, we propose LLM-driven Motivation-aware Multimodal Recommendation (LMMRec), a model-agnostic framework leveraging large language models for deep semantic priors and motivation understanding. LMMRec uses chain-of-thought prompting to extract fine-grained user and item motivations from text. A dual-encoder architecture models textual and interaction-based motivations for cross-modal alignment, while Motivation Coordination Strategy and Interaction-Text Correspondence Method mitigate noise and semantic drift through contrastive learning and momentum updates. Experiments on three datasets show LMMRec achieves up to a 4.98\% performance improvement.

