---
layout: default
title: EvoPrune: Early-Stage Visual Token Pruning for Efficient MLLMs
---

# EvoPrune: Early-Stage Visual Token Pruning for Efficient MLLMs
**arXiv**：[2603.03681v1](https://arxiv.org/abs/2603.03681) · [PDF](https://arxiv.org/pdf/2603.03681.pdf)  
**作者**：Yuhao Chen, Bin Shan, Xin Ye, Cheng Chen  

**一句话要点**：提出EvoPrune以解决MLLMs视觉编码阶段计算效率低的问题

**关键词**：多模态大语言模型, 视觉令牌剪枝, 早期剪枝, 推理加速, 视频理解

## 3 点简述
- 核心问题：MLLMs在高分辨率图像和视频中视觉令牌指数增长导致推理效率低下
- 方法要点：在视觉编码阶段基于令牌相似性、多样性和注意力重要性进行层间剪枝
- 实验或效果：在VideoMME数据集上实现2倍推理加速且性能下降小于1%

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown strong performance in vision-language tasks, but their inference efficiency is severely limited by the exponential growth of visual tokens in complex scenarios such as high-resolution images and videos. Existing visual token pruning methods mainly operate after visual encoding, overlooking the substantial computational cost incurred during the encoding stage. To address this issue, we propose EvoPrune, an early-stage visual token pruning method for MLLMs that performs pruning directly during visual encoding. Specifically, EvoPrune employs a layer-wise pruning strategy guided by token similarity, diversity, and attention-based importance to retain the most informative visual tokens at selected encoding layers. Extensive experiments on image and video benchmarks validate the effectiveness of EvoPrune. In particular, on the VideoMME dataset, EvoPrune achieves 2$\times$ inference speedup with less than 1% performance degradation, demonstrating its potential for latency-sensitive MLLM deployment.

