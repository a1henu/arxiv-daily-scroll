---
layout: default
title: An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
---

# An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
**arXiv**：[2601.09971v1](https://arxiv.org/abs/2601.09971) · [PDF](https://arxiv.org/pdf/2601.09971.pdf)  
**作者**：Hansen He, Shuheng Li  

**一句话要点**：探索将LLMs与时间序列编码器结合的统一架构，用于时间序列分类任务。

**关键词**：时间序列分类, 大语言模型, 混合架构, Inception编码器, 探索性研究

## 3 点简述
- 核心问题：时间序列分类中，LLMs的编码器架构选择未充分探索。
- 方法要点：研究混合架构，结合专用时间序列编码器与冻结LLM骨干。
- 实验或效果：Inception编码器在集成LLM时表现最佳，提示未来研究方向。

## 摘要（原文）

> Time series classification (TSC) is a core machine learning problem with broad applications. Recently there has been growing interest in repurposing large language models (LLMs) for TSC, motivated by their strong reasoning and generalization ability. Prior work has primarily focused on alignment strategies that explicitly map time series data into the textual domain; however, the choice of time series encoder architecture remains underexplored. In this work, we conduct an exploratory study of hybrid architectures that combine specialized time series encoders with a frozen LLM backbone. We evaluate a diverse set of encoder families, including Inception, convolutional, residual, transformer-based, and multilayer perceptron architectures, among which the Inception model is the only encoder architecture that consistently yields positive performance gains when integrated with an LLM backbone. Overall, this study highlights the impact of time series encoder choice in hybrid LLM architectures and points to Inception-based models as a promising direction for future LLM-driven time series learning.

