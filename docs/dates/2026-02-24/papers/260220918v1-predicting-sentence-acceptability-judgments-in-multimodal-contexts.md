---
layout: default
title: Predicting Sentence Acceptability Judgments in Multimodal Contexts
---

# Predicting Sentence Acceptability Judgments in Multimodal Contexts
**arXiv**：[2602.20918v1](https://arxiv.org/abs/2602.20918) · [PDF](https://arxiv.org/pdf/2602.20918.pdf)  
**作者**：Hyewon Jang, Nikolai Ilinykh, Sharid Loáiciga, Jey Han Lau, Shalom Lappin  

**一句话要点**：研究视觉上下文对句子可接受性判断的影响，比较人类与大型语言模型的表现差异

**关键词**：句子可接受性判断, 多模态上下文, 大型语言模型, 视觉上下文, 人类认知比较

## 3 点简述
- 核心问题：视觉图像是否影响人类和大型语言模型对句子可接受性的判断
- 方法要点：通过实验比较人类和多种大型语言模型在有无视觉上下文时的判断表现
- 实验或效果：视觉上下文对人类判断影响小，但对大型语言模型预测准确性和内部表示有影响

## 摘要（原文）

> Previous work has examined the capacity of deep neural networks (DNNs), particularly transformers, to predict human sentence acceptability judgments, both independently of context, and in document contexts. We consider the effect of prior exposure to visual images (i.e., visual context) on these judgments for humans and large language models (LLMs). Our results suggest that, in contrast to textual context, visual images appear to have little if any impact on human acceptability ratings. However, LLMs display the compression effect seen in previous work on human judgments in document contexts. Different sorts of LLMs are able to predict human acceptability judgments to a high degree of accuracy, but in general, their performance is slightly better when visual contexts are removed. Moreover, the distribution of LLM judgments varies among models, with Qwen resembling human patterns, and others diverging from them. LLM-generated predictions on sentence acceptability are highly correlated with their normalised log probabilities in general. However, the correlations decrease when visual contexts are present, suggesting that a higher gap exists between the internal representations of LLMs and their generated predictions in the presence of visual contexts. Our experimental work suggests interesting points of similarity and of difference between human and LLM processing of sentences in multimodal contexts.

