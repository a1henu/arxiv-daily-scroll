---
layout: default
title: Sharp Eyes and Memory for VideoLLMs: Information-Aware Visual Token Pruning for Efficient and Reliable VideoLLM Reasoning
---

# Sharp Eyes and Memory for VideoLLMs: Information-Aware Visual Token Pruning for Efficient and Reliable VideoLLM Reasoning
**arXiv**：[2511.08003v1](https://arxiv.org/abs/2511.08003) · [PDF](https://arxiv.org/pdf/2511.08003.pdf)  
**作者**：Jialong Qin, Xin Zou, Di Lu, Yibo Yan, Xuming Hu  

**一句话要点**：提出SharpV以解决VideoLLMs中视觉令牌冗余导致的效率问题

**关键词**：视频大语言模型, 视觉令牌剪枝, KV缓存优化, 自适应压缩, 信息瓶颈, 硬件加速兼容

## 3 点简述
- 核心问题：VideoLLMs因处理冗余视觉令牌导致计算复杂度和KV缓存增长
- 方法要点：基于时空信息动态调整剪枝比例，并自校准剪枝退化特征
- 实验或效果：在多个基准测试中表现优越，无需注意力分数即可兼容硬件加速

## 摘要（原文）

> Current Video Large Language Models (VideoLLMs) suffer from quadratic computational complexity and key-value cache scaling, due to their reliance on processing excessive redundant visual tokens. To address this problem, we propose SharpV, a minimalist and efficient method for adaptive pruning of visual tokens and KV cache. Different from most uniform compression approaches, SharpV dynamically adjusts pruning ratios based on spatial-temporal information. Remarkably, this adaptive mechanism occasionally achieves performance gains over dense models, offering a novel paradigm for adaptive pruning. During the KV cache pruning stage, based on observations of visual information degradation, SharpV prunes degraded visual features via a self-calibration manner, guided by similarity to original visual features. In this way, SharpV achieves hierarchical cache pruning from the perspective of information bottleneck, offering a new insight into VideoLLMs' information flow. Experiments on multiple public benchmarks demonstrate the superiority of SharpV. Moreover, to the best of our knowledge, SharpV is notably the first two-stage pruning framework that operates without requiring access to exposed attention scores, ensuring full compatibility with hardware acceleration techniques like Flash Attention.

