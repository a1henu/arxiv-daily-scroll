---
layout: default
title: Phishing Detection System: An Ensemble Approach Using Character-Level CNN and Feature Engineering
---

# Phishing Detection System: An Ensemble Approach Using Character-Level CNN and Feature Engineering
**arXiv**：[2512.16717v1](https://arxiv.org/abs/2512.16717) · [PDF](https://arxiv.org/pdf/2512.16717.pdf)  
**作者**：Rudra Dubey, Arpit Mani Tripathi, Archit Srivastava, Sarvpal Singh  

**一句话要点**：提出基于字符级CNN与特征工程的集成模型，用于实时钓鱼URL检测。

**关键词**：钓鱼检测, 集成学习, 字符级CNN, URL分析, 网络安全, 机器学习

## 3 点简述
- 钓鱼攻击是主要网络安全风险，需应对不断演变的欺骗策略。
- 集成字符级CNN和LightGBM，结合36个URL特征，提升检测性能。
- 在19,873个URL测试集上，准确率达99.819%，假阳性率极低。

## 摘要（原文）

> In actuality, phishing attacks remain one of the most prevalent cybersecurity risks in existence today, with malevolent actors constantly changing their strategies to successfully trick users. This paper presents an AI model for a phishing detection system that uses an ensemble approach to combine character-level Convolutional Neural Networks (CNN) and LightGBM with engineered features. Our system uses a character-level CNN to extract sequential features after extracting 36 lexical, structural, and domain-based features from the URLs. On a test dataset of 19,873 URLs, the ensemble model achieves an accuracy of 99.819 percent, precision of 100 percent, recall of 99.635 percent, and ROC-AUC of 99.947 percent. Through a FastAPI-based service with an intuitive user interface, the suggested system has been utilised to offer real-time detection. In contrast, the results demonstrate that the suggested solution performs better than individual models; LightGBM contributes 40 percent and character-CNN contributes 60 percent to the final prediction. The suggested method maintains extremely low false positive rates while doing a good job of identifying contemporary phishing techniques. Index Terms - Phishing detection, machine learning, deep learning, CNN, ensemble methods, cybersecurity, URL analysis

