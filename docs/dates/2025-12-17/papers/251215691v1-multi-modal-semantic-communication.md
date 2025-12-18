---
layout: default
title: Multi-Modal Semantic Communication
---

# Multi-Modal Semantic Communication
**arXiv**：[2512.15691v1](https://arxiv.org/abs/2512.15691) · [PDF](https://arxiv.org/pdf/2512.15691.pdf)  
**作者**：Matin Mortaheb, Erciyes Karakaya, Sennur Ulukus  

**一句话要点**：提出多模态语义通信框架，通过文本查询引导信息提取以提升复杂场景下的通信效率。

**关键词**：语义通信, 多模态融合, 跨模态注意力, 自适应传输, 带宽优化

## 3 点简述
- 核心问题：传统基于自注意力的语义通信在复杂多物体场景中缺乏任务指导，导致信息提取不精准。
- 方法要点：集成文本查询与视觉特征，使用跨模态注意力机制生成软相关性分数，自适应传输图像块。
- 实验或效果：在带宽受限环境下实现高效语义通信，总比特率匹配信道容量，保留任务关键信息。

## 摘要（原文）

> Semantic communication aims to transmit information most relevant to a task rather than raw data, offering significant gains in communication efficiency for applications such as telepresence, augmented reality, and remote sensing. Recent transformer-based approaches have used self-attention maps to identify informative regions within images, but they often struggle in complex scenes with multiple objects, where self-attention lacks explicit task guidance. To address this, we propose a novel Multi-Modal Semantic Communication framework that integrates text-based user queries to guide the information extraction process. Our proposed system employs a cross-modal attention mechanism that fuses visual features with language embeddings to produce soft relevance scores over the visual data. Based on these scores and the instantaneous channel bandwidth, we use an algorithm to transmit image patches at adaptive resolutions using independently trained encoder-decoder pairs, with total bitrate matching the channel capacity. At the receiver, the patches are reconstructed and combined to preserve task-critical information. This flexible and goal-driven design enables efficient semantic communication in complex and bandwidth-constrained environments.

