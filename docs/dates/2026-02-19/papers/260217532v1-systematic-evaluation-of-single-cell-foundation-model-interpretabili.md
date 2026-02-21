---
layout: default
title: Systematic Evaluation of Single-Cell Foundation Model Interpretability Reveals Attention Captures Co-Expression Rather Than Unique Regulatory Signal
---

# Systematic Evaluation of Single-Cell Foundation Model Interpretability Reveals Attention Captures Co-Expression Rather Than Unique Regulatory Signal
**arXiv**：[2602.17532v1](https://arxiv.org/abs/2602.17532) · [PDF](https://arxiv.org/pdf/2602.17532.pdf)  
**作者**：Ihor Kendiukhov  

**一句话要点**：提出系统性评估框架以揭示单细胞基础模型中注意力机制捕获共表达而非独特调控信号

**关键词**：单细胞基础模型, 注意力机制, 可解释性评估, 基因调控网络, 系统性框架, 共表达分析

## 3 点简述
- 核心问题：评估单细胞基础模型的机制可解释性，关注注意力模式是否编码独特生物学信号
- 方法要点：开发包含37项分析、153个统计测试的系统框架，应用于scGPT和Geneformer模型
- 实验或效果：发现注意力结构无增量预测价值，基因级基线更优，并提出CSSI方法提升GRN恢复

## 摘要（原文）

> We present a systematic evaluation framework - thirty-seven analyses, 153 statistical tests, four cell types, two perturbation modalities - for assessing mechanistic interpretability in single-cell foundation models. Applying this framework to scGPT and Geneformer, we find that attention patterns encode structured biological information with layer-specific organisation - protein-protein interactions in early layers, transcriptional regulation in late layers - but this structure provides no incremental value for perturbation prediction: trivial gene-level baselines outperform both attention and correlation edges (AUROC 0.81-0.88 versus 0.70), pairwise edge scores add zero predictive contribution, and causal ablation of regulatory heads produces no degradation. These findings generalise from K562 to RPE1 cells; the attention-correlation relationship is context-dependent, but gene-level dominance is universal. Cell-State Stratified Interpretability (CSSI) addresses an attention-specific scaling failure, improving GRN recovery up to 1.85x. The framework establishes reusable quality-control standards for the field.

