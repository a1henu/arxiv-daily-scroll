---
layout: default
title: SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning
---

# SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning
**arXiv**：[2603.05437v1](https://arxiv.org/abs/2603.05437) · [PDF](https://arxiv.org/pdf/2603.05437.pdf)  
**作者**：Ye-Chan Kim, SeungJu Cha, Si-Woo Kim, Minju Jeon, Hyungee Kim, Dong-Jin Kim  

**一句话要点**：提出SAIL方法，通过相似性感知训练和跨字幕增强，解决弱监督密集视频描述中语义对齐和标注稀疏问题。

**关键词**：弱监督密集视频描述, 语义对齐, 跨模态学习, 大语言模型增强, 视频事件定位

## 3 点简述
- 核心问题：现有方法生成掩码时忽略语义关系，且依赖稀疏标注导致性能受限。
- 方法要点：引入相似性感知训练指导掩码对齐事件描述，并基于LLM生成合成字幕增强对齐信号。
- 实验或效果：在ActivityNet Captions和YouCook2数据集上实现描述和定位指标的先进性能。

## 摘要（原文）

> Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically meaningful regions. Moreover, relying solely on ground-truth captions leads to sub-optimal performance due to the inherent sparsity of existing datasets. In this work, we propose SAIL, which constructs semantically-aware masks through cross-modal alignment. Our similarity aware training objective guides masks to emphasize video regions with high similarity to their corresponding event captions. Furthermore, to guide more accurate mask generation under sparse annotation settings, we introduce an LLM-based augmentation strategy that generates synthetic captions to provide additional alignment signals. These synthetic captions are incorporated through an inter-mask mechanism, providing auxiliary guidance for precise temporal localization without degrading the main objective. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance on both captioning and localization metrics.

