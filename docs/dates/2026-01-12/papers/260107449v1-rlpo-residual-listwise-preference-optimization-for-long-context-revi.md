---
layout: default
title: RLPO: Residual Listwise Preference Optimization for Long-Context Review Ranking
---

# RLPO: Residual Listwise Preference Optimization for Long-Context Review Ranking
**arXiv**：[2601.07449v1](https://arxiv.org/abs/2601.07449) · [PDF](https://arxiv.org/pdf/2601.07449.pdf)  
**作者**：Hao Jiang, Zhi Yang, Annan Wang, Yichi Zhang, Weisi Lin  

**一句话要点**：提出RLPO以解决长上下文评论排序中点级与列表级方法的权衡问题

**关键词**：评论排序, 长上下文处理, 列表级优化, 残差校正, LLM应用

## 3 点简述
- 核心问题：长上下文评论排序中点级方法忽略列表交互，列表级方法计算昂贵且不稳定
- 方法要点：RLPO基于点级LLM评分器，通过列表级表示残差校正实现高效排序
- 实验或效果：在大型基准上，RLPO提升NDCG@k，并在列表增长时保持鲁棒性

## 摘要（原文）

> Review ranking is pivotal in e-commerce for prioritizing diagnostic and authentic feedback from the deluge of user-generated content. While large language models have improved semantic assessment, existing ranking paradigms face a persistent trade-off in long-context settings. Pointwise scoring is efficient but often fails to account for list-level interactions, leading to miscalibrated top-$k$ rankings. Listwise approaches can leverage global context, yet they are computationally expensive and become unstable as candidate lists grow. To address this, we propose Residual Listwise Preference Optimization (RLPO), which formulates ranking as listwise representation-level residual correction over a strong pointwise LLM scorer. RLPO first produces calibrated pointwise scores and item representations, then applies a lightweight encoder over the representations to predict listwise score residuals, avoiding full token-level listwise processing. We also introduce a large-scale benchmark for long-context review ranking with human verification. Experiments show RLPO improves NDCG@k over strong pointwise and listwise baselines and remains robust as list length increases.

