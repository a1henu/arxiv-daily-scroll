---
layout: default
title: How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing
---

# How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing
**arXiv**：[2602.01851v1](https://arxiv.org/abs/2602.01851) · [PDF](https://arxiv.org/pdf/2602.01851.pdf)  
**作者**：Huanyu Zhang, Xuehai Bai, Chengzu Li, Chen Liang, Haochen Tian, Haodong Li, Ruichuan An, Yifan Zhang, Anna Korhonen, Zhang Zhang, Liang Wang, Tieniu Tan  

**一句话要点**：提出VIBE基准以评估模型在视觉指令驱动的图像编辑中的性能

**关键词**：视觉指令编辑, 基准评估, 多模态交互, 图像生成, 模型性能分析

## 3 点简述
- 核心问题：现有图像编辑系统主要依赖文本指导，缺乏对视觉指令（如草图）的评估。
- 方法要点：构建VIBE基准，包含三层交互层次，涵盖指示性定位、形态操作和因果推理。
- 实验或效果：评估17个模型，发现专有模型优于开源模型，但性能随任务难度增加而下降。

## 摘要（原文）

> Recent generative models have achieved remarkable progress in image editing. However, existing systems and benchmarks remain largely text-guided. In contrast, human communication is inherently multimodal, where visual instructions such as sketches efficiently convey spatial and structural intent. To address this gap, we introduce VIBE, the Visual Instruction Benchmark for Image Editing with a three-level interaction hierarchy that captures deictic grounding, morphological manipulation, and causal reasoning. Across these levels, we curate high-quality and diverse test cases that reflect progressively increasing complexity in visual instruction following. We further propose a robust LMM-as-a-judge evaluation framework with task-specific metrics to enable scalable and fine-grained assessment. Through a comprehensive evaluation of 17 representative open-source and proprietary image editing models, we find that proprietary models exhibit early-stage visual instruction-following capabilities and consistently outperform open-source models. However, performance degrades markedly with increasing task difficulty even for the strongest systems, highlighting promising directions for future research.

