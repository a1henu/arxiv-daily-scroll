---
layout: default
title: Auto-scaling Continuous Memory for GUI Agent
---

# Auto-scaling Continuous Memory for GUI Agent
**arXiv**：[2510.09038v1](https://arxiv.org/abs/2510.09038) · [PDF](https://arxiv.org/pdf/2510.09038.pdf)  
**作者**：Wenyi Wu, Kun Zhou, Ruoxin Yuan, Vivian Yu, Stephen Wang, Zhiting Hu, Biwei Huang  
**一句话要点**：提出连续记忆方法以增强GUI代理在陌生界面和长任务中的泛化能力

**关键词**：GUI代理, 连续记忆, 视觉语言模型, 自动扩展, 长任务泛化, 嵌入编码

## 3 点简述
- 核心问题：现有GUI代理压缩轨迹为文本，导致上下文过长且丢失关键视觉信息。
- 方法要点：使用VLM编码轨迹为固定长度连续嵌入，直接输入骨干网络，降低上下文成本。
- 实验或效果：在真实GUI基准测试中，成功率和泛化能力显著提升，性能接近闭源模型。

## 摘要（原文）

> We study how to endow GUI agents with scalable memory that help generalize
> across unfamiliar interfaces and long-horizon tasks. Prior GUI agents compress
> past trajectories into text tokens, which balloons context length and misses
> decisive visual cues (e.g., exact widget size and position). We propose a
> continuous memory that encodes each GUI trajectory into a fixed-length sequence
> of continuous embeddings using the VLM itself as an encoder; these embeddings
> are plugged directly into the backbone's input layer, sharply reducing context
> cost while preserving fine-grained visual information. As memory size and
> retrieval depth increase, performance improves monotonically, unlike text
> memories that degrade with long prompts. To grow memory at low cost, we
> introduce an auto-scaling data flywheel that (i) discovers new environments via
> search, (ii) synthesizes tasks with an open-source VLM, (iii) rolls out
> trajectories with the agent, and (iv) verifies success with the same VLM. Using
> this pipeline, we collect 100k+ trajectories for about \$4000 and fine-tune
> only the memory encoder (LoRA on a Q-Former, 1.2\% parameters) with 1,500
> samples. On real-world GUI benchmarks, our memory-augmented agent consistently
> improves success rates under long horizons and distribution shifts. Notably,
> Qwen-2.5-VL-7B + continuous memory achieves performance comparable to
> state-of-the-art closed-source models (e.g., GPT-4o, Claude-4).

