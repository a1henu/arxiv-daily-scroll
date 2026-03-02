---
layout: default
title: Inferring Chronic Treatment Onset from ePrescription Data: A Renewal Process Approach
---

# Inferring Chronic Treatment Onset from ePrescription Data: A Renewal Process Approach
**arXiv**：[2602.23824v1](https://arxiv.org/abs/2602.23824) · [PDF](https://arxiv.org/pdf/2602.23824.pdf)  
**作者**：Pavlin G. Poličar, Dalibor Stanimirović, Blaž Zupan  

**一句话要点**：提出基于更新过程的概率框架，从电子处方数据推断慢性治疗起始时间

**关键词**：电子处方数据, 更新过程, 变点检测, 慢性治疗推断, 概率建模, 左截断处理

## 3 点简述
- 问题：电子健康记录左截断导致疾病起始诊断不可靠，需从处方轨迹推断慢性治疗起始
- 方法：建模处方动态为更新过程，通过变点检测区分偶发与持续治疗，使用泊松-威布尔模型
- 效果：在240万人数据集上，相比基于规则方法，减少左截断下的早期误检，性能随处方密度变化

## 摘要（原文）

> Longitudinal electronic health record (EHR) data are often left-censored, making diagnosis records incomplete and unreliable for determining disease onset. In contrast, outpatient prescriptions form renewal-based trajectories that provide a continuous signal of disease management. We propose a probabilistic framework to infer chronic treatment onset by modeling prescription dynamics as a renewal process and detecting transitions from sporadic to sustained therapy via change-point detection between a baseline Poisson (sporadic prescribing) regime and a regime-specific Weibull (sustained therapy) renewal model. Using a nationwide ePrescription dataset of 2.4 million individuals, we show that the approach yields more temporally plausible onset estimates than naive rule-based triggering, substantially reducing implausible early detections under strong left censoring. Detection performance varies across diseases and is strongly associated with prescription density, highlighting both the strengths and limits of treatment-based onset inference.

