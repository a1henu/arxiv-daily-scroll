---
layout: default
title: AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts
---

# AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts
**arXiv**：[2601.11044v1](https://arxiv.org/abs/2601.11044) · [PDF](https://arxiv.org/pdf/2601.11044.pdf)  
**作者**：Keyu Li, Junhao Shi, Yang Xiao, Mohan Jiang, Jie Sun, Yunze Wu, Shijie Xia, Xiaojie Cai, Tianze Xu, Weiye Si, Wenjie Li, Dequan Wang, Pengfei Liu  

**一句话要点**：提出AgencyBench基准以评估百万令牌级真实场景中自主代理的六项核心能力

**关键词**：自主代理基准, 长程真实场景, 自动化评估, 工具调用, 模型性能对比, 代理框架优化

## 3 点简述
- 现有基准聚焦单一代理能力，缺乏长程真实场景评估，且依赖人工反馈限制可扩展性
- 构建包含32个真实场景、138个任务的基准，采用用户模拟代理和Docker沙箱实现自动化评估
- 实验显示闭源模型优于开源模型，并揭示资源效率、自我纠正和工具使用偏好等方面的差异

## 摘要（原文）

> Large Language Models (LLMs) based autonomous agents demonstrate multifaceted capabilities to contribute substantially to economic production. However, existing benchmarks remain focused on single agentic capability, failing to capture long-horizon real-world scenarios. Moreover, the reliance on human-in-the-loop feedback for realistic tasks creates a scalability bottleneck, hindering automated rollout collection and evaluation. To bridge this gap, we introduce AgencyBench, a comprehensive benchmark derived from daily AI usage, evaluating 6 core agentic capabilities across 32 real-world scenarios, comprising 138 tasks with specific queries, deliverables, and rubrics. These scenarios require an average of 90 tool calls, 1 million tokens, and hours of execution time to resolve. To enable automated evaluation, we employ a user simulation agent to provide iterative feedback, and a Docker sandbox to conduct visual and functional rubric-based assessment. Experiments reveal that closed-source models significantly outperform open-source models (48.4% vs 32.1%). Further analysis reveals significant disparities across models in resource efficiency, feedback-driven self-correction, and specific tool-use preferences. Finally, we investigate the impact of agentic scaffolds, observing that proprietary models demonstrate superior performance within their native ecosystems (e.g., Claude-4.5-Opus via Claude-Agent-SDK), while open-source models exhibit distinct performance peaks, suggesting potential optimization for specific execution frameworks. AgencyBench serves as a critical testbed for next-generation agents, highlighting the necessity of co-optimizing model architecture with agentic frameworks. We believe this work sheds light on the future direction of autonomous agents, and we release the full benchmark and evaluation toolkit at https://github.com/GAIR-NLP/AgencyBench.

