---
layout: default
title: SUPER -- A Framework for Sensitivity-based Uncertainty-aware Performance and Risk Assessment in Visual Inertial Odometry
---

# SUPER -- A Framework for Sensitivity-based Uncertainty-aware Performance and Risk Assessment in Visual Inertial Odometry
**arXiv**：[2512.14189v1](https://arxiv.org/abs/2512.14189) · [PDF](https://arxiv.org/pdf/2512.14189.pdf)  
**作者**：Johannes A. Gaus, Daniel Häufle, Woo-Jeong Baek  

**一句话要点**：提出SUPER框架，通过灵敏度传播不确定性，实现视觉惯性里程计中的实时风险评估。

**关键词**：视觉惯性里程计, 不确定性传播, 实时风险评估, 舒尔补, 后端无关, 轨迹退化预测

## 3 点简述
- 核心问题：现有视觉惯性里程计系统缺乏运行时风险评估能力，可能导致轨迹退化。
- 方法要点：利用高斯-牛顿法正规矩阵的舒尔补块传播不确定性，基于残差、几何条件和短期趋势估计风险。
- 实验或效果：框架可提前50帧预测轨迹退化，改进20%，实时运行且CPU开销低于0.2%。

## 摘要（原文）

> While many visual odometry (VO), visual-inertial odometry (VIO), and SLAM systems achieve high accuracy, the majority of existing methods miss to assess risks at runtime. This paper presents SUPER (Sensitivity-based Uncertainty-aware PErformance and Risk assessment) that is a generic and explainable framework that propagates uncertainties via sensitivities for real-time risk assessment in VIO. The scientific novelty lies in the derivation of a real-time risk indicator that is backend-agnostic and exploits the Schur complement blocks of the Gauss-Newton normal matrix to propagate uncertainties. Practically, the Schur complement captures the sensitivity that reflects the influence of the uncertainty on the risk occurrence. Our framework estimates risks on the basis of the residual magnitudes, geometric conditioning, and short horizon temporal trends without requiring ground truth knowledge. Our framework enables to reliably predict trajectory degradation 50 frames ahead with an improvement of 20% to the baseline. In addition, SUPER initiates a stop or relocalization policy with 89.1% recall. The framework is backend agnostic and operates in real time with less than 0.2% additional CPU cost. Experiments show that SUPER provides consistent uncertainty estimates. A SLAM evaluation highlights the applicability to long horizon mapping.

