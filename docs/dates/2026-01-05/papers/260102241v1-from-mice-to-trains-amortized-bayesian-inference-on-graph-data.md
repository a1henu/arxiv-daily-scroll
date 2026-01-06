---
layout: default
title: From Mice to Trains: Amortized Bayesian Inference on Graph Data
---

# From Mice to Trains: Amortized Bayesian Inference on Graph Data
**arXiv**：[2601.02241v1](https://arxiv.org/abs/2601.02241) · [PDF](https://arxiv.org/pdf/2601.02241.pdf)  
**作者**：Svenja Jedhoff, Elizaveta Semenova, Aura Raulo, Anne Meyer, Paul-Christian Bürkner  

**一句话要点**：提出基于摊销贝叶斯推断的图数据推理方法，以解决图参数后验估计的挑战。

**关键词**：图数据推理, 摊销贝叶斯推断, 置换不变编码器, 神经后验估计, 生物网络, 物流优化

## 3 点简述
- 核心问题：图数据推理需满足置换不变性、可扩展性及捕获长程依赖，后验估计困难。
- 方法要点：结合置换不变图编码器与神经后验估计器，构建两模块流水线进行节点、边和图级参数推理。
- 实验或效果：在合成和真实世界（生物与物流）场景中评估多种架构的性能与校准。

## 摘要（原文）

> Graphs arise across diverse domains, from biology and chemistry to social and information networks, as well as in transportation and logistics. Inference on graph-structured data requires methods that are permutation-invariant, scalable across varying sizes and sparsities, and capable of capturing complex long-range dependencies, making posterior estimation on graph parameters particularly challenging. Amortized Bayesian Inference (ABI) is a simulation-based framework that employs generative neural networks to enable fast, likelihood-free posterior inference. We adapt ABI to graph data to address these challenges to perform inference on node-, edge-, and graph-level parameters. Our approach couples permutation-invariant graph encoders with flexible neural posterior estimators in a two-module pipeline: a summary network maps attributed graphs to fixed-length representations, and an inference network approximates the posterior over parameters. In this setting, several neural architectures can serve as the summary network. In this work we evaluate multiple architectures and assess their performance on controlled synthetic settings and two real-world domains - biology and logistics - in terms of recovery and calibration.

