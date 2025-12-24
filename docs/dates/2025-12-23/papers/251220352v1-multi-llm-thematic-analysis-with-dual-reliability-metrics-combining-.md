---
layout: default
title: Multi-LLM Thematic Analysis with Dual Reliability Metrics: Combining Cohen's Kappa and Semantic Similarity for Qualitative Research Validation
---

# Multi-LLM Thematic Analysis with Dual Reliability Metrics: Combining Cohen's Kappa and Semantic Similarity for Qualitative Research Validation
**arXiv**：[2512.20352v1](https://arxiv.org/abs/2512.20352) · [PDF](https://arxiv.org/pdf/2512.20352.pdf)  
**作者**：Nilesh Jain, Seyi Adeyinka, Leor Roseman, Aza Allsop  

**一句话要点**：提出多LLM主题分析框架，结合双可靠性指标以解决定性研究中的可靠性挑战。

**关键词**：多LLM主题分析, 可靠性验证, Cohen's Kappa, 语义相似度, 定性研究, 共识主题提取

## 3 点简述
- 核心问题：定性研究依赖人工编码，存在耗时且一致性低的问题。
- 方法要点：集成多个LLM运行，使用Cohen's Kappa和余弦相似度评估可靠性。
- 实验或效果：在迷幻艺术疗法访谈数据上验证，Gemini可靠性最高，所有模型κ>0.80。

## 摘要（原文）

> Qualitative research faces a critical reliability challenge: traditional inter-rater agreement methods require multiple human coders, are time-intensive, and often yield moderate consistency. We present a multi-perspective validation framework for LLM-based thematic analysis that combines ensemble validation with dual reliability metrics: Cohen's Kappa ($κ$) for inter-rater agreement and cosine similarity for semantic consistency. Our framework enables configurable analysis parameters (1-6 seeds, temperature 0.0-2.0), supports custom prompt structures with variable substitution, and provides consensus theme extraction across any JSON format. As proof-of-concept, we evaluate three leading LLMs (Gemini 2.5 Pro, GPT-4o, Claude 3.5 Sonnet) on a psychedelic art therapy interview transcript, conducting six independent runs per model. Results demonstrate Gemini achieves highest reliability ($κ= 0.907$, cosine=95.3%), followed by GPT-4o ($κ= 0.853$, cosine=92.6%) and Claude ($κ= 0.842$, cosine=92.1%). All three models achieve a high agreement ($κ> 0.80$), validating the multi-run ensemble approach. The framework successfully extracts consensus themes across runs, with Gemini identifying 6 consensus themes (50-83% consistency), GPT-4o identifying 5 themes, and Claude 4 themes. Our open-source implementation provides researchers with transparent reliability metrics, flexible configuration, and structure-agnostic consensus extraction, establishing methodological foundations for reliable AI-assisted qualitative research.

