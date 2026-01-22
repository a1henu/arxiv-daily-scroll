---
layout: default
title: AQAScore: Evaluating Semantic Alignment in Text-to-Audio Generation via Audio Question Answering
---

# AQAScore: Evaluating Semantic Alignment in Text-to-Audio Generation via Audio Question Answering
**arXiv**：[2601.14728v1](https://arxiv.org/abs/2601.14728) · [PDF](https://arxiv.org/pdf/2601.14728.pdf)  
**作者**：Chun-Yi Kuan, Kai-Wei Chang, Hung-yi Lee  

**一句话要点**：提出AQAScore框架，通过音频问答评估文生音频的语义对齐，解决现有指标在细粒度语义和组合推理上的不足。

**关键词**：文生音频评估, 语义对齐, 音频问答, 概率验证, 音频感知大语言模型, 组合推理

## 3 点简述
- 核心问题：文生音频评估指标如CLAPScore在细粒度语义对齐和组合推理方面有限。
- 方法要点：利用音频感知大语言模型，将评估转化为概率性语义验证任务，计算目标查询的“是”答案对数概率。
- 实验或效果：在多个基准测试中，AQAScore比基于相似性的指标和生成提示基线更符合人类判断，能捕捉细微语义不一致。

## 摘要（原文）

> Although text-to-audio generation has made remarkable progress in realism and diversity, the development of evaluation metrics has not kept pace. Widely-adopted approaches, typically based on embedding similarity like CLAPScore, effectively measure general relevance but remain limited in fine-grained semantic alignment and compositional reasoning. To address this, we introduce AQAScore, a backbone-agnostic evaluation framework that leverages the reasoning capabilities of audio-aware large language models (ALLMs). AQAScore reformulates assessment as a probabilistic semantic verification task; rather than relying on open-ended text generation, it estimates alignment by computing the exact log-probability of a "Yes" answer to targeted semantic queries. We evaluate AQAScore across multiple benchmarks, including human-rated relevance, pairwise comparison, and compositional reasoning tasks. Experimental results show that AQAScore consistently achieves higher correlation with human judgments than similarity-based metrics and generative prompting baselines, showing its effectiveness in capturing subtle semantic inconsistencies and scaling with the capability of underlying ALLMs.

