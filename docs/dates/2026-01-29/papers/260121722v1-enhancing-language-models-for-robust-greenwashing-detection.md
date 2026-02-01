---
layout: default
title: Enhancing Language Models for Robust Greenwashing Detection
---

# Enhancing Language Models for Robust Greenwashing Detection
**arXiv**：[2601.21722v1](https://arxiv.org/abs/2601.21722) · [PDF](https://arxiv.org/pdf/2601.21722.pdf)  
**作者**：Neil Heinrich Braun, Keane Ong, Rui Mao, Erik Cambria, Gianmarco Mengaldo  

**一句话要点**：提出参数高效框架以增强语言模型在绿色清洗检测中的鲁棒性

**关键词**：绿色清洗检测, 语言模型增强, 对比学习, 序数排序, 参数高效框架, 多目标优化

## 3 点简述
- 核心问题：现有NLP模型对绿色清洗和模糊声明的鲁棒性不足，依赖表面模式泛化差。
- 方法要点：结合对比学习和序数排序目标结构化LLM潜在空间，并引入门控特征调制和MetaGradNorm优化。
- 实验或效果：跨类别实验显示优于基线，揭示了表示刚性与泛化之间的权衡。

## 摘要（原文）

> Sustainability reports are critical for ESG assessment, yet greenwashing and vague claims often undermine their reliability. Existing NLP models lack robustness to these practices, typically relying on surface-level patterns that generalize poorly. We propose a parameter-efficient framework that structures LLM latent spaces by combining contrastive learning with an ordinal ranking objective to capture graded distinctions between concrete actions and ambiguous claims. Our approach incorporates gated feature modulation to filter disclosure noise and utilizes MetaGradNorm to stabilize multi-objective optimization. Experiments in cross-category settings demonstrate superior robustness over standard baselines while revealing a trade-off between representational rigidity and generalization.

