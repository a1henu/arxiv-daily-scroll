---
layout: default
title: Real Eyes Realize Faster: Gaze Stability and Pupil Novelty for Efficient Egocentric Learning
---

# Real Eyes Realize Faster: Gaze Stability and Pupil Novelty for Efficient Egocentric Learning
**arXiv**：[2603.04098v1](https://arxiv.org/abs/2603.04098) · [PDF](https://arxiv.org/pdf/2603.04098.pdf)  
**作者**：Ajan Subramanian, Sumukh Bettadapura, Rohan Sathish  

**一句话要点**：提出基于注视稳定性和瞳孔响应的双准则帧策展方法，以提升头戴式设备上自我中心视频的学习效率。

**关键词**：自我中心学习, 帧策展, 眼动追踪, 注视稳定性, 瞳孔响应, 活动识别

## 3 点简述
- 问题：头戴式自我中心摄像头产生冗余低质量帧，受存储和电池限制需高效选择帧。
- 方法：利用眼动追踪数据，通过注视稳定性筛选高质量帧，再基于瞳孔响应排序新颖帧。
- 效果：在10%预算下策展帧达到全流分类性能，瞳孔排序提升活动识别，注视筛选主导场景识别。

## 摘要（原文）

> Always-on egocentric cameras are increasingly used as demonstrations for embodied robotics, imitation learning, and assistive AR, but the resulting video streams are dominated by redundant and low-quality frames. Under the storage and battery constraints of wearable devices, choosing which frames to keep is as important as how to learn from them. We observe that modern eye-tracking headsets provide a continuous, training-free side channel that decomposes into two complementary axes: gaze fixation captures visual stability (quality), while pupil response captures arousal-linked moments (novelty). We operationalize this insight as a Dual-Criterion Frame Curator that first gates frames by gaze quality and then ranks the survivors by pupil-derived novelty. On the Visual Experience Dataset (VEDB), curated frames at 10% budget match the classification performance of the full stream, and naive signal fusion consistently destroys both contributions. The benefit is task-dependent: pupil ranking improves activity recognition, while gaze-only selection already dominates for scene recognition, confirming that the two signals serve genuinely different roles. Our method requires no model inference and operates at capture time, offering a path toward efficient, always-on egocentric data curation.

