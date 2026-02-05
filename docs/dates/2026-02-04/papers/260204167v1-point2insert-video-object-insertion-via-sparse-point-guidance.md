---
layout: default
title: Point2Insert: Video Object Insertion via Sparse Point Guidance
---

# Point2Insert: Video Object Insertion via Sparse Point Guidance
**arXiv**：[2602.04167v1](https://arxiv.org/abs/2602.04167) · [PDF](https://arxiv.org/pdf/2602.04167.pdf)  
**作者**：Yu Zhou, Xiaoyan Yang, Bojia Zi, Lihan Zhang, Ruijie Sun, Weishi Zheng, Haibin Huang, Chi Zhang, Xuelong Li  

**一句话要点**：提出Point2Insert框架，通过稀疏点引导实现视频对象插入，解决掩码标注繁琐和指令定位不准问题。

**关键词**：视频对象插入, 稀疏点引导, 蒸馏训练, 两阶段训练, 掩码引导

## 3 点简述
- 核心问题：现有方法需密集掩码标注或难以精确控制对象位置，导致视频对象插入不灵活。
- 方法要点：使用正负稀疏点替代掩码，分两阶段训练，结合掩码引导蒸馏提升插入成功率。
- 实验或效果：在实验中优于基线模型，参数效率高，支持细粒度空间控制。

## 摘要（原文）

> This paper introduces Point2Insert, a sparse-point-based framework for flexible and user-friendly object insertion in videos, motivated by the growing popularity of accurate, low-effort object placement. Existing approaches face two major challenges: mask-based insertion methods require labor-intensive mask annotations, while instruction-based methods struggle to place objects at precise locations. Point2Insert addresses these issues by requiring only a small number of sparse points instead of dense masks, eliminating the need for tedious mask drawing. Specifically, it supports both positive and negative points to indicate regions that are suitable or unsuitable for insertion, enabling fine-grained spatial control over object locations. The training of Point2Insert consists of two stages. In Stage 1, we train an insertion model that generates objects in given regions conditioned on either sparse-point prompts or a binary mask. In Stage 2, we further train the model on paired videos synthesized by an object removal model, adapting it to video insertion. Moreover, motivated by the higher insertion success rate of mask-guided editing, we leverage a mask-guided insertion model as a teacher to distill reliable insertion behavior into the point-guided model. Extensive experiments demonstrate that Point2Insert consistently outperforms strong baselines and even surpasses models with $\times$10 more parameters.

