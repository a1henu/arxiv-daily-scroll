---
layout: default
title: Prescriptive Scaling Reveals the Evolution of Language Model Capabilities
---

# Prescriptive Scaling Reveals the Evolution of Language Model Capabilities
**arXiv**：[2602.15327v1](https://arxiv.org/abs/2602.15327) · [PDF](https://arxiv.org/pdf/2602.15327.pdf)  
**作者**：Hanlin Zhang, Jikai Jin, Vasilis Syrgkanis, Sham Kakade  

**一句话要点**：提出描述性缩放定律以预测语言模型能力边界，支持部署决策与演进监控

**关键词**：缩放定律, 能力边界估计, 分位数回归, 模型评估, 计算预算映射, 演进监控

## 3 点简述
- 核心问题：预训练计算预算如何映射到下游任务准确率，且该映射随时间是否稳定
- 方法要点：使用平滑分位数回归估计能力边界，基于大规模观测数据与单调饱和S形参数化
- 实验或效果：验证边界在多数任务中稳定，数学推理边界随时间推进，并开发高效算法节省评估成本

## 摘要（原文）

> For deploying foundation models, practitioners increasingly need prescriptive scaling laws: given a pre training compute budget, what downstream accuracy is attainable with contemporary post training practice, and how stable is that mapping as the field evolves? Using large scale observational evaluations with 5k observational and 2k newly sampled data on model performance, we estimate capability boundaries, high conditional quantiles of benchmark scores as a function of log pre training FLOPs, via smoothed quantile regression with a monotone, saturating sigmoid parameterization. We validate the temporal reliability by fitting on earlier model generations and evaluating on later releases. Across various tasks, the estimated boundaries are mostly stable, with the exception of math reasoning that exhibits a consistently advancing boundary over time. We then extend our approach to analyze task dependent saturation and to probe contamination related shifts on math reasoning tasks. Finally, we introduce an efficient algorithm that recovers near full data frontiers using roughly 20% of evaluation budget. Together, our work releases the Proteus 2k, the latest model performance evaluation dataset, and introduces a practical methodology for translating compute budgets into reliable performance expectations and for monitoring when capability boundaries shift across time.

