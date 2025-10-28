---
layout: default
title: Progressive Growing of Patch Size: Curriculum Learning for Accelerated and Improved Medical Image Segmentation
---

# Progressive Growing of Patch Size: Curriculum Learning for Accelerated and Improved Medical Image Segmentation
**arXiv**：[2510.23241v1](https://arxiv.org/abs/2510.23241) · [PDF](https://arxiv.org/pdf/2510.23241.pdf)  
**作者**：Stefan M. Fischer, Johannes Kiechle, Laura Daza, Lina Felsner, Richard Osuala, Daniel M. Lang, Karim Lekadir, Jan C. Peeken, Julia A. Schnabel  

**一句话要点**：提出渐进式补丁大小增长方法，以加速和改进3D医学图像分割。

**关键词**：3D医学图像分割, 课程学习, 渐进式训练, 补丁大小优化, 计算效率提升

## 3 点简述
- 核心问题：3D医学图像分割中类不平衡和训练效率低的问题。
- 方法要点：训练中逐步增大补丁大小，改善类平衡并加速收敛。
- 实验或效果：在15个任务中，性能模式提升Dice分数1.28%，训练时间减少至89%。

## 摘要（原文）

> In this work, we introduce Progressive Growing of Patch Size, an automatic
> curriculum learning approach for 3D medical image segmentation. Our approach
> progressively increases the patch size during model training, resulting in an
> improved class balance for smaller patch sizes and accelerated convergence of
> the training process. We evaluate our curriculum approach in two settings: a
> resource-efficient mode and a performance mode, both regarding Dice score
> performance and computational costs across 15 diverse and popular 3D medical
> image segmentation tasks. The resource-efficient mode matches the Dice score
> performance of the conventional constant patch size sampling baseline with a
> notable reduction in training time to only 44%. The performance mode improves
> upon constant patch size segmentation results, achieving a statistically
> significant relative mean performance gain of 1.28% in Dice Score. Remarkably,
> across all 15 tasks, our proposed performance mode manages to surpass the
> constant patch size baseline in Dice Score performance, while simultaneously
> reducing training time to only 89%. The benefits are particularly pronounced
> for highly imbalanced tasks such as lesion segmentation tasks. Rigorous
> experiments demonstrate that our performance mode not only improves mean
> segmentation performance but also reduces performance variance, yielding more
> trustworthy model comparison. Furthermore, our findings reveal that the
> proposed curriculum sampling is not tied to a specific architecture but
> represents a broadly applicable strategy that consistently boosts performance
> across diverse segmentation models, including UNet, UNETR, and SwinUNETR. In
> summary, we show that this simple yet elegant transformation on input data
> substantially improves both Dice Score performance and training runtime, while
> being compatible across diverse segmentation backbones.

