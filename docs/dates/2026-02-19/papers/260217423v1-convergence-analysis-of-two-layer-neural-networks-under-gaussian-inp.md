---
layout: default
title: Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking
---

# Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking
**arXiv**：[2602.17423v1](https://arxiv.org/abs/2602.17423) · [PDF](https://arxiv.org/pdf/2602.17423.pdf)  
**作者**：Afroditi Kolomvaki, Fangshuo Liao, Evan Dramko, Ziyun Guang, Anastasios Kyrillidis  

**一句话要点**：分析高斯随机掩码输入下两层神经网络训练的收敛性，基于NTK证明线性收敛至误差区域与掩码方差成正比。

**关键词**：高斯随机掩码输入, 两层神经网络, 神经正切核分析, 线性收敛, dropout训练, 噪声输入训练

## 3 点简述
- 研究高斯随机掩码输入下两层神经网络训练的收敛保证，对应输入级高斯dropout或噪声输入训练场景。
- 采用神经正切核分析，证明两层ReLU网络在高斯随机掩码输入下实现线性收敛，误差区域与掩码方差成正比。
- 关键技术贡献是解决非线性激活中的随机性问题，这是一个独立兴趣问题。

## 摘要（原文）

> We investigate the convergence guarantee of two-layer neural network training with Gaussian randomly masked inputs. This scenario corresponds to Gaussian dropout at the input level, or noisy input training common in sensor networks, privacy-preserving training, and federated learning, where each user may have access to partial or corrupted features. Using a Neural Tangent Kernel (NTK) analysis, we demonstrate that training a two-layer ReLU network with Gaussian randomly masked inputs achieves linear convergence up to an error region proportional to the mask's variance. A key technical contribution is resolving the randomness within the non-linear activation, a problem of independent interest.

