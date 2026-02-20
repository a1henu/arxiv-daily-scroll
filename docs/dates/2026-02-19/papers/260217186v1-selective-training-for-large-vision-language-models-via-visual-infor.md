---
layout: default
title: Selective Training for Large Vision Language Models via Visual Information Gain
---

# Selective Training for Large Vision Language Models via Visual Information Gain
**arXiv**：[2602.17186v1](https://arxiv.org/abs/2602.17186) · [PDF](https://arxiv.org/pdf/2602.17186.pdf)  
**作者**：Seulbi Lee, Sangheum Hwang  

**一句话要点**：提出视觉信息增益以解决大型视觉语言模型的语言偏见问题，通过选择性训练提升视觉基础能力。

**关键词**：视觉信息增益, 大型视觉语言模型, 语言偏见, 选择性训练, 视觉基础, 困惑度度量

## 3 点简述
- 核心问题：大型视觉语言模型存在语言偏见，常忽略视觉证据生成答案，缺乏量化视觉贡献的指标。
- 方法要点：引入视觉信息增益，基于困惑度度量视觉输入减少预测不确定性的程度，指导样本和令牌级别的选择性训练。
- 实验或效果：该方法优先训练高视觉信息增益的样本和令牌，改善视觉基础，减少语言偏见，在减少监督下实现更优性能。

## 摘要（原文）

> Large Vision Language Models (LVLMs) have achieved remarkable progress, yet they often suffer from language bias, producing answers without relying on visual evidence. While prior work attempts to mitigate this issue through decoding strategies, architectural modifications, or curated instruction data, they typically lack a quantitative measure of how much individual training samples or tokens actually benefit from the image. In this work, we introduce Visual Information Gain (VIG), a perplexity-based metric that measures the reduction in prediction uncertainty provided by visual input. VIG enables fine-grained analysis at both sample and token levels, effectively highlighting visually grounded elements such as colors, spatial relations, and attributes. Leveraging this, we propose a VIG-guided selective training scheme that prioritizes high-VIG samples and tokens. This approach improves visual grounding and mitigates language bias, achieving superior performance with significantly reduced supervision by focusing exclusively on visually informative samples and tokens.

