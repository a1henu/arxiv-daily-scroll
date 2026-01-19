---
layout: default
title: Effects of Introducing Synaptic Scaling on Spiking Neural Network Learning
---

# Effects of Introducing Synaptic Scaling on Spiking Neural Network Learning
**arXiv**：[2601.11261v1](https://arxiv.org/abs/2601.11261) · [PDF](https://arxiv.org/pdf/2601.11261.pdf)  
**作者**：Shinnosuke Touda, Hirotsugu Okuno  

**一句话要点**：引入突触缩放提升脉冲神经网络在胜者通吃网络中的分类性能

**关键词**：脉冲神经网络, 突触缩放, STDP, 胜者通吃网络, MNIST分类

## 3 点简述
- 研究突触缩放对脉冲神经网络学习的影响，结合STDP等可塑性机制
- 在MNIST和Fashion-MNIST数据集上测试，比较不同参数和归一化方法
- L2范数突触缩放最有效，单轮训练后分类准确率分别达88.84%和68.01%

## 摘要（原文）

> Spiking neural networks (SNNs) employing unsupervised learning methods inspired by neural plasticity are expected to be a new framework for artificial intelligence. In this study, we investigated the effect of multiple types of neural plasticity, such as spike-time-dependent plasticity (STDP) and synaptic scaling, on the learning in a winner-take-all (WTA) network composed of spiking neurons. We implemented a WTA network with multiple types of neural plasticity using Python. The MNIST and the Fashion-MNIST datasets were used for training and testing. We varied the number of neurons, the time constant of STDP, and the normalization method used in synaptic scaling to compare classification accuracy. The results demonstrated that synaptic scaling based on the L2 norm was the most effective in improving classification performance. By implementing L2-norm-based synaptic scaling and setting the number of neurons in both excitatory and inhibitory layers to 400, the network achieved classification accuracies of 88.84 % on the MNIST dataset and 68.01 % on the Fashion-MNIST dataset after one epoch of training.

