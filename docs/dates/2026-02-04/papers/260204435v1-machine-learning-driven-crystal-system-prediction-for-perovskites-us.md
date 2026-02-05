---
layout: default
title: Machine Learning-Driven Crystal System Prediction for Perovskites Using Augmented X-ray Diffraction Data
---

# Machine Learning-Driven Crystal System Prediction for Perovskites Using Augmented X-ray Diffraction Data
**arXiv**：[2602.04435v1](https://arxiv.org/abs/2602.04435) · [PDF](https://arxiv.org/pdf/2602.04435.pdf)  
**作者**：Ansu Mathew, Ahmer A. B. Baloch, Alamin Yakasai, Hemant Mittal, Vivian Alberts, Jayakumar V. Karunamurthy  

**一句话要点**：提出机器学习框架，利用增强X射线衍射数据预测钙钛矿晶体系统

**关键词**：钙钛矿材料, X射线衍射分析, 机器学习分类, 数据增强, 晶体系统预测

## 3 点简述
- 核心问题：从X射线衍射光谱预测钙钛矿晶体系统、点群和空间群，以加速材料发现。
- 方法要点：集成多种机器学习模型，结合SMOTE等特征增强策略，处理数据不平衡并提升鲁棒性。
- 实验效果：TSF模型在晶体系统预测中MCC达0.9，准确率97.76%，点群和空间群预测平衡准确率超95%。

## 摘要（原文）

> Prediction of crystal system from X-ray diffraction (XRD) spectra is a critical task in materials science, particularly for perovskite materials which are known for their diverse applications in photovoltaics, optoelectronics, and catalysis. In this study, we present a machine learning (ML)-driven framework that leverages advanced models, including Time Series Forest (TSF), Random Forest (RF), Extreme Gradient Boosting (XGBoost), Recurrent Neural Network (RNN), Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and a simple feedforward neural network (NN), to classify crystal systems, point groups, and space groups from XRD data of perovskite materials. To address class imbalance and enhance model robustness, we integrated feature augmentation strategies such as Synthetic Minority Over-sampling Technique (SMOTE), class weighting, jittering, and spectrum shifting, along with efficient data preprocessing pipelines. The TSF model with SMOTE augmentation achieved strong performance for crystal system prediction, with a Matthews correlation coefficient (MCC) of 0.9, an F1 score of 0.92, and an accuracy of 97.76%. For point and space group prediction, balanced accuracies above 95% were obtained. The model demonstrated high performance for symmetry-distinct classes, including cubic crystal systems, point groups 3m and m-3m, and space groups Pnma and Pnnn. This work highlights the potential of ML for XRD-based structural characterization and accelerated discovery of perovskite materials

