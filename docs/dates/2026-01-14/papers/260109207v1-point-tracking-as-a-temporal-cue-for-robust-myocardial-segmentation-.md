---
layout: default
title: Point Tracking as a Temporal Cue for Robust Myocardial Segmentation in Echocardiography Videos
---

# Point Tracking as a Temporal Cue for Robust Myocardial Segmentation in Echocardiography Videos
**arXiv**：[2601.09207v1](https://arxiv.org/abs/2601.09207) · [PDF](https://arxiv.org/pdf/2601.09207.pdf)  
**作者**：Bahar Khodabakhshian, Nima Hashemi, Armin Saadat, Zahra Gholami, In-Chang Hwang, Samira Sojoudi, Christina Luong, Purang Abolmaesumi, Teresa Tsang  

**一句话要点**：提出Point-Seg，通过点追踪作为时序线索，提升超声心动图视频中心肌分割的鲁棒性。

**关键词**：心肌分割, 超声心动图, 点追踪, 时序一致性, Transformer, 视频分割

## 3 点简述
- 心肌分割在超声心动图视频中因低对比度和噪声而困难，传统方法忽略时序或累积误差。
- Point-Seg基于Transformer，集成点追踪模块提供运动感知信号，避免基于记忆的特征传播。
- 在公开和私有数据集上验证，Point-Seg在低质量数据中精度更高，并提供像素级运动信息。

## 摘要（原文）

> Purpose: Myocardium segmentation in echocardiography videos is a challenging task due to low contrast, noise, and anatomical variability. Traditional deep learning models either process frames independently, ignoring temporal information, or rely on memory-based feature propagation, which accumulates error over time. Methods: We propose Point-Seg, a transformer-based segmentation framework that integrates point tracking as a temporal cue to ensure stable and consistent segmentation of myocardium across frames. Our method leverages a point-tracking module trained on a synthetic echocardiography dataset to track key anatomical landmarks across video sequences. These tracked trajectories provide an explicit motion-aware signal that guides segmentation, reducing drift and eliminating the need for memory-based feature accumulation. Additionally, we incorporate a temporal smoothing loss to further enhance temporal consistency across frames. Results: We evaluate our approach on both public and private echocardiography datasets. Experimental results demonstrate that Point-Seg has statistically similar accuracy in terms of Dice to state-of-the-art segmentation models in high quality echo data, while it achieves better segmentation accuracy in lower quality echo with improved temporal stability. Furthermore, Point-Seg has the key advantage of pixel-level myocardium motion information as opposed to other segmentation methods. Such information is essential in the computation of other downstream tasks such as myocardial strain measurement and regional wall motion abnormality detection. Conclusion: Point-Seg demonstrates that point tracking can serve as an effective temporal cue for consistent video segmentation, offering a reliable and generalizable approach for myocardium segmentation in echocardiography videos. The code is available at https://github.com/DeepRCL/PointSeg.

