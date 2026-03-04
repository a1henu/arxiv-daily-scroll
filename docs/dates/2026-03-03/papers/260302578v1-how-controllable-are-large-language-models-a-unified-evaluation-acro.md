---
layout: default
title: How Controllable Are Large Language Models? A Unified Evaluation across Behavioral Granularities
---

# How Controllable Are Large Language Models? A Unified Evaluation across Behavioral Granularities
**arXiv**：[2603.02578v1](https://arxiv.org/abs/2603.02578) · [PDF](https://arxiv.org/pdf/2603.02578.pdf)  
**作者**：Ziwen Xu, Kewei Xu, Haoming Xu, Haiwen Hong, Longtao Huang, Hui Xue, Ningyu Zhang, Yongliang Shen, Guozhou Zheng, Huajun Chen, Shumin Deng  

**一句话要点**：提出SteerEval分层基准以评估大语言模型在语言特征、情感和人格领域的可控性

**关键词**：大语言模型可控性, 分层评估基准, 行为规范, 文本生成控制, 安全部署

## 3 点简述
- 核心问题：大语言模型在敏感领域部署时，不可预测行为如意图错位和人格不一致带来风险
- 方法要点：构建三层规范（表达内容、表达方式、实例化）连接行为意图与文本输出
- 实验或效果：系统评估现有控制方法，发现控制精度随粒度细化而下降

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in socially sensitive domains, yet their unpredictable behaviors, ranging from misaligned intent to inconsistent personality, pose significant risks. We introduce SteerEval, a hierarchical benchmark for evaluating LLM controllability across three domains: language features, sentiment, and personality. Each domain is structured into three specification levels: L1 (what to express), L2 (how to express), and L3 (how to instantiate), connecting high-level behavioral intent to concrete textual output. Using SteerEval, we systematically evaluate contemporary steering methods, revealing that control often degrades at finer-grained levels. Our benchmark offers a principled and interpretable framework for safe and controllable LLM behavior, serving as a foundation for future research.

