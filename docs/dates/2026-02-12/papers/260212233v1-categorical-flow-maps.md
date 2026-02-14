---
layout: default
title: Categorical Flow Maps
---

# Categorical Flow Maps
**arXiv**：[2602.12233v1](https://arxiv.org/abs/2602.12233) · [PDF](https://arxiv.org/pdf/2602.12233.pdf)  
**作者**：Daan Roos, Oscar Davis, Floor Eijkelboom, Michael Bronstein, Max Welling, İsmail İlkan Ceylan, Luca Ambrogioni, Jan-Willem van de Meent  

**一句话要点**：提出Categorical Flow Maps以加速分类数据的少步生成，通过自蒸馏实现连续轨迹建模。

**关键词**：流匹配, 分类数据生成, 自蒸馏, 少步推理, 连续轨迹建模, 端点一致性

## 3 点简述
- 核心问题：加速基于流匹配的分类数据生成，传统方法在少步推理中效率低或约束难。
- 方法要点：定义流向单纯形的流映射，通过自蒸馏和端点一致性目标训练连续轨迹，自然约束预测。
- 实验或效果：在图像、分子图和文本上实现少步生成SOTA，单步生成表现强劲，支持现有引导技术。

## 摘要（原文）

> We introduce Categorical Flow Maps, a flow-matching method for accelerated few-step generation of categorical data via self-distillation. Building on recent variational formulations of flow matching and the broader trend towards accelerated inference in diffusion and flow-based models, we define a flow map towards the simplex that transports probability mass toward a predicted endpoint, yielding a parametrisation that naturally constrains model predictions. Since our trajectories are continuous rather than discrete, Categorical Flow Maps can be trained with existing distillation techniques, as well as a new objective based on endpoint consistency. This continuous formulation also automatically unlocks test-time inference: we can directly reuse existing guidance and reweighting techniques in the categorical setting to steer sampling toward downstream objectives. Empirically, we achieve state-of-the-art few-step results on images, molecular graphs, and text, with strong performance even in single-step generation.

