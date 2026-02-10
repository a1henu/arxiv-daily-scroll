---
layout: default
title: From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models
---

# From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models
**arXiv**：[2602.08735v1](https://arxiv.org/abs/2602.08735) · [PDF](https://arxiv.org/pdf/2602.08735.pdf)  
**作者**：Masanari Oi, Koki Maeda, Ryuto Koike, Daisuke Oba, Nakamasa Inoue, Naoaki Okazaki  

**一句话要点**：提出HATCH训练框架以提升多模态大语言模型的多图像空间推理能力

**关键词**：多模态大语言模型, 多图像空间推理, 跨视图对应, 视角变换, 训练框架, 人类认知机制

## 3 点简述
- 核心问题：多图像空间推理需整合多视角信息，现有方法仅部分或隐式处理人类认知机制。
- 方法要点：通过补丁级空间对齐和动作-答案推理，显式监督跨视图对应和逐步视角变换。
- 实验或效果：在三个基准测试中优于同规模基线，与更大模型竞争，保持单图像推理能力。

## 摘要（原文）

> While multimodal large language models (MLLMs) have made substantial progress in single-image spatial reasoning, multi-image spatial reasoning, which requires integration of information from multiple viewpoints, remains challenging. Cognitive studies suggest that humans address such tasks through two mechanisms: cross-view correspondence, which identifies regions across different views that correspond to the same physical locations, and stepwise viewpoint transformation, which composes relative viewpoint changes sequentially. However, existing studies incorporate these mechanisms only partially and often implicitly, without explicit supervision for both. We propose Human-Aware Training for Cross-view correspondence and viewpoint cHange (HATCH), a training framework with two complementary objectives: (1) Patch-Level Spatial Alignment, which encourages patch representations to align across views for spatially corresponding regions, and (2) Action-then-Answer Reasoning, which requires the model to generate explicit viewpoint transition actions before predicting the final answer. Experiments on three benchmarks demonstrate that HATCH consistently outperforms baselines of comparable size by a clear margin and achieves competitive results against much larger models, while preserving single-image reasoning capabilities.

