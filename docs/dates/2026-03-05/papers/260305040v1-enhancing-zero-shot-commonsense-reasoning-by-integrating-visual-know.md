---
layout: default
title: Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination
---

# Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination
**arXiv**：[2603.05040v1](https://arxiv.org/abs/2603.05040) · [PDF](https://arxiv.org/pdf/2603.05040.pdf)  
**作者**：Hyuntae Park, Yeachan Kim, SangKeun Lee  

**一句话要点**：提出Imagine框架，通过机器想象整合视觉知识以增强零样本常识推理

**关键词**：零样本常识推理, 机器想象, 视觉知识整合, 报告偏差缓解, 多模态增强

## 3 点简述
- 核心问题：文本知识存在人类报告偏差，导致机器与人类理解差异
- 方法要点：嵌入图像生成器，补充文本输入为机器生成的视觉信号
- 实验或效果：在多个基准上超越现有零样本方法及大型语言模型

## 摘要（原文）

> Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

