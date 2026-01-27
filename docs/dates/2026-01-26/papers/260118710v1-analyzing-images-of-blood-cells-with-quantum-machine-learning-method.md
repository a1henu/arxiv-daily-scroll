---
layout: default
title: Analyzing Images of Blood Cells with Quantum Machine Learning Methods: Equilibrium Propagation and Variational Quantum Circuits to Detect Acute Myeloid Leukemia
---

# Analyzing Images of Blood Cells with Quantum Machine Learning Methods: Equilibrium Propagation and Variational Quantum Circuits to Detect Acute Myeloid Leukemia
**arXiv**：[2601.18710v1](https://arxiv.org/abs/2601.18710) · [PDF](https://arxiv.org/pdf/2601.18710.pdf)  
**作者**：A. Bano, L. Liebovitch  

**一句话要点**：提出量子机器学习方法用于血细胞图像分析，以检测急性髓系白血病。

**关键词**：量子机器学习, 医疗图像分析, 急性髓系白血病检测, 平衡传播, 变分量子电路, NISQ时代

## 3 点简述
- 核心问题：在量子系统约束下实现医疗图像分类，避免反向传播。
- 方法要点：采用平衡传播和变分量子电路，处理低分辨率图像和工程特征。
- 实验或效果：量子方法在有限样本下达到接近经典CNN的准确率，数据效率更高。

## 摘要（原文）

> This paper presents a feasibility study demonstrating that quantum machine learning (QML) algorithms achieve competitive performance on real-world medical imaging despite operating under severe constraints. We evaluate Equilibrium Propagation (EP), an energy-based learning method that does not use backpropagation (incompatible with quantum systems due to state-collapsing measurements) and Variational Quantum Circuits (VQCs) for automated detection of Acute Myeloid Leukemia (AML) from blood cell microscopy images using binary classification (2 classes: AML vs. Healthy).
>   Key Result: Using limited subsets (50-250 samples per class) of the AML-Cytomorphology dataset (18,365 expert-annotated images), quantum methods achieve performance only 12-15% below classical CNNs despite reduced image resolution (64x64 pixels), engineered features (20D), and classical simulation via Qiskit. EP reaches 86.4% accuracy (only 12% below CNN) without backpropagation, while the 4-qubit VQC attains 83.0% accuracy with consistent data efficiency: VQC maintains stable 83% performance with only 50 samples per class, whereas CNN requires 250 samples (5x more data) to reach 98%. These results establish reproducible baselines for QML in healthcare, validating NISQ-era feasibility.

