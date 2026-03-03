---
layout: default
title: Rich Insights from Cheap Signals: Efficient Evaluations via Tensor Factorization
---

# Rich Insights from Cheap Signals: Efficient Evaluations via Tensor Factorization
**arXiv**：[2603.02029v1](https://arxiv.org/abs/2603.02029) · [PDF](https://arxiv.org/pdf/2603.02029.pdf)  
**作者**：Felipe Maia Polo, Aida Nematzadeh, Virginia Aglietti, Adam Fisch, Isabela Albuquerque  

**一句话要点**：提出基于张量分解的统计模型，以廉价自动评分与有限人工标注高效评估生成模型

**关键词**：张量分解, 生成模型评估, 自动评分校准, 细粒度评估, 样本效率

## 3 点简述
- 核心问题：细粒度评估生成模型时，人工标注成本高，自动评分与人类判断不一致
- 方法要点：用张量分解融合自动评分预训练提示和模型表示，小校准集对齐人类偏好
- 实验或效果：方法对自动评分质量鲁棒，比基线更准确预测人类偏好，提供紧置信区间

## 摘要（原文）

> Moving beyond evaluations that collapse performance across heterogeneous prompts toward fine-grained evaluation at the prompt level, or within relatively homogeneous subsets, is necessary to diagnose generative models' strengths and weaknesses. Such fine-grained evaluations, however, suffer from a data bottleneck: human gold-standard labels are too costly at this scale, while automated ratings are often misaligned with human judgment. To resolve this challenge, we propose a novel statistical model based on tensor factorization that merges cheap autorater data with a limited set of human gold-standard labels. Specifically, our approach uses autorater scores to pretrain latent representations of prompts and generative models, and then aligns those pretrained representations to human preferences using a small calibration set. This sample-efficient methodology is robust to autorater quality, more accurately predicts human preferences on a per-prompt basis than standard baselines, and provides tight confidence intervals for key statistical parameters of interest. We also showcase the practical utility of our method by constructing granular leaderboards based on prompt qualities and by estimating model performance solely from autorater scores, eliminating the need for additional human annotations.

