---
layout: default
title: SpaTeoGL: Spatiotemporal Graph Learning for Interpretable Seizure Onset Zone Analysis from Intracranial EEG
---

# SpaTeoGL: Spatiotemporal Graph Learning for Interpretable Seizure Onset Zone Analysis from Intracranial EEG
**arXiv**：[2602.11801v1](https://arxiv.org/abs/2602.11801) · [PDF](https://arxiv.org/pdf/2602.11801.pdf)  
**作者**：Elham Rostami, Aref Einizade, Taous-Meriem Laleg-Kirati  

**一句话要点**：提出SpaTeoGL框架，通过时空图学习分析颅内脑电以定位癫痫发作区

**关键词**：癫痫发作区定位, 时空图学习, 颅内脑电分析, 图信号处理, 可解释性分析

## 3 点简述
- 核心问题：颅内脑电中癫痫发作区的精确定位受复杂时空动态干扰
- 方法要点：联合学习电极间空间图和基于结构相似性的时间图，采用平滑图信号处理框架
- 实验或效果：在多中心数据集上表现与基线竞争，提升非发作区识别并提供可解释性

## 摘要（原文）

> Accurate localization of the seizure onset zone (SOZ) from intracranial EEG (iEEG) is essential for epilepsy surgery but is challenged by complex spatiotemporal seizure dynamics. We propose SpaTeoGL, a spatiotemporal graph learning framework for interpretable seizure network analysis. SpaTeoGL jointly learns window-level spatial graphs capturing interactions among iEEG electrodes and a temporal graph linking time windows based on similarity of their spatial structure. The method is formulated within a smooth graph signal processing framework and solved via an alternating block coordinate descent algorithm with convergence guarantees. Experiments on a multicenter iEEG dataset with successful surgical outcomes show that SpaTeoGL is competitive with a baseline based on horizontal visibility graphs and logistic regression, while improving non-SOZ identification and providing interpretable insights into seizure onset and propagation dynamics.

