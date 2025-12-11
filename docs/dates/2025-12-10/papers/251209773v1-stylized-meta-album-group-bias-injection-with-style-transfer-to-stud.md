---
layout: default
title: Stylized Meta-Album: Group-bias injection with style transfer to study robustness against distribution shifts
---

# Stylized Meta-Album: Group-bias injection with style transfer to study robustness against distribution shifts
**arXiv**：[2512.09773v1](https://arxiv.org/abs/2512.09773) · [PDF](https://arxiv.org/pdf/2512.09773.pdf)  
**作者**：Romain Mussard, Aurélien Gauffre, Ihsan Ullah, Thanh Gia Hieu Khuong, Massih-Reza Amini, Isabelle Guyon, Lisheng Sun-Hosoya  

**一句话要点**：提出Stylized Meta-Album元数据集，通过风格迁移注入组偏差以研究分布偏移下的鲁棒性

**关键词**：风格迁移, 分布外泛化, 元数据集, 组公平性, 无监督域适应, 图像分类

## 3 点简述
- 核心问题：现实数据收集难以覆盖广泛组多样性，影响分布外泛化与公平性研究
- 方法要点：使用风格迁移技术从12个内容数据集生成12个风格化数据集，构建4800个可配置组
- 实验效果：创建OOD泛化与无监督域适应基准，显示增加组多样性显著改变算法公平性排名

## 摘要（原文）

> We introduce Stylized Meta-Album (SMA), a new image classification meta-dataset comprising 24 datasets (12 content datasets, and 12 stylized datasets), designed to advance studies on out-of-distribution (OOD) generalization and related topics. Created using style transfer techniques from 12 subject classification datasets, SMA provides a diverse and extensive set of 4800 groups, combining various subjects (objects, plants, animals, human actions, textures) with multiple styles. SMA enables flexible control over groups and classes, allowing us to configure datasets to reflect diverse benchmark scenarios. While ideally, data collection would capture extensive group diversity, practical constraints often make this infeasible. SMA addresses this by enabling large and configurable group structures through flexible control over styles, subject classes, and domains-allowing datasets to reflect a wide range of real-world benchmark scenarios. This design not only expands group and class diversity, but also opens new methodological directions for evaluating model performance across diverse group and domain configurations-including scenarios with many minority groups, varying group imbalance, and complex domain shifts-and for studying fairness, robustness, and adaptation under a broader range of realistic conditions. To demonstrate SMA's effectiveness, we implemented two benchmarks: (1) a novel OOD generalization and group fairness benchmark leveraging SMA's domain, class, and group diversity to evaluate existing benchmarks. Our findings reveal that while simple balancing and algorithms utilizing group information remain competitive as claimed in previous benchmarks, increasing group diversity significantly impacts fairness, altering the superiority and relative rankings of algorithms. We also propose to use \textit{Top-M worst group accuracy} as a new hyperparameter tuning metric, demonstrating broader fairness during optimization and delivering better final worst-group accuracy for larger group diversity. (2) An unsupervised domain adaptation (UDA) benchmark utilizing SMA's group diversity to evaluate UDA algorithms across more scenarios, offering a more comprehensive benchmark with lower error bars (reduced by 73\% and 28\% in closed-set setting and UniDA setting, respectively) compared to existing efforts. These use cases highlight SMA's potential to significantly impact the outcomes of conventional benchmarks.

