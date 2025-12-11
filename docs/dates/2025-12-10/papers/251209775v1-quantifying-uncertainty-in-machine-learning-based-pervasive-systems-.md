---
layout: default
title: Quantifying Uncertainty in Machine Learning-Based Pervasive Systems: Application to Human Activity Recognition
---

# Quantifying Uncertainty in Machine Learning-Based Pervasive Systems: Application to Human Activity Recognition
**arXiv**：[2512.09775v1](https://arxiv.org/abs/2512.09775) · [PDF](https://arxiv.org/pdf/2512.09775.pdf)  
**作者**：Vladimir Balditsyn, Philippe Lalanda, German Vega, Stéphanie Chollet  

**一句话要点**：提出量化机器学习不确定性方法，应用于人类活动识别系统

**关键词**：不确定性量化, 机器学习系统, 人类活动识别, 运行时评估, 普适计算

## 3 点简述
- 核心问题：机器学习模型在普适系统中存在不确定性，难以保证无错误性能
- 方法要点：适配并联合使用多种技术，在运行时评估模型预测的相关性
- 实验或效果：在人类活动识别领域应用并评估，结果验证了方法的有效性

## 摘要（原文）

> The recent convergence of pervasive computing and machine learning has given rise to numerous services, impacting almost all areas of economic and social activity. However, the use of AI techniques precludes certain standard software development practices, which emphasize rigorous testing to ensure the elimination of all bugs and adherence to well-defined specifications. ML models are trained on numerous high-dimensional examples rather than being manually coded. Consequently, the boundaries of their operating range are uncertain, and they cannot guarantee absolute error-free performance. In this paper, we propose to quantify uncertainty in ML-based systems. To achieve this, we propose to adapt and jointly utilize a set of selected techniques to evaluate the relevance of model predictions at runtime. We apply and evaluate these proposals in the highly heterogeneous and evolving domain of Human Activity Recognition (HAR). The results presented demonstrate the relevance of the approach, and we discuss in detail the assistance provided to domain experts.

