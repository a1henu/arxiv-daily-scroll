---
layout: default
title: Imputation of Unknown Missingness in Sparse Electronic Health Records
---

# Imputation of Unknown Missingness in Sparse Electronic Health Records
**arXiv**：[2602.20442v1](https://arxiv.org/abs/2602.20442) · [PDF](https://arxiv.org/pdf/2602.20442.pdf)  
**作者**：Jun Han, Josue Nassar, Sanjit Singh Batra, Aldo Cordova-Palomera, Vijay Nori, Robert E. Tillman  

**一句话要点**：提出基于Transformer的去噪算法以恢复电子健康记录中的未知缺失值

**关键词**：电子健康记录, 缺失数据插补, Transformer网络, 去噪算法, 医疗预测

## 3 点简述
- 核心问题：电子健康记录稀疏且存在未知缺失，如诊断代码缺失可能表示未诊断或未共享。
- 方法要点：设计Transformer去噪神经网络，自适应阈值化输出以恢复预测缺失值。
- 实验或效果：在真实数据集上优于现有插补方法，提升下游任务如再入院预测性能。

## 摘要（原文）

> Machine learning holds great promise for advancing the field of medicine, with electronic health records (EHRs) serving as a primary data source. However, EHRs are often sparse and contain missing data due to various challenges and limitations in data collection and sharing between healthcare providers. Existing techniques for imputing missing values predominantly focus on known unknowns, such as missing or unavailable values of lab test results; most do not explicitly address situations where it is difficult to distinguish what is missing. For instance, a missing diagnosis code in an EHR could signify either that the patient has not been diagnosed with the condition or that a diagnosis was made, but not shared by a provider. Such situations fall into the paradigm of unknown unknowns. To address this challenge, we develop a general purpose algorithm for denoising data to recover unknown missing values in binary EHRs. We design a transformer-based denoising neural network where the output is thresholded adaptively to recover values in cases where we predict data are missing. Our results demonstrate improved accuracy in denoising medical codes within a real EHR dataset compared to existing imputation approaches and leads to increased performance on downstream tasks using the denoised data. In particular, when applying our method to a real world application, predicting hospital readmission from EHRs, our method achieves statistically significant improvement over all existing baselines.

