---
layout: default
title: Vision Transformer for Robust Occluded Person Reidentification in Complex Surveillance Scenes
---

# Vision Transformer for Robust Occluded Person Reidentification in Complex Surveillance Scenes
**arXiv**：[2510.27677v1](https://arxiv.org/abs/2510.27677) · [PDF](https://arxiv.org/pdf/2510.27677.pdf)  
**作者**：Bo Li, Duyuan Zheng, Xinyang Liu, Qingwen Li, Hong Li, Hongyan Cui, Ge Gao, Chen Liu  

**一句话要点**：提出Sh-ViT模型以解决复杂监控场景中遮挡行人重识别问题

**关键词**：行人重识别, 视觉Transformer, 遮挡鲁棒性, 知识蒸馏, 监控场景, 数据增强

## 3 点简述
- 核心问题：监控行人重识别受遮挡、视角扭曲和图像质量差影响，现有方法依赖复杂模块或仅适用于清晰正面图像。
- 方法要点：基于ViT-Base，引入Shuffle模块、场景适应增强和DeiT知识蒸馏，提升对遮挡和模糊的鲁棒性。
- 实验或效果：在MyTT数据集上Rank-1达83.2%，mAP达80.1%，优于CNN和ViT基线，并在Market1501上表现优异。

## 摘要（原文）

> Person re-identification (ReID) in surveillance is challenged by occlusion,
> viewpoint distortion, and poor image quality. Most existing methods rely on
> complex modules or perform well only on clear frontal images. We propose Sh-ViT
> (Shuffling Vision Transformer), a lightweight and robust model for occluded
> person ReID. Built on ViT-Base, Sh-ViT introduces three components: First, a
> Shuffle module in the final Transformer layer to break spatial correlations and
> enhance robustness to occlusion and blur; Second, scenario-adapted augmentation
> (geometric transforms, erasing, blur, and color adjustment) to simulate
> surveillance conditions; Third, DeiT-based knowledge distillation to improve
> learning with limited labels.To support real-world evaluation, we construct the
> MyTT dataset, containing over 10,000 pedestrians and 30,000+ images from base
> station inspections, with frequent equipment occlusion and camera variations.
> Experiments show that Sh-ViT achieves 83.2% Rank-1 and 80.1% mAP on MyTT,
> outperforming CNN and ViT baselines, and 94.6% Rank-1 and 87.5% mAP on
> Market1501, surpassing state-of-the-art methods.In summary, Sh-ViT improves
> robustness to occlusion and blur without external modules, offering a practical
> solution for surveillance-based personnel monitoring.

