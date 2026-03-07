---
layout: default
title: MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis
---

# MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis
**arXiv**：[2603.05421v1](https://arxiv.org/abs/2603.05421) · [PDF](https://arxiv.org/pdf/2603.05421.pdf)  
**作者**：Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub  

**一句话要点**：提出选择性排斥知识蒸馏以在移动胎儿超声分析中解决极端容量差距问题

**关键词**：知识蒸馏, 胎儿超声分析, 移动AI部署, 对比学习, 模型压缩, 实时处理

## 3 点简述
- 核心问题：胎儿超声AI模型参数过大（超300M），无法部署在资源受限的移动设备上，标准知识蒸馏在约26倍容量差距下失效。
- 方法要点：引入选择性排斥知识蒸馏，分解对比知识蒸馏为对角和非对角成分，通过负权重排斥学生模型模仿教师模型的类间混淆，促使其发现架构原生特征。
- 实验或效果：11.4M参数学生模型在零样本HC18生物测量有效性和脑亚平面F1上超越304M参数教师模型，并在iPhone 16 Pro上以1.6毫秒运行，实现实时辅助AI。

## 摘要（原文）

> Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair alignment is preserved while the off-diagonal weight decays into negative values, repelling the student from the teacher's inter-class confusions and forcing discovery of architecturally native features. Our 11.4M parameter student surpasses the 304M-parameter FetalCLIP teacher on zero-shot HC18 biometry validity (88.6% vs. 83.5%) and brain sub-plane F1 (0.784 vs. 0.702), while running at 1.6 ms on iPhone 16 Pro, enabling real-time assistive AI on handheld ultrasound devices. Our code, models, and app are publicly available at https://github.com/numanai/MobileFetalCLIP.

