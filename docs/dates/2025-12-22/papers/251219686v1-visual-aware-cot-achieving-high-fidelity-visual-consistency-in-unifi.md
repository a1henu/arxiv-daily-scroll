---
layout: default
title: Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models
---

# Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models
**arXiv**：[2512.19686v1](https://arxiv.org/abs/2512.19686) · [PDF](https://arxiv.org/pdf/2512.19686.pdf)  
**作者**：Zixuan Ye, Quande Liu, Cong Wei, Yuanxing Zhang, Xintao Wang, Pengfei Wan, Kun Gai, Wenhan Luo  

**一句话要点**：提出Visual-Aware CoT以解决统一模型在多模态生成中视觉上下文一致性问题

**关键词**：视觉上下文一致性, 多模态生成, 自适应视觉规划, 迭代视觉校正, 统一模型, 监督微调

## 3 点简述
- 核心问题：当前统一模型在生成时忽视视觉上下文一致性，导致关键视觉特征丢失
- 方法要点：通过自适应视觉规划和迭代视觉校正，集成视觉一致性到推理过程
- 实验或效果：在实验中优于零样本模型和文本CoT方法，展示更高视觉一致性

## 摘要（原文）

> Recently, the introduction of Chain-of-Thought (CoT) has largely improved the generation ability of unified models. However, it is observed that the current thinking process during generation mainly focuses on the text consistency with the text prompt, ignoring the \textbf{visual context consistency} with the visual reference images during the multi-modal generation, e.g., multi-reference generation. The lack of such consistency results in the failure in maintaining key visual features (like human ID, object attribute, style). To this end, we integrate the visual context consistency into the reasoning of unified models, explicitly motivating the model to sustain such consistency by 1) Adaptive Visual Planning: generating structured visual check list to figure out the visual element of needed consistency keeping, and 2) Iterative Visual Correction: performing self-reflection with the guidance of check lists and refining the generated result in an iterative manner. To achieve this, we use supervised finetuning to teach the model how to plan the visual checking, conduct self-reflection and self-refinement, and use flow-GRPO to further enhance the visual consistency through a customized visual checking reward. The experiments show that our method outperforms both zero-shot unified models and those with text CoTs in multi-modal generation, demonstrating higher visual context consistency.

