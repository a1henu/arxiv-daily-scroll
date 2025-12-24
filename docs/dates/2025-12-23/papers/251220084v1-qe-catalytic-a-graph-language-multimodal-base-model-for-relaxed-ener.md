---
layout: default
title: QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption
---

# QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption
**arXiv**：[2512.20084v1](https://arxiv.org/abs/2512.20084) · [PDF](https://arxiv.org/pdf/2512.20084.pdf)  
**作者**：Yanjie Li, Jian Xu, Xueqing Chen, Lina Yu, Shiming Xiang, Weijun Li, Cheng-lin Liu  

**一句话要点**：提出QE-Catalytic多模态基模型，通过图-语言深度融合提升催化吸附弛豫能量预测精度与逆设计能力。

**关键词**：催化吸附能量预测, 图-语言多模态模型, E(3)-等变图神经网络, 弛豫能量计算, 逆设计, 结构文本生成

## 3 点简述
- 核心问题：催化吸附弛豫能量预测精度不足，现有语言模型方法在能量预测和配置区分上表现不佳。
- 方法要点：结合大语言模型Qwen与E(3)-等变图Transformer Equiformer-V2，通过图-文本对齐注入三维几何信息。
- 实验或效果：在OC20数据集上，将弛豫吸附能量MAE从0.713 eV降至0.486 eV，优于CatBERTa等基线模型。

## 摘要（原文）

> Adsorption energy is a key descriptor of catalytic reactivity. It is fundamentally defined as the difference between the relaxed total energy of the adsorbate-surface system and that of an appropriate reference state; therefore, the accuracy of relaxed-energy prediction directly determines the reliability of machine-learning-driven catalyst screening. E(3)-equivariant graph neural networks (GNNs) can natively operate on three-dimensional atomic coordinates under periodic boundary conditions and have demonstrated strong performance on such tasks. In contrast, language-model-based approaches, while enabling human-readable textual descriptions and reducing reliance on explicit graph -- thereby broadening applicability -- remain insufficient in both adsorption-configuration energy prediction accuracy and in distinguishing ``the same system with different configurations,'' even with graph-assisted pretraining in the style of GAP-CATBERTa.
>   To this end, we propose QE-Catalytic, a multimodal framework that deeply couples a large language model (\textbf{Q}wen) with an E(3)-equivariant graph Transformer (\textbf{E}quiformer-V2), enabling unified support for adsorption-configuration property prediction and inverse design on complex catalytic surfaces. During prediction, QE-Catalytic jointly leverages three-dimensional structures and structured configuration text, and injects ``3D geometric information'' into the language channel via graph-text alignment, allowing it to function as a high-performance text-based predictor when precise coordinates are unavailable, while also autoregressively generating CIF files for target-energy-driven structure design and information completion. On OC20, QE-Catalytic reduces the MAE of relaxed adsorption energy from 0.713~eV to 0.486~eV, and consistently outperforms baseline models such as CatBERTa and GAP-CATBERTa across multiple evaluation protocols.

