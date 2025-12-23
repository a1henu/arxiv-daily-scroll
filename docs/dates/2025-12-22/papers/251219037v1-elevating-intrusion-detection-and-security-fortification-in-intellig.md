---
layout: default
title: Elevating Intrusion Detection and Security Fortification in Intelligent Networks through Cutting-Edge Machine Learning Paradigms
---

# Elevating Intrusion Detection and Security Fortification in Intelligent Networks through Cutting-Edge Machine Learning Paradigms
**arXiv**：[2512.19037v1](https://arxiv.org/abs/2512.19037) · [PDF](https://arxiv.org/pdf/2512.19037.pdf)  
**作者**：Md Minhazul Islam Munna, Md Mahbubur Rahman, Jaroslav Frnda, Muhammad Shahid Anwar, Alpamis Kutlimuratov  

**一句话要点**：提出基于堆叠集成学习的入侵检测框架，以增强物联网Wi-Fi网络安全性。

**关键词**：入侵检测, 机器学习, 堆叠集成学习, 特征选择, 物联网安全, Wi-Fi攻击

## 3 点简述
- 核心问题：物联网Wi-Fi网络易受KRACK和Kr00k攻击，传统入侵检测系统存在过拟合和误报率高的问题。
- 方法要点：集成噪声注入、主成分分析和元学习，通过特征选择提升检测精度和泛化能力。
- 实验或效果：在AWID3数据集上实现98%准确率、98%召回率和2%误报率，优于现有方法。

## 摘要（原文）

> The proliferation of IoT devices and their reliance on Wi-Fi networks have introduced significant security vulnerabilities, particularly the KRACK and Kr00k attacks, which exploit weaknesses in WPA2 encryption to intercept and manipulate sensitive data. Traditional IDS using classifiers face challenges such as model overfitting, incomplete feature extraction, and high false positive rates, limiting their effectiveness in real-world deployments. To address these challenges, this study proposes a robust multiclass machine learning based intrusion detection framework. The methodology integrates advanced feature selection techniques to identify critical attributes, mitigating redundancy and enhancing detection accuracy. Two distinct ML architectures are implemented: a baseline classifier pipeline and a stacked ensemble model combining noise injection, Principal Component Analysis (PCA), and meta learning to improve generalization and reduce false positives. Evaluated on the AWID3 data set, the proposed ensemble architecture achieves superior performance, with an accuracy of 98%, precision of 98%, recall of 98%, and a false positive rate of just 2%, outperforming existing state-of-the-art methods. This work demonstrates the efficacy of combining preprocessing strategies with ensemble learning to fortify network security against sophisticated Wi-Fi attacks, offering a scalable and reliable solution for IoT environments. Future directions include real-time deployment and adversarial resilience testing to further enhance the model's adaptability.

