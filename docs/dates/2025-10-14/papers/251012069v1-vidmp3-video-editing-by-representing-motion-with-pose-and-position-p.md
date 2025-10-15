---
layout: default
title: VIDMP3: Video Editing by Representing Motion with Pose and Position Priors
---

# VIDMP3: Video Editing by Representing Motion with Pose and Position Priors
**arXiv**：[2510.12069v1](https://arxiv.org/abs/2510.12069) · [PDF](https://arxiv.org/pdf/2510.12069.pdf)  
**作者**：Sandeep Mishra, Oindrila Saha, Alan C. Bovik  

**一句话要点**：提出VidMP3方法，利用姿态和位置先验解决运动保持视频编辑中的结构灵活性问题。

**关键词**：视频编辑, 运动表示, 姿态先验, 位置先验, 扩散模型, 时间一致性

## 3 点简述
- 核心问题：现有视频编辑方法在结构可变编辑中存在时间不一致、主体身份漂移等问题。
- 方法要点：基于姿态和位置先验学习广义运动表示，实现运动保持与结构语义灵活编辑。
- 实验或效果：定性和定量评估显示优于现有方法，代码将开源。

## 摘要（原文）

> Motion-preserved video editing is crucial for creators, particularly in
> scenarios that demand flexibility in both the structure and semantics of
> swapped objects. Despite its potential, this area remains underexplored.
> Existing diffusion-based editing methods excel in structure-preserving tasks,
> using dense guidance signals to ensure content integrity. While some recent
> methods attempt to address structure-variable editing, they often suffer from
> issues such as temporal inconsistency, subject identity drift, and the need for
> human intervention. To address these challenges, we introduce VidMP3, a novel
> approach that leverages pose and position priors to learn a generalized motion
> representation from source videos. Our method enables the generation of new
> videos that maintain the original motion while allowing for structural and
> semantic flexibility. Both qualitative and quantitative evaluations demonstrate
> the superiority of our approach over existing methods. The code will be made
> publicly available at https://github.com/sandeep-sm/VidMP3.

