---
layout: default
title: SeNeDiF-OOD: Semantic Nested Dichotomy Fusion for Out-of-Distribution Detection Methodology in Open-World Classification. A Case Study on Monument Style Classification
---

# SeNeDiF-OOD: Semantic Nested Dichotomy Fusion for Out-of-Distribution Detection Methodology in Open-World Classification. A Case Study on Monument Style Classification
**arXiv**：[2601.18739v1](https://arxiv.org/abs/2601.18739) · [PDF](https://arxiv.org/pdf/2601.18739.pdf)  
**作者**：Ignacio Antequera-Sánchez, Juan Luis Suárez-Díaz, Rosana Montes, Francisco Herrera  

**一句话要点**：提出SeNeDiF-OOD方法，基于语义嵌套二分融合解决开放世界分类中的分布外检测问题，以纪念碑风格分类为例。

**关键词**：分布外检测, 开放世界分类, 语义嵌套二分融合, 纪念碑风格分类, 层次化融合, 异质性数据

## 3 点简述
- 核心问题：开放世界环境中，分布外数据具有异质性，从低级损坏到语义偏移，单阶段检测器难以有效处理。
- 方法要点：采用语义嵌套二分融合框架，将检测任务分解为层次化二元融合节点，每层集成与特定语义抽象级别对齐的决策边界。
- 实验或效果：在MonuMAI系统上进行案例研究，实验表明该方法显著优于传统基线，能有效过滤多样分布外类别，同时保持分布内性能。

## 摘要（原文）

> Out-of-distribution (OOD) detection is a fundamental requirement for the reliable deployment of artificial intelligence applications in open-world environments. However, addressing the heterogeneous nature of OOD data, ranging from low-level corruption to semantic shifts, remains a complex challenge that single-stage detectors often fail to resolve. To address this issue, we propose SeNeDiF-OOD, a novel methodology based on Semantic Nested Dichotomy Fusion. This framework decomposes the detection task into a hierarchical structure of binary fusion nodes, where each layer is designed to integrate decision boundaries aligned with specific levels of semantic abstraction. To validate the proposed framework, we present a comprehensive case study using MonuMAI, a real-world architectural style recognition system exposed to an open environment. This application faces a diverse range of inputs, including non-monument images, unknown architectural styles, and adversarial attacks, making it an ideal testbed for our proposal. Through extensive experimental evaluation in this domain, results demonstrate that our hierarchical fusion methodology significantly outperforms traditional baselines, effectively filtering these diverse OOD categories while preserving in-distribution performance.

