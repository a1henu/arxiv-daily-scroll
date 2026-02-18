---
layout: default
title: Spanning the Visual Analogy Space with a Weight Basis of LoRAs
---

# Spanning the Visual Analogy Space with a Weight Basis of LoRAs
**arXiv**：[2602.15727v1](https://arxiv.org/abs/2602.15727) · [PDF](https://arxiv.org/pdf/2602.15727.pdf)  
**作者**：Hila Manor, Rinon Gal, Haggai Maron, Tomer Michaeli, Gal Chechik  

**一句话要点**：提出LoRWeB方法，通过动态组合LoRA基模块解决视觉类比学习中固定模块泛化受限的问题。

**关键词**：视觉类比学习, 低秩适应, 动态模块组合, 图像生成, 泛化能力, 变换空间建模

## 3 点简述
- 核心问题：现有方法使用单一LoRA模块难以泛化到多样视觉变换，限制了视觉类比学习能力。
- 方法要点：引入可学习的LoRA基模块和轻量编码器，在推理时动态选择和加权基模块以适配不同类比任务。
- 实验或效果：评估显示该方法达到最先进性能，显著提升对未见视觉变换的泛化能力。

## 摘要（原文）

> Visual analogy learning enables image manipulation through demonstration rather than textual description, allowing users to specify complex transformations difficult to articulate in words. Given a triplet $\{\mathbf{a}$, $\mathbf{a}'$, $\mathbf{b}\}$, the goal is to generate $\mathbf{b}'$ such that $\mathbf{a} : \mathbf{a}' :: \mathbf{b} : \mathbf{b}'$. Recent methods adapt text-to-image models to this task using a single Low-Rank Adaptation (LoRA) module, but they face a fundamental limitation: attempting to capture the diverse space of visual transformations within a fixed adaptation module constrains generalization capabilities. Inspired by recent work showing that LoRAs in constrained domains span meaningful, interpolatable semantic spaces, we propose LoRWeB, a novel approach that specializes the model for each analogy task at inference time through dynamic composition of learned transformation primitives, informally, choosing a point in a "space of LoRAs". We introduce two key components: (1) a learnable basis of LoRA modules, to span the space of different visual transformations, and (2) a lightweight encoder that dynamically selects and weighs these basis LoRAs based on the input analogy pair. Comprehensive evaluations demonstrate our approach achieves state-of-the-art performance and significantly improves generalization to unseen visual transformations. Our findings suggest that LoRA basis decompositions are a promising direction for flexible visual manipulation. Code and data are in https://research.nvidia.com/labs/par/lorweb

