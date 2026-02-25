---
layout: default
title: XMorph: Explainable Brain Tumor Analysis Via LLM-Assisted Hybrid Deep Intelligence
---

# XMorph: Explainable Brain Tumor Analysis Via LLM-Assisted Hybrid Deep Intelligence
**arXiv**：[2602.21178v1](https://arxiv.org/abs/2602.21178) · [PDF](https://arxiv.org/pdf/2602.21178.pdf)  
**作者**：Sepehr Salem Ghahfarokhi, M. Moein Esfahani, Raj Sunderraman, Vince Calhoun, Mohammed Alser  

**一句话要点**：提出XMorph框架，通过LLM辅助混合深度智能实现可解释脑肿瘤分析。

**关键词**：脑肿瘤分类, 可解释人工智能, 信息加权边界归一化, LLM辅助分析, 医学影像分析

## 3 点简述
- 核心问题：深度学习在脑肿瘤诊断中因可解释性差和计算限制而临床采用受限。
- 方法要点：结合信息加权边界归一化和双通道可解释AI模块，增强形态表示和临床解释。
- 实验或效果：在三种脑肿瘤分类中达到96.0%准确率，证明可解释性与高性能可共存。

## 摘要（原文）

> Deep learning has significantly advanced automated brain tumor diagnosis, yet clinical adoption remains limited by interpretability and computational constraints. Conventional models often act as opaque ''black boxes'' and fail to quantify the complex, irregular tumor boundaries that characterize malignant growth. To address these challenges, we present XMorph, an explainable and computationally efficient framework for fine-grained classification of three prominent brain tumor types: glioma, meningioma, and pituitary tumors. We propose an Information-Weighted Boundary Normalization (IWBN) mechanism that emphasizes diagnostically relevant boundary regions alongside nonlinear chaotic and clinically validated features, enabling a richer morphological representation of tumor growth. A dual-channel explainable AI module combines GradCAM++ visual cues with LLM-generated textual rationales, translating model reasoning into clinically interpretable insights. The proposed framework achieves a classification accuracy of 96.0%, demonstrating that explainability and high performance can co-exist in AI-based medical imaging systems. The source code and materials for XMorph are all publicly available at: https://github.com/ALSER-Lab/XMorph.

