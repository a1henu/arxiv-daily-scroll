---
layout: default
title: Vectorized Video Representation with Easy Editing via Hierarchical Spatio-Temporally Consistent Proxy Embedding
---

# Vectorized Video Representation with Easy Editing via Hierarchical Spatio-Temporally Consistent Proxy Embedding
**arXiv**：[2510.12256v1](https://arxiv.org/abs/2510.12256) · [PDF](https://arxiv.org/pdf/2510.12256.pdf)  
**作者**：Ye Chen, Liming Tan, Yupeng Zhu, Yuanbin Wang, Bingbing Ni  

**一句话要点**：提出分层时空一致代理嵌入以实现稳定视频表示与易编辑

**关键词**：视频表示学习, 时空一致性, 代理节点, 视频编辑, 分层结构

## 3 点简述
- 问题：现有视频表示依赖像素级跟踪，易受跟踪误差、遮挡和大运动影响。
- 方法：使用分层代理节点稳定表达多尺度对象，并动态更新以利用时空先验。
- 效果：实验显示高重建精度、少参数，支持视频修复和关键帧编辑任务。

## 摘要（原文）

> Current video representations heavily rely on unstable and over-grained
> priors for motion and appearance modelling, \emph{i.e.}, pixel-level matching
> and tracking. A tracking error of just a few pixels would lead to the collapse
> of the visual object representation, not to mention occlusions and large motion
> frequently occurring in videos. To overcome the above mentioned vulnerability,
> this work proposes spatio-temporally consistent proxy nodes to represent
> dynamically changing objects/scenes in the video. On the one hand, the
> hierarchical proxy nodes have the ability to stably express the multi-scale
> structure of visual objects, so they are not affected by accumulated tracking
> error, long-term motion, occlusion, and viewpoint variation. On the other hand,
> the dynamic representation update mechanism of the proxy nodes adequately
> leverages spatio-temporal priors of the video to mitigate the impact of
> inaccurate trackers, thereby effectively handling drastic changes in scenes and
> objects. Additionally, the decoupled encoding manner of the shape and texture
> representations across different visual objects in the video facilitates
> controllable and fine-grained appearance editing capability. Extensive
> experiments demonstrate that the proposed representation achieves high video
> reconstruction accuracy with fewer parameters and supports complex video
> processing tasks, including video in-painting and keyframe-based temporally
> consistent video editing.

