---
layout: default
title: SpaTeoGL: Spatiotemporal Graph Learning for Interpretable Seizure Onset Zone Analysis from Intracranial EEG
---

# SpaTeoGL: Spatiotemporal Graph Learning for Interpretable Seizure Onset Zone Analysis from Intracranial EEG
**arXiv**：[2602.11801v1](https://arxiv.org/abs/2602.11801) · [PDF](https://arxiv.org/pdf/2602.11801.pdf)  
**作者**：Elham Rostami, Aref Einizade, Taous-Meriem Laleg-Kirati  

**一句话要点**：提出SpaTeoGL框架，用于从颅内脑电图进行可解释的癫痫发作区分析

**关键词**：时空图学习, 癫痫发作区分析, 颅内脑电图, 可解释性分析, 图信号处理

## 3 点简述
- 核心问题：颅内脑电图癫痫发作区定位受复杂时空动态影响，准确性受限
- 方法要点：联合学习窗口级空间图和时间图，基于平滑图信号处理框架，采用交替块坐标下降算法
- 实验或效果：在多中心数据集上验证，与基线方法竞争，提升非发作区识别并提供可解释性

## 摘要（原文）

> Accurate localization of the seizure onset zone (SOZ) from intracranial EEG (iEEG) is essential for epilepsy surgery but is challenged by complex spatiotemporal seizure dynamics. We propose SpaTeoGL, a spatiotemporal graph learning framework for interpretable seizure network analysis. SpaTeoGL jointly learns window-level spatial graphs capturing interactions among iEEG electrodes and a temporal graph linking time windows based on similarity of their spatial structure. The method is formulated within a smooth graph signal processing framework and solved via an alternating block coordinate descent algorithm with convergence guarantees. Experiments on a multicenter iEEG dataset with successful surgical outcomes show that SpaTeoGL is competitive with a baseline based on horizontal visibility graphs and logistic regression, while improving non-SOZ identification and providing interpretable insights into seizure onset and propagation dynamics.

