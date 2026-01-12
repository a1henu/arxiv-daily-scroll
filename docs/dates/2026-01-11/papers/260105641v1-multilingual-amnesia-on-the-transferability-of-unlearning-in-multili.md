---
layout: default
title: Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs
---

# Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs
**arXiv**：[2601.05641v1](https://arxiv.org/abs/2601.05641) · [PDF](https://arxiv.org/pdf/2601.05641.pdf)  
**作者**：Alireza Dehghanpour Farashah, Aditi Khandelwal, Marylou Fauchard, Zhuan Shi, Negar Rostamzadeh, Golnoosh Farnadi  

**一句话要点**：研究多语言大语言模型中的遗忘机制，分析跨语言知识转移与遗忘稳定性

**关键词**：多语言大语言模型, 机器遗忘, 跨语言知识转移, 句法相似性, 多语言基准

## 3 点简述
- 核心问题：多语言环境下机器遗忘的挑战，涉及跨语言知识转移和偏见。
- 方法要点：使用Aya-Expanse 8B模型，在数据和概念遗忘两种设置下进行实验。
- 实验或效果：扩展基准至十种语言，发现高资源语言遗忘更稳定，句法相似性预测跨语言遗忘行为。

## 摘要（原文）

> As multilingual large language models become more widely used, ensuring their safety and fairness across diverse linguistic contexts presents unique challenges. While existing research on machine unlearning has primarily focused on monolingual settings, typically English, multilingual environments introduce additional complexities due to cross-lingual knowledge transfer and biases embedded in both pretraining and fine-tuning data. In this work, we study multilingual unlearning using the Aya-Expanse 8B model under two settings: (1) data unlearning and (2) concept unlearning. We extend benchmarks for factual knowledge and stereotypes to ten languages through translation: English, French, Arabic, Japanese, Russian, Farsi, Korean, Hindi, Hebrew, and Indonesian. These languages span five language families and a wide range of resource levels. Our experiments show that unlearning in high-resource languages is generally more stable, with asymmetric transfer effects observed between typologically related languages. Furthermore, our analysis of linguistic distances indicates that syntactic similarity is the strongest predictor of cross-lingual unlearning behavior.

