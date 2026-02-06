---
layout: default
title: Faithful Bi-Directional Model Steering via Distribution Matching and Distributed Interchange Interventions
---

# Faithful Bi-Directional Model Steering via Distribution Matching and Distributed Interchange Interventions
**arXiv**：[2602.05234v1](https://arxiv.org/abs/2602.05234) · [PDF](https://arxiv.org/pdf/2602.05234.pdf)  
**作者**：Yuntai Bao, Xuhong Zhang, Jintao Chen, Ge Su, Yuxiang Cai, Hao Peng, Bing Sun, Haiqin Weng, Liu Yan, Jianwei Yin  

**一句话要点**：提出概念分布式对齐搜索以通过分布匹配和分布式互换干预实现忠实双向模型操控

**关键词**：模型操控, 分布式对齐搜索, 分布匹配, 干预学习, 双向控制, 安全对齐

## 3 点简述
- 当前基于干预的模型操控方法易过拟合且输出不自然，因过度依赖外部偏好而非内部机制识别
- CDAS采用分布式互换干预，通过分布匹配目标对齐干预输出与反事实分布，实现弱监督学习
- 在安全相关案例中，CDAS能系统操控模型如覆盖拒绝行为，同时保持模型通用效用

## 摘要（原文）

> Intervention-based model steering offers a lightweight and interpretable alternative to prompting and fine-tuning. However, by adapting strong optimization objectives from fine-tuning, current methods are susceptible to overfitting and often underperform, sometimes generating unnatural outputs. We hypothesize that this is because effective steering requires the faithful identification of internal model mechanisms, not the enforcement of external preferences. To this end, we build on the principles of distributed alignment search (DAS), the standard for causal variable localization, to propose a new steering method: Concept DAS (CDAS). While we adopt the core mechanism of DAS, distributed interchange intervention (DII), we introduce a novel distribution matching objective tailored for the steering task by aligning intervened output distributions with counterfactual distributions. CDAS differs from prior work in two main ways: first, it learns interventions via weak-supervised distribution matching rather than probability maximization; second, it uses DIIs that naturally enable bi-directional steering and allow steering factors to be derived from data, reducing the effort required for hyperparameter tuning and resulting in more faithful and stable control. On AxBench, a large-scale model steering benchmark, we show that CDAS does not always outperform preference-optimization methods but may benefit more from increased model scale. In two safety-related case studies, overriding refusal behaviors of safety-aligned models and neutralizing a chain-of-thought backdoor, CDAS achieves systematic steering while maintaining general model utility. These results indicate that CDAS is complementary to preference-optimization approaches and conditionally constitutes a robust approach to intervention-based model steering. Our code is available at https://github.com/colored-dye/concept_das.

