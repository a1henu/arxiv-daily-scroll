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
- 核心问题：多模态动机融合中，跨模态对齐不稳定且难以识别跨模态的相同动机特征。
- 方法要点：使用链式思维提示提取细粒度动机，通过双编码器架构和对比学习实现动机协调与对齐。
- 实验或效果：在三个数据集上，LMMRec实现了最高4.98%的性能提升。

## 摘要（原文）

> Motivation-based recommendation systems uncover user behavior drivers. Motivation modeling, crucial for decision-making and content preference, explains recommendation generation. Existing methods often treat motivation as latent variables from interaction data, neglecting heterogeneous information like review text. In multimodal motivation fusion, two challenges arise: 1) achieving stable cross-modal alignment amid noise, and 2) identifying features reflecting the same underlying motivation across modalities. To address these, we propose LLM-driven Motivation-aware Multimodal Recommendation (LMMRec), a model-agnostic framework leveraging large language models for deep semantic priors and motivation understanding. LMMRec uses chain-of-thought prompting to extract fine-grained user and item motivations from text. A dual-encoder architecture models textual and interaction-based motivations for cross-modal alignment, while Motivation Coordination Strategy and Interaction-Text Correspondence Method mitigate noise and semantic drift through contrastive learning and momentum updates. Experiments on three datasets show LMMRec achieves up to a 4.98\% performance improvement.

