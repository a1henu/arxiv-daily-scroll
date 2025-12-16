---
layout: default
title: ModSSC: A Modular Framework for Semi-Supervised Classification on Heterogeneous Data
---

# ModSSC: A Modular Framework for Semi-Supervised Classification on Heterogeneous Data
**arXiv**：[2512.13228v1](https://arxiv.org/abs/2512.13228) · [PDF](https://arxiv.org/pdf/2512.13228.pdf)  
**作者**：Melvin Barbaux  

**一句话要点**：提出ModSSC框架以统一异构数据上的半监督分类算法实现与实验配置

**关键词**：半监督分类, 异构数据处理, 模块化框架, 开源软件, 实验复现

## 3 点简述
- 核心问题：现有半监督分类软件支持分散，缺乏统一框架处理异构数据和方法。
- 方法要点：提供模块化开源Python框架，集成归纳与直推式算法，支持多种数据类型和硬件。
- 实验或效果：通过YAML声明式实验配置，便于复现和比较研究，已发布1.0.0版本。

## 摘要（原文）

> Semi-supervised classification leverages both labeled and unlabeled data to improve predictive performance, but existing software support is fragmented across methods and modalities. We introduce ModSSC, an open source Python framework that unifies inductive and transductive semi-supervised classification in a modular code base. ModSSC implements a broad range of classical and recent algorithms, provides loaders for tabular, image, text, audio and graph datasets, and exposes a single configuration interface for specifying datasets, models and evaluation protocols. It supports both lightweight classical methods on small datasets running on CPU and recent deep approaches that can exploit multiple GPUs within the same experimental framework. Experiments are described declaratively in YAML, which facilitates reproducing existing work and running large comparative studies. ModSSC 1.0.0 is released under the MIT license with extensive documentation and tests, and is available at https://github.com/ModSSC/ModSSC.

