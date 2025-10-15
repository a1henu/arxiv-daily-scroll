---
layout: default
title: ViCO: A Training Strategy towards Semantic Aware Dynamic High-Resolution
---

# ViCO: A Training Strategy towards Semantic Aware Dynamic High-Resolution
**arXiv**：[2510.12793v1](https://arxiv.org/abs/2510.12793) · [PDF](https://arxiv.org/pdf/2510.12793.pdf)  
**作者**：Long Cui, Weiyun Wang, Jie Shao, Zichen Wen, Gen Luo, Linfeng Zhang, Yanting Zhang, Yu Qiao, Wenhai Wang  

**一句话要点**：提出ViCO训练策略，通过语义感知动态调整视觉令牌数量以降低MLLM推理成本

**关键词**：多模态大语言模型, 视觉令牌压缩, 语义复杂度, 动态高分辨率, 推理效率优化

## 3 点简述
- 核心问题：多模态大语言模型因图像输入增加视觉令牌，导致推理成本上升
- 方法要点：使用多MLP连接器基于语义复杂度压缩视觉令牌，并最小化KL散度
- 实验或效果：减少视觉令牌达50%，保持感知、推理和OCR能力

## 摘要（原文）

> Existing Multimodal Large Language Models (MLLMs) suffer from increased
> inference costs due to the additional vision tokens introduced by image inputs.
> In this work, we propose Visual Consistency Learning (ViCO), a novel training
> algorithm that enables the model to represent images of varying semantic
> complexities using different numbers of vision tokens. The key idea behind our
> method is to employ multiple MLP connectors, each with a different image
> compression ratio, to downsample the vision tokens based on the semantic
> complexity of the image. During training, we minimize the KL divergence between
> the responses conditioned on different MLP connectors. At inference time, we
> introduce an image router, termed Visual Resolution Router (ViR), that
> automatically selects the appropriate compression rate for each image patch.
> Compared with existing dynamic high-resolution strategies, which adjust the
> number of visual tokens based on image resolutions, our method dynamically
> adapts the number of visual tokens according to semantic complexity.
> Experimental results demonstrate that our method can reduce the number of
> vision tokens by up to 50% while maintaining the model's perception, reasoning,
> and OCR capabilities. We hope this work will contribute to the development of
> more efficient MLLMs. The code and models will be released to facilitate future
> research.

