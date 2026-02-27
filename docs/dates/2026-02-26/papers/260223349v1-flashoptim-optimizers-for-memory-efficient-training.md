---
layout: default
title: FlashOptim: Optimizers for Memory Efficient Training
---

# FlashOptim: Optimizers for Memory Efficient Training
**arXiv**：[2602.23349v1](https://arxiv.org/abs/2602.23349) · [PDF](https://arxiv.org/pdf/2602.23349.pdf)  
**作者**：Jose Javier Gonzalez Ortiz, Abhay Gupta, Chris Renard, Davis Blalock  

**一句话要点**：提出FlashOptim优化器套件，通过量化技术减少训练内存需求，保持模型质量。

**关键词**：内存高效训练, 优化器量化, 混合精度训练, 模型压缩, 深度学习优化

## 3 点简述
- 标准混合精度训练中，每个参数需多字节内存，限制大模型训练。
- 采用主权重分割和压缩扩展函数，降低8位优化器状态量化误差。
- 实验显示在视觉和语言基准上无质量下降，内存减少超50%。

## 摘要（原文）

> Standard mixed-precision training of neural networks requires many bytes of accelerator memory for each model parameter. These bytes reflect not just the parameter itself, but also its gradient and one or more optimizer state variables. With each of these values typically requiring 4 bytes, training even a 7 billion parameter model can be impractical for researchers with less than 100GB of accelerator memory.
>   We introduce FlashOptim, a suite of optimizations that reduces per-parameter memory by over 50% while preserving model quality and API compatibility. Our approach introduces two key techniques. First, we improve master weight splitting by finding and exploiting a tight bound on its quantization error. Second, we design companding functions that greatly reduce the error in 8-bit optimizer state quantization. Together with 16-bit gradients, these techniques reduce AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release. They also cut model checkpoint sizes by more than half.
>   Experiments with FlashOptim applied to SGD, AdamW, and Lion show no measurable quality degradation on any task from a collection of standard vision and language benchmarks, including Llama-3.1-8B finetuning.

