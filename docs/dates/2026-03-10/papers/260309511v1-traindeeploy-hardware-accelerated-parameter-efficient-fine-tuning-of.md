---
layout: default
title: TrainDeeploy: Hardware-Accelerated Parameter-Efficient Fine-Tuning of Small Transformer Models at the Extreme Edge
---

# TrainDeeploy: Hardware-Accelerated Parameter-Efficient Fine-Tuning of Small Transformer Models at the Extreme Edge
**arXiv**：[2603.09511v1](https://arxiv.org/abs/2603.09511) · [PDF](https://arxiv.org/pdf/2603.09511.pdf)  
**作者**：Run Wang, Victor J. B. Jung, Philip Wiese, Francesco Conti, Alessio Burrello, Luca Benini  

**一句话要点**：提出TrainDeeploy框架，在超低功耗边缘SoC上实现参数高效微调，支持CNN和Transformer模型。

**关键词**：边缘计算, 参数高效微调, Transformer模型, 超低功耗SoC, LoRA, 设备端训练

## 3 点简述
- 核心问题：边缘设备上反向传播的计算和内存需求高，限制了深度神经网络的设备端调优。
- 方法要点：统一高效推理和设备端训练，支持选择性层微调和LoRA等策略，减少参数和内存使用。
- 实验或效果：在RISC-V SoC上实现CCT端到端微调，LoRA降低动态内存23%，减少可训练参数15倍。

## 摘要（原文）

> On-device tuning of deep neural networks enables long-term adaptation at the edge while preserving data privacy. However, the high computational and memory demands of backpropagation pose significant challenges for ultra-low-power, memory-constrained extreme-edge devices. These challenges are further amplified for attention-based models due to their architectural complexity and computational scale. We present TrainDeeploy, a framework that unifies efficient inference and on-device training on heterogeneous ultra-low-power System-on-Chips (SoCs). TrainDeeploy provides the first complete on-device training pipeline for extreme-edge SoCs supporting both Convolutional Neural Networks (CNNs) and Transformer models, together with multiple training strategies such as selective layer-wise fine-tuning and Low-Rank Adaptation (LoRA). On a RISC-V-based heterogeneous SoC, we demonstrate the first end-to-end on-device fine-tuning of a Compact Convolutional Transformer (CCT), achieving up to 11 trained images per second. We show that LoRA reduces dynamic memory usage by 23%, decreases the number of trainable parameters and gradients by 15x, and reduces memory transfer volume by 1.6x compared to full backpropagation. TrainDeeploy achieves up to 4.6 FLOP/cycle on CCT (0.28M parameters, 71-126M FLOPs) and up to 13.4 FLOP/cycle on Deep-AE (0.27M parameters, 0.8M FLOPs), while expanding the scope of prior frameworks to support both CNN and Transformer models with parameter-efficient tuning on extreme-edge platforms.

