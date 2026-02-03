---
layout: default
title: SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration
---

# SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration
**arXiv**：[2602.02419v1](https://arxiv.org/abs/2602.02419) · [PDF](https://arxiv.org/pdf/2602.02419.pdf)  
**作者**：Qingni Wang, Yue Fan, Xin Eric Wang  

**一句话要点**：提出SafeGround框架，通过不确定性校准提升GUI grounding模型的可靠性，实现风险感知预测。

**关键词**：GUI grounding, 不确定性校准, 风险控制, 错误发现率, 自动化交互

## 3 点简述
- 核心问题：GUI grounding模型错误可能导致不可逆操作，需提高预测可靠性。
- 方法要点：采用分布感知不确定性量化，结合校准过程控制错误发现率。
- 实验或效果：在ScreenSpot-Pro基准上，提升系统级准确率最高达5.38个百分点。

## 摘要（原文）

> Graphical User Interface (GUI) grounding aims to translate natural language instructions into executable screen coordinates, enabling automated GUI interaction. Nevertheless, incorrect grounding can result in costly, hard-to-reverse actions (e.g., erroneous payment approvals), raising concerns about model reliability. In this paper, we introduce SafeGround, an uncertainty-aware framework for GUI grounding models that enables risk-aware predictions through calibrations before testing. SafeGround leverages a distribution-aware uncertainty quantification method to capture the spatial dispersion of stochastic samples from outputs of any given model. Then, through the calibration process, SafeGround derives a test-time decision threshold with statistically guaranteed false discovery rate (FDR) control. We apply SafeGround on multiple GUI grounding models for the challenging ScreenSpot-Pro benchmark. Experimental results show that our uncertainty measure consistently outperforms existing baselines in distinguishing correct from incorrect predictions, while the calibrated threshold reliably enables rigorous risk control and potentials of substantial system-level accuracy improvements. Across multiple GUI grounding models, SafeGround improves system-level accuracy by up to 5.38\% percentage points over Gemini-only inference.

