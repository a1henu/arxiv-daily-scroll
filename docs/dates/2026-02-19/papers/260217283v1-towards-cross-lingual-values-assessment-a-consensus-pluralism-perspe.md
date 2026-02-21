---
layout: default
title: Towards Cross-lingual Values Assessment: A Consensus-Pluralism Perspective
---

# Towards Cross-lingual Values Assessment: A Consensus-Pluralism Perspective
**arXiv**：[2602.17283v1](https://arxiv.org/abs/2602.17283) · [PDF](https://arxiv.org/pdf/2602.17283.pdf)  
**作者**：Yukun Chen, Xinyu Zhang, Jialong Tang, Yu Wan, Baosong Yang, Yiming Li, Zhan Qin, Kui Ren  

**一句话要点**：提出跨语言价值观评估基准X-Value，以解决大语言模型在内容深层价值观评估上的不足。

**关键词**：跨语言价值观评估, 大语言模型评估, 内容安全, Schwartz价值观理论, 共识与多元主义, 多语言基准

## 3 点简述
- 当前大语言模型评估主要关注显性危害，忽略内容中的深层价值观维度。
- 基于Schwartz基本人类价值观理论，构建包含18种语言、5000多QA对的跨语言评估基准，采用共识与多元主义两阶段标注框架。
- 实验显示SOTA大语言模型在跨语言价值观评估上表现不佳，准确率低于77%，且语言间性能差异显著。

## 摘要（原文）

> While large language models (LLMs) have become pivotal to content safety, current evaluation paradigms primarily focus on detecting explicit harms (e.g., violence or hate speech), neglecting the subtler value dimensions conveyed in digital content. To bridge this gap, we introduce X-Value, a novel Cross-lingual Values Assessment Benchmark designed to evaluate LLMs' ability to assess deep-level values of content from a global perspective. X-Value consists of more than 5,000 QA pairs across 18 languages, systematically organized into 7 core domains grounded in Schwartz's Theory of Basic Human Values and categorized into easy and hard levels for discriminative evaluation. We further propose a unique two-stage annotation framework that first identifies whether an issue falls under global consensus (e.g., human rights) or pluralism (e.g., religion), and subsequently conducts a multi-party evaluation of the latent values embedded within the content. Systematic evaluations on X-Value reveal that current SOTA LLMs exhibit deficiencies in cross-lingual values assessment ($Acc < 77\%$), with significant performance disparities across different languages ($ΔAcc > 20\%$). This work highlights the urgent need to improve the nuanced, values-aware content assessment capability of LLMs. Our X-Value is available at: https://huggingface.co/datasets/Whitolf/X-Value.

