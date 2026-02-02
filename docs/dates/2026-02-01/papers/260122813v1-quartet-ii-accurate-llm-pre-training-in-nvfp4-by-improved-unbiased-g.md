---
layout: default
title: Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation
---

# Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation
**arXiv**：[2601.22813v1](https://arxiv.org/abs/2601.22813) · [PDF](https://arxiv.org/pdf/2601.22813.pdf)  
**作者**：Andrei Panferov, Erik Schultheis, Soroush Tabesh, Dan Alistarh  

**一句话要点**：提出Quartet II方案，通过MS-EDEN量化方法提升NVFP4格式下LLM预训练的精度与效率。

**关键词**：低精度训练, 量化梯度估计, LLM预训练, NVFP4格式, 硬件加速

## 3 点简述
- NVFP4格式支持端到端量化预训练，但现有方法因使用随机舍入牺牲精度。
- 引入MS-EDEN量化方法，量化误差比随机舍入降低2倍以上，集成到Quartet II方案中。
- 实验验证在1.9B参数LLM训练中有效，提供Blackwell GPU内核，速度提升达4.2倍。

## 摘要（原文）

> The NVFP4 lower-precision format, supported in hardware by NVIDIA Blackwell GPUs, promises to allow, for the first time, end-to-end fully-quantized pre-training of massive models such as LLMs. Yet, existing quantized training methods still sacrifice some of the representation capacity of this format in favor of more accurate unbiased quantized gradient estimation by stochastic rounding (SR), losing noticeable accuracy relative to standard FP16 and FP8 training. In this paper, improve the state of the art for quantized training in NVFP4 via a novel unbiased quantization routine for micro-scaled formats, called MS-EDEN, that has more than 2x lower quantization error than SR. We integrate it into a novel fully-NVFP4 quantization scheme for linear layers, called Quartet II. We show analytically that Quartet II achieves consistently better gradient estimation across all major matrix multiplications, both on the forward and on the backward passes. In addition, our proposal synergizes well with recent training improvements aimed specifically at NVFP4. We further validate Quartet II on end-to-end LLM training with up to 1.9B parameters on 38B tokens. We provide kernels for execution on NVIDIA Blackwell GPUs with up to 4.2x speedup over BF16. Our code is available at https://github.com/IST-DASLab/Quartet-II .

