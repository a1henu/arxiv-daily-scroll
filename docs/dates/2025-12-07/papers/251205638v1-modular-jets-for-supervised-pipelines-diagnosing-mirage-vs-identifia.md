---
layout: default
title: Modular Jets for Supervised Pipelines: Diagnosing Mirage vs Identifiability
---

# Modular Jets for Supervised Pipelines: Diagnosing Mirage vs Identifiability
**arXiv**：[2512.05638v1](https://arxiv.org/abs/2512.05638) · [PDF](https://arxiv.org/pdf/2512.05638.pdf)  
**作者**：Suman Sanyal  

**一句话要点**：提出模块化喷射以诊断监督学习管道中的幻象与可识别性

**关键词**：模块化喷射, 监督学习管道, 可识别性, 幻象诊断, 线性回归, 深度学习

## 3 点简述
- 核心问题：传统监督学习评估仅关注预测风险，无法确定模型内部分解是否由数据和评估设计唯一确定。
- 方法要点：引入模块化喷射，通过局部线性响应图估计模块对输入扰动的反应，区分幻象与可识别性。
- 实验或效果：在线性回归管道中证明喷射可识别性定理，并开发MoJet算法进行实证估计和诊断。

## 摘要（原文）

> Classical supervised learning evaluates models primarily via predictive risk on hold-out data. Such evaluations quantify how well a function behaves on a distribution, but they do not address whether the internal decomposition of a model is uniquely determined by the data and evaluation design. In this paper, we introduce \emph{Modular Jets} for regression and classification pipelines. Given a task manifold (input space), a modular decomposition, and access to module-level representations, we estimate empirical jets, which are local linear response maps that describe how each module reacts to small structured perturbations of the input. We propose an empirical notion of \emph{mirage} regimes, where multiple distinct modular decompositions induce indistinguishable jets and thus remain observationally equivalent, and contrast this with an \emph{identifiable} regime, where the observed jets single out a decomposition up to natural symmetries. In the setting of two-module linear regression pipelines we prove a jet-identifiability theorem. Under mild rank assumptions and access to module-level jets, the internal factorisation is uniquely determined, whereas risk-only evaluation admits a large family of mirage decompositions that implement the same input-to-output map. We then present an algorithm (MoJet) for empirical jet estimation and mirage diagnostics, and illustrate the framework using linear and deep regression as well as pipeline classification.

