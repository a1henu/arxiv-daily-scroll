---
layout: default
title: SerpentFlow: Generative Unpaired Domain Alignment via Shared-Structure Decomposition
---

# SerpentFlow: Generative Unpaired Domain Alignment via Shared-Structure Decomposition
**arXiv**：[2601.01979v1](https://arxiv.org/abs/2601.01979) · [PDF](https://arxiv.org/pdf/2601.01979.pdf)  
**作者**：Julie Keisler, Anastase Alexandre Charantonis, Yannig Goude, Boutheina Oueslati, Claire Monteleoni  

**一句话要点**：提出SerpentFlow框架，通过共享结构分解实现无配对域对齐，应用于超分辨率等任务。

**关键词**：无配对域对齐, 共享结构分解, 条件生成模型, 超分辨率, 流匹配, 气候降尺度

## 3 点简述
- 核心问题：无配对域对齐中，缺乏跨域监督，难以学习共享结构。
- 方法要点：在潜在空间分解数据为共享和域特定组件，生成伪配对训练条件生成模型。
- 实验或效果：在合成图像、物理模拟和气候降尺度任务中有效重建高频结构。

## 摘要（原文）

> Domain alignment refers broadly to learning correspondences between data distributions from distinct domains. In this work, we focus on a setting where domains share underlying structural patterns despite differences in their specific realizations. The task is particularly challenging in the absence of paired observations, which removes direct supervision across domains. We introduce a generative framework, called SerpentFlow (SharEd-structuRe decomPosition for gEnerative domaiN adapTation), for unpaired domain alignment. SerpentFlow decomposes data within a latent space into a shared component common to both domains and a domain-specific one. By isolating the shared structure and replacing the domain-specific component with stochastic noise, we construct synthetic training pairs between shared representations and target-domain samples, thereby enabling the use of conditional generative models that are traditionally restricted to paired settings. We apply this approach to super-resolution tasks, where the shared component naturally corresponds to low-frequency content while high-frequency details capture domain-specific variability. The cutoff frequency separating low- and high-frequency components is determined automatically using a classifier-based criterion, ensuring a data-driven and domain-adaptive decomposition. By generating pseudo-pairs that preserve low-frequency structures while injecting stochastic high-frequency realizations, we learn the conditional distribution of the target domain given the shared representation. We implement SerpentFlow using Flow Matching as the generative pipeline, although the framework is compatible with other conditional generative approaches. Experiments on synthetic images, physical process simulations, and a climate downscaling task demonstrate that the method effectively reconstructs high-frequency structures consistent with underlying low-frequency patterns, supporting shared-structure decomposition as an effective strategy for unpaired domain alignment.

