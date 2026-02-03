---
layout: default
title: Rotation-free Online Handwritten Character Recognition Using Linear Recurrent Units
---

# Rotation-free Online Handwritten Character Recognition Using Linear Recurrent Units
**arXiv**：[2602.01533v1](https://arxiv.org/abs/2602.01533) · [PDF](https://arxiv.org/pdf/2602.01533.pdf)  
**作者**：Zhe Ling, Sicheng Yu, Danyu Yang  

**一句话要点**：提出SW-PS+LRU框架以解决在线手写字符识别中的旋转变形问题

**关键词**：在线手写字符识别, 旋转不变特征, 滑动窗口路径签名, 线性循环单元, 动态笔画建模, 集成学习

## 3 点简述
- 核心问题：旋转变形破坏笔画空间布局，降低识别准确率，提取旋转不变特征是挑战
- 方法要点：使用滑动窗口路径签名捕获局部结构特征，引入轻量级线性循环单元作为分类器
- 实验或效果：在CASIA-OLHWDB1.1数据集上，数字、英文大写字母和中文部首的识别准确率分别达99.62%、96.67%和94.33%

## 摘要（原文）

> Online handwritten character recognition leverages stroke order and dynamic features, which generally provide higher accuracy and robustness compared with offline recognition. However, in practical applications, rotational deformations can disrupt the spatial layout of strokes, substantially reducing recognition accuracy. Extracting rotation-invariant features therefore remains a challenging open problem. In this work, we employ the Sliding Window Path Signature (SW-PS) to capture local structural features of characters, and introduce the lightweight Linear Recurrent Units (LRU) as the classifier. The LRU combine the fast incremental processing capability of recurrent neural networks (RNN) with the efficient parallel training of state space models (SSM), while reliably modelling dynamic stroke characteristics. We conducted recognition experiments with random rotation angle up to $\pm 180^{\circ}$ on three subsets of the CASIA-OLHWDB1.1 dataset: digits, English upper letters, and Chinese radicals. The accuracies achieved after ensemble learning were $99.62\%$, $96.67\%$, and $94.33\%$, respectively. Experimental results demonstrate that the proposed SW-PS+LRU framework consistently surpasses competing models in both convergence speed and test accuracy.

