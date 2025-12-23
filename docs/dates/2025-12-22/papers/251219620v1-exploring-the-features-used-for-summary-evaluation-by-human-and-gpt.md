---
layout: default
title: Exploring the features used for summary evaluation by Human and GPT
---

# Exploring the features used for summary evaluation by Human and GPT
**arXiv**：[2512.19620v1](https://arxiv.org/abs/2512.19620) · [PDF](https://arxiv.org/pdf/2512.19620.pdf)  
**作者**：Zahra Sadeghi, Evangelos Milios, Frank Rudzicz  

**一句话要点**：探索人类与GPT用于摘要评估的特征，以提升大语言模型与人类判断的一致性

**关键词**：摘要评估, 大语言模型, 特征分析, 人类对齐, 评估指标, GPT优化

## 3 点简述
- 核心问题：研究人类与GPT在摘要评估中利用的特征差异，以及如何映射评估分数与指标
- 方法要点：通过统计和机器学习指标分析特征，并指导GPT使用人类评估指标
- 实验或效果：发现GPT采用人类指标可改进其判断，增强与人类响应的一致性

## 摘要（原文）

> Summary assessment involves evaluating how well a generated summary reflects the key ideas and meaning of the source text, requiring a deep understanding of the content. Large Language Models (LLMs) have been used to automate this process, acting as judges to evaluate summaries with respect to the original text. While previous research investigated the alignment between LLMs and Human responses, it is not yet well understood what properties or features are exploited by them when asked to evaluate based on a particular quality dimension, and there has not been much attention towards mapping between evaluation scores and metrics. In this paper, we address this issue and discover features aligned with Human and Generative Pre-trained Transformers (GPTs) responses by studying statistical and machine learning metrics. Furthermore, we show that instructing GPTs to employ metrics used by Human can improve their judgment and conforming them better with human responses.

