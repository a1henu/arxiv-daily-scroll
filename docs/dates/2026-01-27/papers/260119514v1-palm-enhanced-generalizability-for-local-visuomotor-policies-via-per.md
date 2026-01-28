---
layout: default
title: PALM: Enhanced Generalizability for Local Visuomotor Policies via Perception Alignment
---

# PALM: Enhanced Generalizability for Local Visuomotor Policies via Perception Alignment
**arXiv**：[2601.19514v1](https://arxiv.org/abs/2601.19514) · [PDF](https://arxiv.org/pdf/2601.19514.pdf)  
**作者**：Ruiyu Wang, Zheyu Zhuang, Danica Kragic, Florian T. Pokorny  

**一句话要点**：提出PALM方法，通过感知对齐增强局部视觉运动策略的泛化能力

**关键词**：视觉运动策略, 感知对齐, 域外泛化, 行为克隆, 机器人操作

## 3 点简述
- 核心问题：图像行为克隆在训练域外泛化困难，现有方法常孤立处理不同泛化轴且依赖复杂流程。
- 方法要点：将策略模块化为全局粗调与局部细调，通过强制局部视觉焦点和一致本体感知表示，减少域内外输入差异。
- 实验或效果：在仿真和真实世界中，PALM将域外性能下降限制在8%和24%，优于基线方法的45%和77%。

## 摘要（原文）

> Generalizing beyond the training domain in image-based behavior cloning remains challenging. Existing methods address individual axes of generalization, workspace shifts, viewpoint changes, and cross-embodiment transfer, yet they are typically developed in isolation and often rely on complex pipelines. We introduce PALM (Perception Alignment for Local Manipulation), which leverages the invariance of local action distributions between out-of-distribution (OOD) and demonstrated domains to address these OOD shifts concurrently, without additional input modalities, model changes, or data collection. PALM modularizes the manipulation policy into coarse global components and a local policy for fine-grained actions. We reduce the discrepancy between in-domain and OOD inputs at the local policy level by enforcing local visual focus and consistent proprioceptive representation, allowing the policy to retrieve invariant local actions under OOD conditions. Experiments show that PALM limits OOD performance drops to 8% in simulation and 24% in the real world, compared to 45% and 77% for baselines.

