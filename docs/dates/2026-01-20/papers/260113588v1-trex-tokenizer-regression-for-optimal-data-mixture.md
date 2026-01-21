---
layout: default
title: TREX: Tokenizer Regression for Optimal Data Mixture
---

# TREX: Tokenizer Regression for Optimal Data Mixture
**arXiv**：[2601.13588v1](https://arxiv.org/abs/2601.13588) · [PDF](https://arxiv.org/pdf/2601.13588.pdf)  
**作者**：Inho Won, Hangyeol Yoo, Minkyung Cho, Jungyeul Park, Hoyun Song, KyungTae Lim  

**一句话要点**：提出TREX框架以优化多语言大语言模型分词器的数据混合比例

**关键词**：多语言分词器, 数据混合优化, 回归框架, 压缩效率, 大语言模型训练

## 3 点简述
- 核心问题：多语言分词器设计需平衡数据混合比例，现有方法依赖启发式或高成本搜索
- 方法要点：基于回归框架，训练代理分词器预测压缩性能，实现高效混合比例搜索
- 实验或效果：TREX预测的混合比例在压缩效率上优于LLaMA3和均匀分布，提升达12%

## 摘要（原文）

> Building effective tokenizers for multilingual Large Language Models (LLMs) requires careful control over language-specific data mixtures. While a tokenizer's compression performance critically affects the efficiency of LLM training and inference, existing approaches rely on heuristics or costly large-scale searches to determine optimal language ratios. We introduce Tokenizer Regression for Optimal Data MiXture (TREX), a regression-based framework that efficiently predicts the optimal data mixture for tokenizer training. TREX trains small-scale proxy tokenizers on random mixtures, gathers their compression statistics, and learns to predict compression performance from data mixtures. This learned model enables scalable mixture search before large-scale tokenizer training, mitigating the accuracy-cost trade-off in multilingual tokenizer design. Tokenizers trained with TReX's predicted mixtures outperform mixtures based on LLaMA3 and uniform distributions by up to 12% in both inand out-of-distribution compression efficiency, demonstrating strong scalability, robustness, and practical effectiveness.

