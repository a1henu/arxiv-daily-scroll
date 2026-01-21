---
layout: default
title: Copy-Trasform-Paste: Zero-Shot Object-Object Alignment Guided by Vision-Language and Geometric Constraints
---

# Copy-Trasform-Paste: Zero-Shot Object-Object Alignment Guided by Vision-Language and Geometric Constraints
**arXiv**：[2601.14207v1](https://arxiv.org/abs/2601.14207) · [PDF](https://arxiv.org/pdf/2601.14207.pdf)  
**作者**：Rotem Gatenyo, Ohad Fried  

**一句话要点**：提出基于视觉语言与几何约束的零样本三维网格对齐方法，优化相对位姿以提升内容创建效果。

**关键词**：零样本学习, 三维对齐, 视觉语言模型, 几何约束, 可微分渲染, 内容创建

## 3 点简述
- 研究零样本三维网格对齐问题，使用文本提示描述空间关系，无需训练新模型。
- 通过可微分渲染器结合CLIP梯度优化位姿，并引入几何感知目标如软ICP和穿透损失。
- 在多样化基准上评估，方法优于基线，实现语义忠实和物理合理的对齐。

## 摘要（原文）

> We study zero-shot 3D alignment of two given meshes, using a text prompt describing their spatial relation -- an essential capability for content creation and scene assembly. Earlier approaches primarily rely on geometric alignment procedures, while recent work leverages pretrained 2D diffusion models to model language-conditioned object-object spatial relationships. In contrast, we directly optimize the relative pose at test time, updating translation, rotation, and isotropic scale with CLIP-driven gradients via a differentiable renderer, without training a new model. Our framework augments language supervision with geometry-aware objectives: a variant of soft-Iterative Closest Point (ICP) term to encourage surface attachment and a penetration loss to discourage interpenetration. A phased schedule strengthens contact constraints over time, and camera control concentrates the optimization on the interaction region. To enable evaluation, we curate a benchmark containing diverse categories and relations, and compare against baselines. Our method outperforms all alternatives, yielding semantically faithful and physically plausible alignments.

