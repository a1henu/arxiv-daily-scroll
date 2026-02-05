---
layout: default
title: Capturing Visual Environment Structure Correlates with Control Performance
---

# Capturing Visual Environment Structure Correlates with Control Performance
**arXiv**：[2602.04880v1](https://arxiv.org/abs/2602.04880) · [PDF](https://arxiv.org/pdf/2602.04880.pdf)  
**作者**：Jiahua Dong, Yunze Man, Pavel Tokmakov, Yu-Xiong Wang  

**一句话要点**：提出基于环境状态解码的视觉编码器评估方法，以提升机器人策略泛化能力

**关键词**：视觉表示评估, 机器人控制, 环境状态解码, 预训练编码器, 策略泛化

## 3 点简述
- 核心问题：现有视觉表示评估指标局限于物体形状等狭窄方面，难以预测跨环境策略性能
- 方法要点：通过解码图像中的几何、物体结构和物理属性等环境状态来评估预训练编码器
- 实验或效果：该评估准确性与下游策略性能强相关，优于现有指标，支持高效表示选择

## 摘要（原文）

> The choice of visual representation is key to scaling generalist robot policies. However, direct evaluation via policy rollouts is expensive, even in simulation. Existing proxy metrics focus on the representation's capacity to capture narrow aspects of the visual world, like object shape, limiting generalization across environments. In this paper, we take an analytical perspective: we probe pretrained visual encoders by measuring how well they support decoding of environment state -- including geometry, object structure, and physical attributes -- from images. Leveraging simulation environments with access to ground-truth state, we show that this probing accuracy strongly correlates with downstream policy performance across diverse environments and learning settings, significantly outperforming prior metrics and enabling efficient representation selection. More broadly, our study provides insight into the representational properties that support generalizable manipulation, suggesting that learning to encode the latent physical state of the environment is a promising objective for control.

