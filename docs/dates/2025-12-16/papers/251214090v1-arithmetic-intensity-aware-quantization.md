---
layout: default
title: Arithmetic-Intensity-Aware Quantization
---

# Arithmetic-Intensity-Aware Quantization
**arXiv**：[2512.14090v1](https://arxiv.org/abs/2512.14090) · [PDF](https://arxiv.org/pdf/2512.14090.pdf)  
**作者**：Taig Singh, Shreshth Rajan, Nikhil Iyer  

**一句话要点**：提出算术强度感知量化以优化内存受限神经网络推理吞吐量

**关键词**：混合精度量化, 算术强度优化, 后训练量化, 内存带宽优化, 神经网络推理加速

## 3 点简述
- 核心问题：现代神经网络推理受DRAM带宽限制，而非计算能力。
- 方法要点：采用混合精度量化，通过搜索算法选择每层位宽以最大化算术强度并最小化精度损失。
- 实验或效果：在ResNet-20/CIFAR-10上算术强度提升约50%，MobileNetV2推理吞吐量提高1.66倍，精度损失控制在约1个百分点内。

## 摘要（原文）

> As modern neural networks become increasingly memory-bound, inference throughput is limited by DRAM bandwidth rather than compute. We present Arithmetic-Intensity-Aware Quantization (AIQ), a mixed precision quantization framework that chooses per-layer bit-widths to maximize arithmetic intensity (AI) while minimizing accuracy loss. AIQ is a post-training quantization method that uses search algorithms over per-layer quantization schemes to minimize a weighted loss over AI and accuracy. On ResNet-20/CIFAR-10, AIQ increases AI by ~50% over an FP32 baseline while keeping test accuracy within ~1 percentage point, and outperforming global uniform quantization schemes. On a memory-bound MobileNetV2 architecture, AIQ configurations give a 1.66x higher throughput than the FP32 baseline while keeping test accuracy within 1 percentage point. We also find that AIQ naturally quantizes larger layers more aggressively.

