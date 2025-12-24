---
layout: default
title: Degradation-Aware Metric Prompting for Hyperspectral Image Restoration
---

# Degradation-Aware Metric Prompting for Hyperspectral Image Restoration
**arXiv**：[2512.20251v1](https://arxiv.org/abs/2512.20251) · [PDF](https://arxiv.org/pdf/2512.20251.pdf)  
**作者**：Binfeng Wang, Di Wang, Haonan Guo, Ying Fu, Jing Zhang  

**一句话要点**：提出Degradation-Aware Metric Prompting框架，以解决统一高光谱图像恢复中依赖显式退化先验的挑战。

**关键词**：高光谱图像恢复, 退化感知, 度量提示, 空间-光谱自适应, 专家混合架构, 统一模型

## 3 点简述
- 核心问题：统一高光谱图像恢复依赖难以获取的显式退化先验，如退化标签，限制了实际应用。
- 方法要点：设计空间-光谱退化度量作为退化提示，结合空间-光谱自适应模块和专家混合架构，实现自适应特征调制。
- 实验或效果：在自然和遥感数据集上实现先进性能，展示卓越的泛化能力，代码已公开。

## 摘要（原文）

> Unified hyperspectral image (HSI) restoration aims to recover various degraded HSIs using a single model, offering great practical value. However, existing methods often depend on explicit degradation priors (e.g., degradation labels) as prompts to guide restoration, which are difficult to obtain due to complex and mixed degradations in real-world scenarios. To address this challenge, we propose a Degradation-Aware Metric Prompting (DAMP) framework. Instead of relying on predefined degradation priors, we design spatial-spectral degradation metrics to continuously quantify multi-dimensional degradations, serving as Degradation Prompts (DP). These DP enable the model to capture cross-task similarities in degradation distributions and enhance shared feature learning. Furthermore, we introduce a Spatial-Spectral Adaptive Module (SSAM) that dynamically modulates spatial and spectral feature extraction through learnable parameters. By integrating SSAM as experts within a Mixture-of-Experts architecture, and using DP as the gating router, the framework enables adaptive, efficient, and robust restoration under diverse, mixed, or unseen degradations. Extensive experiments on natural and remote sensing HSI datasets show that DAMP achieves state-of-the-art performance and demonstrates exceptional generalization capability. Code is publicly available at https://github.com/MiliLab/DAMP.

