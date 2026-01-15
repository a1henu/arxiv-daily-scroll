---
layout: default
title: Interpretable Probability Estimation with LLMs via Shapley Reconstruction
---

# Interpretable Probability Estimation with LLMs via Shapley Reconstruction
**arXiv**：[2601.09151v1](https://arxiv.org/abs/2601.09151) · [PDF](https://arxiv.org/pdf/2601.09151.pdf)  
**作者**：Yang Nan, Qihao Wen, Jiahao Wang, Pengfei He, Ravi Tandon, Yong Ge, Han Xu  

**一句话要点**：提出PRISM框架，通过Shapley值分解LLM概率估计以提升透明度和准确性

**关键词**：概率估计, Shapley值, 可解释性, 大语言模型, 决策支持

## 3 点简述
- 核心问题：LLM直接概率估计存在输出噪声和过程不透明问题
- 方法要点：使用Shapley值量化输入因素贡献，并聚合重建校准估计
- 实验或效果：在金融、医疗和农业领域验证PRISM优于直接提示和其他基线

## 摘要（原文）

> Large Language Models (LLMs) demonstrate potential to estimate the probability of uncertain events, by leveraging their extensive knowledge and reasoning capabilities. This ability can be applied to support intelligent decision-making across diverse fields, such as financial forecasting and preventive healthcare. However, directly prompting LLMs for probability estimation faces significant challenges: their outputs are often noisy, and the underlying predicting process is opaque. In this paper, we propose PRISM: Probability Reconstruction via Shapley Measures, a framework that brings transparency and precision to LLM-based probability estimation. PRISM decomposes an LLM's prediction by quantifying the marginal contribution of each input factor using Shapley values. These factor-level contributions are then aggregated to reconstruct a calibrated final estimate. In our experiments, we demonstrate PRISM improves predictive accuracy over direct prompting and other baselines, across multiple domains including finance, healthcare, and agriculture. Beyond performance, PRISM provides a transparent prediction pipeline: our case studies visualize how individual factors shape the final estimate, helping build trust in LLM-based decision support systems.

