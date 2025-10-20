---
layout: default
title: Uncertainty-Aware Extreme Point Tracing for Weakly Supervised Ultrasound Image Segmentation
---

# Uncertainty-Aware Extreme Point Tracing for Weakly Supervised Ultrasound Image Segmentation
**arXiv**：[2510.15666v1](https://arxiv.org/abs/2510.15666) · [PDF](https://arxiv.org/pdf/2510.15666.pdf)  
**作者**：Lei Shi, Gang Li, Junxing Zhang  

**一句话要点**：提出不确定性感知极值点追踪方法，以弱监督方式实现超声图像分割

**关键词**：弱监督分割, 超声图像, 不确定性估计, 极值点追踪, SAM2模型, 边界对齐

## 3 点简述
- 核心问题：全监督医学图像分割需要高成本像素级标注，标注负担重。
- 方法要点：利用极值点生成边界框提示SAM2，结合不确定性估计和一致性损失优化分割。
- 实验或效果：在BUSI和UNS数据集上性能媲美或超越全监督方法，显著降低标注成本。

## 摘要（原文）

> Automatic medical image segmentation is a fundamental step in computer-aided
> diagnosis, yet fully supervised approaches demand extensive pixel-level
> annotations that are costly and time-consuming. To alleviate this burden, we
> propose a weakly supervised segmentation framework that leverages only four
> extreme points as annotation. Specifically, bounding boxes derived from the
> extreme points are used as prompts for the Segment Anything Model 2 (SAM2) to
> generate reliable initial pseudo labels. These pseudo labels are progressively
> refined by an enhanced Feature-Guided Extreme Point Masking (FGEPM) algorithm,
> which incorporates Monte Carlo dropout-based uncertainty estimation to
> construct a unified gradient uncertainty cost map for boundary tracing.
> Furthermore, a dual-branch Uncertainty-aware Scale Consistency (USC) loss and a
> box alignment loss are introduced to ensure spatial consistency and precise
> boundary alignment during training. Extensive experiments on two public
> ultrasound datasets, BUSI and UNS, demonstrate that our method achieves
> performance comparable to, and even surpassing fully supervised counterparts
> while significantly reducing annotation cost. These results validate the
> effectiveness and practicality of the proposed weakly supervised framework for
> ultrasound image segmentation.

