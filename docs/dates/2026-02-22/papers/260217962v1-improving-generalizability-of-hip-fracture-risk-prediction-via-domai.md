---
layout: default
title: Improving Generalizability of Hip Fracture Risk Prediction via Domain Adaptation Across Multiple Cohorts
---

# Improving Generalizability of Hip Fracture Risk Prediction via Domain Adaptation Across Multiple Cohorts
**arXiv**：[2602.17962v1](https://arxiv.org/abs/2602.17962) · [PDF](https://arxiv.org/pdf/2602.17962.pdf)  
**作者**：Shuo Sun, Meiling Zhou, Chen Zhao, Joyce H. Keyak, Nancy E. Lane, Jeffrey D. Deng, Kuan-Jui Su, Hui Shen, Hong-Wen Deng, Kui Zhang, Weihua Zhou  

**一句话要点**：提出多域适应方法组合以提升跨队列髋部骨折风险预测的泛化性

**关键词**：域适应, 髋部骨折风险预测, 跨队列泛化, 最大均值差异, 相关对齐, 对抗神经网络

## 3 点简述
- 临床风险预测模型常因数据分布差异而泛化不佳，尤其在髋部骨折风险预测中。
- 系统评估了MMD、CORAL和DANN等域适应方法及其组合，在三个大型队列上进行实验。
- 组合方法在仅男性或仅女性源队列中实现最高AUC（0.88和0.95），无需目标队列标签即可提升泛化性。

## 摘要（原文）

> Clinical risk prediction models often fail to be generalized across cohorts because underlying data distributions differ by clinical site, region, demographics, and measurement protocols. This limitation is particularly pronounced in hip fracture risk prediction, where the performance of models trained on one cohort (the source cohort) can degrade substantially when deployed in other cohorts (target cohorts). We used a shared set of clinical and DXA-derived features across three large cohorts - the Study of Osteoporotic Fractures (SOF), the Osteoporotic Fractures in Men Study (MrOS), and the UK Biobank (UKB), to systematically evaluate the performance of three domain adaptation methods - Maximum Mean Discrepancy (MMD), Correlation Alignment (CORAL), and Domain - Adversarial Neural Networks (DANN) and their combinations. For a source cohort with males only and a source cohort with females only, domain-adaptation methods consistently showed improved performance than the no-adaptation baseline (source-only training), and the use of combinations of multiple domain adaptation methods delivered the largest and most stable gains. The method that combines MMD, CORAL, and DANN achieved the highest discrimination with the area under curve (AUC) of 0.88 for a source cohort with males only and 0.95 for a source cohort with females only), demonstrating that integrating multiple domain adaptation methods could produce feature representations that are less sensitive to dataset differences. Unlike existing methods that rely heavily on supervised tuning or assume known outcomes of samples in target cohorts, our outcome-free approaches enable the model selection under realistic deployment conditions and improve generalization of models in hip fracture risk prediction.

