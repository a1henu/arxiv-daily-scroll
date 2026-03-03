---
layout: default
title: From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck for Long-Horizon Video Agents
---

# From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck for Long-Horizon Video Agents
**arXiv**：[2603.01455v1](https://arxiv.org/abs/2603.01455) · [PDF](https://arxiv.org/pdf/2603.01455.pdf)  
**作者**：Niu Lian, Yuting Wang, Hanshu Yao, Jinpeng Wang, Bin Chen, Yaowei Wang, Min Zhang, Shu-Tao Xia  

**一句话要点**：提出MM-Mem金字塔多模态记忆架构，通过语义信息瓶颈优化长视频理解任务。

**关键词**：长视频理解, 多模态记忆, 语义信息瓶颈, 金字塔架构, 模糊痕迹理论

## 3 点简述
- 核心问题：多模态大语言模型在长视频理解中受限于上下文窗口和静态记忆机制，导致效率低下和细节丢失。
- 方法要点：基于模糊痕迹理论构建分层记忆，包括感官缓冲、情节流和符号模式，并引入语义信息瓶颈目标进行动态压缩。
- 实验或效果：在4个基准测试中验证了MM-Mem在离线和流式任务上的有效性，展示了鲁棒泛化能力。

## 摘要（原文）

> While multimodal large language models have demonstrated impressive short-term reasoning, they struggle with long-horizon video understanding due to limited context windows and static memory mechanisms that fail to mirror human cognitive efficiency. Existing paradigms typically fall into two extremes: vision-centric methods that incur high latency and redundancy through dense visual accumulation, or text-centric approaches that suffer from detail loss and hallucination via aggressive captioning. To bridge this gap, we propose MM-Mem, a pyramidal multimodal memory architecture grounded in Fuzzy-Trace Theory. MM-Mem structures memory hierarchically into a Sensory Buffer, Episodic Stream, and Symbolic Schema, enabling the progressive distillation of fine-grained perceptual traces (verbatim) into high-level semantic schemas (gist). Furthermore, to govern the dynamic construction of memory, we derive a Semantic Information Bottleneck objective and introduce SIB-GRPO to optimize the trade-off between memory compression and task-relevant information retention. In inference, we design an entropy-driven top-down memory retrieval strategy, which first tries with the abstract Symbolic Schema and progressively "drills down" to the Sensory Buffer and Episodic Stream under high uncertainty. Extensive experiments across 4 benchmarks confirm the effectiveness of MM-Mem on both offline and streaming tasks, demonstrating robust generalization and validating the effectiveness of cognition-inspired memory organization. Code is available at https://github.com/EliSpectre/MM-Mem.

