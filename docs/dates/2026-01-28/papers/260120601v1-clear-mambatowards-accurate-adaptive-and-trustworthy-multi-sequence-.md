---
layout: default
title: CLEAR-Mamba:Towards Accurate, Adaptive and Trustworthy Multi-Sequence Ophthalmic Angiography Classification
---

# CLEAR-Mamba:Towards Accurate, Adaptive and Trustworthy Multi-Sequence Ophthalmic Angiography Classification
**arXiv**：[2601.20601v1](https://arxiv.org/abs/2601.20601) · [PDF](https://arxiv.org/pdf/2601.20601.pdf)  
**作者**：Zhuonan Wang, Wenjie Yan, Wenqiao Zhang, Xiaohui Song, Jian Ma, Ke Yao, Yibo Yu, Beng Chin Ooi  

**一句话要点**：提出CLEAR-Mamba框架，通过自适应参数生成和可靠性感知预测，提升多序列眼科血管造影分类的准确性与可信度。

**关键词**：医学图像分类, 眼科血管造影, 自适应条件层, 可靠性感知预测, 多序列分析, 证据不确定性学习

## 3 点简述
- 针对眼科血管造影分类中单模态限制、病灶模式细微及设备间差异大导致的泛化与高置信度预测难题。
- 引入基于超网络的自适应条件层（HaC）动态生成参数，并采用基于证据不确定性学习的可靠性感知预测（RaP）方案。
- 在构建的大规模FFA和ICGA数据集上，实验显示CLEAR-Mamba在多项指标上优于基线模型，尤其在多疾病分类和可靠性预测方面表现突出。

## 摘要（原文）

> Medical image classification is a core task in computer-aided diagnosis (CAD), playing a pivotal role in early disease detection, treatment planning, and patient prognosis assessment. In ophthalmic practice, fluorescein fundus angiography (FFA) and indocyanine green angiography (ICGA) provide hemodynamic and lesion-structural information that conventional fundus photography cannot capture. However, due to the single-modality nature, subtle lesion patterns, and significant inter-device variability, existing methods still face limitations in generalization and high-confidence prediction. To address these challenges, we propose CLEAR-Mamba, an enhanced framework built upon MedMamba with optimizations in both architecture and training strategy. Architecturally, we introduce HaC, a hypernetwork-based adaptive conditioning layer that dynamically generates parameters according to input feature distributions, thereby improving cross-domain adaptability. From a training perspective, we develop RaP, a reliability-aware prediction scheme built upon evidential uncertainty learning, which encourages the model to emphasize low-confidence samples and improves overall stability and reliability. We further construct a large-scale ophthalmic angiography dataset covering both FFA and ICGA modalities, comprising multiple retinal disease categories for model training and evaluation. Experimental results demonstrate that CLEAR-Mamba consistently outperforms multiple baseline models, including the original MedMamba, across various metrics-showing particular advantages in multi-disease classification and reliability-aware prediction. This study provides an effective solution that balances generalizability and reliability for modality-specific medical image classification tasks.

