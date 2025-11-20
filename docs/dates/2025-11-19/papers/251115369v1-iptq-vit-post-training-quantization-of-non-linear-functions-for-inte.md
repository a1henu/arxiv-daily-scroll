---
layout: default
title: IPTQ-ViT: Post-Training Quantization of Non-linear Functions for Integer-only Vision Transformers
---

# IPTQ-ViT: Post-Training Quantization of Non-linear Functions for Integer-only Vision Transformers
**arXiv**：[2511.15369v1](https://arxiv.org/abs/2511.15369) · [PDF](https://arxiv.org/pdf/2511.15369.pdf)  
**作者**：Gihwan Kim, Jemin Lee, Hyungshin Kim  

**一句话要点**：提出IPTQ-ViT框架，实现无需重训练的整数化视觉Transformer量化

**关键词**：视觉Transformer, 后训练量化, 整数推理, 非线性函数近似, 图像分类, 目标检测

## 3 点简述
- 现有PTQ方法无法完全量化非线性函数，导致整数推理不完整
- 引入多项式GELU和位移Softmax近似函数，提升量化精度
- 在图像分类和检测任务中，精度优于其他PTQ方法，接近QAT方法

## 摘要（原文）

> Previous Quantization-Aware Training (QAT) methods for vision transformers rely on expensive retraining to recover accuracy loss in non-linear layer quantization, limiting their use in resource-constrained environments. In contrast, existing Post-Training Quantization (PTQ) methods either partially quantize non-linear functions or adjust activation distributions to maintain accuracy but fail to achieve fully integer-only inference. In this paper, we introduce IPTQ-ViT, a novel PTQ framework for fully integer-only vision transformers without retraining. We present approximation functions: a polynomial-based GELU optimized for vision data and a bit-shifting-based Softmax designed to improve approximation accuracy in PTQ. In addition, we propose a unified metric integrating quantization sensitivity, perturbation, and computational cost to select the optimal approximation function per activation layer. IPTQ-ViT outperforms previous PTQ methods, achieving up to 6.44\%p (avg. 1.78\%p) top-1 accuracy improvement for image classification, 1.0 mAP for object detection. IPTQ-ViT outperforms partial floating-point PTQ methods under W8A8 and W4A8, and achieves accuracy and latency comparable to integer-only QAT methods. We plan to release our code https://github.com/gihwan-kim/IPTQ-ViT.git.

