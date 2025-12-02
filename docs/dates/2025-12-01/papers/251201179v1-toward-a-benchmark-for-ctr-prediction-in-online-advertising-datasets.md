---
layout: default
title: Toward a benchmark for CTR prediction in online advertising: datasets, evaluation protocols and perspectives
---

# Toward a benchmark for CTR prediction in online advertising: datasets, evaluation protocols and perspectives
**arXiv**：[2512.01179v1](https://arxiv.org/abs/2512.01179) · [PDF](https://arxiv.org/pdf/2512.01179.pdf)  
**作者**：Shan Gao, Yanwu Yang  

**一句话要点**：提出Bench-CTR基准平台以统一在线广告点击率预测的评估体系

**关键词**：点击率预测, 基准平台, 评估协议, 数据集构建, 模型比较, 数据效率

## 3 点简述
- 核心问题：在线广告点击率预测缺乏标准化评估基准，阻碍模型比较与进展。
- 方法要点：设计统一基准平台，集成多样化数据集、模型组件和评估协议。
- 实验或效果：评估多种模型，发现高阶模型优势、LLM模型数据效率高，性能进展趋缓。

## 摘要（原文）

> This research designs a unified architecture of CTR prediction benchmark (Bench-CTR) platform that offers flexible interfaces with datasets and components of a wide range of CTR prediction models. Moreover, we construct a comprehensive system of evaluation protocols encompassing real-world and synthetic datasets, a taxonomy of metrics, standardized procedures and experimental guidelines for calibrating the performance of CTR prediction models. Furthermore, we implement the proposed benchmark platform and conduct a comparative study to evaluate a wide range of state-of-the-art models from traditional multivariate statistical to modern large language model (LLM)-based approaches on three public datasets and two synthetic datasets. Experimental results reveal that, (1) high-order models largely outperform low-order models, though such advantage varies in terms of metrics and on different datasets; (2) LLM-based models demonstrate a remarkable data efficiency, i.e., achieving the comparable performance to other models while using only 2% of the training data; (3) the performance of CTR prediction models has achieved significant improvements from 2015 to 2016, then reached a stage with slow progress, which is consistent across various datasets. This benchmark is expected to facilitate model development and evaluation and enhance practitioners' understanding of the underlying mechanisms of models in the area of CTR prediction. Code is available at https://github.com/NuriaNinja/Bench-CTR.

