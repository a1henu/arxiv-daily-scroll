---
layout: default
title: High-fidelity lunar topographic reconstruction across diverse terrain and illumination environments using deep learning
---

# High-fidelity lunar topographic reconstruction across diverse terrain and illumination environments using deep learning
**arXiv**：[2601.09468v1](https://arxiv.org/abs/2601.09468) · [PDF](https://arxiv.org/pdf/2601.09468.pdf)  
**作者**：Hao Chen, Philipp Gläser, Konrad Willner, Jürgen Oberst  

**一句话要点**：提出深度学习框架以提升月球地形重建在多样地貌和光照条件下的鲁棒性与精度

**关键词**：月球地形重建, 深度学习, 单视图图像, 明暗恢复形状, 极地区域, 尺度恢复

## 3 点简述
- 核心问题：现有单视图地形重建方法在月球多样地貌和光照条件下鲁棒性不足，限制高分辨率地形数据获取。
- 方法要点：基于先前深度学习框架，引入更鲁棒的尺度恢复方案，并扩展至低光照极地区域，利用单视图图像和低分辨率地形约束。
- 实验或效果：相比单视图明暗恢复形状方法，该方法在变化光照下更鲁棒，重建更一致准确，适用于不同尺度、形态和地质年龄的月球特征，包括永久阴影区。

## 摘要（原文）

> Topographic models are essential for characterizing planetary surfaces and for inferring underlying geological processes. Nevertheless, meter-scale topographic data remain limited, which constrains detailed planetary investigations, even for the Moon, where extensive high-resolution orbital images are available. Recent advances in deep learning (DL) exploit single-view imagery, constrained by low-resolution topography, for fast and flexible reconstruction of fine-scale topography. However, their robustness and general applicability across diverse lunar landforms and illumination conditions remain insufficiently explored. In this study, we build upon our previously proposed DL framework by incorporating a more robust scale recovery scheme and extending the model to polar regions under low solar illumination conditions. We demonstrate that, compared with single-view shape-from-shading methods, the proposed DL approach exhibits greater robustness to varying illumination and achieves more consistent and accurate topographic reconstructions. Furthermore, it reliably reconstructs topography across lunar features of diverse scales, morphologies, and geological ages. High-quality topographic models are also produced for the lunar south polar areas, including permanently shadowed regions, demonstrating the method's capability in reconstructing complex and low-illumination terrain. These findings suggest that DL-based approaches have the potential to leverage extensive lunar datasets to support advanced exploration missions and enable investigations of the Moon at unprecedented topographic resolution.

