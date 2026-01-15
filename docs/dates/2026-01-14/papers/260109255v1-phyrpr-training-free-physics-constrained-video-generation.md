---
layout: default
title: PhyRPR: Training-Free Physics-Constrained Video Generation
---

# PhyRPR: Training-Free Physics-Constrained Video Generation
**arXiv**：[2601.09255v1](https://arxiv.org/abs/2601.09255) · [PDF](https://arxiv.org/pdf/2601.09255.pdf)  
**作者**：Yibo Zhao, Hengjia Li, Xiaofei He, Boxi Wu  

**一句话要点**：提出PhyRPR训练免费三阶段流程，以解决扩散视频生成中物理约束不足的问题。

**关键词**：视频生成, 物理约束, 训练免费方法, 扩散模型, 多阶段流程

## 3 点简述
- 核心问题：现有扩散视频生成模型常违反物理约束，因物理理解与视觉合成纠缠。
- 方法要点：采用PhyReason-PhyPlan-PhyRefine三阶段，解耦物理推理与合成，通过可控运动支架注入。
- 实验或效果：在物理约束下实验显示，方法提升物理合理性和运动可控性。

## 摘要（原文）

> Recent diffusion-based video generation models can synthesize visually plausible videos, yet they often struggle to satisfy physical constraints. A key reason is that most existing approaches remain single-stage: they entangle high-level physical understanding with low-level visual synthesis, making it hard to generate content that require explicit physical reasoning. To address this limitation, we propose a training-free three-stage pipeline,\textit{PhyRPR}:\textit{Phy\uline{R}eason}--\textit{Phy\uline{P}lan}--\textit{Phy\uline{R}efine}, which decouples physical understanding from visual synthesis. Specifically, \textit{PhyReason} uses a large multimodal model for physical state reasoning and an image generator for keyframe synthesis; \textit{PhyPlan} deterministically synthesizes a controllable coarse motion scaffold; and \textit{PhyRefine} injects this scaffold into diffusion sampling via a latent fusion strategy to refine appearance while preserving the planned dynamics. This staged design enables explicit physical control during generation. Extensive experiments under physics constraints show that our method consistently improves physical plausibility and motion controllability.

