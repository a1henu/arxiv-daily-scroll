---
layout: default
title: Accelerating Vision Transformers on Brain Processing Unit
---

# Accelerating Vision Transformers on Brain Processing Unit
**arXiv**：[2602.06300v1](https://arxiv.org/abs/2602.06300) · [PDF](https://arxiv.org/pdf/2602.06300.pdf)  
**作者**：Jinchi Tang, Yan Guo  

**一句话要点**：提出卷积化ViT以解决BPU加速Vision Transformer的架构不匹配问题

**关键词**：Vision Transformer, BPU加速, 卷积化, 模型部署, 量化推理

## 3 点简述
- 核心问题：CNN优化的BPU硬件与ViT线性层三维数据计算不匹配，难以利用BPU加速。
- 方法要点：通过设计卷积算子替换ViT中的线性层和层归一化，实现模型重构而不需重新训练。
- 实验或效果：量化DeiT-Base在ImageNet上精度80.4%，推理速度提升3.8倍，验证方法有效性。

## 摘要（原文）

> With the advancement of deep learning technologies, specialized neural processing hardware such as Brain Processing Units (BPUs) have emerged as dedicated platforms for CNN acceleration, offering optimized INT8 computation capabilities for convolutional operations. Meanwhile, Vision Transformer (ViT) models, such as the Data-efficient Image Transformer (DeiT), have demonstrated superior performance and play increasingly crucial roles in computer vision tasks. However, due to the architectural mismatch between CNN-optimized hardware and Vision Transformer computation characteristics--namely, that linear layers in Transformers operate on three-dimensional data while BPU acceleration is designed for four-dimensional convolution operations-it is difficult or even impossible to leverage BPU's advantages when deploying Vision Transformers. To address this challenge, we propose a novel approach that restructures the Vision Transformer by replacing linear layers and layer normalization operations with carefully designed convolutional operators. This enables DeiT to fully utilize the acceleration capabilities of BPUs, while allowing the original weight parameters to be inherited by the restructured models without retraining or fine-tuning. To the best of our knowledge, this is the first successful deployment of Vision Transformers that fully leverages BPU classification datasets demonstrate the effectiveness of our approach. Specifically, the quantized DeiT-Base model achieves 80.4% accuracy on ImageNet, compared to the original 81.8%, while obtaining up to a 3.8* inference speedup. Our finetuned DeiT model on the flower classification dataset also achieves excellent performance, with only a 0.5% accuracy drop for the DeiT-Base model, further demonstrating the effectiveness of our method.

