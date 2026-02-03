---
layout: default
title: A Lightweight Sparse Interaction Network for Time Series Forecasting
---

# A Lightweight Sparse Interaction Network for Time Series Forecasting
**arXiv**：[2602.01585v1](https://arxiv.org/abs/2602.01585) · [PDF](https://arxiv.org/pdf/2602.01585.pdf)  
**作者**：Xu Zhang, Qitong Wang, Peng Wang, Wei Wang  

**一句话要点**：提出轻量稀疏交互网络以提升时间序列预测的准确性与效率

**关键词**：时间序列预测, 稀疏交互, 线性模型, 多头机制, 轻量网络

## 3 点简述
- 线性模型在长时预测中表现优异，但隐含交互可能不足；
- 引入多头稀疏交互机制，通过稀疏伯努利分布学习时间步重要连接；
- 实验显示在公开数据集上优于先进线性与Transformer模型。

## 摘要（原文）

> Recent work shows that linear models can outperform several transformer models in long-term time-series forecasting (TSF). However, instead of explicitly performing temporal interaction through self-attention, linear models implicitly perform it based on stacked MLP structures, which may be insufficient in capturing the complex temporal dependencies and their performance still has potential for improvement. To this end, we propose a Lightweight Sparse Interaction Network (LSINet) for TSF task. Inspired by the sparsity of self-attention, we propose a Multihead Sparse Interaction Mechanism (MSIM). Different from self-attention, MSIM learns the important connections between time steps through sparsity-induced Bernoulli distribution to capture temporal dependencies for TSF. The sparsity is ensured by the proposed self-adaptive regularization loss. Moreover, we observe the shareability of temporal interactions and propose to perform Shared Interaction Learning (SIL) for MSIM to further enhance efficiency and improve convergence. LSINet is a linear model comprising only MLP structures with low overhead and equipped with explicit temporal interaction mechanisms. Extensive experiments on public datasets show that LSINet achieves both higher accuracy and better efficiency than advanced linear models and transformer models in TSF tasks. The code is available at the link https://github.com/Meteor-Stars/LSINet.

