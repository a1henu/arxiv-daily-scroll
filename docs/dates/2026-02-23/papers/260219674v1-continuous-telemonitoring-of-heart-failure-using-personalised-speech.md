---
layout: default
title: Continuous Telemonitoring of Heart Failure using Personalised Speech Dynamics
---

# Continuous Telemonitoring of Heart Failure using Personalised Speech Dynamics
**arXiv**：[2602.19674v1](https://arxiv.org/abs/2602.19674) · [PDF](https://arxiv.org/pdf/2602.19674.pdf)  
**作者**：Yue Pan, Xingyao Wang, Hanyue Zhang, Liwei Liu, Changxin Li, Gang Yang, Rong Sheng, Yili Xia, Ming Chu  

**一句话要点**：提出纵向患者内追踪方案，通过个性化序列编码器提升远程心衰监测准确性。

**关键词**：远程心衰监测, 语音信号分析, 个性化建模, 纵向追踪, 序列编码器

## 3 点简述
- 核心问题：传统跨患者分类模型因个体语音差异大，在心衰远程监测中准确性受限。
- 方法要点：设计个性化序列编码器，利用历史语音数据捕捉个体症状变化的相对轨迹。
- 实验或效果：在225名患者数据上，模型对临床状态转换的识别准确率达99.7%，优于传统方法。

## 摘要（原文）

> Remote monitoring of heart failure (HF) via speech signals provides a non-invasive and cost-effective solution for long-term patient management. However, substantial inter-individual heterogeneity in vocal characteristics often limits the accuracy of traditional cross-sectional classification models. To address this, we propose a Longitudinal Intra-Patient Tracking (LIPT) scheme designed to capture the trajectory of relative symptomatic changes within individuals. Central to this framework is a Personalised Sequential Encoder (PSE), which transforms longitudinal speech recordings into context-aware latent representations. By incorporating historical data at each timestamp, the PSE facilitates a holistic assessment of the clinical trajectory rather than modelling discrete visits independently. Experimental results from a cohort of 225 patients demonstrate that the LIPT paradigm significantly outperforms the classic cross-sectional approaches, achieving a recognition accuracy of 99.7% for clinical status transitions. The model's high sensitivity was further corroborated by additional follow-up data, confirming its efficacy in predicting HF deterioration and its potential to secure patient safety in remote, home-based settings. Furthermore, this work addresses the gap in existing literature by providing a comprehensive analysis of different speech task designs and acoustic features. Taken together, the superior performance of the LIPT framework and PSE architecture validates their readiness for integration into long-term telemonitoring systems, offering a scalable solution for remote heart failure management.

