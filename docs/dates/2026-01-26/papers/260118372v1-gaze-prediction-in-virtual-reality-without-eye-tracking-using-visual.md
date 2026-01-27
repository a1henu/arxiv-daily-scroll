---
layout: default
title: Gaze Prediction in Virtual Reality Without Eye Tracking Using Visual and Head Motion Cues
---

# Gaze Prediction in Virtual Reality Without Eye Tracking Using Visual and Head Motion Cues
**arXiv**：[2601.18372v1](https://arxiv.org/abs/2601.18372) · [PDF](https://arxiv.org/pdf/2601.18372.pdf)  
**作者**：Christos Petrou, Harris Partaourides, Athanasios Balomenos, Yannis Kopsinis, Sotirios Chatzis  

**一句话要点**：提出结合视觉显著性与头部运动的无眼动追踪VR注视预测框架，以降低感知延迟。

**关键词**：虚拟现实, 注视预测, 视觉显著性, 头部运动, 时间序列预测, 无眼动追踪

## 3 点简述
- 核心问题：VR中眼动追踪常因硬件限制或隐私问题不可用，需预测注视方向以支持如注视点渲染等技术。
- 方法要点：使用UniSal提取视频帧视觉特征，融合HMD运动数据，通过TSMixer或LSTM时间序列模块预测未来注视方向。
- 实验或效果：在EHTask数据集和商业VR硬件上评估，优于Center-of-HMD和Mean Gaze基线，减少感知滞后。

## 摘要（原文）

> Gaze prediction plays a critical role in Virtual Reality (VR) applications by reducing sensor-induced latency and enabling computationally demanding techniques such as foveated rendering, which rely on anticipating user attention. However, direct eye tracking is often unavailable due to hardware limitations or privacy concerns. To address this, we present a novel gaze prediction framework that combines Head-Mounted Display (HMD) motion signals with visual saliency cues derived from video frames. Our method employs UniSal, a lightweight saliency encoder, to extract visual features, which are then fused with HMD motion data and processed through a time-series prediction module. We evaluate two lightweight architectures, TSMixer and LSTM, for forecasting future gaze directions. Experiments on the EHTask dataset, along with deployment on commercial VR hardware, show that our approach consistently outperforms baselines such as Center-of-HMD and Mean Gaze. These results demonstrate the effectiveness of predictive gaze modeling in reducing perceptual lag and enhancing natural interaction in VR environments where direct eye tracking is constrained.

