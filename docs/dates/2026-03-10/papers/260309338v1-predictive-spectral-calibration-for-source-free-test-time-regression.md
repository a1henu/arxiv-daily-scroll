---
layout: default
title: Predictive Spectral Calibration for Source-Free Test-Time Regression
---

# Predictive Spectral Calibration for Source-Free Test-Time Regression
**arXiv**：[2603.09338v1](https://arxiv.org/abs/2603.09338) · [PDF](https://arxiv.org/pdf/2603.09338.pdf)  
**作者**：Nguyen Viet Tuan Kiet, Huynh Thanh Trung, Pham Huy Hieu  

**一句话要点**：提出预测性谱校准以解决无源测试时回归中的分布偏移问题

**关键词**：测试时适应, 图像回归, 子空间对齐, 谱校准, 无源学习, 分布偏移

## 3 点简述
- 核心问题：图像回归的测试时适应研究较少，分类方法难以直接迁移到连续回归目标。
- 方法要点：基于子空间对齐，通过块谱匹配联合对齐源预测支持子空间并校准正交补中的残差谱松弛。
- 实验或效果：在多个图像回归基准上表现优于强基线，尤其在严重分布偏移下增益明显。

## 摘要（原文）

> Test-time adaptation (TTA) for image regression has received far less attention than its classification counterpart. Methods designed for classification often depend on classification-specific objectives and decision boundaries, making them difficult to transfer directly to continuous regression targets. Recent progress revisits regression TTA through subspace alignment, showing that simple source-guided alignment can be both practical and effective. Building on this line of work, we propose Predictive Spectral Calibration (PSC), a source-free framework that extends subspace alignment to block spectral matching. Instead of relying on a fixed support subspace alone, PSC jointly aligns target features within the source predictive support and calibrates residual spectral slack in the orthogonal complement. PSC remains simple to implement, model-agnostic, and compatible with off-the-shelf pretrained regressors. Experiments on multiple image regression benchmarks show consistent improvements over strong baselines, with particularly clear gains under severe distribution shifts.

