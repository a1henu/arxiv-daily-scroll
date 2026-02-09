---
layout: default
title: T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility
---

# T-STAR: A Context-Aware Transformer Framework for Short-Term Probabilistic Demand Forecasting in Dock-Based Shared Micro-Mobility
**arXiv**：[2602.06866v1](https://arxiv.org/abs/2602.06866) · [PDF](https://arxiv.org/pdf/2602.06866.pdf)  
**作者**：Jingyi Cheng, Gonçalo Homem de Almeida Correia, Oded Cats, Shadi Sharif Azadeh  

**一句话要点**：提出T-STAR框架，用于基于码头的共享微出行短期概率需求预测

**关键词**：共享微出行, 需求预测, Transformer模型, 概率预测, 时空建模

## 3 点简述
- 核心问题：高分辨率短期需求预测中，需分离稳定模式与短期波动。
- 方法要点：采用两阶段Transformer结构，结合粗粒度小时模式和细粒度实时输入。
- 实验或效果：在华盛顿数据上优于现有方法，展示时空鲁棒性和零样本迁移能力。

## 摘要（原文）

> Reliable short-term demand forecasting is essential for managing shared micro-mobility services and ensuring responsive, user-centered operations. This study introduces T-STAR (Two-stage Spatial and Temporal Adaptive contextual Representation), a novel transformer-based probabilistic framework designed to forecast station-level bike-sharing demand at a 15-minute resolution. T-STAR addresses key challenges in high-resolution forecasting by disentangling consistent demand patterns from short-term fluctuations through a hierarchical two-stage structure. The first stage captures coarse-grained hourly demand patterns, while the second stage improves prediction accuracy by incorporating high-frequency, localized inputs, including recent fluctuations and real-time demand variations in connected metro services, to account for temporal shifts in short-term demand. Time series transformer models are employed in both stages to generate probabilistic predictions. Extensive experiments using Washington D.C.'s Capital Bikeshare data demonstrate that T-STAR outperforms existing methods in both deterministic and probabilistic accuracy. The model exhibits strong spatial and temporal robustness across stations and time periods. A zero-shot forecasting experiment further highlights T-STAR's ability to transfer to previously unseen service areas without retraining. These results underscore the framework's potential to deliver granular, reliable, and uncertainty-aware short-term demand forecasts, which enable seamless integration to support multimodal trip planning for travelers and enhance real-time operations in shared micro-mobility services.

