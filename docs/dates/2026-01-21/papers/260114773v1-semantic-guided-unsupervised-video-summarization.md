---
layout: default
title: Semantic-Guided Unsupervised Video Summarization
---

# Semantic-Guided Unsupervised Video Summarization
**arXiv**：[2601.14773v1](https://arxiv.org/abs/2601.14773) · [PDF](https://arxiv.org/pdf/2601.14773.pdf)  
**作者**：Haizhou Liu, Haodong Jin, Yiming Wang, Hui Yu  

**一句话要点**：提出语义引导的无监督视频摘要方法，通过语义对齐注意力机制和增量训练提升关键帧选择与生成稳定性。

**关键词**：视频摘要, 无监督学习, 语义引导, 注意力机制, 生成对抗网络, 增量训练

## 3 点简述
- 现有无监督方法依赖GAN但忽视语义引导，导致训练不稳定和关键帧选择不足。
- 设计帧级语义对齐注意力机制，集成到关键帧选择器中，指导Transformer生成器重构视频。
- 采用增量训练策略逐步更新模型组件，在多个基准数据集上实现优越性能。

## 摘要（原文）

> Video summarization is a crucial technique for social understanding, enabling efficient browsing of massive multimedia content and extraction of key information from social platforms. Most existing unsupervised summarization methods rely on Generative Adversarial Networks (GANs) to enhance keyframe selection and generate coherent, video summaries through adversarial training. However, such approaches primarily exploit unimodal features, overlooking the guiding role of semantic information in keyframe selection, and often suffer from unstable training. To address these limitations, we propose a novel Semantic-Guided Unsupervised Video Summarization method. Specifically, we design a novel frame-level semantic alignment attention mechanism and integrate it into a keyframe selector, which guides the Transformer-based generator within the adversarial framework to better reconstruct videos. In addition, we adopt an incremental training strategy to progressively update the model components, effectively mitigating the instability of GAN training. Experimental results demonstrate that our approach achieves superior performance on multiple benchmark datasets.

