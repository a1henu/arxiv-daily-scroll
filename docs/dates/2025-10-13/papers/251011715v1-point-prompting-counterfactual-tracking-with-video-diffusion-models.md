---
layout: default
title: Point Prompting: Counterfactual Tracking with Video Diffusion Models
---

# Point Prompting: Counterfactual Tracking with Video Diffusion Models
**arXiv**：[2510.11715v1](https://arxiv.org/abs/2510.11715) · [PDF](https://arxiv.org/pdf/2510.11715.pdf)  
**作者**：Ayush Shrivastava, Sanyam Mehta, Daniel Geng, Andrew Owens  

**一句话要点**：提出点提示方法，利用视频扩散模型实现零样本点跟踪。

**关键词**：点跟踪, 视频扩散模型, 零样本学习, 反事实生成, 运动分析

## 3 点简述
- 核心问题：如何利用视频生成模型进行零样本点跟踪，分析物体运动轨迹。
- 方法要点：通过添加彩色标记点并反事实生成视频，传播标记以追踪轨迹。
- 实验效果：在多个模型上测试，性能优于现有零样本方法，对遮挡鲁棒。

## 摘要（原文）

> Trackers and video generators solve closely related problems: the former
> analyze motion, while the latter synthesize it. We show that this connection
> enables pretrained video diffusion models to perform zero-shot point tracking
> by simply prompting them to visually mark points as they move over time. We
> place a distinctively colored marker at the query point, then regenerate the
> rest of the video from an intermediate noise level. This propagates the marker
> across frames, tracing the point's trajectory. To ensure that the marker
> remains visible in this counterfactual generation, despite such markers being
> unlikely in natural videos, we use the unedited initial frame as a negative
> prompt. Through experiments with multiple image-conditioned video diffusion
> models, we find that these "emergent" tracks outperform those of prior
> zero-shot methods and persist through occlusions, often obtaining performance
> that is competitive with specialized self-supervised models.

