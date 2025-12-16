---
layout: default
title: Uncovering the Role of Initial Saliency in U-Shaped Attention Bias: Scaling Initial Token Weight for Enhanced Long-Text Processing
---

# Uncovering the Role of Initial Saliency in U-Shaped Attention Bias: Scaling Initial Token Weight for Enhanced Long-Text Processing
**arXiv**：[2512.13109v1](https://arxiv.org/abs/2512.13109) · [PDF](https://arxiv.org/pdf/2512.13109.pdf)  
**作者**：Zewen Qiang, Sendong Zhao, Haochun Wang, Bing Qin, Ting Liu  

**一句话要点**：提出缩放初始令牌权重以缓解U形注意力偏差，增强大语言模型的长文本处理能力

**关键词**：长文本处理, 注意力机制, U形偏差, 初始显著性, 大语言模型优化

## 3 点简述
- 核心问题：大语言模型在长文本处理中存在'中间丢失'现象，源于U形注意力偏差，即注意力过度集中于文本首尾。
- 方法要点：研究发现初始显著性因素，通过缩放初始令牌与其他令牌的注意力权重来改善偏差。
- 实验或效果：在MDQA数据集上最高提升3.6%，结合现有方法在KV-Retrieval任务中最高提升3.4%。

## 摘要（原文）

> Large language models (LLMs) have demonstrated strong performance on a variety of natural language processing (NLP) tasks. However, they often struggle with long-text sequences due to the ``lost in the middle'' phenomenon. This issue has been shown to arise from a U-shaped attention bias, where attention is disproportionately focused on the beginning and end of a text, leaving the middle section underrepresented. While previous studies have attributed this bias to position encoding, our research first identifies an additional factor: initial saliency. It means that in the attention computation for each token, tokens with higher attention weights relative to the initial token tend to receive more attention in the prediction of the next token. We further find that utilizing this property by scaling attention weight between the initial token and others improves the model's ability to process long contexts, achieving a maximum improvement of 3.6\% in MDQA dataset. Moreover, combining this approach with existing methods to reduce position encoding bias further enhances performance, achieving a maximum improvement of 3.4\% in KV-Retrieval tasks.

