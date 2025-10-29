---
layout: default
title: Fast and accurate neural reflectance transformation imaging through knowledge distillation
---

# Fast and accurate neural reflectance transformation imaging through knowledge distillation
**arXiv**：[2510.24486v1](https://arxiv.org/abs/2510.24486) · [PDF](https://arxiv.org/pdf/2510.24486.pdf)  
**作者**：Tinsae G. Dulecha, Leonardo Righetto, Ruggero Pintus, Enrico Gobbetti, Andrea Giachetti  

**一句话要点**：提出基于知识蒸馏的快速准确神经反射变换成像方法，以降低计算成本。

**关键词**：反射变换成像, 知识蒸馏, 神经渲染, 计算优化, 表面分析

## 3 点简述
- 核心问题：神经反射变换成像渲染计算昂贵，难以在有限硬件上处理大图像。
- 方法要点：采用知识蒸馏技术，训练小型网络以近似原模型，减少参数。
- 实验或效果：未知，但旨在实现高质量渲染，同时降低计算需求。

## 摘要（原文）

> Reflectance Transformation Imaging (RTI) is very popular for its ability to
> visually analyze surfaces by enhancing surface details through interactive
> relighting, starting from only a few tens of photographs taken with a fixed
> camera and variable illumination. Traditional methods like Polynomial Texture
> Maps (PTM) and Hemispherical Harmonics (HSH) are compact and fast, but struggle
> to accurately capture complex reflectance fields using few per-pixel
> coefficients and fixed bases, leading to artifacts, especially in highly
> reflective or shadowed areas. The NeuralRTI approach, which exploits a neural
> autoencoder to learn a compact function that better approximates the local
> reflectance as a function of light directions, has been shown to produce
> superior quality at comparable storage cost. However, as it performs
> interactive relighting with custom decoder networks with many parameters, the
> rendering step is computationally expensive and not feasible at full resolution
> for large images on limited hardware. Earlier attempts to reduce costs by
> directly training smaller networks have failed to produce valid results. For
> this reason, we propose to reduce its computational cost through a novel
> solution based on Knowledge Distillation (DisK-NeuralRTI). ...

