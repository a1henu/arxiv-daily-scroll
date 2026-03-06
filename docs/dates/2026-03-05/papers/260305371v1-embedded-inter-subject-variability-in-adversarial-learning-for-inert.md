---
layout: default
title: Embedded Inter-Subject Variability in Adversarial Learning for Inertial Sensor-Based Human Activity Recognition
---

# Embedded Inter-Subject Variability in Adversarial Learning for Inertial Sensor-Based Human Activity Recognition
**arXiv**：[2603.05371v1](https://arxiv.org/abs/2603.05371) · [PDF](https://arxiv.org/pdf/2603.05371.pdf)  
**作者**：Francisco M. Calatrava-Nicolás, Shoko Miyauchi, Vitor Fortes Rey, Paul Lukowicz, Todor Stoyanov, Oscar Martinez Mozos  

**一句话要点**：提出嵌入主体间变异的对抗学习框架，以提升惯性传感器人体活动识别的泛化性能

**关键词**：人体活动识别, 惯性传感器, 对抗学习, 主体间变异, 特征表示, 泛化性能

## 3 点简述
- 核心问题：人体活动识别中主体间变异导致模型对新个体泛化能力差
- 方法要点：通过对抗任务集成主体间变异，鼓励主体不变特征表示
- 实验或效果：在三个数据集上使用留一主体交叉验证，性能优于先前方法

## 摘要（原文）

> This paper addresses the problem of Human Activity Recognition (HAR) using data from wearable inertial sensors. An important challenge in HAR is the model's generalization capabilities to new unseen individuals due to inter-subject variability, i.e., the same activity is performed differently by different individuals. To address this problem, we propose a novel deep adversarial framework that integrates the concept of inter-subject variability in the adversarial task, thereby encouraging subject-invariant feature representations and enhancing the classification performance in the HAR problem. Our approach outperforms previous methods in three well-established HAR datasets using a leave-one-subject-out (LOSO) cross-validation. Further results indicate that our proposed adversarial task effectively reduces inter-subject variability among different users in the feature space, and it outperforms adversarial tasks from previous works when integrated into our framework. Code: https://github.com/FranciscoCalatrava/EmbeddedSubjectVariability.git

