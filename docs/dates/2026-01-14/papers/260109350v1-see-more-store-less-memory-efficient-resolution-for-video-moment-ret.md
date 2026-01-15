---
layout: default
title: See More, Store Less: Memory-Efficient Resolution for Video Moment Retrieval
---

# See More, Store Less: Memory-Efficient Resolution for Video Moment Retrieval
**arXiv**：[2601.09350v1](https://arxiv.org/abs/2601.09350) · [PDF](https://arxiv.org/pdf/2601.09350.pdf)  
**作者**：Mingyu Jeon, Sungjin Han, Jinkwon Hwang, Minchol Kwon, Jonghee Kim, Junyeong Kim  

**一句话要点**：提出SMORE框架以解决视频时刻检索中的内存效率与信息分辨率权衡问题。

**关键词**：视频时刻检索, 内存效率, 查询引导编码, 自适应压缩, 多模态大语言模型

## 3 点简述
- 核心问题：视频时刻检索因密集帧处理导致内存限制，稀疏采样可能丢失信息。
- 方法要点：使用查询引导字幕、查询感知重要性调制和自适应帧压缩来提升效率。
- 实验或效果：在QVHighlights等基准上实现最先进性能，验证内存高效性。

## 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have improved image recognition and reasoning, but video-related tasks remain challenging due to memory constraints from dense frame processing. Existing Video Moment Retrieval (VMR) methodologies rely on sparse frame sampling, risking potential information loss, especially in lengthy videos. We propose SMORE (See MORE, store less), a framework that enhances memory efficiency while maintaining high information resolution. SMORE (1) uses query-guided captions to encode semantics aligned with user intent, (2) applies query-aware importance modulation to highlight relevant segments, and (3) adaptively compresses frames to preserve key content while reducing redundancy. This enables efficient video understanding without exceeding memory budgets. Experimental validation reveals that SMORE achieves state-of-the-art performance on QVHighlights, Charades-STA, and ActivityNet-Captions benchmarks.

