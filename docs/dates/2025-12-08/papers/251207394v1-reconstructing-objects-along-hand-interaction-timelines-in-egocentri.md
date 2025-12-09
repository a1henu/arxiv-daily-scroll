---
layout: default
title: Reconstructing Objects along Hand Interaction Timelines in Egocentric Video
---

# Reconstructing Objects along Hand Interaction Timelines in Egocentric Video
**arXiv**：[2512.07394v1](https://arxiv.org/abs/2512.07394) · [PDF](https://arxiv.org/pdf/2512.07394.pdf)  
**作者**：Zhifan Zhu, Siddhant Bansal, Shashank Tripathi, Dima Damen  

**一句话要点**：提出ROHIT任务与COP框架，通过手交互时间线约束优化物体姿态传播，提升第一人称视频中物体重建精度。

**关键词**：第一人称视频, 物体重建, 手交互时间线, 姿态传播, 约束优化, 稳定抓取

## 3 点简述
- 核心问题：在第一人称视频中，如何基于手交互时间线（HIT）重建物体姿态，尤其关注稳定抓取阶段。
- 方法要点：定义HIT并建模姿态约束，提出COP框架进行约束优化与姿态传播，无需3D真值标注。
- 实验或效果：在HOT3D和EPIC-Kitchens数据集上评估，COP提升稳定抓取重建6.2-11.3%，HIT重建最高达24.5%。

## 摘要（原文）

> We introduce the task of Reconstructing Objects along Hand Interaction Timelines (ROHIT). We first define the Hand Interaction Timeline (HIT) from a rigid object's perspective. In a HIT, an object is first static relative to the scene, then is held in hand following contact, where its pose changes. This is usually followed by a firm grip during use, before it is released to be static again w.r.t. to the scene. We model these pose constraints over the HIT, and propose to propagate the object's pose along the HIT enabling superior reconstruction using our proposed Constrained Optimisation and Propagation (COP) framework. Importantly, we focus on timelines with stable grasps - i.e. where the hand is stably holding an object, effectively maintaining constant contact during use. This allows us to efficiently annotate, study, and evaluate object reconstruction in videos without 3D ground truth. We evaluate our proposed task, ROHIT, over two egocentric datasets, HOT3D and in-the-wild EPIC-Kitchens. In HOT3D, we curate 1.2K clips of stable grasps. In EPIC-Kitchens, we annotate 2.4K clips of stable grasps including 390 object instances across 9 categories from videos of daily interactions in 141 environments. Without 3D ground truth, we utilise 2D projection error to assess the reconstruction. Quantitatively, COP improves stable grasp reconstruction by 6.2-11.3% and HIT reconstruction by up to 24.5% with constrained pose propagation.

