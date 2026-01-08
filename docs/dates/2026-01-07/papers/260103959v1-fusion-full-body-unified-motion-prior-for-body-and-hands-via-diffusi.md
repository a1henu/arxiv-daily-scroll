---
layout: default
title: FUSION: Full-Body Unified Motion Prior for Body and Hands via Diffusion
---

# FUSION: Full-Body Unified Motion Prior for Body and Hands via Diffusion
**arXiv**：[2601.03959v1](https://arxiv.org/abs/2601.03959) · [PDF](https://arxiv.org/pdf/2601.03959.pdf)  
**作者**：Enes Duran, Nikos Athanasiou, Muhammed Kocabas, Michael J. Black, Omid Taheri  

**一句话要点**：提出FUSION扩散模型以联合生成身体与手部运动，解决全身体运动合成中手部缺失问题。

**关键词**：全身体运动合成, 扩散模型, 手部运动建模, 运动先验, 数据集整合, 优化管道

## 3 点简述
- 核心问题：现有方法忽略手部运动或局限于狭窄任务，缺乏大规模联合身体与手部运动数据集。
- 方法要点：整合现有手部与身体运动数据，构建首个基于扩散的无条件全身体运动先验模型FUSION。
- 实验或效果：在HumanML3D数据集上超越现有骨骼控制模型，并展示物体交互和自交互应用中的精确手部控制。

## 摘要（原文）

> Hands are central to interacting with our surroundings and conveying gestures, making their inclusion essential for full-body motion synthesis. Despite this, existing human motion synthesis methods fall short: some ignore hand motions entirely, while others generate full-body motions only for narrowly scoped tasks under highly constrained settings. A key obstacle is the lack of large-scale datasets that jointly capture diverse full-body motion with detailed hand articulation. While some datasets capture both, they are limited in scale and diversity. Conversely, large-scale datasets typically focus either on body motion without hands or on hand motions without the body. To overcome this, we curate and unify existing hand motion datasets with large-scale body motion data to generate full-body sequences that capture both hand and body. We then propose the first diffusion-based unconditional full-body motion prior, FUSION, which jointly models body and hand motion. Despite using a pose-based motion representation, FUSION surpasses state-of-the-art skeletal control models on the Keypoint Tracking task in the HumanML3D dataset and achieves superior motion naturalness. Beyond standard benchmarks, we demonstrate that FUSION can go beyond typical uses of motion priors through two applications: (1) generating detailed full-body motion including fingers during interaction given the motion of an object, and (2) generating Self-Interaction motions using an LLM to transform natural language cues into actionable motion constraints. For these applications, we develop an optimization pipeline that refines the latent space of our diffusion model to generate task-specific motions. Experiments on these tasks highlight precise control over hand motion while maintaining plausible full-body coordination. The code will be public.

