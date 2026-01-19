---
layout: default
title: Forcing and Diagnosing Failure Modes of Fourier Neural Operators Across Diverse PDE Families
---

# Forcing and Diagnosing Failure Modes of Fourier Neural Operators Across Diverse PDE Families
**arXiv**：[2601.11428v1](https://arxiv.org/abs/2601.11428) · [PDF](https://arxiv.org/pdf/2601.11428.pdf)  
**作者**：Lennon Shikhman  

**一句话要点**：提出系统压力测试框架以诊断傅里叶神经算子在多种偏微分方程中的失败模式

**关键词**：傅里叶神经算子, 偏微分方程, 鲁棒性测试, 分布偏移, 谱分析, 算子学习

## 3 点简述
- 核心问题：傅里叶神经算子在分布偏移、长时程推演和结构扰动下的鲁棒性未知
- 方法要点：设计控制压力测试，包括参数偏移、边界条件变化和分辨率外推，暴露谱偏差等漏洞
- 实验或效果：大规模评估显示参数或边界条件偏移可导致误差增加超过一个数量级

## 摘要（原文）

> Fourier Neural Operators (FNOs) have shown strong performance in learning solution maps of partial differential equations (PDEs), but their robustness under distribution shifts, long-horizon rollouts, and structural perturbations remains poorly understood. We present a systematic stress-testing framework that probes failure modes of FNOs across five qualitatively different PDE families: dispersive, elliptic, multi-scale fluid, financial, and chaotic systems. Rather than optimizing in-distribution accuracy, we design controlled stress tests--including parameter shifts, boundary or terminal condition changes, resolution extrapolation with spectral analysis, and iterative rollouts--to expose vulnerabilities such as spectral bias, compounding integration errors, and overfitting to restricted boundary regimes. Our large-scale evaluation (1{,}000 trained models) reveals that distribution shifts in parameters or boundary conditions can inflate errors by more than an order of magnitude, while resolution changes primarily concentrate error in high-frequency modes. Input perturbations generally do not amplify error, though worst-case scenarios (e.g., localized Poisson perturbations) remain challenging. These findings provide a comparative failure-mode atlas and actionable insights for improving robustness in operator learning.

