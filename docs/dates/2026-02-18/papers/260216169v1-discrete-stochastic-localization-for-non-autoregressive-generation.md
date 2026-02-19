---
layout: default
title: Discrete Stochastic Localization for Non-autoregressive Generation
---

# Discrete Stochastic Localization for Non-autoregressive Generation
**arXiv**：[2602.16169v1](https://arxiv.org/abs/2602.16169) · [PDF](https://arxiv.org/pdf/2602.16169.pdf)  
**作者**：Yunshu Wu, Jiayi Cheng, Partha Thakuria, Rob Brekelmans, Evangelos E. Papalexakis, Greg Ver Steeg  

**一句话要点**：提出离散随机定位以提升掩码扩散语言模型的采样效率

**关键词**：非自回归生成, 掩码扩散语言模型, 迭代精炼, 采样效率, 去噪器训练

## 3 点简述
- 非自回归生成中迭代精炼存在误差累积和分布偏移问题
- 训练单一信噪比不变去噪器，桥接噪声与掩码端点损坏
- 在低步数预算下显著提升MAUVE分数，匹配自回归质量

## 摘要（原文）

> Non-autoregressive (NAR) generation reduces decoding latency by predicting many tokens in parallel, but iterative refinement often suffers from error accumulation and distribution shift under self-generated drafts. Masked diffusion language models (MDLMs) and their remasking samplers (e.g., ReMDM) can be viewed as modern NAR iterative refinement, where generation repeatedly revises a partially observed draft. In this work we show that \emph{training alone} can substantially improve the step-efficiency of MDLM/ReMDM sampling. We propose \textsc{DSL} (Discrete Stochastic Localization), which trains a single SNR-invariant denoiser across a continuum of corruption levels, bridging intermediate draft noise and mask-style endpoint corruption within one Diffusion Transformer. On OpenWebText, \textsc{DSL} fine-tuning yields large MAUVE gains at low step budgets, surpassing the MDLM+ReMDM baseline with \(\sim\)4$\times$ fewer denoiser evaluations, and matches autoregressive quality at high budgets. Analyses show improved self-correction and uncertainty calibration, making remasking markedly more compute-efficient.

