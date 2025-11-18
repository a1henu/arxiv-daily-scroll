---
layout: default
title: Uncovering and Mitigating Transient Blindness in Multimodal Model Editing
---

# Uncovering and Mitigating Transient Blindness in Multimodal Model Editing
**arXiv**：[2511.13243v1](https://arxiv.org/abs/2511.13243) · [PDF](https://arxiv.org/pdf/2511.13243.pdf)  
**作者**：Xiaoqi Han, Ru Li, Ran Yi, Hongye Tan, Zhuomin Liang, Víctor Gutiérrez-Basulto, Jeff Z. Pan  

**一句话要点**：提出多模态模型编辑的局部性评估框架和对抗损失以缓解瞬态盲视

**关键词**：多模态模型编辑, 瞬态盲视, 局部性评估, 视觉问答, 对抗训练, 跨模态表示

## 3 点简述
- 核心问题：现有多模态模型编辑评估方法高估成功，存在过拟合和瞬态盲视现象。
- 方法要点：引入局部性评估框架和De-VQA动态评估，使用对抗损失平衡跨模态表示。
- 实验或效果：方法优于基线，平均减少瞬态盲视并提升局部性17%。

## 摘要（原文）

> Multimodal Model Editing (MMED) aims to correct erroneous knowledge in multimodal models. Existing evaluation methods, adapted from textual model editing, overstate success by relying on low-similarity or random inputs, obscure overfitting. We propose a comprehensive locality evaluation framework, covering three key dimensions: random-image locality, no-image locality, and consistent-image locality, operationalized through seven distinct data types, enabling a detailed and structured analysis of multimodal edits. We introduce De-VQA, a dynamic evaluation for visual question answering, uncovering a phenomenon we term transient blindness, overfitting to edit-similar text while ignoring visuals. Token analysis shows edits disproportionately affect textual tokens. We propose locality-aware adversarial losses to balance cross-modal representations. Empirical results demonstrate that our approach consistently outperforms existing baselines, reducing transient blindness and improving locality by 17% on average.

