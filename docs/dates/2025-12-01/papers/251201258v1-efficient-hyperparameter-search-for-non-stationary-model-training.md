---
layout: default
title: Efficient Hyperparameter Search for Non-Stationary Model Training
---

# Efficient Hyperparameter Search for Non-Stationary Model Training
**arXiv**：[2512.01258v1](https://arxiv.org/abs/2512.01258) · [PDF](https://arxiv.org/pdf/2512.01258.pdf)  
**作者**：Berivan Isik, Matthew Fahrbach, Dima Kuzmin, Nicolas Mayoraz, Emil Praun, Steffen Rendle, Raghavendra Vasudeva  

**一句话要点**：提出两阶段超参数搜索框架以降低非平稳在线学习模型训练成本

**关键词**：超参数优化, 在线学习, 非平稳数据, 成本效率, 两阶段训练

## 3 点简述
- 核心问题：在线学习系统超参数搜索成本高昂，传统方法未处理非平稳数据挑战
- 方法要点：两阶段范式，先高效识别有前景配置，再充分训练，采用数据缩减和预测策略
- 实验或效果：在Criteo 1TB数据集上成本降低达10倍，工业广告系统中验证显著效率提升

## 摘要（原文）

> Online learning is the cornerstone of applications like recommendation and advertising systems, where models continuously adapt to shifting data distributions. Model training for such systems is remarkably expensive, a cost that multiplies during hyperparameter search. We introduce a two-stage paradigm to reduce this cost: (1) efficiently identifying the most promising configurations, and then (2) training only these selected candidates to their full potential. Our core insight is that focusing on accurate identification in the first stage, rather than achieving peak performance, allows for aggressive cost-saving measures. We develop novel data reduction and prediction strategies that specifically overcome the challenges of sequential, non-stationary data not addressed by conventional hyperparameter optimization. We validate our framework's effectiveness through a dual evaluation: first on the Criteo 1TB dataset, the largest suitable public benchmark, and second on an industrial advertising system operating at a scale two orders of magnitude larger. Our methods reduce the total hyperparameter search cost by up to 10$\times$ on the public benchmark and deliver significant, validated efficiency gains in the industrial setting.

