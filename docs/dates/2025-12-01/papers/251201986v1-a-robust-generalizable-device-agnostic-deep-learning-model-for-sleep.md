---
layout: default
title: A robust generalizable device-agnostic deep learning model for sleep-wake determination from triaxial wrist accelerometry
---

# A robust generalizable device-agnostic deep learning model for sleep-wake determination from triaxial wrist accelerometry
**arXiv**：[2512.01986v1](https://arxiv.org/abs/2512.01986) · [PDF](https://arxiv.org/pdf/2512.01986.pdf)  
**作者**：Nasim Montazeri, Stone Yang, Dominik Luszczynski, John Zhang, Dharmendra Gurve, Andrew Centen, Maged Goubran, Andrew Lim  

**一句话要点**：提出一种鲁棒通用的深度学习模型，用于从三轴腕部加速度计数据中检测睡眠-觉醒状态。

**关键词**：睡眠-觉醒检测, 腕部加速度计, 深度学习模型, 跨设备泛化, 睡眠障碍

## 3 点简述
- 核心问题：现有方法在觉醒检测、跨设备泛化及不同年龄和睡眠障碍验证方面表现不佳。
- 方法要点：基于三轴加速度计特征，训练3类模型并决策树整合，增强觉醒检测。
- 实验或效果：在453名成人中验证，模型性能稳健，F1分数0.86，跨设备一致。

## 摘要（原文）

> Study Objectives: Wrist accelerometry is widely used for inferring sleep-wake state. Previous works demonstrated poor wake detection, without cross-device generalizability and validation in different age range and sleep disorders. We developed a robust deep learning model for to detect sleep-wakefulness from triaxial accelerometry and evaluated its validity across three devices and in a large adult population spanning a wide range of ages with and without sleep disorders. Methods: We collected wrist accelerometry simultaneous to polysomnography (PSG) in 453 adults undergoing clinical sleep testing at a tertiary care sleep laboratory, using three devices. We extracted features in 30-second epochs and trained a 3-class model to detect wake, sleep, and sleep with arousals, which was then collapsed into wake vs. sleep using a decision tree. To enhance wake detection, the model was specifically trained on randomly selected subjects with low sleep efficiency and/or high arousal index from one device recording and then tested on the remaining recordings. Results: The model showed high performance with F1 Score of 0.86, sensitivity (sleep) of 0.87, and specificity (wakefulness) of 0.78, and significant and moderate correlation to PSG in predicting total sleep time (R=0.69) and sleep efficiency (R=0.63). Model performance was robust to the presence of sleep disorders, including sleep apnea and periodic limb movements in sleep, and was consistent across all three models of accelerometer. Conclusions: We present a deep model to detect sleep-wakefulness from actigraphy in adults with relative robustness to the presence of sleep disorders and generalizability across diverse commonly used wrist accelerometers.

