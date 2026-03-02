---
layout: default
title: Leveraging Geometric Prior Uncertainty and Complementary Constraints for High-Fidelity Neural Indoor Surface Reconstruction
---

# Leveraging Geometric Prior Uncertainty and Complementary Constraints for High-Fidelity Neural Indoor Surface Reconstruction
**arXiv**：[2602.23926v1](https://arxiv.org/abs/2602.23926) · [PDF](https://arxiv.org/pdf/2602.23926.pdf)  
**作者**：Qiyu Feng, Jiwei Shan, Shing Shin Cheng, Hesheng Wang  

**一句话要点**：提出GPU-SDF框架，利用几何先验不确定性和互补约束提升室内表面重建的细节恢复能力。

**关键词**：神经隐式表面重建, 几何先验不确定性, 室内场景重建, 自监督学习, 多视图一致性

## 3 点简述
- 核心问题：神经隐式表面重建中，不可靠或噪声几何先验导致薄结构和复杂几何细节恢复困难。
- 方法要点：引入自监督模块显式估计先验不确定性，设计不确定性引导损失和边缘距离场、多视图一致性正则化作为互补约束。
- 实验或效果：实验证实GPU-SDF能改善细节重建，可作为现有框架的即插即用增强模块。

## 摘要（原文）

> Neural implicit surface reconstruction with signed distance function has made significant progress, but recovering fine details such as thin structures and complex geometries remains challenging due to unreliable or noisy geometric priors. Existing approaches rely on implicit uncertainty that arises during optimization to filter these priors, which is indirect and inefficient, and masking supervision in high-uncertainty regions further leads to under-constrained optimization. To address these issues, we propose GPU-SDF, a neural implicit framework for indoor surface reconstruction that leverages geometric prior uncertainty and complementary constraints. We introduce a self-supervised module that explicitly estimates prior uncertainty without auxiliary networks. Based on this estimation, we design an uncertainty-guided loss that modulates prior influence rather than discarding it, thereby retaining weak but informative cues. To address regions with high prior uncertainty, GPU-SDF further incorporates two complementary constraints: an edge distance field that strengthens boundary supervision and a multi-view consistency regularization that enforces geometric coherence. Extensive experiments confirm that GPU-SDF improves the reconstruction of fine details and serves as a plug-and-play enhancement for existing frameworks. Source code will be available at https://github.com/IRMVLab/GPU-SDF

