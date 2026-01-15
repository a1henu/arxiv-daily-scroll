---
layout: default
title: ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection
---

# ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection
**arXiv**：[2601.09195v1](https://arxiv.org/abs/2601.09195) · [PDF](https://arxiv.org/pdf/2601.09195.pdf)  
**作者**：Tao Liu, Taiqiang Wu, Runming Yang, Shaoning Sun, Junjie Wang, Yujiu Yang  

**一句话要点**：提出ProFit方法，通过概率引导的令牌选择缓解监督微调中的单参考过拟合问题。

**关键词**：监督微调, 令牌选择, 过拟合缓解, 概率引导, 语言模型对齐

## 3 点简述
- 传统监督微调强制对齐单一参考答案，忽略语言一对多特性，导致模型过拟合非核心表达。
- 基于令牌概率与语义重要性关联，ProFit选择性掩码低概率令牌，防止表面级过拟合。
- 实验表明ProFit在通用推理和数学基准上持续优于传统监督微调基线。

## 摘要（原文）

> Supervised fine-tuning (SFT) is a fundamental post-training strategy to align Large Language Models (LLMs) with human intent. However, traditional SFT often ignores the one-to-many nature of language by forcing alignment with a single reference answer, leading to the model overfitting to non-core expressions. Although our empirical analysis suggests that introducing multiple reference answers can mitigate this issue, the prohibitive data and computational costs necessitate a strategic shift: prioritizing the mitigation of single-reference overfitting over the costly pursuit of answer diversity. To achieve this, we reveal the intrinsic connection between token probability and semantic importance: high-probability tokens carry the core logical framework, while low-probability tokens are mostly replaceable expressions. Based on this insight, we propose ProFit, which selectively masks low-probability tokens to prevent surface-level overfitting. Extensive experiments confirm that ProFit consistently outperforms traditional SFT baselines on general reasoning and mathematical benchmarks.

