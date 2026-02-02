---
layout: default
title: Shattered Compositionality: Counterintuitive Learning Dynamics of Transformers for Arithmetic
---

# Shattered Compositionality: Counterintuitive Learning Dynamics of Transformers for Arithmetic
**arXiv**：[2601.22510v1](https://arxiv.org/abs/2601.22510) · [PDF](https://arxiv.org/pdf/2601.22510.pdf)  
**作者**：Xingyu Zhao, Darsh Sharma, Rheeya Uppaal, Yiqiao Zhong  

**一句话要点**：揭示Transformer在算术任务中非人类技能组合学习动态，导致分布偏移下混合错误

**关键词**：Transformer学习动态, 技能组合, 算术任务, 分布偏移, 大语言模型错误, 相关匹配

## 3 点简述
- 核心问题：大语言模型技能组合学习动态与人类规则不符，导致意外错误和分布偏移脆弱性
- 方法要点：通过合成算术任务训练Transformer，使用消融实验和细粒度诊断指标分析学习机制
- 实验或效果：发现模型以反向或并行方式获取技能，相关匹配而非因果组合主导学习，现象在现有LLMs中持续存在

## 摘要（原文）

> Large language models (LLMs) often exhibit unexpected errors or unintended behavior, even at scale. While recent work reveals the discrepancy between LLMs and humans in skill compositions, the learning dynamics of skill compositions and the underlying cause of non-human behavior remain elusive. In this study, we investigate the mechanism of learning dynamics by training transformers on synthetic arithmetic tasks. Through extensive ablations and fine-grained diagnostic metrics, we discover that transformers do not reliably build skill compositions according to human-like sequential rules. Instead, they often acquire skills in reverse order or in parallel, which leads to unexpected mixing errors especially under distribution shifts--a phenomenon we refer to as shattered compositionality. To explain these behaviors, we provide evidence that correlational matching to the training data, rather than causal or procedural composition, shapes learning dynamics. We further show that shattered compositionality persists in modern LLMs and is not mitigated by pure model scaling or scratchpad-based reasoning. Our results reveal a fundamental mismatch between a model's learning behavior and desired skill compositions, with implications for reasoning reliability, out-of-distribution robustness, and alignment.

