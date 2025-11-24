---
layout: default
title: Do Vision-Language Models Understand Visual Persuasiveness?
---

# Do Vision-Language Models Understand Visual Persuasiveness?
**arXiv**：[2511.17036v1](https://arxiv.org/abs/2511.17036) · [PDF](https://arxiv.org/pdf/2511.17036.pdf)  
**作者**：Gyuwon Park  

**一句话要点**：提出视觉说服因素分类与干预策略，评估视觉语言模型对视觉说服力的理解。

**关键词**：视觉语言模型, 视觉说服力, 多模态推理, 数据集构建, 干预策略, 语义对齐

## 3 点简述
- 核心问题：视觉语言模型是否理解视觉说服力，即视觉线索如何影响人类态度和决策。
- 方法要点：构建高共识数据集，引入视觉说服因素分类，探索认知引导和知识注入策略。
- 实验或效果：模型存在召回偏向，高级语义对齐预测力强，对象基础理性显著提升性能。

## 摘要（原文）

> Recent advances in vision-language models (VLMs) have enabled impressive multi-modal reasoning and understanding. Yet, whether these models truly grasp visual persuasion-how visual cues shape human attitudes and decisions-remains unclear. To probe this question, we construct a high-consensus dataset for binary persuasiveness judgment and introduce the taxonomy of Visual Persuasive Factors (VPFs), encompassing low-level perceptual, mid-level compositional, and high-level semantic cues. We also explore cognitive steering and knowledge injection strategies for persuasion-relevant reasoning. Empirical analysis across VLMs reveals a recall-oriented bias-models over-predict high persuasiveness-and weak discriminative power for low/mid-level features. In contrast, high-level semantic alignment between message and object presence emerges as the strongest predictor of human judgment. Among intervention strategies, simple instruction or unguided reasoning scaffolds yield marginal or negative effects, whereas concise, object-grounded rationales significantly improve precision and F1 scores. These results indicate that VLMs core limitation lies not in recognizing persuasive objects but in linking them to communicative intent.

