---
layout: default
title: Low Rank Support Quaternion Matrix Machine
---

# Low Rank Support Quaternion Matrix Machine
**arXiv**：[2512.08327v1](https://arxiv.org/abs/2512.08327) · [PDF](https://arxiv.org/pdf/2512.08327.pdf)  
**作者**：Wang Chen, Ziyan Luo, Shuangyue Wang  

**一句话要点**：提出低秩支持四元数矩阵机以提升彩色图像分类性能

**关键词**：彩色图像分类, 四元数建模, 低秩正则化, ADMM算法, 支持矩阵机

## 3 点简述
- 核心问题：传统彩色图像分类方法使用向量、矩阵或张量表示，可能忽略通道间内在耦合关系。
- 方法要点：将RGB通道建模为纯四元数，引入四元数核范数正则化以促进低秩结构，设计ADMM算法求解优化模型。
- 实验或效果：在多个数据集上验证，相比支持向量机、支持矩阵机和支持张量机，在准确性、鲁棒性和计算效率方面有优势。

## 摘要（原文）

> Input features are conventionally represented as vectors, matrices, or third order tensors in the real field, for color image classification. Inspired by the success of quaternion data modeling for color images in image recovery and denoising tasks, we propose a novel classification method for color image classification, named as the Low-rank Support Quaternion Matrix Machine (LSQMM), in which the RGB channels are treated as pure quaternions to effectively preserve the intrinsic coupling relationships among channels via the quaternion algebra. For the purpose of promoting low-rank structures resulting from strongly correlated color channels, a quaternion nuclear norm regularization term, serving as a natural extension of the conventional matrix nuclear norm to the quaternion domain, is added to the hinge loss in our LSQMM model. An Alternating Direction Method of Multipliers (ADMM)-based iterative algorithm is designed to effectively resolve the proposed quaternion optimization model. Experimental results on multiple color image classification datasets demonstrate that our proposed classification approach exhibits advantages in classification accuracy, robustness and computational efficiency, compared to several state-of-the-art methods using support vector machines, support matrix machines, and support tensor machines.

