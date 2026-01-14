---
layout: default
title: Interpretability and Individuality in Knee MRI: Patient-Specific Radiomic Fingerprint with Reconstructed Healthy Personas
---

# Interpretability and Individuality in Knee MRI: Patient-Specific Radiomic Fingerprint with Reconstructed Healthy Personas
**arXiv**：[2601.08604v1](https://arxiv.org/abs/2601.08604) · [PDF](https://arxiv.org/pdf/2601.08604.pdf)  
**作者**：Yaxi Chen, Simin Ni, Shuai Li, Shaheer U. Saeed, Aleksandra Ivanova, Rikin Hargunani, Jie Huang, Chaozong Liu, Yipeng Hu  

**一句话要点**：提出患者特异性放射组学指纹和健康人格以增强膝MRI自动评估的个体化与可解释性。

**关键词**：膝MRI自动评估, 患者特异性放射组学, 健康人格合成, 可解释性AI, 扩散模型, 病理定位

## 3 点简述
- 传统放射组学特征在群体层面选择，难以捕捉患者特异性变异，影响临床可解释性和性能。
- 方法包括动态构建患者特异性放射组学指纹和基于扩散模型合成健康膝MRI作为病理基线。
- 实验表明，该方法在三个临床任务中性能媲美或超越先进深度学习模型，支持多层次可解释性。

## 摘要（原文）

> For automated assessment of knee MRI scans, both accuracy and interpretability are essential for clinical use and adoption. Traditional radiomics rely on predefined features chosen at the population level; while more interpretable, they are often too restrictive to capture patient-specific variability and can underperform end-to-end deep learning (DL). To address this, we propose two complementary strategies that bring individuality and interpretability: radiomic fingerprints and healthy personas. First, a radiomic fingerprint is a dynamically constructed, patient-specific feature set derived from MRI. Instead of applying a uniform population-level signature, our model predicts feature relevance from a pool of candidate features and selects only those most predictive for each patient, while maintaining feature-level interpretability. This fingerprint can be viewed as a latent-variable model of feature usage, where an image-conditioned predictor estimates usage probabilities and a transparent logistic regression with global coefficients performs classification. Second, a healthy persona synthesises a pathology-free baseline for each patient using a diffusion model trained to reconstruct healthy knee MRIs. Comparing features extracted from pathological images against their personas highlights deviations from normal anatomy, enabling intuitive, case-specific explanations of disease manifestations. We systematically compare fingerprints, personas, and their combination across three clinical tasks. Experimental results show that both approaches yield performance comparable to or surpassing state-of-the-art DL models, while supporting interpretability at multiple levels. Case studies further illustrate how these perspectives facilitate human-explainable biomarker discovery and pathology localisation.

