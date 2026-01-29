---
layout: default
title: An explainable framework for the relationship between dementia and glucose metabolism patterns
---

# An explainable framework for the relationship between dementia and glucose metabolism patterns
**arXiv**：[2601.20480v1](https://arxiv.org/abs/2601.20480) · [PDF](https://arxiv.org/pdf/2601.20480.pdf)  
**作者**：C. Vázquez-García, F. J. Martínez-Murcia, F. Segovia Román, A. Forte, J. Ramírez, I. Illán, A. Hernández-Segura, C. Jiménez-Mesa, Juan M. Górriz  

**一句话要点**：提出半监督变分自编码器框架，通过相似性正则化对齐痴呆进展与神经影像特征。

**关键词**：变分自编码器, 神经影像分析, 痴呆进展, 半监督学习, 代谢模式, 可解释性框架

## 3 点简述
- 高维神经影像数据存在复杂非线性关系，评估神经退行性疾病面临挑战。
- 采用半监督VAE框架，引入灵活相似性正则化项，将潜在变量与临床或生物标志物对齐。
- 在ADNI PET扫描中验证，生成认知障碍水平平均重建，揭示关键脑区代谢降低模式。

## 摘要（原文）

> High-dimensional neuroimaging data presents challenges for assessing neurodegenerative diseases due to complex non-linear relationships. Variational Autoencoders (VAEs) can encode scans into lower-dimensional latent spaces capturing disease-relevant features. We propose a semi-supervised VAE framework with a flexible similarity regularization term that aligns selected latent variables with clinical or biomarker measures of dementia progression. This allows adapting the similarity metric and supervised variables to specific goals or available data. We demonstrate the approach using PET scans from the Alzheimer's Disease Neuroimaging Initiative (ADNI), guiding the first latent dimension to align with a cognitive score. Using this supervised latent variable, we generate average reconstructions across levels of cognitive impairment. Voxel-wise GLM analysis reveals reduced metabolism in key regions, mainly the hippocampus, and within major Resting State Networks, particularly the Default Mode and Central Executive Networks. The remaining latent variables encode affine transformations and intensity variations, capturing confounds such as inter-subject variability and site effects. Our framework effectively extracts disease-related patterns aligned with established Alzheimer's biomarkers, offering an interpretable and adaptable tool for studying neurodegenerative progression.

