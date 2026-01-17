---
layout: default
title: Meta Dynamic Graph for Traffic Flow Prediction
---

# Meta Dynamic Graph for Traffic Flow Prediction
**arXiv**：[2601.10328v1](https://arxiv.org/abs/2601.10328) · [PDF](https://arxiv.org/pdf/2601.10328.pdf)  
**作者**：Yiqing Zou, Hanning Yuan, Qianyu Yang, Ziqiang Yuan, Shuliang Wang, Sijie Ruan  

**一句话要点**：提出MetaDG框架，通过动态图结构建模时空动态性以提升交通流预测性能。

**关键词**：交通流预测, 时空依赖建模, 动态图结构, 元参数学习, 异质性建模

## 3 点简述
- 核心问题：交通流预测需建模复杂时空依赖，现有方法在动态性和异质性建模上存在局限。
- 方法要点：利用节点表示的动态图结构，生成动态邻接矩阵和元参数，统一捕捉时空异质性。
- 实验或效果：在四个真实数据集上验证了MetaDG的有效性，具体性能指标未知。

## 摘要（原文）

> Traffic flow prediction is a typical spatio-temporal prediction problem and has a wide range of applications. The core challenge lies in modeling the underlying complex spatio-temporal dependencies. Various methods have been proposed, and recent studies show that the modeling of dynamics is useful to meet the core challenge. While handling spatial dependencies and temporal dependencies using separate base model structures may hinder the modeling of spatio-temporal correlations, the modeling of dynamics can bridge this gap. Incorporating spatio-temporal heterogeneity also advances the main goal, since it can extend the parameter space and allow more flexibility. Despite these advances, two limitations persist: 1) the modeling of dynamics is often limited to the dynamics of spatial topology (e.g., adjacency matrix changes), which, however, can be extended to a broader scope; 2) the modeling of heterogeneity is often separated for spatial and temporal dimensions, but this gap can also be bridged by the modeling of dynamics. To address the above limitations, we propose a novel framework for traffic prediction, called Meta Dynamic Graph (MetaDG). MetaDG leverages dynamic graph structures of node representations to explicitly model spatio-temporal dynamics. This generates both dynamic adjacency matrices and meta-parameters, extending dynamic modeling beyond topology while unifying the capture of spatio-temporal heterogeneity into a single dimension. Extensive experiments on four real-world datasets validate the effectiveness of MetaDG.

