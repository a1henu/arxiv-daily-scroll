---
layout: default
title: Locally Interpretable Individualized Treatment Rules for Black-Box Decision Models
---

# Locally Interpretable Individualized Treatment Rules for Black-Box Decision Models
**arXiv**：[2602.11520v1](https://arxiv.org/abs/2602.11520) · [PDF](https://arxiv.org/pdf/2602.11520.pdf)  
**作者**：Yasin Khadem Charvadeh, Katherine S. Panageas, Yuan Chen  

**一句话要点**：提出局部可解释个体化治疗规则方法，结合黑盒模型与局部近似以优化医疗决策。

**关键词**：个体化治疗规则, 局部可解释性, 变分自编码器, 黑盒模型, 医疗决策优化

## 3 点简述
- 核心问题：现有个体化治疗规则方法在可解释性与灵活性间存在权衡，且多采用全局规则。
- 方法要点：使用变分自编码器生成局部合成样本，通过可解释专家混合学习个体化决策规则。
- 实验或效果：模拟研究准确恢复局部系数，乳腺癌副作用管理应用展示实用性与可解释性。

## 摘要（原文）

> Individualized treatment rules (ITRs) aim to optimize healthcare by tailoring treatment decisions to patient-specific characteristics. Existing methods typically rely on either interpretable but inflexible models or highly flexible black-box approaches that sacrifice interpretability; moreover, most impose a single global decision rule across patients. We introduce the Locally Interpretable Individualized Treatment Rule (LI-ITR) method, which combines flexible machine learning models to accurately learn complex treatment outcomes with locally interpretable approximations to construct subject-specific treatment rules. LI-ITR employs variational autoencoders to generate realistic local synthetic samples and learns individualized decision rules through a mixture of interpretable experts. Simulation studies show that LI-ITR accurately recovers true subject-specific local coefficients and optimal treatment strategies. An application to precision side-effect management in breast cancer illustrates the necessity of flexible predictive modeling and highlights the practical utility of LI-ITR in estimating optimal treatment rules while providing transparent, clinically interpretable explanations.

