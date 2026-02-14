---
layout: default
title: Stroke of Surprise: Progressive Semantic Illusions in Vector Sketching
---

# Stroke of Surprise: Progressive Semantic Illusions in Vector Sketching
**arXiv**：[2602.12280v1](https://arxiv.org/abs/2602.12280) · [PDF](https://arxiv.org/pdf/2602.12280.pdf)  
**作者**：Huai-Hsun Cheng, Siang-Ling Zhang, Yu-Lun Liu  

**一句话要点**：提出Stroke of Surprise框架以解决渐进语义幻觉的向量草图生成任务

**关键词**：向量草图生成, 渐进语义幻觉, 双分支SDS, 序列感知优化, 覆盖损失, 视觉字谜

## 3 点简述
- 核心问题：向量草图中如何通过顺序添加笔画实现语义转换，同时满足双重约束。
- 方法要点：采用序列感知联合优化框架，结合双分支SDS机制和覆盖损失，动态调整笔画。
- 实验或效果：在可识别性和幻觉强度上显著优于基线，将视觉字谜从空间扩展到时间维度。

## 摘要（原文）

> Visual illusions traditionally rely on spatial manipulations such as multi-view consistency. In this work, we introduce Progressive Semantic Illusions, a novel vector sketching task where a single sketch undergoes a dramatic semantic transformation through the sequential addition of strokes. We present Stroke of Surprise, a generative framework that optimizes vector strokes to satisfy distinct semantic interpretations at different drawing stages. The core challenge lies in the "dual-constraint": initial prefix strokes must form a coherent object (e.g., a duck) while simultaneously serving as the structural foundation for a second concept (e.g., a sheep) upon adding delta strokes. To address this, we propose a sequence-aware joint optimization framework driven by a dual-branch Score Distillation Sampling (SDS) mechanism. Unlike sequential approaches that freeze the initial state, our method dynamically adjusts prefix strokes to discover a "common structural subspace" valid for both targets. Furthermore, we introduce a novel Overlay Loss that enforces spatial complementarity, ensuring structural integration rather than occlusion. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines in recognizability and illusion strength, successfully expanding visual anagrams from the spatial to the temporal dimension. Project page: https://stroke-of-surprise.github.io/

