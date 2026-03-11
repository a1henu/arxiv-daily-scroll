---
layout: default
title: Robust Provably Secure Image Steganography via Latent Iterative Optimization
---

# Robust Provably Secure Image Steganography via Latent Iterative Optimization
**arXiv**：[2603.09348v1](https://arxiv.org/abs/2603.09348) · [PDF](https://arxiv.org/pdf/2603.09348.pdf)  
**作者**：Yanan Li, Zixuan Wang, Qiyang Xiao, Yanzhen Ren  

**一句话要点**：提出基于潜在空间迭代优化的鲁棒可证明安全图像隐写框架，以增强压缩和图像处理下的稳健性。

**关键词**：图像隐写, 潜在空间优化, 可证明安全, 鲁棒性增强, 迭代优化, 消息提取

## 3 点简述
- 核心问题：现有可证明安全隐写方法在压缩和图像处理下稳健性不足，影响消息提取准确性。
- 方法要点：接收端将传输图像作为固定参考，迭代优化潜在变量以最小化重构误差，提升消息提取精度。
- 实验或效果：在基准数据集上，该方法在保持可证明安全性的同时，显著提高了对压缩的鲁棒性，并可作为独立模块增强其他方案。

## 摘要（原文）

> We propose a robust and provably secure image steganography framework based on latent-space iterative optimization. Within this framework, the receiver treats the transmitted image as a fixed reference and iteratively refines a latent variable to minimize the reconstruction error, thereby improving message extraction accuracy. Unlike prior methods, our approach preserves the provable security of the embedding while markedly enhancing robustness under various compression and image processing scenarios. On benchmark datasets, the experimental results demonstrate that the proposed iterative optimization not only improves robustness against image compression while preserving provable security, but can also be applied as an independent module to further reinforce robustness in other provably secure steganographic schemes. This highlights the practicality and promise of latent-space optimization for building reliable, robust, and secure steganographic systems.

