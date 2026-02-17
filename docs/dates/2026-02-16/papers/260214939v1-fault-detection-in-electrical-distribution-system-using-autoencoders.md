---
layout: default
title: Fault Detection in Electrical Distribution System using Autoencoders
---

# Fault Detection in Electrical Distribution System using Autoencoders
**arXiv**：[2602.14939v1](https://arxiv.org/abs/2602.14939) · [PDF](https://arxiv.org/pdf/2602.14939.pdf)  
**作者**：Sidharthenee Nayak, Victor Sam Moses Babu, Chandrashekhar Narayan Bhende, Pratyush Chakraborty, Mayukha Pal  

**一句话要点**：提出基于深度自编码器的异常检测方法，用于电力系统故障检测，提升准确率。

**关键词**：电力系统故障检测, 深度自编码器, 异常检测, 卷积自编码器, 降维, 准确率提升

## 3 点简述
- 电力系统故障检测面临数据稀缺和概率性挑战，传统方法应用困难。
- 采用深度自编码器进行异常检测，并利用卷积自编码器降维以减少训练时间。
- 在模拟和公开数据集上分别达到97.62%和99.92%的准确率，优于其他方法。

## 摘要（原文）

> In recent times, there has been considerable interest in fault detection within electrical power systems, garnering attention from both academic researchers and industry professionals. Despite the development of numerous fault detection methods and their adaptations over the past decade, their practical application remains highly challenging. Given the probabilistic nature of fault occurrences and parameters, certain decision-making tasks could be approached from a probabilistic standpoint. Protective systems are tasked with the detection, classification, and localization of faulty voltage and current line magnitudes, culminating in the activation of circuit breakers to isolate the faulty line. An essential aspect of designing effective fault detection systems lies in obtaining reliable data for training and testing, which is often scarce. Leveraging deep learning techniques, particularly the powerful capabilities of pattern classifiers in learning, generalizing, and parallel processing, offers promising avenues for intelligent fault detection. To address this, our paper proposes an anomaly-based approach for fault detection in electrical power systems, employing deep autoencoders. Additionally, we utilize Convolutional Autoencoders (CAE) for dimensionality reduction, which, due to its fewer parameters, requires less training time compared to conventional autoencoders. The proposed method demonstrates superior performance and accuracy compared to alternative detection approaches by achieving an accuracy of 97.62% and 99.92% on simulated and publicly available datasets.

