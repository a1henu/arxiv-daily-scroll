---
layout: default
title: Concept Component Analysis: A Principled Approach for Concept Extraction in LLMs
---

# Concept Component Analysis: A Principled Approach for Concept Extraction in LLMs
**arXiv**：[2601.20420v1](https://arxiv.org/abs/2601.20420) · [PDF](https://arxiv.org/pdf/2601.20420.pdf)  
**作者**：Yuhang Liu, Erdun Gao, Dong Gong, Anton van den Hengel, Javen Qinfeng Shi  

**一句话要点**：提出概念成分分析以解决大语言模型中概念提取的理论模糊性问题

**关键词**：概念提取, 大语言模型解释性, 稀疏自编码器, 潜在变量模型, 线性解混, 无监督学习

## 3 点简述
- 核心问题：稀疏自编码器提取概念缺乏理论依据，导致方法设计和评估困难
- 方法要点：基于潜在变量模型，将表示近似为概念对数后验的线性混合，通过无监督线性解混恢复概念
- 实验或效果：实现12个稀疏变体，在多个大语言模型中提取有意义概念，理论优势优于稀疏自编码器

## 摘要（原文）

> Developing human understandable interpretation of large language models (LLMs) becomes increasingly critical for their deployment in essential domains. Mechanistic interpretability seeks to mitigate the issues through extracts human-interpretable process and concepts from LLMs' activations. Sparse autoencoders (SAEs) have emerged as a popular approach for extracting interpretable and monosemantic concepts by decomposing the LLM internal representations into a dictionary. Despite their empirical progress, SAEs suffer from a fundamental theoretical ambiguity: the well-defined correspondence between LLM representations and human-interpretable concepts remains unclear. This lack of theoretical grounding gives rise to several methodological challenges, including difficulties in principled method design and evaluation criteria. In this work, we show that, under mild assumptions, LLM representations can be approximated as a {linear mixture} of the log-posteriors over concepts given the input context, through the lens of a latent variable model where concepts are treated as latent variables. This motivates a principled framework for concept extraction, namely Concept Component Analysis (ConCA), which aims to recover the log-posterior of each concept from LLM representations through a {unsupervised} linear unmixing process. We explore a specific variant, termed sparse ConCA, which leverages a sparsity prior to address the inherent ill-posedness of the unmixing problem. We implement 12 sparse ConCA variants and demonstrate their ability to extract meaningful concepts across multiple LLMs, offering theory-backed advantages over SAEs.

