---
layout: default
title: Learning Transient Convective Heat Transfer with Geometry Aware World Models
---

# Learning Transient Convective Heat Transfer with Geometry Aware World Models
**arXiv**：[2601.22086v1](https://arxiv.org/abs/2601.22086) · [PDF](https://arxiv.org/pdf/2601.22086.pdf)  
**作者**：Onur T. Doganay, Alexander Klawonn, Martin Eigel, Hanno Gottschalk  

**一句话要点**：提出几何感知世界模型架构，用于学习瞬态对流热传递，以替代计算流体动力学模拟。

**关键词**：几何感知世界模型, 瞬态物理学习, 计算流体动力学, 条件生成模型, 对流热传递

## 3 点简述
- 核心问题：偏微分方程模拟计算成本高，标准视频生成架构缺乏物理模拟所需的控制和数据兼容性。
- 方法要点：引入双重条件机制（全局物理参数和局部几何掩码）及支持任意通道维度的架构适配。
- 实验或效果：在2D瞬态计算流体动力学问题上评估，模型能复现复杂时空动态，并测试了未见几何配置的泛化能力。

## 摘要（原文）

> Partial differential equation (PDE) simulations are fundamental to engineering and physics but are often computationally prohibitive for real-time applications. While generative AI offers a promising avenue for surrogate modeling, standard video generation architectures lack the specific control and data compatibility required for physical simulations. This paper introduces a geometry aware world model architecture, derived from a video generation architecture (LongVideoGAN), designed to learn transient physics. We introduce two key architecture elements: (1) a twofold conditioning mechanism incorporating global physical parameters and local geometric masks, and (2) an architectural adaptation to support arbitrary channel dimensions, moving beyond standard RGB constraints. We evaluate this approach on a 2D transient computational fluid dynamics (CFD) problem involving convective heat transfer from buoyancy-driven flow coupled to a heat flow in a solid structure. We demonstrate that the conditioned model successfully reproduces complex temporal dynamics and spatial correlations of the training data. Furthermore, we assess the model's generalization capabilities on unseen geometric configurations, highlighting both its potential for controlled simulation synthesis and current limitations in spatial precision for out-of-distribution samples.

