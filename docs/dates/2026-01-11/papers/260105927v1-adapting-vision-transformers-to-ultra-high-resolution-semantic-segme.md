---
layout: default
title: Adapting Vision Transformers to Ultra-High Resolution Semantic Segmentation with Relay Tokens
---

# Adapting Vision Transformers to Ultra-High Resolution Semantic Segmentation with Relay Tokens
**arXiv**：[2601.05927v1](https://arxiv.org/abs/2601.05927) · [PDF](https://arxiv.org/pdf/2601.05927.pdf)  
**作者**：Yohann Perron, Vladyslav Sydorov, Christophe Pottier, Loic Landrieu  

**一句话要点**：提出Relay Tokens方法，以解决超高分辨率图像语义分割中全局上下文与局部细节的平衡问题。

**关键词**：超高分辨率语义分割, 视觉Transformer, 多尺度推理, 中继令牌, 全局上下文, 局部细节

## 3 点简述
- 核心问题：现有方法在超高分辨率分割中，滑动窗口丢弃全局上下文，下采样丢失细节。
- 方法要点：并行处理局部高分辨率小裁剪和全局低分辨率大裁剪，通过可学习中继令牌聚合特征。
- 实验或效果：在多个基准测试中实现一致提升，相对mIoU最高提升15%，参数增加少于2%。

## 摘要（原文）

> Current approaches for segmenting ultra high resolution images either slide a window, thereby discarding global context, or downsample and lose fine detail. We propose a simple yet effective method that brings explicit multi scale reasoning to vision transformers, simultaneously preserving local details and global awareness. Concretely, we process each image in parallel at a local scale (high resolution, small crops) and a global scale (low resolution, large crops), and aggregate and propagate features between the two branches with a small set of learnable relay tokens. The design plugs directly into standard transformer backbones (eg ViT and Swin) and adds fewer than 2 % parameters. Extensive experiments on three ultra high resolution segmentation benchmarks, Archaeoscape, URUR, and Gleason, and on the conventional Cityscapes dataset show consistent gains, with up to 15 % relative mIoU improvement. Code and pretrained models are available at https://archaeoscape.ai/work/relay-tokens/ .

