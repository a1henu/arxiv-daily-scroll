---
layout: default
title: Zero-shot Low-Field MRI Enhancement via Diffusion-Based Adaptive Contrast Transport
---

# Zero-shot Low-Field MRI Enhancement via Diffusion-Based Adaptive Contrast Transport
**arXiv**：[2603.01913v1](https://arxiv.org/abs/2603.01913) · [PDF](https://arxiv.org/pdf/2603.01913.pdf)  
**作者**：Muyu Liu, Chenhe Du, Xuanyu Tian, Qing Wu, Xiao Wang, Haonan Zhang, Hongjiang Wei, Yuyao Zhang  

**一句话要点**：提出DACT零样本框架，通过扩散模型和最优传输解决低场MRI增强问题。

**关键词**：零样本学习, MRI增强, 扩散模型, 最优传输, 对比度校正, 医学图像重建

## 3 点简述
- 核心问题：低场MRI图像质量差，缺乏配对数据，对比度变换未知，现有方法假设线性退化效果不佳。
- 方法要点：结合预训练扩散先验和物理引导前向模型，使用可微Sinkhorn最优传输模块动态学习对比度映射。
- 实验或效果：在模拟和真实临床数据集上验证，DACT实现最先进性能，恢复结构细节和正确组织对比度。

## 摘要（原文）

> Low-field (LF) magnetic resonance imaging (MRI) democratizes access to diagnostic imaging but is fundamentally limited by low signal-to-noise ratio and significant tissue contrast distortion due to field-dependent relaxation dynamics. Reconstructing high-field (HF) quality images from LF data is a blind inverse problem, severely challenged by the scarcity of paired training data and the unknown, non-linear contrast transformation operator. Existing zero-shot methods, which assume simplified linear degradation, often fail to recover authentic tissue contrast. In this paper, we propose DACT(Diffusion-Based Adaptive Contrast Transport), a novel zero-shot framework that restores HF-quality images without paired supervision. DACT synergizes a pre-trained HF diffusion prior to ensure anatomical fidelity with a physically-informed adaptive forward model. Specifically, we introduce a differentiable Sinkhorn optimal transport module that explicitly models and corrects the intensity distribution shift between LF and HF domains during the reverse diffusion process. This allows the framework to dynamically learn the intractable contrast mapping while preserving topological consistency. Extensive experiments on simulated and real clinical LF datasets demonstrate that DACT achieves state-of-the-art performance, yielding reconstructions with superior structural detail and correct tissue contrast.

