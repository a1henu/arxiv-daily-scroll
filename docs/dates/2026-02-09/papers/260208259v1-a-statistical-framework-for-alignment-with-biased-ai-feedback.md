---
layout: default
title: A Statistical Framework for Alignment with Biased AI Feedback
---

# A Statistical Framework for Alignment with Biased AI Feedback
**arXiv**：[2602.08259v1](https://arxiv.org/abs/2602.08259) · [PDF](https://arxiv.org/pdf/2602.08259.pdf)  
**作者**：Xintao Xia, Zhiqiu Xia, Linjun Zhang, Zhanrui Cai  

**一句话要点**：提出两种去偏对齐方法以解决AI反馈偏差问题，提升大语言模型对齐效率。

**关键词**：AI反馈偏差, 去偏对齐, 直接偏好优化, 统计框架, 大语言模型对齐

## 3 点简述
- 核心问题：AI反馈标签相比高质量人类反馈存在系统性偏差，影响对齐效果。
- 方法要点：DDPO通过残差校正和密度比重加权去偏，DIPO直接估计人类偏好概率，无需参数化奖励模型。
- 实验或效果：在情感生成、摘要和单轮对话任务中，方法显著提升对齐效率，接近全人类标注数据的性能。

## 摘要（原文）

> Modern alignment pipelines are increasingly replacing expensive human preference labels with evaluations from large language models (LLM-as-Judge). However, AI labels can be systematically biased compared to high-quality human feedback datasets. In this paper, we develop two debiased alignment methods within a general framework that accommodates heterogeneous prompt-response distributions and external human feedback sources. Debiased Direct Preference Optimization (DDPO) augments standard DPO with a residual-based correction and density-ratio reweighting to mitigate systematic bias, while retaining DPO's computational efficiency. Debiased Identity Preference Optimization (DIPO) directly estimates human preference probabilities without imposing a parametric reward model. We provide theoretical guarantees for both methods: DDPO offers a practical and computationally efficient solution for large-scale alignment, whereas DIPO serves as a robust, statistically optimal alternative that attains the semiparametric efficiency bound. Empirical studies on sentiment generation, summarization, and single-turn dialogue demonstrate that the proposed methods substantially improve alignment efficiency and recover performance close to that of an oracle trained on fully human-labeled data.

