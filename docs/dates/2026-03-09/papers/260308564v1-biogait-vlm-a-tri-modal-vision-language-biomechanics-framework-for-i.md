---
layout: default
title: BioGait-VLM: A Tri-Modal Vision-Language-Biomechanics Framework for Interpretable Clinical Gait Assessment
---

# BioGait-VLM: A Tri-Modal Vision-Language-Biomechanics Framework for Interpretable Clinical Gait Assessment
**arXiv**：[2603.08564v1](https://arxiv.org/abs/2603.08564) · [PDF](https://arxiv.org/pdf/2603.08564.pdf)  
**作者**：Erdong Chen, Yuyang Ji, Jacob K. Greenberg, Benjamin Steel, Faraz Arkam, Abigail Lewis, Pranay Singh, Feng Liu  

**一句话要点**：提出BioGait-VLM三模态框架以解决视频步态分析泛化差问题，实现可解释临床评估。

**关键词**：视频步态分析, 多模态学习, 生物力学建模, 可解释性评估, 临床数据集, 时序蒸馏

## 3 点简述
- 视频步态分析易过拟合环境偏差，泛化能力差。
- 融合视觉、语言和生物力学模态，通过时序证据蒸馏和生物力学标记化捕获动态与关节机制。
- 在增强数据集上实现最优识别精度，专家研究证实生物力学标记提升临床合理性与证据基础。

## 摘要（原文）

> Video-based Clinical Gait Analysis often suffers from poor generalization as models overfit environmental biases instead of capturing pathological motion. To address this, we propose BioGait-VLM, a tri-modal Vision-Language-Biomechanics framework for interpretable clinical gait assessment. Unlike standard video encoders, our architecture incorporates a Temporal Evidence Distillation branch to capture rhythmic dynamics and a Biomechanical Tokenization branch that projects 3D skeleton sequences into language-aligned semantic tokens. This enables the model to explicitly reason about joint mechanics independent of visual shortcuts. To ensure rigorous benchmarking, we augment the public GAVD dataset with a high-fidelity Degenerative Cervical Myelopathy (DCM) cohort to form a unified 8-class taxonomy, establishing a strict subject-disjoint protocol to prevent data leakage. Under this setting, BioGait-VLM achieves state-of-the-art recognition accuracy. Furthermore, a blinded expert study confirms that biomechanical tokens significantly improve clinical plausibility and evidence grounding, offering a path toward transparent, privacy-enhanced gait assessment.

