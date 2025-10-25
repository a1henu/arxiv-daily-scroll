---
layout: default
title: GMFVAD: Using Grained Multi-modal Feature to Improve Video Anomaly Detection
---

# GMFVAD: Using Grained Multi-modal Feature to Improve Video Anomaly Detection
**arXiv**：[2510.20268v1](https://arxiv.org/abs/2510.20268) · [PDF](https://arxiv.org/pdf/2510.20268.pdf)  
**作者**：Guangyu Dai, Dong Chen, Siliang Tang, Yueting Zhuang  

**一句话要点**：提出GMFVAD方法，利用细粒度多模态特征减少冗余信息以改进视频异常检测。

**关键词**：视频异常检测, 多模态特征, 冗余减少, 细粒度融合, 文本增强

## 3 点简述
- 核心问题：现有视频异常检测方法在多模态融合中存在冗余信息，影响检测准确性。
- 方法要点：基于视频片段生成细粒度多模态特征，结合文本特征增强视觉特征。
- 实验或效果：在四个主要数据集上达到SOTA性能，消融实验验证冗余减少的有效性。

## 摘要（原文）

> Video anomaly detection (VAD) is a challenging task that detects anomalous
> frames in continuous surveillance videos. Most previous work utilizes the
> spatio-temporal correlation of visual features to distinguish whether there are
> abnormalities in video snippets. Recently, some works attempt to introduce
> multi-modal information, like text feature, to enhance the results of video
> anomaly detection. However, these works merely incorporate text features into
> video snippets in a coarse manner, overlooking the significant amount of
> redundant information that may exist within the video snippets. Therefore, we
> propose to leverage the diversity among multi-modal information to further
> refine the extracted features, reducing the redundancy in visual features, and
> we propose Grained Multi-modal Feature for Video Anomaly Detection (GMFVAD).
> Specifically, we generate more grained multi-modal feature based on the video
> snippet, which summarizes the main content, and text features based on the
> captions of original video will be introduced to further enhance the visual
> features of highlighted portions. Experiments show that the proposed GMFVAD
> achieves state-of-the-art performance on four mainly datasets. Ablation
> experiments also validate that the improvement of GMFVAD is due to the
> reduction of redundant information.

