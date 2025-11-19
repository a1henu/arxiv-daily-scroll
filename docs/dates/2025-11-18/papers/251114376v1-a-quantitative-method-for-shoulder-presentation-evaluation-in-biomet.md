---
layout: default
title: A Quantitative Method for Shoulder Presentation Evaluation in Biometric Identity Documents
---

# A Quantitative Method for Shoulder Presentation Evaluation in Biometric Identity Documents
**arXiv**：[2511.14376v1](https://arxiv.org/abs/2511.14376) · [PDF](https://arxiv.org/pdf/2511.14376.pdf)  
**作者**：Alfonso Pedro Ridao  

**一句话要点**：提出肩部姿态评估算法以解决生物识别证件中肩部姿态自动合规检查问题

**关键词**：生物识别证件, 姿态评估, 肩部姿态, 合规检查, 自动化质量评估

## 3 点简述
- 生物识别证件标准要求肩部方正姿态，但缺乏自动化定量评估方法
- 算法使用两个肩部标志点的3D坐标量化肩部偏转和滚动角度
- 在121张肖像图像数据集上验证，与人工标签强相关，过滤性能良好

## 摘要（原文）

> International standards for biometric identity documents mandate strict compliance with pose requirements, including the square presentation of a subject's shoulders. However, the literature on automated quality assessment offers few quantitative methods for evaluating this specific attribute. This paper proposes a Shoulder Presentation Evaluation (SPE) algorithm to address this gap. The method quantifies shoulder yaw and roll using only the 3D coordinates of two shoulder landmarks provided by common pose estimation frameworks. The algorithm was evaluated on a dataset of 121 portrait images. The resulting SPE scores demonstrated a strong Pearson correlation (r approx. 0.80) with human-assigned labels. An analysis of the metric's filtering performance, using an adapted Error-versus-Discard methodology, confirmed its utility in identifying non-compliant samples. The proposed algorithm is a viable lightweight tool for automated compliance checking in enrolment systems.

