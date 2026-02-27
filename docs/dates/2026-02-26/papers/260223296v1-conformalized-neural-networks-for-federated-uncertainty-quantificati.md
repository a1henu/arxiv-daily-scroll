---
layout: default
title: Conformalized Neural Networks for Federated Uncertainty Quantification under Dual Heterogeneity
---

# Conformalized Neural Networks for Federated Uncertainty Quantification under Dual Heterogeneity
**arXiv**：[2602.23296v1](https://arxiv.org/abs/2602.23296) · [PDF](https://arxiv.org/pdf/2602.23296.pdf)  
**作者**：Quang-Huy Nguyen, Jiaqi Wang, Wei-Shinn Ku  

**一句话要点**：提出FedWQ-CP方法，在联邦学习中解决双重异构性下的不确定性量化问题。

**关键词**：联邦学习, 不确定性量化, 保形预测, 双重异构性, 覆盖可靠性

## 3 点简述
- 核心问题：联邦学习面临数据与模型双重异构性，现有不确定性量化方法覆盖可靠性不足。
- 方法要点：基于保形预测，通过单轮通信的代理-服务器校准，加权聚合局部阈值实现全局覆盖。
- 实验或效果：在七个公开数据集上验证，保持代理和全局覆盖，同时生成最小预测集或区间。

## 摘要（原文）

> Federated learning (FL) faces challenges in uncertainty quantification (UQ). Without reliable UQ, FL systems risk deploying overconfident models at under-resourced agents, leading to silent local failures despite seemingly satisfactory global performance. Existing federated UQ approaches often address data heterogeneity or model heterogeneity in isolation, overlooking their joint effect on coverage reliability across agents. Conformal prediction is a widely used distribution-free UQ framework, yet its applications in heterogeneous FL settings remains underexplored. We provide FedWQ-CP, a simple yet effective approach that balances empirical coverage performance with efficiency at both global and agent levels under the dual heterogeneity. FedWQ-CP performs agent-server calibration in a single communication round. On each agent, conformity scores are computed on calibration data and a local quantile threshold is derived. Each agent then transmits only its quantile threshold and calibration sample size to the server. The server simply aggregates these thresholds through a weighted average to produce a global threshold. Experimental results on seven public datasets for both classification and regression demonstrate that FedWQ-CP empirically maintains agent-wise and global coverage while producing the smallest prediction sets or intervals.

