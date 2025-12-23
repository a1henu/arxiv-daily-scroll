---
layout: default
title: VIGOR+: Iterative Confounder Generation and Validation via LLM-CEVAE Feedback Loop
---

# VIGOR+: Iterative Confounder Generation and Validation via LLM-CEVAE Feedback Loop
**arXiv**：[2512.19349v1](https://arxiv.org/abs/2512.19349) · [PDF](https://arxiv.org/pdf/2512.19349.pdf)  
**作者**：JiaWei Zhu, ZiHeng Liu  

**一句话要点**：提出VIGOR+框架，通过LLM-CEVAE反馈循环迭代生成和验证隐藏混杂因子以解决观测数据因果推断问题。

**关键词**：因果推断, 隐藏混杂因子, 大语言模型, 变分自编码器, 迭代优化, 反馈机制

## 3 点简述
- 核心问题：隐藏混杂因子在观测数据因果推断中难以识别，LLM生成的混杂因子语义合理但统计效用不足。
- 方法要点：建立LLM生成与CEVAE验证的迭代反馈机制，利用统计信号指导LLM优化混杂因子生成。
- 实验或效果：形式化反馈机制，证明收敛性，提供完整算法框架，提升混杂因子统计效用。

## 摘要（原文）

> Hidden confounding remains a fundamental challenge in causal inference from observational data. Recent advances leverage Large Language Models (LLMs) to generate plausible hidden confounders based on domain knowledge, yet a critical gap exists: LLM-generated confounders often exhibit semantic plausibility without statistical utility. We propose VIGOR+ (Variational Information Gain for iterative cOnfounder Refinement), a novel framework that closes the loop between LLM-based confounder generation and CEVAE-based statistical validation. Unlike prior approaches that treat generation and validation as separate stages, VIGOR+ establishes an iterative feedback mechanism: validation signals from CEVAE (including information gain, latent consistency metrics, and diagnostic messages) are transformed into natural language feedback that guides subsequent LLM generation rounds. This iterative refinement continues until convergence criteria are met. We formalize the feedback mechanism, prove convergence properties under mild assumptions, and provide a complete algorithmic framework.

