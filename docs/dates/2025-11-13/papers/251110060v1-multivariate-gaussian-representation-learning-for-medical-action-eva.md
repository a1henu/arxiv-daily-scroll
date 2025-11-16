---
layout: default
title: Multivariate Gaussian Representation Learning for Medical Action Evaluation
---

# Multivariate Gaussian Representation Learning for Medical Action Evaluation
**arXiv**：[2511.10060v1](https://arxiv.org/abs/2511.10060) · [PDF](https://arxiv.org/pdf/2511.10060.pdf)  
**作者**：Luming Yang, Haoxian Liu, Siqing Li, Alper Yilmaz  

**一句话要点**：提出GaussMedAct框架以解决医疗动作评估中的精细建模挑战

**关键词**：医疗动作评估, 多元高斯表示, 时空建模, 骨骼特征编码, 实时推理

## 3 点简述
- 医疗动作评估面临数据集稀缺、精度要求高和快速动作建模不足的问题
- 采用多元高斯编码将动作分解为自适应3D高斯令牌，结合双流空间编码
- 在CPREval-6k基准上达到92.1%准确率，优于基线且计算效率高

## 摘要（原文）

> Fine-grained action evaluation in medical vision faces unique challenges due to the unavailability of comprehensive datasets, stringent precision requirements, and insufficient spatiotemporal dynamic modeling of very rapid actions. To support development and evaluation, we introduce CPREval-6k, a multi-view, multi-label medical action benchmark containing 6,372 expert-annotated videos with 22 clinical labels. Using this dataset, we present GaussMedAct, a multivariate Gaussian encoding framework, to advance medical motion analysis through adaptive spatiotemporal representation learning. Multivariate Gaussian Representation projects the joint motions to a temporally scaled multi-dimensional space, and decomposes actions into adaptive 3D Gaussians that serve as tokens. These tokens preserve motion semantics through anisotropic covariance modeling while maintaining robustness to spatiotemporal noise. Hybrid Spatial Encoding, employing a Cartesian and Vector dual-stream strategy, effectively utilizes skeletal information in the form of joint and bone features. The proposed method achieves 92.1% Top-1 accuracy with real-time inference on the benchmark, outperforming the ST-GCN baseline by +5.9% accuracy with only 10% FLOPs. Cross-dataset experiments confirm the superiority of our method in robustness.

