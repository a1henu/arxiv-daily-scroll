---
layout: default
title: THOR: A Versatile Foundation Model for Earth Observation Climate and Society Applications
---

# THOR: A Versatile Foundation Model for Earth Observation Climate and Society Applications
**arXiv**：[2601.16011v1](https://arxiv.org/abs/2601.16011) · [PDF](https://arxiv.org/pdf/2601.16011.pdf)  
**作者**：Theodor Forgaard, Jarle H. Reksten, Anders U. Waldeland, Valerio Marsocci, Nicolas Longépé, Michael Kampffmeyer, Arnt-Børre Salberg  

**一句话要点**：提出THOR计算自适应基础模型，解决地球观测中传感器异构与部署刚性问题

**关键词**：地球观测基础模型, 多传感器融合, 计算自适应, 随机化补丁策略, Sentinel卫星数据, 下游应用基准

## 3 点简述
- 当前地球观测基础模型架构僵化，难以处理多传感器数据且受限于固定补丁大小
- THOR统一处理Sentinel-1、-2、-3卫星数据，通过随机化补丁和输入尺寸策略实现计算自适应
- 在THOR Pretrain数据集预训练，下游基准测试中表现优异，尤其在数据有限场景下验证其灵活性

## 摘要（原文）

> Current Earth observation foundation models are architecturally rigid, struggle with heterogeneous sensors and are constrained to fixed patch sizes. This limits their deployment in real-world scenarios requiring flexible computeaccuracy trade-offs. We propose THOR, a "computeadaptive" foundation model that solves both input heterogeneity and deployment rigidity. THOR is the first architecture to unify data from Copernicus Sentinel-1, -2, and -3 (OLCI & SLSTR) satellites, processing their native 10 m to 1000 m resolutions in a single model. We pre-train THOR with a novel randomized patch and input image size strategy. This allows a single set of pre-trained weights to be deployed at inference with any patch size, enabling a dynamic trade-off between computational cost and feature resolution without retraining. We pre-train THOR on THOR Pretrain, a new, large-scale multi-sensor dataset and demonstrate state-of-the-art performance on downstream benchmarks, particularly in data-limited regimes like the PANGAEA 10% split, validating that THOR's flexible feature generation excels for diverse climate and society applications.

