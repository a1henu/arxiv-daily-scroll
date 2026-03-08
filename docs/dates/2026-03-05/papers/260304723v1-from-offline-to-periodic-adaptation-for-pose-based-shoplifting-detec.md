---
layout: default
title: From Offline to Periodic Adaptation for Pose-Based Shoplifting Detection in Real-world Retail Security
---

# From Offline to Periodic Adaptation for Pose-Based Shoplifting Detection in Real-world Retail Security
**arXiv**：[2603.04723v1](https://arxiv.org/abs/2603.04723) · [PDF](https://arxiv.org/pdf/2603.04723.pdf)  
**作者**：Shanle Yao, Narges Rashvand, Armin Danesh Pazho, Hamed Tabkhi  

**一句话要点**：提出周期性适应框架，基于姿态检测实现零售安防中的实时盗窃检测。

**关键词**：姿态检测, 视频异常检测, 周期性适应, 边缘计算, 零售安防, 无监督学习

## 3 点简述
- 核心问题：零售盗窃频发，传统视频监控依赖人工，需自动化、隐私保护且资源高效的检测方案。
- 方法要点：将盗窃检测视为基于姿态的无监督视频异常检测，引入周期性适应框架，支持边缘设备从流式无标签数据中自适应学习。
- 实验或效果：在RetailS数据集上，框架在91.6%评估中优于离线基线，AUC-ROC和AUC-PR表现更佳，边缘硬件训练更新<30分钟。

## 摘要（原文）

> Shoplifting is a growing operational and economic challenge for retailers, with incidents rising and losses increasing despite extensive video surveillance. Continuous human monitoring is infeasible, motivating automated, privacy-preserving, and resource-aware detection solutions. In this paper, we cast shoplifting detection as a pose-based, unsupervised video anomaly detection problem and introduce a periodic adaptation framework designed for on-site Internet of Things (IoT) deployment. Our approach enables edge devices in smart retail environments to adapt from streaming, unlabeled data, supporting scalable and low-latency anomaly detection across distributed camera networks. To support reproducibility, we introduce RetailS, a new large-scale real-world shoplifting dataset collected from a retail store under multi-day, multi-camera conditions, capturing unbiased shoplifting behavior in realistic IoT settings. For deployable operation, thresholds are selected using both F1 and H_PRS scores, the harmonic mean of precision, recall, and specificity, during data filtering and training. In periodic adaptation experiments, our framework consistently outperformed offline baselines on AUC-ROC and AUC-PR in 91.6% of evaluations, with each training update completing in under 30 minutes on edge-grade hardware, demonstrating the feasibility and reliability of our solution for IoT-enabled smart retail deployment.

