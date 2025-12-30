---
layout: default
title: Iterative Inference-time Scaling with Adaptive Frequency Steering for Image Super-Resolution
---

# Iterative Inference-time Scaling with Adaptive Frequency Steering for Image Super-Resolution
**arXiv**：[2512.23532v1](https://arxiv.org/abs/2512.23532) · [PDF](https://arxiv.org/pdf/2512.23532.pdf)  
**作者**：Hexin Zhang, Dong Li, Jie Huang, Bingzhou Wang, Xueyang Fu, Zhengjun Zha  

**一句话要点**：提出IAFS框架以解决扩散模型在图像超分辨率中感知质量与结构保真度的平衡问题

**关键词**：图像超分辨率, 扩散模型, 推理时间缩放, 频率引导, 迭代精炼

## 3 点简述
- 核心问题：现有扩散模型在图像超分辨率中难以同时保证高频感知质量和低频结构保真度
- 方法要点：通过迭代推理时间缩放和自适应频率引导，结合迭代精炼与频率感知粒子融合
- 实验或效果：在多个扩散模型上验证，IAFS有效缓解感知-保真度冲突，提升细节和结构准确性

## 摘要（原文）

> Diffusion models have become a leading paradigm for image super-resolution (SR), but existing methods struggle to guarantee both the high-frequency perceptual quality and the low-frequency structural fidelity of generated images. Although inference-time scaling can theoretically improve this trade-off by allocating more computation, existing strategies remain suboptimal: reward-driven particle optimization often causes perceptual over-smoothing, while optimal-path search tends to lose structural consistency. To overcome these difficulties, we propose Iterative Diffusion Inference-Time Scaling with Adaptive Frequency Steering (IAFS), a training-free framework that jointly leverages iterative refinement and frequency-aware particle fusion. IAFS addresses the challenge of balancing perceptual quality and structural fidelity by progressively refining the generated image through iterative correction of structural deviations. Simultaneously, it ensures effective frequency fusion by adaptively integrating high-frequency perceptual cues with low-frequency structural information, allowing for a more accurate and balanced reconstruction across different image details. Extensive experiments across multiple diffusion-based SR models show that IAFS effectively resolves the perception-fidelity conflict, yielding consistently improved perceptual detail and structural accuracy, and outperforming existing inference-time scaling methods.

