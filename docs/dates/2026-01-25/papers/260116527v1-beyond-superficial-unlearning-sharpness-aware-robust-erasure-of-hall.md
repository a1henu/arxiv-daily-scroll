---
layout: default
title: Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs
---

# Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs
**arXiv**：[2601.16527v1](https://arxiv.org/abs/2601.16527) · [PDF](https://arxiv.org/pdf/2601.16527.pdf)  
**作者**：Xianya Fang, Feiyang Ren, Xiang Chen, Yu Tian, Zhen Bi, Haiyang Yu, Sheng-Jun Huang  

**一句话要点**：提出SARE方法，通过锐度感知优化解决多模态大语言模型幻觉消除的结构脆弱性问题。

**关键词**：多模态大语言模型, 对象幻觉, 遗忘学习, 锐度感知优化, 损失景观平坦化, 稳健性

## 3 点简述
- 核心问题：标准遗忘方法仅实现表面抑制，模型陷入尖锐最小值，导致幻觉在轻量再学习后灾难性复发。
- 方法要点：将遗忘建模为定向最小-最大优化问题，使用Targeted-SAM机制显式平坦化幻觉概念周围的损失景观。
- 实验或效果：SARE在消除效果上显著优于基线，保持生成质量，并能持久抑制幻觉对抗再学习和参数更新。

## 摘要（原文）

> Multimodal LLMs are powerful but prone to object hallucinations, which describe non-existent entities and harm reliability. While recent unlearning methods attempt to mitigate this, we identify a critical flaw: structural fragility. We empirically demonstrate that standard erasure achieves only superficial suppression, trapping the model in sharp minima where hallucinations catastrophically resurge after lightweight relearning. To ensure geometric stability, we propose SARE, which casts unlearning as a targeted min-max optimization problem and uses a Targeted-SAM mechanism to explicitly flatten the loss landscape around hallucinated concepts. By suppressing hallucinations under simulated worst-case parameter perturbations, our framework ensures robust removal stable against weight shifts. Extensive experiments demonstrate that SARE significantly outperforms baselines in erasure efficacy while preserving general generation quality. Crucially, it maintains persistent hallucination suppression against relearning and parameter updates, validating the effectiveness of geometric stabilization.

