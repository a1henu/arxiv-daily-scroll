---
layout: default
title: PIMCST: Physics-Informed Multi-Phase Consensus and Spatio-Temporal Few-Shot Learning for Traffic Flow Forecasting
---

# PIMCST: Physics-Informed Multi-Phase Consensus and Spatio-Temporal Few-Shot Learning for Traffic Flow Forecasting
**arXiv**：[2602.01936v1](https://arxiv.org/abs/2602.01936) · [PDF](https://arxiv.org/pdf/2602.01936.pdf)  
**作者**：Abdul Joseph Fofanah, Lian Wen, David Chen  

**一句话要点**：提出多阶段共识时空框架以解决跨域少样本交通流预测问题

**关键词**：交通流预测, 少样本学习, 时空图学习, 跨域迁移, 元学习, 共识机制

## 3 点简述
- 核心问题：跨域数据稀缺场景下交通流预测的时空依赖建模与泛化挑战
- 方法要点：通过多阶段引擎建模动态、自适应共识机制融合预测、结构化元学习快速适应
- 实验或效果：在四个真实数据集上超越十四种先进方法，提升准确性并减少训练数据需求

## 摘要（原文）

> Accurate traffic flow prediction remains a fundamental challenge in intelligent transportation systems, particularly in cross-domain, data-scarce scenarios where limited historical data hinders model training and generalisation. The complex spatio-temporal dependencies and nonlinear dynamics of urban mobility networks further complicate few-shot learning across different cities. This paper proposes MCPST, a novel Multi-phase Consensus Spatio-Temporal framework for few-shot traffic forecasting that reconceptualises traffic prediction as a multi-phase consensus learning problem. Our framework introduces three core innovations: (1) a multi-phase engine that models traffic dynamics through diffusion, synchronisation, and spectral embeddings for comprehensive dynamic characterisation; (2) an adaptive consensus mechanism that dynamically fuses phase-specific predictions while enforcing consistency; and (3) a structured meta-learning strategy for rapid adaptation to new cities with minimal data. We establish extensive theoretical guarantees, including representation theorems with bounded approximation errors and generalisation bounds for few-shot adaptation. Through experiments on four real-world datasets, MCPST outperforms fourteen state-of-the-art methods in spatio-temporal graph learning methods, dynamic graph transfer learning methods, prompt-based spatio-temporal prediction methods and cross-domain few-shot settings, improving prediction accuracy while reducing required training data and providing interpretable insights. The implementation code is available at https://github.com/afofanah/MCPST.

