---
layout: default
title: AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents
---

# AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents
**arXiv**：[2602.06485v1](https://arxiv.org/abs/2602.06485) · [PDF](https://arxiv.org/pdf/2602.06485.pdf)  
**作者**：Haotian Chen, Xin Cong, Shengda Fan, Yuyang Fu, Ziqin Gong, Yaxi Lu, Yishan Li, Boye Niu, Chengjun Pan, Zijun Song, Huadong Wang, Yesai Wu, Yueying Wu, Zihao Xie, Yukun Yan, Zhong Zhang, Yankai Lin, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出AgentCPM-Explore以解决边缘规模代理模型在长视野深度探索中的性能瓶颈

**关键词**：边缘规模代理模型, 长视野深度探索, 参数空间模型融合, 奖励信号去噪, 上下文信息精炼, 推理稳定性

## 3 点简述
- 核心问题：边缘规模模型存在监督微调灾难性遗忘、强化学习奖励信号噪声敏感和长上下文冗余信息导致推理退化
- 方法要点：采用参数空间模型融合、奖励信号去噪和上下文信息精炼的整体训练框架
- 实验或效果：在4B规模模型中达到SOTA，匹配或超越8B规模SOTA模型，并在五个基准上优于Claude-4.5-Sonnet等更大模型

## 摘要（原文）

> While Large Language Model (LLM)-based agents have shown remarkable potential for solving complex tasks, existing systems remain heavily reliant on large-scale models, leaving the capabilities of edge-scale models largely underexplored. In this paper, we present the first systematic study on training agentic models at the 4B-parameter scale. We identify three primary bottlenecks hindering the performance of edge-scale models: catastrophic forgetting during Supervised Fine-Tuning (SFT), sensitivity to reward signal noise during Reinforcement Learning (RL), and reasoning degradation caused by redundant information in long-context scenarios. To address the issues, we propose AgentCPM-Explore, a compact 4B agent model with high knowledge density and strong exploration capability. We introduce a holistic training framework featuring parameter-space model fusion, reward signal denoising, and contextual information refinement. Through deep exploration, AgentCPM-Explore achieves state-of-the-art (SOTA) performance among 4B-class models, matches or surpasses 8B-class SOTA models on four benchmarks, and even outperforms larger-scale models such as Claude-4.5-Sonnet or DeepSeek-v3.2 in five benchmarks. Notably, AgentCPM-Explore achieves 97.09% accuracy on GAIA text-based tasks under pass@64. These results provide compelling evidence that the bottleneck for edge-scale models is not their inherent capability ceiling, but rather their inference stability. Based on our well-established training framework, AgentCPM-Explore effectively unlocks the significant, yet previously underestimated, potential of edge-scale models.

