---
layout: default
title: Similarity of Processing Steps in Vision Model Representations
---

# Similarity of Processing Steps in Vision Model Representations
**arXiv**：[2601.21621v1](https://arxiv.org/abs/2601.21621) · [PDF](https://arxiv.org/pdf/2601.21621.pdf)  
**作者**：Matéo Mahaut, Marco Baroni  

**一句话要点**：研究视觉模型处理步骤相似性，揭示不同模型在中间层和操作上的收敛差异。

**关键词**：视觉模型表示, 处理步骤相似性, 模型收敛分析, CNN与Transformer比较, 表示距离量化

## 3 点简述
- 核心问题：探索不同视觉模型是否在中间处理步骤和操作上收敛到相似状态，而非仅最终表示。
- 方法要点：量化不同模型在多个处理阶段的表示距离，分析距离演变以识别差异最大的处理步骤。
- 实验或效果：发现相似位置的层表示最相似，但CNN与Transformer模型行为不同，分类器模型在最终层丢弃低层信息。

## 摘要（原文）

> Recent literature suggests that the bigger the model, the more likely it is to converge to similar, ``universal'' representations, despite different training objectives, datasets, or modalities. While this literature shows that there is an area where model representations are similar, we study here how vision models might get to those representations -- in particular, do they also converge to the same intermediate steps and operations? We therefore study the processes that lead to convergent representations in different models. First, we quantify distance between different model representations at different stages. We follow the evolution of distances between models throughout processing, identifying the processing steps which are most different between models. We find that while layers at similar positions in different models have the most similar representations, strong differences remain. Classifier models, unlike the others, will discard information about low-level image statistics in their final layers. CNN- and transformer-based models also behave differently, with transformer models applying smoother changes to representations from one layer to the next. These distinctions clarify the level and nature of convergence between model representations, and enables a more qualitative account of the underlying processes in image models.

