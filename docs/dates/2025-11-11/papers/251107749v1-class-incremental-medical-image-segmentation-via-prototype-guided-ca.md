---
layout: default
title: Class Incremental Medical Image Segmentation via Prototype-Guided Calibration and Dual-Aligned Distillation
---

# Class Incremental Medical Image Segmentation via Prototype-Guided Calibration and Dual-Aligned Distillation
**arXiv**：[2511.07749v1](https://arxiv.org/abs/2511.07749) · [PDF](https://arxiv.org/pdf/2511.07749.pdf)  
**作者**：Shengqian Zhu, Chengrong Yu, Qiang Wang, Ying Song, Guangjun Li, Jiafei Wu, Xiaogang Xu, Zhang Yi, Junjie Hu  

**一句话要点**：提出原型引导校准与双对齐蒸馏以解决医学图像增量分割中的知识遗忘问题

**关键词**：医学图像分割, 增量学习, 原型蒸馏, 知识保留, 多器官分割

## 3 点简述
- 核心问题：现有方法对空间区域和特征通道处理均等，或仅对齐原型而忽略局部表示，导致旧知识退化。
- 方法要点：PGCD利用原型-特征相似性校准蒸馏强度，DAPD对齐局部原型与全局原型以增强旧类分割。
- 实验或效果：在多个多器官分割基准上评估，方法优于现有技术，展现鲁棒性和泛化能力。

## 摘要（原文）

> Class incremental medical image segmentation (CIMIS) aims to preserve knowledge of previously learned classes while learning new ones without relying on old-class labels. However, existing methods 1) either adopt one-size-fits-all strategies that treat all spatial regions and feature channels equally, which may hinder the preservation of accurate old knowledge, 2) or focus solely on aligning local prototypes with global ones for old classes while overlooking their local representations in new data, leading to knowledge degradation. To mitigate the above issues, we propose Prototype-Guided Calibration Distillation (PGCD) and Dual-Aligned Prototype Distillation (DAPD) for CIMIS in this paper. Specifically, PGCD exploits prototype-to-feature similarity to calibrate class-specific distillation intensity in different spatial regions, effectively reinforcing reliable old knowledge and suppressing misleading information from old classes. Complementarily, DAPD aligns the local prototypes of old classes extracted from the current model with both global prototypes and local prototypes, further enhancing segmentation performance on old categories. Comprehensive evaluations on two widely used multi-organ segmentation benchmarks demonstrate that our method outperforms state-of-the-art methods, highlighting its robustness and generalization capabilities.

