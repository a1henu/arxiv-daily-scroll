---
layout: default
title: EoS-FM: Can an Ensemble of Specialist Models act as a Generalist Feature Extractor?
---

# EoS-FM: Can an Ensemble of Specialist Models act as a Generalist Feature Extractor?
**arXiv**：[2511.21523v1](https://arxiv.org/abs/2511.21523) · [PDF](https://arxiv.org/pdf/2511.21523.pdf)  
**作者**：Pierre Adorni, Minh-Tan Pham, Stéphane May, Sébastien Lefèvre  

**一句话要点**：提出专家模型集成框架以构建高效遥感基础模型

**关键词**：遥感基础模型, 专家模型集成, 轻量级训练, 联邦学习, 可持续AI, 模块化框架

## 3 点简述
- 当前基础模型依赖大规模计算与数据，资源消耗高且不可持续
- 采用轻量级ConvNeXtV2专家模型分解训练，支持模块化与联邦学习
- 框架在效率、可解释性和扩展性方面表现优异，适合资源受限场景

## 摘要（原文）

> Recent advances in foundation models have shown great promise in domains such as natural language processing and computer vision, and similar efforts are now emerging in the Earth Observation community. These models aim to generalize across tasks with limited supervision, reducing the need for training separate models for each task. However, current strategies, which largely focus on scaling model size and dataset volume, require prohibitive computational and data resources, limiting accessibility to only a few large institutions. Moreover, this paradigm of ever-larger models stands in stark contrast with the principles of sustainable and environmentally responsible AI, as it leads to immense carbon footprints and resource inefficiency. In this work, we present a novel and efficient alternative: an Ensemble-of-Specialists framework for building Remote Sensing Foundation Models (RSFMs). Our method decomposes the training process into lightweight, task-specific ConvNeXtV2 specialists that can be frozen and reused. This modular approach offers strong advantages in efficiency, interpretability, and extensibility. Moreover, it naturally supports federated training, pruning, and continuous specialist integration, making it particularly well-suited for collaborative and resource-constrained settings. Our framework sets a new direction for building scalable and efficient RSFMs.

