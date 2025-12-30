---
layout: default
title: Towards Integrating Uncertainty for Domain-Agnostic Segmentation
---

# Towards Integrating Uncertainty for Domain-Agnostic Segmentation
**arXiv**：[2512.23427v1](https://arxiv.org/abs/2512.23427) · [PDF](https://arxiv.org/pdf/2512.23427.pdf)  
**作者**：Jesse Brouwers, Xiaoyan Xing, Alexander Timans  

**一句话要点**：提出UncertSAM基准与不确定性量化方法以增强分割模型在领域无关场景下的鲁棒性

**关键词**：不确定性量化, 领域无关分割, Segment Anything Model, 基准测试, 后验估计, 鲁棒性增强

## 3 点简述
- 核心问题：基础分割模型如SAM在领域偏移或知识有限时性能下降，需提升泛化能力
- 方法要点：构建UncertSAM基准测试集，评估轻量级后验不确定性估计方法，并探索不确定性引导的预测优化
- 实验或效果：Laplace近似方法的不确定性估计与分割误差相关性强，初步优化显示潜力，支持领域无关性能

## 摘要（原文）

> Foundation models for segmentation such as the Segment Anything Model (SAM) family exhibit strong zero-shot performance, but remain vulnerable in shifted or limited-knowledge domains. This work investigates whether uncertainty quantification can mitigate such challenges and enhance model generalisability in a domain-agnostic manner. To this end, we (1) curate UncertSAM, a benchmark comprising eight datasets designed to stress-test SAM under challenging segmentation conditions including shadows, transparency, and camouflage; (2) evaluate a suite of lightweight, post-hoc uncertainty estimation methods; and (3) assess a preliminary uncertainty-guided prediction refinement step. Among evaluated approaches, a last-layer Laplace approximation yields uncertainty estimates that correlate well with segmentation errors, indicating a meaningful signal. While refinement benefits are preliminary, our findings underscore the potential of incorporating uncertainty into segmentation models to support robust, domain-agnostic performance. Our benchmark and code are made publicly available.

