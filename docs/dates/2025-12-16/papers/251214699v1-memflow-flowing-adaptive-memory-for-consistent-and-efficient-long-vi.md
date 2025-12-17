---
layout: default
title: MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives
---

# MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives
**arXiv**：[2512.14699v1](https://arxiv.org/abs/2512.14699) · [PDF](https://arxiv.org/pdf/2512.14699.pdf)  
**作者**：Sihui Ji, Xi Chen, Shuai Yang, Xin Tao, Pengfei Wan, Hengshuang Zhao  

**一句话要点**：提出MemFlow以解决流式视频生成中长上下文内容一致性问题，通过动态记忆检索提升效率。

**关键词**：流式视频生成, 长上下文一致性, 动态记忆检索, 注意力机制, KV缓存兼容

## 3 点简述
- 核心问题：流式视频生成需保持长上下文内容一致性，现有方法使用固定策略压缩历史帧，难以适应不同生成块的需求。
- 方法要点：在生成新块前，根据文本提示动态检索最相关历史帧更新记忆库，并在注意力层仅激活相关令牌，保证叙事连贯与效率。
- 实验或效果：MemFlow在保持与任何流式视频生成模型兼容的同时，实现出色一致性，计算负担可忽略（相比无记忆基线仅减速7.9%）。

## 摘要（原文）

> The core challenge for streaming video generation is maintaining the content consistency in long context, which poses high requirement for the memory design. Most existing solutions maintain the memory by compressing historical frames with predefined strategies. However, different to-generate video chunks should refer to different historical cues, which is hard to satisfy with fixed strategies. In this work, we propose MemFlow to address this problem. Specifically, before generating the coming chunk, we dynamically update the memory bank by retrieving the most relevant historical frames with the text prompt of this chunk. This design enables narrative coherence even if new event happens or scenario switches in future frames. In addition, during generation, we only activate the most relevant tokens in the memory bank for each query in the attention layers, which effectively guarantees the generation efficiency. In this way, MemFlow achieves outstanding long-context consistency with negligible computation burden (7.9% speed reduction compared with the memory-free baseline) and keeps the compatibility with any streaming video generation model with KV cache.

