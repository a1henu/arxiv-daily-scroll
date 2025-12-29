---
layout: default
title: MASFIN: A Multi-Agent System for Decomposed Financial Reasoning and Forecasting
---

# MASFIN: A Multi-Agent System for Decomposed Financial Reasoning and Forecasting
**arXiv**：[2512.21878v1](https://arxiv.org/abs/2512.21878) · [PDF](https://arxiv.org/pdf/2512.21878.pdf)  
**作者**：Marc S. Montalvo, Hamed Yaghoobian  

**一句话要点**：提出MASFIN多智能体系统，用于分解式金融推理与预测，以解决信号整合和偏差缓解问题。

**关键词**：多智能体系统, 金融预测, 大语言模型, 偏差缓解, 量化金融, 可复现推理

## 3 点简述
- 核心问题：传统量化方法易受生存偏差影响，AI方法在信号整合、可复现性和计算效率方面存在挑战。
- 方法要点：集成大语言模型与结构化金融指标和非结构化新闻，嵌入显式偏差缓解协议，使用GPT-4.1-nano实现可复现推理。
- 实验或效果：八周评估中，MASFIN实现7.33%累计回报，在六周内超越S&P 500等基准，但波动性较高。

## 摘要（原文）

> Recent advances in large language models (LLMs) are transforming data-intensive domains, with finance representing a high-stakes environment where transparent and reproducible analysis of heterogeneous signals is essential. Traditional quantitative methods remain vulnerable to survivorship bias, while many AI-driven approaches struggle with signal integration, reproducibility, and computational efficiency. We introduce MASFIN, a modular multi-agent framework that integrates LLMs with structured financial metrics and unstructured news, while embedding explicit bias-mitigation protocols. The system leverages GPT-4.1-nano for reproducability and cost-efficient inference and generates weekly portfolios of 15-30 equities with allocation weights optimized for short-term performance. In an eight-week evaluation, MASFIN delivered a 7.33% cumulative return, outperforming the S&P 500, NASDAQ-100, and Dow Jones benchmarks in six of eight weeks, albeit with higher volatility. These findings demonstrate the promise of bias-aware, generative AI frameworks for financial forecasting and highlight opportunities for modular multi-agent design to advance practical, transparent, and reproducible approaches in quantitative finance.

