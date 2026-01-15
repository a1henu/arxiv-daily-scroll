---
layout: default
title: Bias Dynamics in BabyLMs: Towards a Compute-Efficient Sandbox for Democratising Pre-Training Debiasing
---

# Bias Dynamics in BabyLMs: Towards a Compute-Efficient Sandbox for Democratising Pre-Training Debiasing
**arXiv**：[2601.09421v1](https://arxiv.org/abs/2601.09421) · [PDF](https://arxiv.org/pdf/2601.09421.pdf)  
**作者**：Filip Trhlik, Andrew Caines, Paula Buttery  

**一句话要点**：提出BabyLMs作为低成本代理模型，以民主化预训练去偏研究并降低计算成本。

**关键词**：语言模型去偏, 预训练代理模型, 计算效率, 偏见动态分析, 民主化研究

## 3 点简述
- 核心问题：大型语言模型训练成本高，去偏研究受限，现有方法难以解决偏见根源。
- 方法要点：使用BabyLMs作为紧凑BERT-like模型，模拟大型模型偏见形成与学习动态。
- 实验或效果：BabyLMs与BERT偏见模式对齐，预训练成本从500+降至30 GPU小时，支持去偏实验。

## 摘要（原文）

> Pre-trained language models (LMs) have, over the last few years, grown substantially in both societal adoption and training costs. This rapid growth in size has constrained progress in understanding and mitigating their biases. Since re-training LMs is prohibitively expensive, most debiasing work has focused on post-hoc or masking-based strategies, which often fail to address the underlying causes of bias. In this work, we seek to democratise pre-model debiasing research by using low-cost proxy models. Specifically, we investigate BabyLMs, compact BERT-like models trained on small and mutable corpora that can approximate bias acquisition and learning dynamics of larger models. We show that BabyLMs display closely aligned patterns of intrinsic bias formation and performance development compared to standard BERT models, despite their drastically reduced size. Furthermore, correlations between BabyLMs and BERT hold across multiple intra-model and post-model debiasing methods. Leveraging these similarities, we conduct pre-model debiasing experiments with BabyLMs, replicating prior findings and presenting new insights regarding the influence of gender imbalance and toxicity on bias formation. Our results demonstrate that BabyLMs can serve as an effective sandbox for large-scale LMs, reducing pre-training costs from over 500 GPU-hours to under 30 GPU-hours. This provides a way to democratise pre-model debiasing research and enables faster, more accessible exploration of methods for building fairer LMs.

