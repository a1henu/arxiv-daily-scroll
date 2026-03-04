---
layout: default
title: Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models
---

# Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models
**arXiv**：[2603.02872v1](https://arxiv.org/abs/2603.02872) · [PDF](https://arxiv.org/pdf/2603.02872.pdf)  
**作者**：Jialiang Zhang, Junlong Tong, Junyan Lin, Hao Wu, Yirong Sun, Yunpu Ma, Xiaoyu Shen  

**一句话要点**：提出Think-as-You-See框架，实现大视觉语言模型在视频流中的实时链式推理

**关键词**：视频流推理, 链式思维, 大视觉语言模型, 并行推理, 实时视频理解

## 3 点简述
- 现有LVLMs的链式推理依赖完整视频输入，与真实视频流数据顺序到达的特性不匹配
- 提出TaYS框架，通过并行化CoT生成、流约束训练和流并行推理实现真正并发推理
- 在Qwen2.5-VL模型上验证，TaYS在推理性能提升的同时显著降低首词时间和整体延迟

## 摘要（原文）

> Large Vision Language Models (LVLMs) exhibit strong Chain-of-Thought (CoT) capabilities, yet most existing paradigms assume full-video availability before inference, a batch-style process misaligned with real-world video streams where information arrives sequentially. Motivated by the streaming nature of video data, we investigate two streaming reasoning paradigms for LVLMs. The first, an interleaved paradigm, alternates between receiving frames and producing partial reasoning but remains constrained by strictly ordered cache updates. To better match streaming inputs, we propose \textbf{Think-as-You-See (TaYS)}, a unified framework enabling true concurrent reasoning. TaYS integrates parallelized CoT generation, stream-constrained training, and stream-parallel inference. It further employs temporally aligned reasoning units, streaming attention masks and positional encodings, and a dual KV-cache that decouples visual encoding from textual reasoning. We evaluate all paradigms on the Qwen2.5-VL family across representative video CoT tasks, including event dynamics analysis, causal reasoning, and thematic understanding. Experiments show that TaYS consistently outperforms both batch and interleaved baselines, improving reasoning performance while substantially reducing time-to-first-token (TTFT) and overall reasoning delay. These results demonstrate the effectiveness of data-aligned streaming reasoning in enabling efficient and responsive video understanding for LVLMs. We release our code at \href{https://github.com/EIT-NLP/StreamingLLM/tree/main/TaYS}{this repository.}

