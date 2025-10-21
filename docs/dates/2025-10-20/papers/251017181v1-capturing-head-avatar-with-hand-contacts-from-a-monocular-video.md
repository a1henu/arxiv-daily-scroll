---
layout: default
title: Capturing Head Avatar with Hand Contacts from a Monocular Video
---

# Capturing Head Avatar with Hand Contacts from a Monocular Video
**arXiv**：[2510.17181v1](https://arxiv.org/abs/2510.17181) · [PDF](https://arxiv.org/pdf/2510.17181.pdf)  
**作者**：Haonan He, Yufeng Zheng, Jie Song  

**一句话要点**：提出联合学习头部化身与手-脸交互变形框架，以解决单目视频中自然交互建模问题

**关键词**：头部化身建模, 手-脸交互, 单目视频重建, 非刚性变形, PCA基学习, 接触损失

## 3 点简述
- 核心问题：现有方法忽略手-脸交互，导致无法捕捉认知状态如沉思时的自然变形
- 方法要点：结合深度顺序损失与接触正则化进行姿态跟踪，并学习手诱导面部变形的PCA基
- 实验或效果：在iPhone视频和合成数据集上评估，优于SOTA方法，减少穿插伪影

## 摘要（原文）

> Photorealistic 3D head avatars are vital for telepresence, gaming, and VR.
> However, most methods focus solely on facial regions, ignoring natural
> hand-face interactions, such as a hand resting on the chin or fingers gently
> touching the cheek, which convey cognitive states like pondering. In this work,
> we present a novel framework that jointly learns detailed head avatars and the
> non-rigid deformations induced by hand-face interactions.
>   There are two principal challenges in this task. First, naively tracking hand
> and face separately fails to capture their relative poses. To overcome this, we
> propose to combine depth order loss with contact regularization during pose
> tracking, ensuring correct spatial relationships between the face and hand.
> Second, no publicly available priors exist for hand-induced deformations,
> making them non-trivial to learn from monocular videos. To address this, we
> learn a PCA basis specific to hand-induced facial deformations from a face-hand
> interaction dataset. This reduces the problem to estimating a compact set of
> PCA parameters rather than a full spatial deformation field. Furthermore,
> inspired by physics-based simulation, we incorporate a contact loss that
> provides additional supervision, significantly reducing interpenetration
> artifacts and enhancing the physical plausibility of the results.
>   We evaluate our approach on RGB(D) videos captured by an iPhone.
> Additionally, to better evaluate the reconstructed geometry, we construct a
> synthetic dataset of avatars with various types of hand interactions. We show
> that our method can capture better appearance and more accurate deforming
> geometry of the face than SOTA surface reconstruction methods.

