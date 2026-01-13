---
layout: default
title: Neural Architecture for Fast and Reliable Coagulation Assessment in Clinical Settings: Leveraging Thromboelastography
---

# Neural Architecture for Fast and Reliable Coagulation Assessment in Clinical Settings: Leveraging Thromboelastography
**arXiv**：[2601.07618v1](https://arxiv.org/abs/2601.07618) · [PDF](https://arxiv.org/pdf/2601.07618.pdf)  
**作者**：Yulu Wang, Ziqian Zeng, Jianjun Wu, Zhifeng Tang  

**一句话要点**：提出生理状态重建算法以加速临床凝血评估，基于小数据集实现高精度预测。

**关键词**：血栓弹力图, 小样本学习, 时序信号处理, 医疗AI, 生理状态重建

## 3 点简述
- 核心问题：传统血栓弹力图需近1小时测量，延迟可能导致死亡率上升，且小数据集下深度学习性能不佳。
- 方法要点：设计PSR算法，利用MDFE整合多域信号，HLA学习高层时序交互，DAM保持体征稳定性。
- 实验或效果：在4个TEG数据集上，凝血特征预测R2>0.98，误差减半，推理时间减半。

## 摘要（原文）

> In an ideal medical environment, real-time coagulation monitoring can enable early detection and prompt remediation of risks. However, traditional Thromboelastography (TEG), a widely employed diagnostic modality, can only provide such outputs after nearly 1 hour of measurement. The delay might lead to elevated mortality rates. These issues clearly point out one of the key challenges for medical AI development: Mak-ing reasonable predictions based on very small data sets and accounting for variation between different patient populations, a task where conventional deep learning methods typically perform poorly. We present Physiological State Reconstruc-tion (PSR), a new algorithm specifically designed to take ad-vantage of dynamic changes between individuals and to max-imize useful information produced by small amounts of clini-cal data through mapping to reliable predictions and diagnosis. We develop MDFE to facilitate integration of varied temporal signals using multi-domain learning, and jointly learn high-level temporal interactions together with attentions via HLA; furthermore, the parameterized DAM we designed maintains the stability of the computed vital signs. PSR evaluates with 4 TEG-specialized data sets and establishes remarkable perfor-mance -- predictions of R2 > 0.98 for coagulation traits and error reduction around half compared to the state-of-the-art methods, and halving the inferencing time too. Drift-aware learning suggests a new future, with potential uses well be-yond thrombophilia discovery towards medical AI applica-tions with data scarcity.

