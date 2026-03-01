---
layout: default
title: Velocity and stroke rate reconstruction of canoe sprint team boats based on panned and zoomed video recordings
---

# Velocity and stroke rate reconstruction of canoe sprint team boats based on panned and zoomed video recordings
**arXiv**：[2602.22941v1](https://arxiv.org/abs/2602.22941) · [PDF](https://arxiv.org/pdf/2602.22941.pdf)  
**作者**：Julian Ziegler, Daniel Matthes, Finn Gerdts, Patrick Frenzel, Torsten Warnke, Matthias Englert, Tina Koevari, Mirco Fuchs  

**一句话要点**：提出基于平移缩放视频的皮划艇团队船速与划桨率重建框架，以替代GPS进行自动化性能分析。

**关键词**：视频分析, 目标检测, 光流跟踪, 性能重建, 皮划艇冲刺

## 3 点简述
- 核心问题：皮划艇冲刺中，GPS分析受限，需自动化视频方案重建速度与划桨率。
- 方法要点：利用YOLOv8检测浮标和运动员，通过U-net校准船头位置，结合光流跟踪多运动员船型。
- 实验或效果：与精英比赛GPS数据对比，速度RRMSE为0.020±0.011，划桨率RRMSE为0.022±0.024，提供高精度自动化反馈。

## 摘要（原文）

> Pacing strategies, defined by velocity and stroke rate profiles, are essential for peak performance in canoe sprint. While GPS is the gold standard for analysis, its limited availability necessitates automated video-based solutions. This paper presents an extended framework for reconstructing performance metrics from panned and zoomed video recordings across all sprint disciplines (K1-K4, C1-C2) and distances (200m-500m). Our method utilizes YOLOv8 for buoy and athlete detection, leveraging the known buoy grid to estimate homographies. We generalized the estimation of the boat position by means of learning a boat-specific athlete offset using a U-net based boat tip calibration. Further, we implement a robust tracking scheme using optical flow to adapt to multi-athlete boat types. Finally, we introduce methods to extract stroke rate information from either pose estimations or the athlete bounding boxes themselves. Evaluation against GPS data from elite competitions yields a velocity RRMSE of 0.020 +- 0.011 (rho = 0.956) and a stroke rate RRMSE of 0.022 +- 0.024 (rho = 0.932). The methods provide coaches with highly accurate, automated feedback without requiring on-boat sensors or manual annotation.

