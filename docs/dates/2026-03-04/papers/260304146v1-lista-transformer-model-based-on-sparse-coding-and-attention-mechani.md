---
layout: default
title: LISTA-Transformer Model Based on Sparse Coding and Attention Mechanism and Its Application in Fault Diagnosis
---

# LISTA-Transformer Model Based on Sparse Coding and Attention Mechanism and Its Application in Fault Diagnosis
**arXiv**：[2603.04146v1](https://arxiv.org/abs/2603.04146) · [PDF](https://arxiv.org/pdf/2603.04146.pdf)  
**作者**：Shuang Liu, Lina Zhao, Tian Wang, Huaqing Wang  

**一句话要点**：提出LISTA-Transformer模型，结合稀疏编码与注意力机制，用于工业故障诊断。

**关键词**：故障诊断, 稀疏编码, 注意力机制, Transformer模型, 时间频分析

## 3 点简述
- 针对CNN和Transformer在局部特征建模与全局依赖捕获上的局限性，提出LISTA-Transformer模型。
- 模型融合LISTA稀疏编码与视觉Transformer，实现自适应局部与全局特征协作。
- 在CWRU数据集上，故障识别率达98.5%，优于传统方法3.3%。

## 摘要（原文）

> Driven by the continuous development of models such as Multi-Layer Perceptron, Convolutional Neural Network (CNN), and Transformer, deep learning has made breakthrough progress in fields such as computer vision and natural language processing, and has been successfully applied in practical scenarios such as image classification and industrial fault diagnosis. However, existing models still have certain limitations in local feature modeling and global dependency capture. Specifically, CNN is limited by local receptive fields, while Transformer has shortcomings in effectively modeling local structures, and both face challenges of high model complexity and insufficient interpretability. In response to the above issues, we proposes the following innovative work: A sparse Transformer based on Learnable Iterative Shrinkage Threshold Algorithm (LISTA-Transformer) was designed, which deeply integrates LISTA sparse encoding with visual Transformer to construct a model architecture with adaptive local and global feature collaboration mechanism. This method utilizes continuous wavelet transform to convert vibration signals into time-frequency maps and inputs them into LISTA-Transformer for more effective feature extraction. On the CWRU dataset, the fault recognition rate of our method reached 98.5%, which is 3.3% higher than traditional methods and exhibits certain superiority over existing Transformer-based approaches.

