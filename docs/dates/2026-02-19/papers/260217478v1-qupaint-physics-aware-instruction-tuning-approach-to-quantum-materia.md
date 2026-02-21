---
layout: default
title: QuPAINT: Physics-Aware Instruction Tuning Approach to Quantum Material Discovery
---

# QuPAINT: Physics-Aware Instruction Tuning Approach to Quantum Material Discovery
**arXiv**：[2602.17478v1](https://arxiv.org/abs/2602.17478) · [PDF](https://arxiv.org/pdf/2602.17478.pdf)  
**作者**：Xuan-Bac Nguyen, Hoang-Quan Nguyen, Sankalp Pandey, Tim Faltermeier, Nicholas Borys, Hugh Churchill, Khoa Luu  

**一句话要点**：提出QuPAINT框架，通过物理感知指令调优解决量子材料光学图像表征难题

**关键词**：量子材料表征, 物理感知学习, 指令调优, 合成数据生成, 多模态大语言模型, 光学图像分析

## 3 点简述
- 核心问题：量子材料光学图像表征因对比度弱、标注数据少和实验条件差异而困难
- 方法要点：结合物理合成数据生成、指令数据集和物理感知注意力模块
- 实验或效果：建立QF-Bench基准，评估多材料、基底和成像设置下的性能

## 摘要（原文）

> Characterizing two-dimensional quantum materials from optical microscopy images is challenging due to the subtle layer-dependent contrast, limited labeled data, and significant variation across laboratories and imaging setups. Existing vision models struggle in this domain since they lack physical priors and cannot generalize to new materials or hardware conditions. This work presents a new physics-aware multimodal framework that addresses these limitations from both the data and model perspectives. We first present Synthia, a physics-based synthetic data generator that simulates realistic optical responses of quantum material flakes under thin-film interference. Synthia produces diverse and high-quality samples, helping reduce the dependence on expert manual annotation. We introduce QMat-Instruct, the first large-scale instruction dataset for quantum materials, comprising multimodal, physics-informed question-answer pairs designed to teach Multimodal Large Language Models (MLLMs) to understand the appearance and thickness of flakes. Then, we propose Physics-Aware Instruction Tuning (QuPAINT), a multimodal architecture that incorporates a Physics-Informed Attention module to fuse visual embeddings with optical priors, enabling more robust and discriminative flake representations. Finally, we establish QF-Bench, a comprehensive benchmark spanning multiple materials, substrates, and imaging settings, offering standardized protocols for fair and reproducible evaluation.

