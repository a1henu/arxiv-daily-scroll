---
layout: default
title: Bloom Filter Encoding for Machine Learning
---

# Bloom Filter Encoding for Machine Learning
**arXiv**：[2512.19991v1](https://arxiv.org/abs/2512.19991) · [PDF](https://arxiv.org/pdf/2512.19991.pdf)  
**作者**：John Cartmell, Mihaela Cardei, Ionut Cardei  

**一句话要点**：提出Bloom Filter编码方法，用于机器学习数据预处理，以压缩内存并保护隐私。

**关键词**：Bloom Filter编码, 数据预处理, 隐私保护, 机器学习, 内存优化

## 3 点简述
- 核心问题：机器学习中数据预处理需平衡内存效率、隐私保护与分类准确性。
- 方法要点：使用Bloom Filter变换将样本编码为紧凑的隐私保护位数组，保留足够结构。
- 实验或效果：在六个数据集上测试，编码数据训练的模型准确率接近原始数据，同时节省内存。

## 摘要（原文）

> We present a method that uses the Bloom filter transform to preprocess data for machine learning. Each sample is encoded into a compact, privacy-preserving bit array. This reduces memory use and protects the original data while keeping enough structure for accurate classification. We test the method on six datasets: SMS Spam Collection, ECG200, Adult 50K, CDC Diabetes, MNIST, and Fashion MNIST. Four classifiers are used: Extreme Gradient Boosting, Deep Neural Networks, Convolutional Neural Networks, and Logistic Regression. Results show that models trained on Bloom filter encodings achieve accuracy similar to models trained on raw data or other transforms. At the same time, the method provides memory savings while enhancing privacy. These results suggest that the Bloom filter transform is an efficient preprocessing approach for diverse machine learning tasks.

