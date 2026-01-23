---
layout: default
title: Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models
---

# Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models
**arXiv**：[2601.15652v1](https://arxiv.org/abs/2601.15652) · [PDF](https://arxiv.org/pdf/2601.15652.pdf)  
**作者**：Manish Bhatt  

**一句话要点**：提出基于预测编码与信息瓶颈的混合检测框架，以解决大语言模型幻觉检测问题。

**关键词**：幻觉检测, 预测编码, 信息瓶颈, 大语言模型, 可解释性, 监督学习

## 3 点简述
- 核心问题：大语言模型生成看似合理但事实不忠的幻觉，阻碍高风险部署。
- 方法要点：结合预测编码和信息瓶颈提取可解释信号，通过监督学习提升检测性能。
- 实验或效果：在HaluBench上AUROC达0.8669，数据效率高、推理快且模型可解释。

## 摘要（原文）

> Hallucinations in Large Language Models (LLMs) -- generations that are plausible but factually unfaithful -- remain a critical barrier to high-stakes deployment. Current detection methods typically rely on computationally expensive external retrieval loops or opaque black-box LLM judges requiring 70B+ parameters. In this work, we introduce [Model Name], a hybrid detection framework that combines neuroscience-inspired signal design with supervised machine learning. We extract interpretable signals grounded in Predictive Coding (quantifying surprise against internal priors) and the Information Bottleneck (measuring signal retention under perturbation). Through systematic ablation, we demonstrate three key enhancements: Entity-Focused Uptake (concentrating on high-value tokens), Context Adherence (measuring grounding strength), and Falsifiability Score (detecting confident but contradictory claims).
>   Evaluating on HaluBench (n=200, perfectly balanced), our theory-guided baseline achieves 0.8017 AUROC. BASE supervised models reach 0.8274 AUROC, while IMPROVED features boost performance to 0.8669 AUROC (4.95% gain), demonstrating consistent improvements across architectures. This competitive performance is achieved while using 75x less training data than Lynx (200 vs 15,000 samples), 1000x faster inference (5ms vs 5s), and remaining fully interpretable. Crucially, we report a negative result: the Rationalization signal fails to distinguish hallucinations, suggesting that LLMs generate coherent reasoning for false premises ("Sycophancy").
>   This work demonstrates that domain knowledge encoded in signal architecture provides superior data efficiency compared to scaling LLM judges, achieving strong performance with lightweight (less than 1M parameter), explainable models suitable for production deployment.

