---
layout: default
title: WFR-MFM: One-Step Inference for Dynamic Unbalanced Optimal Transport
---

# WFR-MFM: One-Step Inference for Dynamic Unbalanced Optimal Transport
**arXiv**：[2601.20606v1](https://arxiv.org/abs/2601.20606) · [PDF](https://arxiv.org/pdf/2601.20606.pdf)  
**作者**：Xinyu Wang, Ruoyu Wang, Qiangwei Peng, Peijie Zhou, Tiejun Li  

**一句话要点**：提出WFR-MFM框架，通过平均流匹配实现动态不平衡最优传输的一步推理，加速单细胞生物学应用。

**关键词**：动态不平衡最优传输, 平均流匹配, 单细胞生物学, 一步推理, Wasserstein-Fisher-Rao几何

## 3 点简述
- 核心问题：动态不平衡最优传输在推理时依赖轨迹模拟，导致可扩展应用瓶颈。
- 方法要点：基于平均流框架，使用平均速度和质量增长场总结任意时间间隔的传输与质量变化。
- 实验或效果：在合成和真实单细胞RNA测序数据上，推理速度比基线快多个数量级，保持高预测精度。

## 摘要（原文）

> Reconstructing dynamical evolution from limited observations is a fundamental challenge in single-cell biology, where dynamic unbalanced optimal transport provides a principled framework for modeling coupled transport and mass variation. However, existing approaches rely on trajectory simulation at inference time, making inference a key bottleneck for scalable applications. In this work, we propose a mean-flow framework for unbalanced flow matching that summarizes both transport and mass-growth dynamics over arbitrary time intervals using mean velocity and mass-growth fields, enabling fast one-step generation without trajectory simulation. To solve dynamic unbalanced optimal transport under the Wasserstein-Fisher-Rao geometry, we further build on this framework to develop Wasserstein-Fisher-Rao Mean Flow Matching (WFR-MFM). Across synthetic and real single-cell RNA sequencing datasets, WFR-MFM achieves orders-of-magnitude faster inference than a range of existing baselines while maintaining high predictive accuracy, and enables efficient perturbation response prediction on large synthetic datasets with thousands of conditions.

