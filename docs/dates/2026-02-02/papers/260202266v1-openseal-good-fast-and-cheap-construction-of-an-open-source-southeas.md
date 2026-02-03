---
layout: default
title: OpenSeal: Good, Fast, and Cheap Construction of an Open-Source Southeast Asian LLM via Parallel Data
---

# OpenSeal: Good, Fast, and Cheap Construction of an Open-Source Southeast Asian LLM via Parallel Data
**arXiv**：[2602.02266v1](https://arxiv.org/abs/2602.02266) · [PDF](https://arxiv.org/pdf/2602.02266.pdf)  
**作者**：Tan Sang Nguyen, Muhammad Reza Qorib, Hwee Tou Ng  

**一句话要点**：提出OpenSeal，通过平行数据高效构建开源东南亚大语言模型

**关键词**：平行数据, 持续预训练, 东南亚语言模型, 开源模型, 多语言性能

## 3 点简述
- 问题：现有东南亚大语言模型非真正开源，缺乏训练数据透明度，影响模型理解与评估。
- 方法：利用平行数据进行持续预训练，仅用34.7B tokens数据在8x NVIDIA H200 GPUs上训练180小时。
- 效果：OpenSeal性能媲美同规模模型，成为首个真正开源的东南亚大语言模型。

## 摘要（原文）

> Large language models (LLMs) have proven to be effective tools for a wide range of natural language processing (NLP) applications. Although many LLMs are multilingual, most remain English-centric and perform poorly on low-resource languages. Recently, several Southeast Asia-focused LLMs have been developed, but none are truly open source, as they do not publicly disclose their training data. Truly open-source models are important for transparency and for enabling a deeper and more precise understanding of LLM internals and development, including biases, generalization, and multilinguality. Motivated by recent advances demonstrating the effectiveness of parallel data in improving multilingual performance, we conduct controlled and comprehensive experiments to study the effectiveness of parallel data in continual pretraining of LLMs. Our findings show that using only parallel data is the most effective way to extend an LLM to new languages. Using just 34.7B tokens of parallel data and 180 hours on 8x NVIDIA H200 GPUs, we built OpenSeal, the first truly open Southeast Asian LLM that rivals the performance of existing models of similar size.

