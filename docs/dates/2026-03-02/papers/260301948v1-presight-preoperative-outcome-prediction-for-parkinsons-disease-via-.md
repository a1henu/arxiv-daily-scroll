---
layout: default
title: PreSight: Preoperative Outcome Prediction for Parkinson's Disease via Region-Prior Morphometry and Patient-Specific Weighting
---

# PreSight: Preoperative Outcome Prediction for Parkinson's Disease via Region-Prior Morphometry and Patient-Specific Weighting
**arXiv**：[2603.01948v1](https://arxiv.org/abs/2603.01948) · [PDF](https://arxiv.org/pdf/2603.01948.pdf)  
**作者**：Yand Wang, Chen Zhang, Lanyun Zhu, Yixin Chen, Qunbo Wang, Yutong Bai, Jurgen Germann, Yinghong Wen, Shuai Shao  

**一句话要点**：提出PreSight模型，通过区域先验形态测量和患者特异性加权，预测帕金森病术前手术改善率。

**关键词**：帕金森病术前预测, 变形形态测量, 患者特异性加权, 多模态融合, 决策支持系统

## 3 点简述
- 核心问题：帕金森病术前改善率预测困难，因影像信号细微且患者异质性高。
- 方法要点：融合临床先验与术前MRI和变形形态测量，通过患者特异性加权模块自适应区域重要性。
- 实验或效果：在400名患者的两中心队列中，优于基线方法，内部验证准确率88.89%，外部测试85.29%。

## 摘要（原文）

> Preoperative improvement rate prediction for Parkinson's disease surgery is clinically important yet difficult because imaging signals are subtle and patients are heterogeneous. We address this setting, where only information available before surgery is used, and the goal is to predict patient-specific postoperative motor benefit. We present PreSight, a presurgical outcome model that fuses clinical priors with preoperative MRI and deformation-based morphometry (DBM) and adapts regional importance through a patient-specific weighting module. The model produces end-to-end, calibrated, decision-ready predictions with patient-level explanations. We evaluate PreSight on a real-world two-center cohort of 400 subjects with multimodal presurgical inputs and postoperative improvement labels. PreSight outperforms strong clinical, imaging-only, and multimodal baselines. It attains 88.89% accuracy on internal validation and 85.29% on an external-center test for responder classification and shows better probability calibration and higher decision-curve net benefit. Ablations and analyses confirm the contribution of DBM and the patient-specific weighting module and indicate that the model emphasizes disease-relevant regions in a patient-specific manner. These results demonstrate that integrating clinical prior knowledge with region-adaptive morphometry enables reliable presurgical decision support in routine practice.

