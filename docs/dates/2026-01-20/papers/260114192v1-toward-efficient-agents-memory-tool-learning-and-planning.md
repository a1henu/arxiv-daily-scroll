---
layout: default
title: Toward Efficient Agents: Memory, Tool learning, and Planning
---

# Toward Efficient Agents: Memory, Tool learning, and Planning
**arXiv**：[2601.14192v1](https://arxiv.org/abs/2601.14192) · [PDF](https://arxiv.org/pdf/2601.14192.pdf)  
**作者**：Xiaofang Yang, Lijun Li, Heng Zhou, Tong Zhu, Xiaoye Qu, Yuchen Fan, Qianshan Wei, Rui Ye, Li Kang, Yiran Qin, Zhiqiang Kou, Daizong Liu, Qi Li, Ning Ding, Siheng Chen, Jing Shao  

**一句话要点**：综述智能体效率问题，聚焦内存、工具学习和规划以优化成本与性能平衡

**关键词**：智能体效率, 内存管理, 工具学习, 规划优化, 成本效益分析, 评估基准

## 3 点简述
- 核心问题：智能体系统在现实部署中效率常被忽视，需考虑延迟、令牌和步骤等成本
- 方法要点：通过压缩管理内存、设计奖励减少工具调用、控制搜索机制提升效率
- 实验或效果：基于帕累托前沿分析效率与效果权衡，总结评估协议和效率指标

## 摘要（原文）

> Recent years have witnessed increasing interest in extending large language models into agentic systems. While the effectiveness of agents has continued to improve, efficiency, which is crucial for real-world deployment, has often been overlooked. This paper therefore investigates efficiency from three core components of agents: memory, tool learning, and planning, considering costs such as latency, tokens, steps, etc. Aimed at conducting comprehensive research addressing the efficiency of the agentic system itself, we review a broad range of recent approaches that differ in implementation yet frequently converge on shared high-level principles including but not limited to bounding context via compression and management, designing reinforcement learning rewards to minimize tool invocation, and employing controlled search mechanisms to enhance efficiency, which we discuss in detail. Accordingly, we characterize efficiency in two complementary ways: comparing effectiveness under a fixed cost budget, and comparing cost at a comparable level of effectiveness. This trade-off can also be viewed through the Pareto frontier between effectiveness and cost. From this perspective, we also examine efficiency oriented benchmarks by summarizing evaluation protocols for these components and consolidating commonly reported efficiency metrics from both benchmark and methodological studies. Moreover, we discuss the key challenges and future directions, with the goal of providing promising insights.

