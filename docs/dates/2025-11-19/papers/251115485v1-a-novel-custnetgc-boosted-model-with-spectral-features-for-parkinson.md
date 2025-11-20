---
layout: default
title: A Novel CustNetGC Boosted Model with Spectral Features for Parkinson's Disease Prediction
---

# A Novel CustNetGC Boosted Model with Spectral Features for Parkinson's Disease Prediction
**arXiv**：[2511.15485v1](https://arxiv.org/abs/2511.15485) · [PDF](https://arxiv.org/pdf/2511.15485.pdf)  
**作者**：Abishek Karthik, Pandiyaraju V, Dominic Savio M, Rohit Swaminathan S  

**一句话要点**：提出CustNetGC模型结合光谱特征以提升帕金森病预测准确性和可解释性

**关键词**：帕金森病预测, 语音特征分析, 卷积神经网络, Grad-CAM可视化, CatBoost分类, 光谱特征提取

## 3 点简述
- 核心问题：帕金森病早期诊断困难，基于语音特征分析可辅助检测神经损伤。
- 方法要点：结合CNN、自定义网络Grad-CAM和CatBoost，提取L-mHP和光谱斜率特征。
- 实验效果：在81人数据集上，模型准确率达99.06%，AUC为0.90（PD类）和0.89（HC类）。

## 摘要（原文）

> Parkinson's disease is a neurodegenerative disorder that can be very tricky to diagnose and treat. Such early symptoms can include tremors, wheezy breathing, and changes in voice quality as critical indicators of neural damage. Notably, there has been growing interest in utilizing changes in vocal attributes as markers for the detection of PD early on. Based on this understanding, the present paper was designed to focus on the acoustic feature analysis based on voice recordings of patients diagnosed with PD and healthy controls (HC). In this paper, we introduce a novel classification and visualization model known as CustNetGC, combining a Convolutional Neural Network (CNN) with Custom Network Grad-CAM and CatBoost to enhance the efficiency of PD diagnosis. We use a publicly available dataset from Figshare, including voice recordings of 81 participants: 40 patients with PD and 41 healthy controls. From these recordings, we extracted the key spectral features: L-mHP and Spectral Slopes. The L-mHP feature combines three spectrogram representations: Log-Mel spectrogram, harmonic spectrogram, and percussive spectrogram, which are derived using Harmonic-Percussive Source Separation (HPSS). Grad-CAM was used to highlight the important regions in the data, thus making the PD predictions interpretable and effective. Our proposed CustNetGC model achieved an accuracy of 99.06% and precision of 95.83%, with the area under the ROC curve (AUC) recorded at 0.90 for the PD class and 0.89 for the HC class. Additionally, the combination of CatBoost, a gradient boosting algorithm, enhanced the robustness and the prediction performance by properly classifying PD and non-PD samples. Therefore, the results provide the potential improvement in the CustNetGC system in enhancing diagnostic accuracy and the interpretability of the Parkinson's Disease prediction model.

