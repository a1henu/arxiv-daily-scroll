---
layout: default
title: Solution to the 10th ABAW Expression Recognition Challenge: A Robust Multimodal Framework with Safe Cross-Attention and Modality Dropout
---

# Solution to the 10th ABAW Expression Recognition Challenge: A Robust Multimodal Framework with Safe Cross-Attention and Modality Dropout
**arXiv**：[2603.08034v1](https://arxiv.org/abs/2603.08034) · [PDF](https://arxiv.org/pdf/2603.08034.pdf)  
**作者**：Jun Yu, Naixiang Zheng, Guoyuan Wang, Yunxiang Zhang, Lingsi Zhu, Jiaen Liang, Wei Huang, Shengping Liu  

**一句话要点**：提出基于安全跨注意力和模态丢失的多模态框架，以解决ABAW表情识别中的遮挡、模态缺失和类别不平衡问题。

**关键词**：多模态融合, 表情识别, Transformer架构, 类别不平衡, 模态丢失, 安全跨注意力

## 3 点简述
- 核心问题：真实环境中表情识别受遮挡、模态缺失和类别不平衡影响，尤其在Aff-Wild2数据集上。
- 方法要点：采用双分支Transformer，结合安全跨注意力机制和模态丢失策略，动态融合视觉和音频表示。
- 实验或效果：在Aff-Wild2验证集上达到60.79%准确率和0.5029 F1分数，有效处理缺失模态和时空依赖。

## 摘要（原文）

> Emotion recognition in real-world environments is hindered by partial occlusions, missing modalities, and severe class imbalance. To address these issues, particularly for the Affective Behavior Analysis in-the-wild (ABAW) Expression challenge, we propose a multimodal framework that dynamically fuses visual and audio representations. Our approach uses a dual-branch Transformer architecture featuring a safe cross-attention mechanism and a modality dropout strategy. This design allows the network to rely on audio-based predictions when visual cues are absent. To mitigate the long-tail distribution of the Aff-Wild2 dataset, we apply focal loss optimization, combined with a sliding-window soft voting strategy to capture dynamic emotional transitions and reduce frame-level classification jitter. Experiments demonstrate that our framework effectively handles missing modalities and complex spatiotemporal dependencies, achieving an accuracy of 60.79% and an F1-score of 0.5029 on the Aff-Wild2 validation set.

