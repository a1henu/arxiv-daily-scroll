---
layout: default
title: Automated Estimation of Anatomical Risk Metrics for Endoscopic Sinus Surgery Using Deep Learning
---

# Automated Estimation of Anatomical Risk Metrics for Endoscopic Sinus Surgery Using Deep Learning
**arXiv**：[2511.07199v1](https://arxiv.org/abs/2511.07199) · [PDF](https://arxiv.org/pdf/2511.07199.pdf)  
**作者**：Konrad Reuter, Lennart Thaysen, Bilkay Doruk, Sarah Latus, Brigitte Holst, Benjamin Becker, Dennis Eggert, Christian Betz, Anna-Sophie Hoffmann, Alexander Schlaefer  

**一句话要点**：提出自动化深度学习管道以估计内窥镜鼻窦手术的解剖风险评分

**关键词**：内窥镜鼻窦手术, 解剖风险评分, 深度学习, 热图回归, CT扫描, 自动化评估

## 3 点简述
- 核心问题：内窥镜鼻窦手术需术前评估颅底解剖风险，手动测量耗时且繁琐。
- 方法要点：通过热图回归定位关键解剖标志，自动估计Keros、Gera和TMS风险评分。
- 实验或效果：在相关测量中，平均绝对误差分别为0.506mm、4.516°和0.802mm/0.777mm。

## 摘要（原文）

> Endoscopic sinus surgery requires careful preoperative assessment of the
> skull base anatomy to minimize risks such as cerebrospinal fluid leakage.
> Anatomical risk scores like the Keros, Gera and Thailand-Malaysia-Singapore
> score offer a standardized approach but require time-consuming manual
> measurements on coronal CT or CBCT scans. We propose an automated deep learning
> pipeline that estimates these risk scores by localizing key anatomical
> landmarks via heatmap regression. We compare a direct approach to a specialized
> global-to-local learning strategy and find mean absolute errors on the relevant
> anatomical measurements of 0.506mm for the Keros, 4.516{\deg} for the Gera and
> 0.802mm / 0.777mm for the TMS classification.

