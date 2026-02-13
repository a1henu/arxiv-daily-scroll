---
layout: default
title: Temporally Unified Adversarial Perturbations for Time Series Forecasting
---

# Temporally Unified Adversarial Perturbations for Time Series Forecasting
**arXiv**：[2602.11940v1](https://arxiv.org/abs/2602.11940) · [PDF](https://arxiv.org/pdf/2602.11940.pdf)  
**作者**：Ruixian Su, Yukun Bao, Xinze Zhang  

**一句话要点**：提出时间统一对抗扰动以解决时间序列预测中扰动时间不一致问题

**关键词**：时间序列预测, 对抗攻击, 时间一致性, 梯度累积, 转移攻击

## 3 点简述
- 核心问题：现有对抗攻击方法忽略时间序列数据的时间一致性，导致重叠样本中相同时间戳的扰动值不一致，影响实际应用。
- 方法要点：引入时间统一对抗扰动约束，确保所有重叠样本中每个时间戳的扰动相同；提出时间戳梯度累积方法，高效生成统一扰动。
- 实验或效果：在三个基准数据集和四个先进模型上，方法在白盒和黑盒转移攻击场景中显著优于基线，且无约束时也表现优异。

## 摘要（原文）

> While deep learning models have achieved remarkable success in time series forecasting, their vulnerability to adversarial examples remains a critical security concern. However, existing attack methods in the forecasting field typically ignore the temporal consistency inherent in time series data, leading to divergent and contradictory perturbation values for the same timestamp across overlapping samples. This temporally inconsistent perturbations problem renders adversarial attacks impractical for real-world data manipulation. To address this, we introduce Temporally Unified Adversarial Perturbations (TUAPs), which enforce a temporal unification constraint to ensure identical perturbations for each timestamp across all overlapping samples. Moreover, we propose a novel Timestamp-wise Gradient Accumulation Method (TGAM) that provides a modular and efficient approach to effectively generate TUAPs by aggregating local gradient information from overlapping samples. By integrating TGAM with momentum-based attack algorithms, we ensure strict temporal consistency while fully utilizing series-level gradient information to explore the adversarial perturbation space. Comprehensive experiments on three benchmark datasets and four representative state-of-the-art models demonstrate that our proposed method significantly outperforms baselines in both white-box and black-box transfer attack scenarios under TUAP constraints. Moreover, our method also exhibits superior transfer attack performance even without TUAP constraints, demonstrating its effectiveness and superiority in generating adversarial perturbations for time series forecasting models.

