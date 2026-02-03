---
layout: default
title: When Is Rank-1 Enough? Geometry-Guided Initialization for Parameter-Efficient Fine-Tuning
---

# When Is Rank-1 Enough? Geometry-Guided Initialization for Parameter-Efficient Fine-Tuning
**arXiv**：[2602.01522v1](https://arxiv.org/abs/2602.01522) · [PDF](https://arxiv.org/pdf/2602.01522.pdf)  
**作者**：Haoran Zhao, Soyeon Caren Han, Eduard Hovy  

**一句话要点**：提出Gap-Init初始化方法以稳定多模态大语言模型的秩-1参数高效微调

**关键词**：参数高效微调, 低秩适应, 多模态大语言模型, 初始化策略, 模态间隙, 梯度分析

## 3 点简述
- 核心问题：秩-1 LoRA微调不稳定，源于预训练特征不匹配导致的梯度方向敏感
- 方法要点：基于几何分析，初始化时对齐秩-1方向与模态间隙向量，保持初始更新为零
- 实验或效果：在多个视觉语言任务中稳定训练，性能可媲美秩-8基线

## 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) is a standard way to adapt multimodal large language models, yet extremely low-rank settings -- especially rank-1 LoRA -- are often unstable. We show that this instability is not solely due to limited capacity: in the rank-1 regime, optimization is highly sensitive to the update direction. Concretely, pretrained vision and text features form mismatched anisotropic regions, yielding a dominant "gap" direction that acts like a translation component and disproportionately steers early gradients under rank-1 constraints. Analyzing pretrained representations, we identify a modality-gap axis that dominates early gradient flow, while a random rank-1 initialization is unlikely to align with it, leading to weak gradients and training collapse. We propose Gap-Init, a geometry-aware initialization that aligns the rank-1 LoRA direction with an estimated modality-gap vector from a small calibration set, while keeping the initial LoRA update zero. Across multiple vision-language tasks and backbones, Gap-Init consistently stabilizes rank-1 training and can match or outperform strong rank-8 baselines. Our results suggest that at the extreme low-rank limit, initial alignment can matter as much as rank itself.

