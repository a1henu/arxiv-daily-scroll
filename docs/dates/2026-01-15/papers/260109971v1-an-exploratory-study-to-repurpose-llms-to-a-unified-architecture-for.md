---
layout: default
title: An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
---

# An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification
**arXiv**：[2601.09971v1](https://arxiv.org/abs/2601.09971) · [PDF](https://arxiv.org/pdf/2601.09971.pdf)  
**作者**：Hansen He, Shuheng Li  

**一句话要点**：探索将LLMs与时间序列编码器结合的统一架构，用于时间序列分类

**关键词**：时间序列分类, 大型语言模型, 混合架构, 编码器选择, Inception模型, 探索性研究

## 3 点简述
- 研究核心问题：时间序列分类中LLMs与编码器架构的集成选择
- 方法要点：评估多种编码器家族，发现Inception模型与冻结LLM结合效果最佳
- 实验效果：Inception编码器在混合架构中持续提升性能，为未来研究提供方向

## 摘要（原文）

> Time series classification (TSC) is a core machine learning problem with broad applications. Recently there has been growing interest in repurposing large language models (LLMs) for TSC, motivated by their strong reasoning and generalization ability. Prior work has primarily focused on alignment strategies that explicitly map time series data into the textual domain; however, the choice of time series encoder architecture remains underexplored. In this work, we conduct an exploratory study of hybrid architectures that combine specialized time series encoders with a frozen LLM backbone. We evaluate a diverse set of encoder families, including Inception, convolutional, residual, transformer-based, and multilayer perceptron architectures, among which the Inception model is the only encoder architecture that consistently yields positive performance gains when integrated with an LLM backbone. Overall, this study highlights the impact of time series encoder choice in hybrid LLM architectures and points to Inception-based models as a promising direction for future LLM-driven time series learning.

