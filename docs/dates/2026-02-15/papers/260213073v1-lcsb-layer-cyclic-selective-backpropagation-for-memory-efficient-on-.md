---
layout: default
title: LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning
---

# LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning
**arXiv**：[2602.13073v1](https://arxiv.org/abs/2602.13073) · [PDF](https://arxiv.org/pdf/2602.13073.pdf)  
**作者**：Juneyoung Park, Eunbeen Yoon, Seongwan Kim. Jaeho Lee  

**一句话要点**：提出层循环选择性反向传播以解决移动设备上大语言模型微调的内存效率问题

**关键词**：内存高效反向传播, 移动设备微调, 层循环选择性反向传播, LoRA参数空间, 4位量化稳定性, 隐式正则化

## 3 点简述
- 核心问题：内存高效反向传播在移动设备上微调大语言模型时，全层反向计算导致时间开销大，权重解压占比较高。
- 方法要点：通过每步仅计算部分层的梯度，利用残差连接保证梯度流，AdamW动量提供隐式更新，理论解释为LoRA参数空间的块坐标下降。
- 实验或效果：在五个模型和三个任务上实现最高1.40倍加速，质量下降小于2%，4位量化设置下表现出更好的稳定性和隐式正则化效果。

## 摘要（原文）

> Memory-efficient backpropagation (MeBP) has enabled first-order fine-tuning of large language models (LLMs) on mobile devices with less than 1GB memory. However, MeBP requires backward computation through all transformer layers at every step, where weight decompression alone accounts for 32--42% of backward time. We propose Layer-Cyclic Selective Backpropagation (LCSB), which computes gradients for only a subset of layers per step. Our key insight is that residual connections guarantee gradient flow through identity paths, while AdamW momentum provides implicit updates for non-selected layers. We interpret LCSB as Block Coordinate Descent on the LoRA parameter space, providing theoretical justification for convergence. LCSB achieves up to 1.40$\times$ speedup with less than 2\% quality degradation across five models and three tasks. Surprisingly, in 4-bit quantized settings, LCSB exhibits superior stability: a 3B model that completely diverges under full backpropagation converges smoothly with LCSB, suggesting an implicit regularization effect from selective gradient computation.

