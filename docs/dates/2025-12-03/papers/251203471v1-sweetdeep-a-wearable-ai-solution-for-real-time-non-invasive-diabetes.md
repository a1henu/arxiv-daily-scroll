---
layout: default
title: SweetDeep: A Wearable AI Solution for Real-Time Non-Invasive Diabetes Screening
---

# SweetDeep: A Wearable AI Solution for Real-Time Non-Invasive Diabetes Screening
**arXiv**：[2512.03471v1](https://arxiv.org/abs/2512.03471) · [PDF](https://arxiv.org/pdf/2512.03471.pdf)  
**作者**：Ian Henriques, Lynda Elhassar, Sarvesh Relekar, Denis Walrave, Shayan Hassantabar, Vishu Ghanakota, Adel Laoui, Mahmoud Aich, Rafia Tir, Mohamed Zerguine, Samir Louafi, Moncef Kimouche, Emmanuel Cosson, Niraj K Jha  

**一句话要点**：提出SweetDeep，一种基于可穿戴设备的轻量神经网络，用于实时非侵入性2型糖尿病筛查。

**关键词**：可穿戴设备, 糖尿病筛查, 轻量神经网络, 实时检测, 非侵入性监测

## 3 点简述
- 核心问题：全球2型糖尿病增长需可扩展、低成本筛查方法，现有生化检测侵入性强且昂贵。
- 方法要点：使用三星Galaxy Watch 7在自由生活条件下收集285名参与者的生理和人口数据，训练少于3000参数的紧凑神经网络。
- 实验或效果：在三折交叉验证中达到82.5%患者级准确率，允许模型在低置信度预测上弃权后，剩余患者准确率提升至84.5%。

## 摘要（原文）

> The global rise in type 2 diabetes underscores the need for scalable and cost-effective screening methods. Current diagnosis requires biochemical assays, which are invasive and costly. Advances in consumer wearables have enabled early explorations of machine learning-based disease detection, but prior studies were limited to controlled settings. We present SweetDeep, a compact neural network trained on physiological and demographic data from 285 (diabetic and non-diabetic) participants in the EU and MENA regions, collected using Samsung Galaxy Watch 7 devices in free-living conditions over six days. Each participant contributed multiple 2-minute sensor recordings per day, totaling approximately 20 recordings per individual. Despite comprising fewer than 3,000 parameters, SweetDeep achieves 82.5% patient-level accuracy (82.1% macro-F1, 79.7% sensitivity, 84.6% specificity) under three-fold cross-validation, with an expected calibration error of 5.5%. Allowing the model to abstain on less than 10% of low-confidence patient predictions yields an accuracy of 84.5% on the remaining patients. These findings demonstrate that combining engineered features with lightweight architectures can support accurate, rapid, and generalizable detection of type 2 diabetes in real-world wearable settings.

