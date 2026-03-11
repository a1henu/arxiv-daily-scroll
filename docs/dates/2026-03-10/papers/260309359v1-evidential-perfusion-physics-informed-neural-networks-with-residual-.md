---
layout: default
title: Evidential Perfusion Physics-Informed Neural Networks with Residual Uncertainty Quantification
---

# Evidential Perfusion Physics-Informed Neural Networks with Residual Uncertainty Quantification
**arXiv**：[2603.09359v1](https://arxiv.org/abs/2603.09359) · [PDF](https://arxiv.org/pdf/2603.09359.pdf)  
**作者**：Junhyeok Lee, Minseo Choi, Han Jang, Young Hun Jeon, Heeseong Eum, Joon Jang, Chul-Ho Sohn, Kyu Sung Choi  

**一句话要点**：提出EPPINN框架，结合证据深度学习和物理约束，用于急性缺血性卒中CT灌注成像的不确定性感知参数估计。

**关键词**：CT灌注成像, 物理信息神经网络, 不确定性量化, 急性缺血性卒中, 证据深度学习, 参数估计

## 3 点简述
- 核心问题：现有PINN方法在CT灌注成像中为确定性，无法量化物理约束违反的不确定性，限制可靠性评估。
- 方法要点：EPPINN使用坐标网络建模，通过Normal-Inverse-Gamma分布表征物理残差的不确定性，无需贝叶斯采样或集成推理。
- 实验或效果：在数字幻影、ISLES 2018基准和临床数据上，EPPINN降低误差，提高梗死核心检测灵敏度，并提供保守不确定性估计。

## 摘要（原文）

> Physics-informed neural networks (PINNs) have shown promise in addressing the ill-posed deconvolution problem in computed tomography perfusion (CTP) imaging for acute ischemic stroke assessment. However, existing PINN-based approaches remain deterministic and do not quantify uncertainty associated with violations of physics constraints, limiting reliability assessment. We propose Evidential Perfusion Physics-Informed Neural Networks (EPPINN), a framework that integrates evidential deep learning with physics-informed modeling to enable uncertainty-aware perfusion parameter estimation. EPPINN models arterial input, tissue concentration, and perfusion parameters using coordinate-based networks, and places a Normal--Inverse--Gamma distribution over the physics residual to characterize voxel-wise aleatoric and epistemic uncertainty in physics consistency without requiring Bayesian sampling or ensemble inference. The framework further incorporates physiologically constrained parameterization and stabilization strategies to promote robust per-case optimization. We evaluate EPPINN on digital phantom data, the ISLES 2018 benchmark, and a clinical cohort. On the evaluated datasets, EPPINN achieves lower normalized mean absolute error than classical deconvolution and PINN baselines, particularly under sparse temporal sampling and low signal-to-noise conditions, while providing conservative uncertainty estimates with high empirical coverage. On clinical data, EPPINN attains the highest voxel-level and case-level infarct-core detection sensitivity. These results suggest that evidential physics-informed learning can improve both accuracy and reliability of CTP analysis for time-critical stroke assessment.

