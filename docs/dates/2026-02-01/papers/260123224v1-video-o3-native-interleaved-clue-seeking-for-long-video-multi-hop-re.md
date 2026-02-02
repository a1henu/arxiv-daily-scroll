---
layout: default
title: Video-o3: Native Interleaved Clue Seeking for Long Video Multi-Hop Reasoning
---

# Video-o3: Native Interleaved Clue Seeking for Long Video Multi-Hop Reasoning
**arXiv**：[2601.23224v1](https://arxiv.org/abs/2601.23224) · [PDF](https://arxiv.org/pdf/2601.23224.pdf)  
**作者**：Xiangyu Zeng, Zhiqiu Zhang, Yuhan Zhu, Xinhao Li, Zikang Wang, Changlian Ma, Qingyu Zhang, Zizheng Huang, Kun Ouyang, Tianxiang Jiang, Ziang Yan, Yi Wang, Hongjie Zhang, Yali Wang, Limin Wang  

**一句话要点**：提出Video-o3框架，通过原生交错工具调用解决长视频多跳推理中的稀疏关键证据识别问题。

**关键词**：长视频理解, 多跳推理, 工具调用, 注意力机制, 强化学习, 数据合成

## 3 点简述
- 现有方法依赖均匀采样和单轮推理，难以在冗余长视频中定位稀疏关键证据。
- 引入任务解耦注意力掩码和可验证轨迹引导奖励，优化工具调用中的注意力分散和上下文长度增长。
- 在MLVU和Video-Holmes基准上分别达到72.1%和46.5%准确率，验证了多跳证据寻求和推理能力。

## 摘要（原文）

> Existing multimodal large language models for long-video understanding predominantly rely on uniform sampling and single-turn inference, limiting their ability to identify sparse yet critical evidence amid extensive redundancy. We introduce Video-o3, a novel framework that supports iterative discovery of salient visual clues, fine-grained inspection of key segments, and adaptive termination once sufficient evidence is acquired. Technically, we address two core challenges in interleaved tool invocation. First, to mitigate attention dispersion induced by the heterogeneity of reasoning and tool-calling, we propose Task-Decoupled Attention Masking, which isolates per-step concentration while preserving shared global context. Second, to control context length growth in multi-turn interactions, we introduce a Verifiable Trajectory-Guided Reward that balances exploration coverage with reasoning efficiency. To support training at scale, we further develop a data synthesis pipeline and construct Seeker-173K, comprising 173K high-quality tool-interaction trajectories for effective supervised and reinforcement learning. Extensive experiments show that Video-o3 substantially outperforms state-of-the-art methods, achieving 72.1% accuracy on MLVU and 46.5% on Video-Holmes. These results demonstrate Video-o3's strong multi-hop evidence-seeking and reasoning capabilities, and validate the effectiveness of native tool invocation in long-video scenarios.

