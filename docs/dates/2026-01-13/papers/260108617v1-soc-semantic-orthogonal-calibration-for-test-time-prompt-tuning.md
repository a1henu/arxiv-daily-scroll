---
layout: default
title: SoC: Semantic Orthogonal Calibration for Test-Time Prompt Tuning
---

# SoC: Semantic Orthogonal Calibration for Test-Time Prompt Tuning
**arXiv**：[2601.08617v1](https://arxiv.org/abs/2601.08617) · [PDF](https://arxiv.org/pdf/2601.08617.pdf)  
**作者**：Leo Fillioux, Omprakash Chakraborty, Ismail Ben Ayed, Paul-Henry Cournède, Stergios Christodoulidis, Maria Vakalopoulou, Jose Dolz  

**一句话要点**：提出语义正交校准以改进视觉语言模型在测试时提示调优中的不确定性校准

**关键词**：视觉语言模型, 测试时提示调优, 不确定性校准, 正交约束, 语义邻近性, Huber正则化

## 3 点简述
- 核心问题：视觉语言模型在测试时提示调优中，不确定性校准被忽视，现有正交方法可能导致模型过度自信。
- 方法要点：基于理论分析，设计Huber正则化器，实现平滑原型分离并保持语义邻近性，以提升校准性能。
- 实验或效果：在广泛实证验证中，SoC一致改善校准，同时保持竞争性判别能力。

## 摘要（原文）

> With the increasing adoption of vision-language models (VLMs) in critical decision-making systems such as healthcare or autonomous driving, the calibration of their uncertainty estimates becomes paramount. Yet, this dimension has been largely underexplored in the VLM test-time prompt-tuning (TPT) literature, which has predominantly focused on improving their discriminative performance. Recent state-of-the-art advocates for enforcing full orthogonality over pairs of text prompt embeddings to enhance separability, and therefore calibration. Nevertheless, as we theoretically show in this work, the inherent gradients from fully orthogonal constraints will strongly push semantically related classes away, ultimately making the model overconfident. Based on our findings, we propose Semantic Orthogonal Calibration (SoC), a Huber-based regularizer that enforces smooth prototype separation while preserving semantic proximity, thereby improving calibration compared to prior orthogonality-based approaches. Across a comprehensive empirical validation, we demonstrate that SoC consistently improves calibration performance, while also maintaining competitive discriminative capabilities.

