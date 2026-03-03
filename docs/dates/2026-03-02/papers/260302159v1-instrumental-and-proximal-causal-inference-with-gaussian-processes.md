---
layout: default
title: Instrumental and Proximal Causal Inference with Gaussian Processes
---

# Instrumental and Proximal Causal Inference with Gaussian Processes
**arXiv**：[2603.02159v1](https://arxiv.org/abs/2603.02159) · [PDF](https://arxiv.org/pdf/2603.02159.pdf)  
**作者**：Yuqi Zhang, Krikamol Muandet, Dino Sejdinovic, Edwin Fong, Siu Lun Chau  

**一句话要点**：提出解条件高斯过程框架，用于未观测混杂下因果推断的可靠不确定性量化。

**关键词**：因果推断, 高斯过程, 不确定性量化, 工具变量, 近端因果学习, 模型选择

## 3 点简述
- 核心问题：工具变量和近端因果方法缺乏可靠认知不确定性量化。
- 方法要点：通过解条件高斯过程统一框架，后验均值恢复核估计器，后验方差提供校准不确定性。
- 实验或效果：实证显示强预测性能和信息性不确定性，通过覆盖频率和决策感知曲线评估。

## 摘要（原文）

> Instrumental variable (IV) and proximal causal learning (Proxy) methods are central frameworks for causal inference in the presence of unobserved confounding. Despite substantial methodological advances, existing approaches rarely provide reliable epistemic uncertainty (EU) quantification. We address this gap through a Deconditional Gaussian Process (DGP) framework for uncertainty-aware causal learning. Our formulation recovers popular kernel estimators as the posterior mean, ensuring predictive precision, while the posterior variance yields principled and well-calibrated EU. Moreover, the probabilistic structure enables systematic model selection via marginal log-likelihood optimization. Empirical results demonstrate strong predictive performance alongside informative EU quantification, evaluated via empirical coverage frequencies and decision-aware accuracy rejection curves. Together, our approach provides a unified, practical solution for causal inference under unobserved confounding with reliable uncertainty.

