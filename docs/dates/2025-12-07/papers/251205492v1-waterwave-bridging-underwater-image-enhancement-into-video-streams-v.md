---
layout: default
title: WaterWave: Bridging Underwater Image Enhancement into Video Streams via Wavelet-based Temporal Consistency Field
---

# WaterWave: Bridging Underwater Image Enhancement into Video Streams via Wavelet-based Temporal Consistency Field
**arXiv**：[2512.05492v1](https://arxiv.org/abs/2512.05492) · [PDF](https://arxiv.org/pdf/2512.05492.pdf)  
**作者**：Qi Zhu, Jingyi Zhang, Naishan Zheng, Wei Yu, Jinghao Zhang, Deyi Ji, Feng Zhao  

**一句话要点**：提出WaterWave方法，通过小波时域一致性场解决水下视频增强中的时序不一致问题。

**关键词**：水下视频增强, 时序一致性, 小波变换, 隐式表示, 水下流校正

## 3 点简述
- 核心问题：现有水下视频增强方法直接逐帧应用单图模型，导致时序不一致。
- 方法要点：基于局部时域频率先验，在小波时域一致性场中隐式表示增强视频，过滤不一致成分并保留运动细节。
- 实验或效果：显著提升单图增强视频质量，在下游跟踪任务中表现优异，如UOSTrack和MAT精度分别提升19.7%和9.7%。

## 摘要（原文）

> Underwater video pairs are fairly difficult to obtain due to the complex underwater imaging. In this case, most existing video underwater enhancement methods are performed by directly applying the single-image enhancement model frame by frame, but a natural issue is lacking temporal consistency. To relieve the problem, we rethink the temporal manifold inherent in natural videos and observe a temporal consistency prior in dynamic scenes from the local temporal frequency perspective. Building upon the specific prior and no paired-data condition, we propose an implicit representation manner for enhanced video signals, which is conducted in the wavelet-based temporal consistency field, WaterWave. Specifically, under the constraints of the prior, we progressively filter and attenuate the inconsistent components while preserving motion details and scenes, achieving a natural-flowing video. Furthermore, to represent temporal frequency bands more accurately, an underwater flow correction module is designed to rectify estimated flows considering the transmission in underwater scenes. Extensive experiments demonstrate that WaterWave significantly enhances the quality of videos generated using single-image underwater enhancements. Additionally, our method demonstrates high potential in downstream underwater tracking tasks, such as UOSTrack and MAT, outperforming the original video by a large margin, i.e., 19.7% and 9.7% on precise respectively.

