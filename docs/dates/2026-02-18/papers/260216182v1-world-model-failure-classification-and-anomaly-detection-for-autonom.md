---
layout: default
title: World Model Failure Classification and Anomaly Detection for Autonomous Inspection
---

# World Model Failure Classification and Anomaly Detection for Autonomous Inspection
**arXiv**：[2602.16182v1](https://arxiv.org/abs/2602.16182) · [PDF](https://arxiv.org/pdf/2602.16182.pdf)  
**作者**：Michelle Ho, Muhammad Fadhil Ginting, Isaac R. Ward, Andrzej Reinke, Mykel J. Kochenderfer, Ali-akbar Agha-Mohammadi, Shayegan Omidshafiei  

**一句话要点**：提出结合监督分类与异常检测的混合框架，用于自主巡检中的世界模型故障分类与异常检测。

**关键词**：自主巡检, 世界模型, 故障分类, 异常检测, 保形预测, 实时部署

## 3 点简述
- 核心问题：自主巡检机器人因遮挡、视角限制或环境变化导致读数不准确，需区分成功、已知故障和异常情况。
- 方法要点：使用世界模型骨干处理压缩视频输入，基于保形预测阈值设置决策函数，实现策略无关和无分布的分类。
- 实验或效果：在办公室和工业现场仪表巡检数据上评估，实时部署于波士顿动力Spot，分类准确率超90%，早于人类观察者。

## 摘要（原文）

> Autonomous inspection robots for monitoring industrial sites can reduce costs and risks associated with human-led inspection. However, accurate readings can be challenging due to occlusions, limited viewpoints, or unexpected environmental conditions. We propose a hybrid framework that combines supervised failure classification with anomaly detection, enabling classification of inspection tasks as a success, known failure, or anomaly (i.e., out-of-distribution) case. Our approach uses a world model backbone with compressed video inputs. This policy-agnostic, distribution-free framework determines classifications based on two decision functions set by conformal prediction (CP) thresholds before a human observer does. We evaluate the framework on gauge inspection feeds collected from office and industrial sites and demonstrate real-time deployment on a Boston Dynamics Spot. Experiments show over 90% accuracy in distinguishing between successes, failures, and OOD cases, with classifications occurring earlier than a human observer. These results highlight the potential for robust, anticipatory failure detection in autonomous inspection tasks or as a feedback signal for model training to assess and improve the quality of training data. Project website: https://autoinspection-classification.github.io

