---
layout: default
title: WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning
---

# WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning
**arXiv**：[2512.02425v1](https://arxiv.org/abs/2512.02425) · [PDF](https://arxiv.org/pdf/2512.02425.pdf)  
**作者**：Woongyeong Yeo, Kangsan Kim, Jaehong Yoon, Sung Ju Hwang  

**一句话要点**：提出WorldMM动态多模态记忆代理，以解决长视频推理中上下文容量有限和视觉细节丢失的问题。

**关键词**：长视频推理, 多模态记忆, 动态检索, 视频问答, 记忆增强

## 3 点简述
- 核心问题：现有视频大语言模型在长视频推理中受限于上下文容量，且依赖文本摘要导致视觉证据利用不足。
- 方法要点：构建多模态记忆，包括跨多时间尺度的情节记忆、持续更新的语义记忆和保留细节的视觉记忆。
- 实验或效果：在五个长视频问答基准上显著优于现有基线，平均性能提升8.4%。

## 摘要（原文）

> Recent advances in video large language models have demonstrated strong capabilities in understanding short clips. However, scaling them to hours- or days-long videos remains highly challenging due to limited context capacity and the loss of critical visual details during abstraction. Existing memory-augmented methods mitigate this by leveraging textual summaries of video segments, yet they heavily rely on text and fail to utilize visual evidence when reasoning over complex scenes. Moreover, retrieving from fixed temporal scales further limits their flexibility in capturing events that span variable durations. To address this, we introduce WorldMM, a novel multimodal memory agent that constructs and retrieves from multiple complementary memories, encompassing both textual and visual representations. WorldMM comprises three types of memory: episodic memory indexes factual events across multiple temporal scales, semantic memory continuously updates high-level conceptual knowledge, and visual memory preserves detailed information about scenes. During inference, an adaptive retrieval agent iteratively selects the most relevant memory source and leverages multiple temporal granularities based on the query, continuing until it determines that sufficient information has been gathered. WorldMM significantly outperforms existing baselines across five long video question-answering benchmarks, achieving an average 8.4% performance gain over previous state-of-the-art methods, showing its effectiveness on long video reasoning.

