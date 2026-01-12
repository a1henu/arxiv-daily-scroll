---
layout: default
title: PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility
---

# PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility
**arXiv**：[2601.05739v1](https://arxiv.org/abs/2601.05739) · [PDF](https://arxiv.org/pdf/2601.05739.pdf)  
**作者**：G M Shahariar, Zabir Al Nazi, Md Olid Hasan Bhuiyan, Zhouxing Shi  

**一句话要点**：提出PII-VisBench基准，评估视觉语言模型在连续在线可见性下的个人可识别信息安全

**关键词**：视觉语言模型, 个人可识别信息安全, 在线可见性, 基准评估, 隐私对齐, 模型安全

## 3 点简述
- 核心问题：现有评估忽视在线存在对隐私对齐的影响，隐私被视为静态提取任务
- 方法要点：基于在线信息量将200个主体分为四类可见性，设计4000个探针评估模型安全
- 实验或效果：模型拒绝率随可见性降低而增加，PII披露率从9.10%降至5.34%，存在模型家族异质性和攻击漏洞

## 摘要（原文）

> Vision Language Models (VLMs) are increasingly integrated into privacy-critical domains, yet existing evaluations of personally identifiable information (PII) leakage largely treat privacy as a static extraction task and ignore how a subject's online presence--the volume of their data available online--influences privacy alignment. We introduce PII-VisBench, a novel benchmark containing 4000 unique probes designed to evaluate VLM safety through the continuum of online presence. The benchmark stratifies 200 subjects into four visibility categories: high, medium, low, and zero--based on the extent and nature of their information available online. We evaluate 18 open-source VLMs (0.3B-32B) based on two key metrics: percentage of PII probing queries refused (Refusal Rate) and the fraction of non-refusal responses flagged for containing PII (Conditional PII Disclosure Rate). Across models, we observe a consistent pattern: refusals increase and PII disclosures decrease (9.10% high to 5.34% low) as subject visibility drops. We identify that models are more likely to disclose PII for high-visibility subjects, alongside substantial model-family heterogeneity and PII-type disparities. Finally, paraphrasing and jailbreak-style prompts expose attack and model-dependent failures, motivating visibility-aware safety evaluation and training interventions.

