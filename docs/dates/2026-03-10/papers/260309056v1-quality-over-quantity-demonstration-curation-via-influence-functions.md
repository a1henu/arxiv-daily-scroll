---
layout: default
title: Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning
---

# Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning
**arXiv**：[2603.09056v1](https://arxiv.org/abs/2603.09056) · [PDF](https://arxiv.org/pdf/2603.09056.pdf)  
**作者**：Haeone Lee, Taywon Min, Junsu Kim, Sinjae Kang, Fangchen Liu, Lerrel Pinto, Kimin Lee  

**一句话要点**：提出QoQ方法，利用影响函数从演示数据中筛选高质量样本以提升机器人学习性能

**关键词**：机器人学习, 演示数据筛选, 影响函数, 数据质量评估, 端到端控制

## 3 点简述
- 核心问题：机器人演示数据质量参差不齐，人类操作误差和噪声影响数据驱动学习效果
- 方法要点：基于影响函数量化训练样本对验证损失的贡献，通过最大影响和轨迹聚合优化数据选择
- 实验或效果：在仿真和真实环境中验证，QoQ优于现有数据选择方法，提升策略性能

## 摘要（原文）

> Learning from demonstrations has emerged as a promising paradigm for end-to-end robot control, particularly when scaled to diverse and large datasets. However, the quality of demonstration data, often collected through human teleoperation, remains a critical bottleneck for effective data-driven robot learning. Human errors, operational constraints, and teleoperator variability introduce noise and suboptimal behaviors, making data curation essential yet largely manual and heuristic-driven. In this work, we propose Quality over Quantity (QoQ), a grounded and systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. To efficiently estimate this contribution, we leverage influence functions, which quantify the impact of individual training samples on model performance. We further introduce two key techniques to adapt influence functions for robot demonstrations: (i) using maximum influence across validation samples to capture the most relevant state-action pairs, and (ii) aggregating influence scores of state-action pairs within the same trajectory to reduce noise and improve data coverage. Experiments in both simulated and real-world settings show that QoQ consistently improves policy performances over prior data selection methods.

