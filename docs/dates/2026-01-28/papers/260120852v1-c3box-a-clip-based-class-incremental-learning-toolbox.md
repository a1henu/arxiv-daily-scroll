---
layout: default
title: C3Box: A CLIP-based Class-Incremental Learning Toolbox
---

# C3Box: A CLIP-based Class-Incremental Learning Toolbox
**arXiv**：[2601.20852v1](https://arxiv.org/abs/2601.20852) · [PDF](https://arxiv.org/pdf/2601.20852.pdf)  
**作者**：Hao Sun, Da-Wei Zhou  

**一句话要点**：提出C3Box工具箱以统一CLIP为基础的类增量学习评估平台

**关键词**：类增量学习, CLIP模型, 工具箱, 可复现性, 预训练模型

## 3 点简述
- 传统机器学习系统在动态数据流中面临灾难性遗忘问题
- C3Box整合多种CIL方法于统一CLIP框架，支持标准化配置
- 工具箱设计模块化，降低工程开销，促进可复现研究

## 摘要（原文）

> Traditional machine learning systems are typically designed for static data distributions, which suffer from catastrophic forgetting when learning from evolving data streams. Class-Incremental Learning (CIL) addresses this challenge by enabling learning systems to continuously learn new classes while preserving prior knowledge. With the rise of pre-trained models (PTMs) such as CLIP, leveraging their strong generalization and semantic alignment capabilities has become a promising direction in CIL. However, existing CLIP-based CIL methods are often scattered across disparate codebases, rely on inconsistent configurations, hindering fair comparisons, reproducibility, and practical adoption. Therefore, we propose C3Box (CLIP-based Class-inCremental learning toolBOX), a modular and comprehensive Python toolbox. C3Box integrates representative traditional CIL methods, ViT-based CIL methods, and state-of-the-art CLIP-based CIL methods into a unified CLIP-based framework. By inheriting the streamlined design of PyCIL, C3Box provides a JSON-based configuration and standardized execution pipeline. This design enables reproducible experimentation with low engineering overhead and makes C3Box a reliable benchmark platform for continual learning research. Designed to be user-friendly, C3Box relies only on widely used open-source libraries and supports major operating systems. The code is available at https://github.com/LAMDA-CL/C3Box.

