---
layout: default
title: S3-CLIP: Video Super Resolution for Person-ReID
---

# S3-CLIP: Video Super Resolution for Person-ReID
**arXiv**：[2601.08807v1](https://arxiv.org/abs/2601.08807) · [PDF](https://arxiv.org/pdf/2601.08807.pdf)  
**作者**：Tamas Endrei, Gyorgy Cserey  

**一句话要点**：提出S3-CLIP框架，通过视频超分辨率提升行人重识别轨迹质量，应对跨视角挑战。

**关键词**：视频超分辨率, 行人重识别, 轨迹质量增强, 跨视角识别, CLIP框架

## 3 点简述
- 核心问题：现有行人重识别方法忽视轨迹质量，在真实复杂场景中部署受限。
- 方法要点：集成超分辨率网络与任务驱动管道，适配视频行人重识别，首次系统研究视频超分辨率增强轨迹质量。
- 实验或效果：在VReID-XFD挑战中，性能与基线竞争，地面到空中场景排名准确率显著提升。

## 摘要（原文）

> Tracklet quality is often treated as an afterthought in most person re-identification (ReID) methods, with the majority of research presenting architectural modifications to foundational models. Such approaches neglect an important limitation, posing challenges when deploying ReID systems in real-world, difficult scenarios. In this paper, we introduce S3-CLIP, a video super-resolution-based CLIP-ReID framework developed for the VReID-XFD challenge at WACV 2026. The proposed method integrates recent advances in super-resolution networks with task-driven super-resolution pipelines, adapting them to the video-based person re-identification setting. To the best of our knowledge, this work represents the first systematic investigation of video super-resolution as a means of enhancing tracklet quality for person ReID, particularly under challenging cross-view conditions. Experimental results demonstrate performance competitive with the baseline, achieving 37.52% mAP in aerial-to-ground and 29.16% mAP in ground-to-aerial scenarios. In the ground-to-aerial setting, S3-CLIP achieves substantial gains in ranking accuracy, improving Rank-1, Rank-5, and Rank-10 performance by 11.24%, 13.48%, and 17.98%, respectively.

