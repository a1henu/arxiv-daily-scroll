---
layout: default
title: DensiCrafter: Physically-Constrained Generation and Fabrication of Self-Supporting Hollow Structures
---

# DensiCrafter: Physically-Constrained Generation and Fabrication of Self-Supporting Hollow Structures
**arXiv**：[2511.09298v1](https://arxiv.org/abs/2511.09298) · [PDF](https://arxiv.org/pdf/2511.09298.pdf)  
**作者**：Shengqi Dang, Fu Chai, Jiaxin Li, Chao Yuan, Wei Ye, Nan Cao  

**一句话要点**：提出DensiCrafter框架以生成轻量自支撑空心结构

**关键词**：3D生成模型, 物理约束优化, 空心结构, 轻量化设计, 自支撑结构

## 3 点简述
- 核心问题：现有3D生成模型忽略物理约束与可制造性，难以生成轻量自支撑结构。
- 方法要点：通过优化密度场，引入物理约束损失项，无需模拟即可优化结构。
- 实验或效果：材料质量减少达43%，3D打印验证结构自支撑性与高几何保真度。

## 摘要（原文）

> The rise of 3D generative models has enabled automatic 3D geometry and texture synthesis from multimodal inputs (e.g., text or images). However, these methods often ignore physical constraints and manufacturability considerations. In this work, we address the challenge of producing 3D designs that are both lightweight and self-supporting. We present DensiCrafter, a framework for generating lightweight, self-supporting 3D hollow structures by optimizing the density field. Starting from coarse voxel grids produced by Trellis, we interpret these as continuous density fields to optimize and introduce three differentiable, physically constrained, and simulation-free loss terms. Additionally, a mass regularization penalizes unnecessary material, while a restricted optimization domain preserves the outer surface. Our method seamlessly integrates with pretrained Trellis-based models (e.g., Trellis, DSO) without any architectural changes. In extensive evaluations, we achieve up to 43% reduction in material mass on the text-to-3D task. Compared to state-of-the-art baselines, our method could improve the stability and maintain high geometric fidelity. Real-world 3D-printing experiments confirm that our hollow designs can be reliably fabricated and could be self-supporting.

