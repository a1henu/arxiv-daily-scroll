---
layout: default
title: LSRE: Latent Semantic Rule Encoding for Real-Time Semantic Risk Detection in Autonomous Driving
---

# LSRE: Latent Semantic Rule Encoding for Real-Time Semantic Risk Detection in Autonomous Driving
**arXiv**：[2512.24712v1](https://arxiv.org/abs/2512.24712) · [PDF](https://arxiv.org/pdf/2512.24712.pdf)  
**作者**：Qian Cheng, Weitao Zhou, Cheng Jing, Nanshan Deng, Junze Wen, Zhaoyang Liu, Kun Jiang, Diange Yang  

**一句话要点**：提出LSRE框架，通过潜在语义规则编码实现自动驾驶实时语义风险检测

**关键词**：自动驾驶, 语义风险检测, 潜在空间编码, 实时系统, 视觉语言模型, 轻量级分类器

## 3 点简述
- 核心问题：自动驾驶需遵循复杂社会规则，但大视觉语言模型推理成本高，难以实时部署。
- 方法要点：将稀疏采样的VLM判断转换为循环世界模型潜在空间中的决策边界，编码语义为轻量级分类器。
- 实验或效果：在CARLA中六种语义失败场景下，检测精度接近大VLM基线，提供更早危险预警，计算延迟低。

## 摘要（原文）

> Real-world autonomous driving must adhere to complex human social rules that extend beyond legally codified traffic regulations. Many of these semantic constraints, such as yielding to emergency vehicles, complying with traffic officers' gestures, or stopping for school buses, are intuitive for humans yet difficult to encode explicitly. Although large vision-language models (VLMs) can interpret such semantics, their inference cost makes them impractical for real-time deployment.This work proposes LSRE, a Latent Semantic Rule Encoding framework that converts sparsely sampled VLM judgments into decision boundaries within the latent space of a recurrent world model. By encoding language-defined safety semantics into a lightweight latent classifier, LSRE enables real-time semantic risk assessment at 10 Hz without per-frame VLM queries. Experiments on six semantic-failure scenarios in CARLA demonstrate that LSRE attains semantic risk detection accuracy comparable to a large VLM baseline, while providing substantially earlier hazard anticipation and maintaining low computational latency. LSRE further generalizes to rarely seen semantic-similar test cases, indicating that language-guided latent classification offers an effective and deployable mechanism for semantic safety monitoring in autonomous driving.

