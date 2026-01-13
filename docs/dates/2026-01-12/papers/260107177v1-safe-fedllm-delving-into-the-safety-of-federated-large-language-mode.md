---
layout: default
title: Safe-FedLLM: Delving into the Safety of Federated Large Language Models
---

# Safe-FedLLM: Delving into the Safety of Federated Large Language Models
**arXiv**：[2601.07177v1](https://arxiv.org/abs/2601.07177) · [PDF](https://arxiv.org/pdf/2601.07177.pdf)  
**作者**：Mingxiang Tao, Yu Tian, Wenxuan Tu, Yue Yang, Xue Yang, Xiangyan Tang  

**一句话要点**：提出Safe-FedLLM以增强联邦大语言模型在开放环境中的安全性

**关键词**：联邦学习, 大语言模型, 模型安全, 低秩适应, 恶意客户端防御

## 3 点简述
- 核心问题：联邦学习中大语言模型易受恶意客户端攻击，安全性被忽视
- 方法要点：基于LoRA权重行为模式，通过轻量级分类器进行探针式防御
- 实验或效果：有效防御恶意攻击，不损害良性数据性能，训练速度影响小

## 摘要（原文）

> Federated learning (FL) addresses data privacy and silo issues in large language models (LLMs). Most prior work focuses on improving the training efficiency of federated LLMs. However, security in open environments is overlooked, particularly defenses against malicious clients. To investigate the safety of LLMs during FL, we conduct preliminary experiments to analyze potential attack surfaces and defensible characteristics from the perspective of Low-Rank Adaptation (LoRA) weights. We find two key properties of FL: 1) LLMs are vulnerable to attacks from malicious clients in FL, and 2) LoRA weights exhibit distinct behavioral patterns that can be filtered through simple classifiers. Based on these properties, we propose Safe-FedLLM, a probe-based defense framework for federated LLMs, constructing defenses across three dimensions: Step-Level, Client-Level, and Shadow-Level. The core concept of Safe-FedLLM is to perform probe-based discrimination on the LoRA weights locally trained by each client during FL, treating them as high-dimensional behavioral features and using lightweight classification models to determine whether they possess malicious attributes. Extensive experiments demonstrate that Safe-FedLLM effectively enhances the defense capability of federated LLMs without compromising performance on benign data. Notably, our method effectively suppresses malicious data impact without significant impact on training speed, and remains effective even with many malicious clients. Our code is available at: https://github.com/dmqx/Safe-FedLLM.

