---
layout: default
title: See in Depth: Training-Free Surgical Scene Segmentation with Monocular Depth Priors
---

# See in Depth: Training-Free Surgical Scene Segmentation with Monocular Depth Priors
**arXiv**：[2512.05529v1](https://arxiv.org/abs/2512.05529) · [PDF](https://arxiv.org/pdf/2512.05529.pdf)  
**作者**：Kunyi Yang, Qingyu Wang, Cheng Yuan, Yutong Ban  

**一句话要点**：提出DepSeg框架，利用单目深度先验实现免训练腹腔镜场景分割

**关键词**：腹腔镜场景分割, 免训练分割, 单目深度先验, 深度引导提示, 模板匹配分类, 计算机辅助手术

## 3 点简述
- 核心问题：腹腔镜场景像素级分割标注成本高，难以扩展。
- 方法要点：结合单目深度估计和预训练视觉基础模型，通过深度引导提示和模板匹配分类。
- 实验或效果：在CholecSeg8k数据集上，mIoU从14.7%提升至35.9%，仅需10-20%模板保持竞争力。

## 摘要（原文）

> Pixel-wise segmentation of laparoscopic scenes is essential for computer-assisted surgery but difficult to scale due to the high cost of dense annotations. We propose depth-guided surgical scene segmentation (DepSeg), a training-free framework that utilizes monocular depth as a geometric prior together with pretrained vision foundation models. DepSeg first estimates a relative depth map with a pretrained monocular depth estimation network and proposes depth-guided point prompts, which SAM2 converts into class-agnostic masks. Each mask is then described by a pooled pretrained visual feature and classified via template matching against a template bank built from annotated frames. On the CholecSeg8k dataset, DepSeg improves over a direct SAM2 auto segmentation baseline (35.9% vs. 14.7% mIoU) and maintains competitive performance even when using only 10--20% of the object templates. These results show that depth-guided prompting and template-based classification offer an annotation-efficient segmentation approach.

