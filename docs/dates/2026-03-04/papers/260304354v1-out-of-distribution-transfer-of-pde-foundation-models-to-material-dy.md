---
layout: default
title: Out-of-distribution transfer of PDE foundation models to material dynamics under extreme loading
---

# Out-of-distribution transfer of PDE foundation models to material dynamics under extreme loading
**arXiv**：[2603.04354v1](https://arxiv.org/abs/2603.04354) · [PDF](https://arxiv.org/pdf/2603.04354.pdf)  
**作者**：Mahindra Rautela, Alexander Most, Siddharth Mansingh, Aleksandra Pachalieva, Bradley Love, Daniel O Malley, Alexander Scheinker, Kyle Hickmann, Diane Oyen, Nathan Debardeleben, Earl Lawrence, Ayan Biswas  

**一句话要点**：评估PDE基础模型在极端载荷材料动力学中的分布外迁移性能

**关键词**：PDE基础模型, 分布外迁移, 材料动力学, 终端状态预测, 极端载荷, 样本效率

## 3 点简述
- 核心问题：PDE基础模型在流体基准上预训练，其在非光滑场主导的极端载荷材料动力学中的适用性未知。
- 方法要点：采用终端状态预测任务，评估预训练模型POSEIDON和MORPH在冲击驱动界面动力学和动态断裂场景中的迁移效果。
- 实验或效果：通过统一协议比较微调与从头训练，量化分布偏移下的样本效率。

## 摘要（原文）

> Most PDE foundation models are pretrained and fine-tuned on fluid-centric benchmarks. Their utility under extreme-loading material dynamics remains unclear. We benchmark out-of-distribution transfer on two discontinuity-dominated regimes in which shocks, evolving interfaces, and fracture produce highly non-smooth fields: shock-driven multi-material interface dynamics (perturbed layered interface or PLI) and dynamic fracture/failure evolution (FRAC). We formulate the downstream task as terminal-state prediction, i.e., learning a long-horizon map that predicts the final state directly from the first snapshot without intermediate supervision. Using a unified training and evaluation protocol, we evaluate two open-source pretrained PDE foundation models, POSEIDON and MORPH, and compare fine-tuning from pretrained weights against training from scratch across training-set sizes to quantify sample efficiency under distribution shift.

