---
layout: default
title: TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
---

# TorchTraceAP: A New Benchmark Dataset for Detecting Performance Anti-Patterns in Computer Vision Models
**arXiv**：[2512.14141v1](https://arxiv.org/abs/2512.14141) · [PDF](https://arxiv.org/pdf/2512.14141.pdf)  
**作者**：Hanning Chen, Keyu Man, Kevin Zhu, Chenguang Zhu, Haonan Li, Tongbo Luo, Xizhou Feng, Wei Sun, Sreen Tallam, Mohsen Imani, Partha Kanuparthy  

**一句话要点**：提出TorchTraceAP基准数据集以检测计算机视觉模型中的性能反模式

**关键词**：性能反模式检测, PyTorch跟踪, 基准数据集, 计算机视觉模型, 迭代检测方法

## 3 点简述
- 核心问题：识别性能反模式需跨领域专家，自动化检测困难且耗时。
- 方法要点：构建首个PyTorch跟踪基准数据集，结合轻量ML模型和LLM进行迭代检测。
- 实验或效果：方法显著优于无监督聚类和基于规则的技术，有效补偿LLM限制。

## 摘要（原文）

> Identifying and addressing performance anti-patterns in machine learning (ML) models is critical for efficient training and inference, but it typically demands deep expertise spanning system infrastructure, ML models and kernel development. While large tech companies rely on dedicated ML infrastructure engineers to analyze torch traces and benchmarks, such resource-intensive workflows are largely inaccessible to computer vision researchers in general. Among the challenges, pinpointing problematic trace segments within lengthy execution traces remains the most time-consuming task, and is difficult to automate with current ML models, including LLMs. In this work, we present the first benchmark dataset specifically designed to evaluate and improve ML models' ability to detect anti patterns in traces. Our dataset contains over 600 PyTorch traces from diverse computer vision models classification, detection, segmentation, and generation collected across multiple hardware platforms. We also propose a novel iterative approach: a lightweight ML model first detects trace segments with anti patterns, followed by a large language model (LLM) for fine grained classification and targeted feedback. Experimental results demonstrate that our method significantly outperforms unsupervised clustering and rule based statistical techniques for detecting anti pattern regions. Our method also effectively compensates LLM's limited context length and reasoning inefficiencies.

