---
layout: default
title: ARCQuant: Boosting NVFP4 Quantization with Augmented Residual Channels for LLMs
---

# ARCQuant: Boosting NVFP4 Quantization with Augmented Residual Channels for LLMs
**arXiv**：[2601.07475v1](https://arxiv.org/abs/2601.07475) · [PDF](https://arxiv.org/pdf/2601.07475.pdf)  
**作者**：Haoqian Meng, Yilun Luo, Yafei Zhao, Wenyuan Liu, Peng Zhang, Xindian Ma  

**一句话要点**：提出ARCQuant框架，通过增强残差通道提升NVFP4量化性能，用于大语言模型高效推理。

**关键词**：大语言模型量化, NVFP4格式, 后训练量化, 残差通道增强, 高效推理, GPU加速

## 3 点简述
- 核心问题：现有后训练量化方法难以适配NVFP4等细粒度数值格式，导致精度损失或硬件冲突。
- 方法要点：采用增强残差通道设计，在激活矩阵中引入量化残差通道，保持统一NVFP4格式并集成误差补偿。
- 实验或效果：在LLaMA和Qwen模型上实现与全精度基线相当的精度，GPU部署获得高达3倍加速。

## 摘要（原文）

> The emergence of fine-grained numerical formats like NVFP4 presents new opportunities for efficient Large Language Model (LLM) inference. However, it is difficult to adapt existing Post-Training Quantization (PTQ) strategies to these formats: rotation-based methods compromise fine-grained block isolation; smoothing techniques struggle with significant 4-bit quantization errors; and mixed-precision approaches often conflict with hardware constraints on unified-precision computation. To address these challenges, we propose ARCQuant, a framework that boosts NVFP4 performance via Augmented Residual Channels. Distinct from methods that compromise block isolation or hardware uniformity, ARCQuant maintains a strictly unified NVFP4 format by augmenting the activation matrix with quantized residual channels. This design integrates the error compensation process directly into the matrix reduction dimension, enabling the use of standard, highly optimized GEMM kernels with minimal overhead. Theoretical analysis confirms that the worst-case error bound of our dual-stage NVFP4 quantization is comparable to that of standard 8-bit formats such as MXFP8. Extensive experiments on LLaMA and Qwen models demonstrate that ARCQuant achieves state-of-the-art accuracy, comparable to full-precision baselines in perplexity and downstream tasks. Furthermore, deployment on RTX 5090 and RTX PRO 6000 GPUs confirms practical benefits, achieving up to 3x speedup over FP16. Our code is available at https://github.com/actypedef/ARCQuant .

