---
layout: default
title: Step-Tagging: Toward controlling the generation of Language Reasoning Models through step monitoring
---

# Step-Tagging: Toward controlling the generation of Language Reasoning Models through step monitoring
**arXiv**：[2512.14332v1](https://arxiv.org/abs/2512.14332) · [PDF](https://arxiv.org/pdf/2512.14332.pdf)  
**作者**：Yannis Belkhiter, Seshu Tirupathi, Giulio Zizzo, John D. Kelleher  

**一句话要点**：提出Step-Tagging框架以通过步骤监控控制语言推理模型的生成效率

**关键词**：语言推理模型, 步骤监控, 推理效率, 早期停止, Step-Tagging, ReasonType分类法

## 3 点简述
- 语言推理模型存在推理步骤冗余和效率低下的问题
- 引入Step-Tagging框架和ReasonType分类法实时标注推理步骤类型
- 实验显示在多个基准上实现20-50%的token减少且保持准确率

## 摘要（原文）

> The field of Language Reasoning Models (LRMs) has been very active over the past few years with advances in training and inference techniques enabling LRMs to reason longer, and more accurately. However, a growing body of studies show that LRMs are still inefficient, over-generating verification and reflection steps. To address this challenge, we introduce the Step-Tagging framework, a lightweight sentence-classifier enabling real-time annotation of the type of reasoning steps that an LRM is generating. To monitor reasoning behaviors, we introduced ReasonType: a novel taxonomy of reasoning steps. Building on this framework, we demonstrated that online monitoring of the count of specific steps can produce effective interpretable early stopping criteria of LRM inferences. We evaluate the Step-tagging framework on three open-source reasoning models across standard benchmark datasets: MATH500, GSM8K, AIME and non-mathematical tasks (GPQA and MMLU-Pro). We achieve 20 to 50\% token reduction while maintaining comparable accuracy to standard generation, with largest gains observed on more computation-heavy tasks. This work offers a novel way to increase control over the generation of LRMs, and a new tool to study behaviors of LRMs.

