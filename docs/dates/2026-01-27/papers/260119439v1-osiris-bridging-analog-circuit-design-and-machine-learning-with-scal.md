---
layout: default
title: OSIRIS: Bridging Analog Circuit Design and Machine Learning with Scalable Dataset Generation
---

# OSIRIS: Bridging Analog Circuit Design and Machine Learning with Scalable Dataset Generation
**arXiv**：[2601.19439v1](https://arxiv.org/abs/2601.19439) · [PDF](https://arxiv.org/pdf/2601.19439.pdf)  
**作者**：Giuseppe Chiari, Michele Piccoli, Davide Zoni  

**一句话要点**：提出OSIRIS可扩展数据集生成管道，以解决模拟集成电路设计中机器学习应用的数据集短缺问题。

**关键词**：模拟集成电路设计, 数据集生成, 机器学习应用, 电子设计自动化, 强化学习优化

## 3 点简述
- 核心问题：模拟IC设计自动化受限于物理布局、寄生效应和性能间的复杂交互，且缺乏开放高质量数据集。
- 方法要点：OSIRIS系统探索模拟电路设计空间，生成包含性能指标和元数据的综合数据集。
- 实验或效果：发布基于OSIRIS生成的87,100个电路变体数据集，并提供强化学习基线方法用于设计优化。

## 摘要（原文）

> The automation of analog integrated circuit (IC) design remains a longstanding challenge, primarily due to the intricate interdependencies among physical layout, parasitic effects, and circuit-level performance. These interactions impose complex constraints that are difficult to accurately capture and optimize using conventional design methodologies. Although recent advances in machine learning (ML) have shown promise in automating specific stages of the analog design flow, the development of holistic, end-to-end frameworks that integrate these stages and iteratively refine layouts using post-layout, parasitic-aware performance feedback is still in its early stages. Furthermore, progress in this direction is hindered by the limited availability of open, high-quality datasets tailored to the analog domain, restricting both the benchmarking and the generalizability of ML-based techniques. To address these limitations, we present OSIRIS, a scalable dataset generation pipeline for analog IC design. OSIRIS systematically explores the design space of analog circuits while producing comprehensive performance metrics and metadata, thereby enabling ML-driven research in electronic design automation (EDA). In addition, we release a dataset consisting of 87,100 circuit variations generated with OSIRIS, accompanied by a reinforcement learning (RL)-based baseline method that exploits OSIRIS for analog design optimization.

