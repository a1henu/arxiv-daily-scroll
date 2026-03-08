---
layout: default
title: KindSleep: Knowledge-Informed Diagnosis of Obstructive Sleep Apnea from Oximetry
---

# KindSleep: Knowledge-Informed Diagnosis of Obstructive Sleep Apnea from Oximetry
**arXiv**：[2603.04755v1](https://arxiv.org/abs/2603.04755) · [PDF](https://arxiv.org/pdf/2603.04755.pdf)  
**作者**：Micky C Nnamdi, Wenqi Shi, Cheng Wan, J. Ben Tamo, Benjamin M Smith, Chad A Purnell, May D Wang  

**一句话要点**：提出KindSleep框架，结合临床知识与深度学习，从血氧信号诊断阻塞性睡眠呼吸暂停。

**关键词**：阻塞性睡眠呼吸暂停诊断, 深度学习框架, 血氧信号分析, 临床知识融合, 多模态数据, 呼吸暂停低通气指数估计

## 3 点简述
- 核心问题：传统多导睡眠图诊断资源密集，需高效替代方案以提升可及性。
- 方法要点：从原始血氧信号学习临床可解释概念，融合多模态数据估计呼吸暂停低通气指数。
- 实验或效果：在三个大型数据集上验证，性能优异，R2达0.917，加权F1分数最高0.941。

## 摘要（原文）

> Obstructive sleep apnea (OSA) is a sleep disorder that affects nearly one billion people globally and significantly elevates cardiovascular risk. Traditional diagnosis through polysomnography is resource-intensive and limits widespread access, creating a critical need for accurate and efficient alternatives. In this paper, we introduce KindSleep, a deep learning framework that integrates clinical knowledge with single-channel patient-specific oximetry signals and clinical data for precise OSA diagnosis. KindSleep first learns to identify clinically interpretable concepts, such as desaturation indices and respiratory disturbance events, directly from raw oximetry signals. It then fuses these AI-derived concepts with multimodal clinical data to estimate the Apnea-Hypopnea Index (AHI). We evaluate KindSleep on three large, independent datasets from the National Sleep Research Resource (SHHS, CFS, MrOS; total n = 9,815). KindSleep demonstrates excellent performance in estimating AHI scores (R2 = 0.917, ICC = 0.957) and consistently outperforms existing approaches in classifying OSA severity, achieving weighted F1-scores from 0.827 to 0.941 across diverse populations. By grounding its predictions in a layer of clinically meaningful concepts, KindSleep provides a more transparent and trustworthy diagnostic tool for sleep medicine practices.

