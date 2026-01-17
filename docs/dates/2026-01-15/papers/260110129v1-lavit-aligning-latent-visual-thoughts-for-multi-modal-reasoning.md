---
layout: default
title: LaViT: Aligning Latent Visual Thoughts for Multi-modal Reasoning
---

# LaViT: Aligning Latent Visual Thoughts for Multi-modal Reasoning
**arXiv**：[2601.10129v1](https://arxiv.org/abs/2601.10129) · [PDF](https://arxiv.org/pdf/2601.10129.pdf)  
**作者**：Linquan Wu, Tianxiang Jiang, Yifei Dong, Haoyu Yang, Fengji Zhang, Shichaang Meng, Ai Xuan, Linqi Song, Jacky Keung  

**一句话要点**：提出LaViT框架以解决多模态推理中的感知差距问题，通过对齐潜在视觉思维增强视觉基础。

**关键词**：多模态推理, 视觉基础, 蒸馏训练, 注意力对齐, 潜在表示学习, 课程学习

## 3 点简述
- 核心问题：当前多模态潜在推理依赖外部监督，忽略内在视觉注意力动态，导致学生模型模仿教师文本输出但关注不同视觉区域。
- 方法要点：LaViT通过自回归重构教师的视觉语义和注意力轨迹，采用课程感官门控机制防止捷径学习，以对齐潜在视觉思维。
- 实验或效果：在复杂推理任务上实现高达+16.9%的性能提升，使紧凑3B模型超越更大开源变体和GPT-4o等专有模型。

## 摘要（原文）

> Current multimodal latent reasoning often relies on external supervision (e.g., auxiliary images), ignoring intrinsic visual attention dynamics. In this work, we identify a critical Perception Gap in distillation: student models frequently mimic a teacher's textual output while attending to fundamentally divergent visual regions, effectively relying on language priors rather than grounded perception. To bridge this, we propose LaViT, a framework that aligns latent visual thoughts rather than static embeddings. LaViT compels the student to autoregressively reconstruct the teacher's visual semantics and attention trajectories prior to text generation, employing a curriculum sensory gating mechanism to prevent shortcut learning. Extensive experiments show that LaViT significantly enhances visual grounding, achieving up to +16.9% gains on complex reasoning tasks and enabling a compact 3B model to outperform larger open-source variants and proprietary models like GPT-4o.

