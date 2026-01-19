---
layout: default
title: LSTM VS. Feed-Forward Autoencoders for Unsupervised Fault Detection in Hydraulic Pumps
---

# LSTM VS. Feed-Forward Autoencoders for Unsupervised Fault Detection in Hydraulic Pumps
**arXiv**：[2601.11163v1](https://arxiv.org/abs/2601.11163) · [PDF](https://arxiv.org/pdf/2601.11163.pdf)  
**作者**：P. Sánchez, K. Reyes, B. Radu, E. Fernández  

**一句话要点**：提出基于前馈和LSTM自编码器的无监督方法，用于液压泵早期故障检测。

**关键词**：无监督故障检测, 自编码器, LSTM, 液压泵, 传感器数据分析

## 3 点简述
- 核心问题：工业液压泵意外故障导致生产中断和高昂成本，需早期检测。
- 方法要点：使用前馈模型分析单点传感器数据，LSTM模型捕捉短时窗口，仅用健康数据训练。
- 实验或效果：在包含七个故障区间的测试集上，模型实现高可靠性，无需故障样本训练。

## 摘要（原文）

> Unplanned failures in industrial hydraulic pumps can halt production and incur substantial costs. We explore two unsupervised autoencoder (AE) schemes for early fault detection: a feed-forward model that analyses individual sensor snapshots and a Long Short-Term Memory (LSTM) model that captures short temporal windows. Both networks are trained only on healthy data drawn from a minute-level log of 52 sensor channels; evaluation uses a separate set that contains seven annotated fault intervals. Despite the absence of fault samples during training, the models achieve high reliability.

