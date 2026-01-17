---
layout: default
title: An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
---

# An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
**arXiv**：[2601.09971v1](https://arxiv.org/abs/2601.09971) · [PDF](https://arxiv.org/pdf/2601.09971.pdf)  
**作者**：Hansen He, Shuheng Li  

**一句话要点**：探索将LLMs与Inception编码器结合的统一架构以提升时间序列分类性能

**关键词**：时间序列分类, 大型语言模型, 混合架构, Inception编码器, 编码器评估

## 3 点简述
- 核心问题：时间序列分类中LLMs的编码器架构选择未充分探索，影响性能提升
- 方法要点：研究混合架构，结合多种时间序列编码器与冻结LLM主干，评估不同编码器家族
- 实验或效果：Inception编码器在集成LLM时表现最佳，为未来LLM驱动的时间序列学习提供方向

## 摘要（原文）

> Time series classification (TSC) is a core machine learning problem with broad applications. Recently there has been growing interest in repurposing large language models (LLMs) for TSC, motivated by their strong reasoning and generalization ability. Prior work has primarily focused on alignment strategies that explicitly map time series data into the textual domain; however, the choice of time series encoder architecture remains underexplored. In this work, we conduct an exploratory study of hybrid architectures that combine specialized time series encoders with a frozen LLM backbone. We evaluate a diverse set of encoder families, including Inception, convolutional, residual, transformer-based, and multilayer perceptron architectures, among which the Inception model is the only encoder architecture that consistently yields positive performance gains when integrated with an LLM backbone. Overall, this study highlights the impact of time series encoder choice in hybrid LLM architectures and points to Inception-based models as a promising direction for future LLM-driven time series learning.

