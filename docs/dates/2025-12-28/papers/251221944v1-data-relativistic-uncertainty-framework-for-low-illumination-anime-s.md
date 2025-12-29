---
layout: default
title: Data relativistic uncertainty framework for low-illumination anime scenery image enhancement
---

# Data relativistic uncertainty framework for low-illumination anime scenery image enhancement
**arXiv**：[2512.21944v1](https://arxiv.org/abs/2512.21944) · [PDF](https://arxiv.org/pdf/2512.21944.pdf)  
**作者**：Yiquan Gao, John See  

**一句话要点**：提出数据相对论不确定性框架以增强低光照动漫场景图像质量

**关键词**：低光照增强, 动漫场景图像, 数据不确定性, 相对论GAN, 图像增强框架

## 3 点简述
- 核心问题：解决低光照动漫场景图像增强任务，填补与自然图像增强的领域差距。
- 方法要点：基于相对论GAN思想，定义光照不确定性并动态调整目标函数以校准模型学习。
- 实验或效果：通过训练EnlightenGANs变体，在感知和美学质量上超越现有方法。

## 摘要（原文）

> By contrast with the prevailing works of low-light enhancement in natural images and videos, this study copes with the low-illumination quality degradation in anime scenery images to bridge the domain gap. For such an underexplored enhancement task, we first curate images from various sources and construct an unpaired anime scenery dataset with diverse environments and illumination conditions to address the data scarcity. To exploit the power of uncertainty information inherent with the diverse illumination conditions, we propose a Data Relativistic Uncertainty (DRU) framework, motivated by the idea from Relativistic GAN. By analogy with the wave-particle duality of light, our framework interpretably defines and quantifies the illumination uncertainty of dark/bright samples, which is leveraged to dynamically adjust the objective functions to recalibrate the model learning under data uncertainty. Extensive experiments demonstrate the effectiveness of DRU framework by training several versions of EnlightenGANs, yielding superior perceptual and aesthetic qualities beyond the state-of-the-art methods that are incapable of learning from data uncertainty perspective. We hope our framework can expose a novel paradigm of data-centric learning for potential visual and language domains. Code is available.

