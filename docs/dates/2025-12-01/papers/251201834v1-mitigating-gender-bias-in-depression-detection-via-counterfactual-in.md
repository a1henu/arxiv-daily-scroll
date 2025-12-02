---
layout: default
title: Mitigating Gender Bias in Depression Detection via Counterfactual Inference
---

# Mitigating Gender Bias in Depression Detection via Counterfactual Inference
**arXiv**：[2512.01834v1](https://arxiv.org/abs/2512.01834) · [PDF](https://arxiv.org/pdf/2512.01834.pdf)  
**作者**：Mingxuan Hu, Hongbo Ma, Xinlan Wu, Ziqi Liu, Jiaqi Liu, Yangbin Chen  

**一句话要点**：提出基于反事实推理的因果去偏框架，以缓解音频抑郁检测中的性别偏见。

**关键词**：音频抑郁检测, 性别偏见缓解, 因果推理, 反事实推理, 公平性, 声学特征

## 3 点简述
- 核心问题：音频抑郁检测模型因训练数据性别不平衡，学习到性别与抑郁的虚假关联，导致对女性过诊断、男性诊断不足。
- 方法要点：构建因果图建模决策过程，识别性别对预测的直接因果效应，通过反事实推理估计并减去该效应，使模型依赖真实声学病理特征。
- 实验或效果：在DAIC-WOZ数据集上使用两种先进声学骨干网络，实验表明框架显著降低性别偏见，并提升整体检测性能优于现有去偏策略。

## 摘要（原文）

> Audio-based depression detection models have demonstrated promising performance but often suffer from gender bias due to imbalanced training data. Epidemiological statistics show a higher prevalence of depression in females, leading models to learn spurious correlations between gender and depression. Consequently, models tend to over-diagnose female patients while underperforming on male patients, raising significant fairness concerns. To address this, we propose a novel Counterfactual Debiasing Framework grounded in causal inference. We construct a causal graph to model the decision-making process and identify gender bias as the direct causal effect of gender on the prediction. During inference, we employ counterfactual inference to estimate and subtract this direct effect, ensuring the model relies primarily on authentic acoustic pathological features. Extensive experiments on the DAIC-WOZ dataset using two advanced acoustic backbones demonstrate that our framework not only significantly reduces gender bias but also improves overall detection performance compared to existing debiasing strategies.

