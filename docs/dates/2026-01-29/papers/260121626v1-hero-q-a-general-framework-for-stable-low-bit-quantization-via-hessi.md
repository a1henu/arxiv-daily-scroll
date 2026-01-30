---
layout: default
title: HeRo-Q: A General Framework for Stable Low Bit Quantization via Hessian Conditioning
---

# HeRo-Q: A General Framework for Stable Low Bit Quantization via Hessian Conditioning
**arXiv**：[2601.21626v1](https://arxiv.org/abs/2601.21626) · [PDF](https://arxiv.org/pdf/2601.21626.pdf)  
**作者**：Jinhao Zhang Yunquan Zhang, Zicheng yan, Boyang Zhang, Jun Sun, Daning Cheng  

**一句话要点**：提出HeRo-Q框架，通过Hessian条件化解决低比特量化中的稳定性问题。

**关键词**：后训练量化, Hessian矩阵, 低比特压缩, 模型鲁棒性, 旋转-压缩矩阵, 量化噪声

## 3 点简述
- 核心问题：PTQ因仅最小化量化误差导致'低误差高损失'现象，源于损失景观Hessian矩阵的高曲率方向敏感。
- 方法要点：引入轻量可学习的旋转-压缩矩阵，在量化前重塑权重空间，降低Hessian最大特征值以增强鲁棒性。
- 实验效果：在Llama和Qwen模型上优于GPTQ等方法，在W3A16超低比特设置下提升GSM8K准确率至70.15%，避免逻辑崩溃。

## 摘要（原文）

> Post Training Quantization (PTQ), a mainstream model compression technique, often leads to the paradoxical 'low error, high loss' phenomenon because it focuses solely on minimizing quantization error. The root cause lies in the Hessian matrix of the LLM loss landscape: a few high curvature directions are extremely sensitive to perturbations. To address this, we propose the Hessian Robust Quantization (HeRo Q) algorithm, which applies a lightweight, learnable rotation-compression matrix to the weight space prior to quantization. This joint framework reshapes the loss landscape by reducing the largest Hessian eigenvalue and reducing its max eigenvalue, thereby significantly enhancing robustness to quantization noise. HeRo-Q requires no architectural modifications, incurs negligible computational overhead, and integrates seamlessly into existing PTQ pipelines. Experiments on Llama and Qwen models show that HeRo Q consistently outperforms state of the art methods including GPTQ, AWQ, and SpinQuant not only achieving superior performance under standard W4A8 settings, but also excelling in the highly challenging W3A16 ultra low bit regime, where it boosts GSM8K accuracy on Llama3 8B to 70.15\% and effectively avoids the logical collapse commonly seen in aggressive quantization.

