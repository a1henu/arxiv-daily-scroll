---
layout: default
title: Handcrafted Feature Fusion for Reliable Detection of AI-Generated Images
---

# Handcrafted Feature Fusion for Reliable Detection of AI-Generated Images
**arXiv**：[2601.19262v1](https://arxiv.org/abs/2601.19262) · [PDF](https://arxiv.org/pdf/2601.19262.pdf)  
**作者**：Syed Mehedi Hasan Nirob, Moqsadur Rahman, Shamim Ehsan, Summit Haque  

**一句话要点**：系统评估手工特征融合与集成学习，提升AI生成图像检测的可靠性与可解释性

**关键词**：AI生成图像检测, 手工特征融合, 集成学习, CIFAKE数据集, LightGBM, 可解释性

## 3 点简述
- 核心问题：生成模型快速发展导致合成图像真实性检测成为紧迫挑战，需可靠方法。
- 方法要点：在CIFAKE数据集上系统评估多种手工特征，结合七种分类器进行基准测试。
- 实验效果：LightGBM在混合特征下表现最佳，性能随特征组合单调提升，验证特征融合优势。

## 摘要（原文）

> The rapid progress of generative models has enabled the creation of highly realistic synthetic images, raising concerns about authenticity and trust in digital media. Detecting such fake content reliably is an urgent challenge. While deep learning approaches dominate current literature, handcrafted features remain attractive for their interpretability, efficiency, and generalizability. In this paper, we conduct a systematic evaluation of handcrafted descriptors, including raw pixels, color histograms, Discrete Cosine Transform (DCT), Histogram of Oriented Gradients (HOG), Local Binary Patterns (LBP), Gray-Level Co-occurrence Matrix (GLCM), and wavelet features, on the CIFAKE dataset of real versus synthetic images. Using 50,000 training and 10,000 test samples, we benchmark seven classifiers ranging from Logistic Regression to advanced gradient-boosted ensembles (LightGBM, XGBoost, CatBoost). Results demonstrate that LightGBM consistently outperforms alternatives, achieving PR-AUC 0.9879, ROC-AUC 0.9878, F1 0.9447, and a Brier score of 0.0414 with mixed features, representing strong gains in calibration and discrimination over simpler descriptors. Across three configurations (baseline, advanced, mixed), performance improves monotonically, confirming that combining diverse handcrafted features yields substantial benefit. These findings highlight the continued relevance of carefully engineered features and ensemble learning for detecting synthetic images, particularly in contexts where interpretability and computational efficiency are critical.

