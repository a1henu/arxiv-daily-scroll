---
layout: default
title: Scaling Laws of Machine Learning for Optimal Power Flow
---

# Scaling Laws of Machine Learning for Optimal Power Flow
**arXiv**：[2601.02706v1](https://arxiv.org/abs/2601.02706) · [PDF](https://arxiv.org/pdf/2601.02706.pdf)  
**作者**：Xinyi Liu, Xuan He, Yize Chen  

**一句话要点**：提出机器学习在最优潮流中的标度律，以指导数据与计算资源分配。

**关键词**：最优潮流, 机器学习标度律, 深度神经网络, 物理信息神经网络, 功率系统优化, 计算最优前沿

## 3 点简述
- 核心问题：机器学习在最优潮流中面临数据量与模型复杂度的标度关系未知。
- 方法要点：系统研究数据规模与计算规模对预测误差、约束违反和速度的影响。
- 实验或效果：发现功率律关系，并识别预测精度与约束可行性的分歧。

## 摘要（原文）

> Optimal power flow (OPF) is one of the fundamental tasks for power system operations. While machine learning (ML) approaches such as deep neural networks (DNNs) have been widely studied to enhance OPF solution speed and performance, their practical deployment faces two critical scaling questions: What is the minimum training data volume required for reliable results? How should ML models' complexity balance accuracy with real-time computational limits? Existing studies evaluate discrete scenarios without quantifying these scaling relationships, leading to trial-and-error-based ML development in real-world applications. This work presents the first systematic scaling study for ML-based OPF across two dimensions: data scale (0.1K-40K training samples) and compute scale (multiple NN architectures with varying FLOPs). Our results reveal consistent power-law relationships on both DNNs and physics-informed NNs (PINNs) between each resource dimension and three core performance metrics: prediction error (MAE), constraint violations and speed. We find that for ACOPF, the accuracy metric scales with dataset size and training compute. These scaling laws enable predictable and principled ML pipeline design for OPF. We further identify the divergence between prediction accuracy and constraint feasibility and characterize the compute-optimal frontier. This work provides quantitative guidance for ML-OPF design and deployments.

