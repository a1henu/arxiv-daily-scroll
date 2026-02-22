---
layout: default
title: EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection
---

# EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection
**arXiv**：[2602.17260v1](https://arxiv.org/abs/2602.17260) · [PDF](https://arxiv.org/pdf/2602.17260.pdf)  
**作者**：Hung Mai, Loi Dinh, Duc Hai Nguyen, Dat Do, Luong Doan, Khanh Nguyen Quoc, Huan Vu, Phong Ho, Naeem Ul Islam, Tuan Do  

**一句话要点**：提出EA-Swin模型以解决AI生成视频检测中现有方法依赖浅层嵌入或计算重的问题。

**关键词**：AI生成视频检测, Swin Transformer, 时空依赖建模, 因子化窗口注意力, 跨分布评估, 视频嵌入

## 3 点简述
- 核心问题：现有检测方法依赖浅层嵌入轨迹、图像适应或计算重的MLLMs，难以应对高度逼真的合成视频。
- 方法要点：EA-Swin通过因子化窗口注意力设计，直接在预训练视频嵌入上建模时空依赖，兼容通用ViT风格编码器。
- 实验或效果：在EA-Video数据集上，EA-Swin达到0.97-0.99准确率，优于先前方法5-20%，并保持对未见分布的强泛化能力。

## 摘要（原文）

> Recent advances in foundation video generators such as Sora2, Veo3, and other commercial systems have produced highly realistic synthetic videos, exposing the limitations of existing detection methods that rely on shallow embedding trajectories, image-based adaptation, or computationally heavy MLLMs. We propose EA-Swin, an Embedding-Agnostic Swin Transformer that models spatiotemporal dependencies directly on pretrained video embeddings via a factorized windowed attention design, making it compatible with generic ViT-style patch-based encoders. Alongside the model, we construct the EA-Video dataset, a benchmark dataset comprising 130K videos that integrates newly collected samples with curated existing datasets, covering diverse commercial and open-source generators and including unseen-generator splits for rigorous cross-distribution evaluation. Extensive experiments show that EA-Swin achieves 0.97-0.99 accuracy across major generators, outperforming prior SoTA methods (typically 0.8-0.9) by a margin of 5-20%, while maintaining strong generalization to unseen distributions, establishing a scalable and robust solution for modern AI-generated video detection.

