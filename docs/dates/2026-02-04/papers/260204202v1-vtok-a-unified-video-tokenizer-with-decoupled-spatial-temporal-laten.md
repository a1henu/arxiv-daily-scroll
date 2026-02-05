---
layout: default
title: VTok: A Unified Video Tokenizer with Decoupled Spatial-Temporal Latents
---

# VTok: A Unified Video Tokenizer with Decoupled Spatial-Temporal Latents
**arXiv**：[2602.04202v1](https://arxiv.org/abs/2602.04202) · [PDF](https://arxiv.org/pdf/2602.04202.pdf)  
**作者**：Feng Wang, Yichun Shi, Ceyuan Yang, Qiushan Guo, Jingxiang Sun, Alan Yuille, Peng Wang  

**一句话要点**：提出VTok统一视频分词框架，通过解耦时空表示以提升视频理解与生成任务效率。

**关键词**：视频分词, 时空解耦, 视频理解, 文本到视频生成, 残差编码, 统一框架

## 3 点简述
- 核心问题：现有视频分词方法采用简单帧采样，导致表示复杂度过高，影响任务性能。
- 方法要点：保留关键帧空间特征，将后续帧编码为残差令牌，实现紧凑且表达力强的时空解耦表示。
- 实验或效果：在视频理解和文本到视频生成基准测试中性能显著提升，同时减少令牌序列长度，增强运动连贯性。

## 摘要（原文）

> This work presents VTok, a unified video tokenization framework that can be used for both generation and understanding tasks. Unlike the leading vision-language systems that tokenize videos through a naive frame-sampling strategy, we propose to decouple the spatial and temporal representations of videos by retaining the spatial features of a single key frame while encoding each subsequent frame into a single residual token, achieving compact yet expressive video tokenization. Our experiments suggest that VTok effectively reduces the complexity of video representation from the product of frame count and per-frame token count to their sum, while the residual tokens sufficiently capture viewpoint and motion changes relative to the key frame. Extensive evaluations demonstrate the efficacy and efficiency of VTok: it achieves notably higher performance on a range of video understanding and text-to-video generation benchmarks compared with baselines using naive tokenization, all with shorter token sequences per video (e.g., 3.4% higher accuracy on our TV-Align benchmark and 1.9% higher VBench score). Remarkably, VTok produces more coherent motion and stronger guidance following in text-to-video generation, owing to its more consistent temporal encoding. We hope VTok can serve as a standardized video tokenization paradigm for future research in video understanding and generation.

