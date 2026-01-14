---
layout: default
title: ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web
---

# ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web
**arXiv**：[2601.08276v1](https://arxiv.org/abs/2601.08276) · [PDF](https://arxiv.org/pdf/2601.08276.pdf)  
**作者**：Zhiyuan Yao, Zishan Xu, Yifu Guo, Zhiguang Han, Cheng Yang, Shuo Zhang, Weinan Zhang, Xingshan Zeng, Weiwen Liu  

**一句话要点**：提出ToolACE-MCP以解决Agent Web中大规模工具生态系统的可扩展性和通用性瓶颈。

**关键词**：Agent Web, 历史感知路由, 工具生态系统, 可扩展性, 多智能体协作, 鲁棒性

## 3 点简述
- 核心问题：Agent Web和MCP工具生态系统中工具数量激增，导致现有架构面临可扩展性和通用性瓶颈。
- 方法要点：通过依赖丰富的候选图合成多轮轨迹，训练历史感知路由器，实现动态上下文理解和即插即用轻量路由代理。
- 实验或效果：在MCP-Universe和MCP-Mark基准测试中表现优异，展现出对多智能体协作的泛化能力和对噪声的鲁棒性。

## 摘要（原文）

> With the rise of the Agent Web and Model Context Protocol (MCP), the agent ecosystem is evolving into an open collaborative network, exponentially increasing accessible tools. However, current architectures face severe scalability and generality bottlenecks. To address this, we propose ToolACE-MCP, a pipeline for training history-aware routers to empower precise navigation in large-scale ecosystems. By leveraging a dependency-rich candidate Graph to synthesize multi-turn trajectories, we effectively train routers with dynamic context understanding to create the plug-and-play Light Routing Agent. Experiments on the real-world benchmarks MCP-Universe and MCP-Mark demonstrate superior performance. Notably, ToolACE-MCP exhibits critical properties for the future Agent Web: it not only generalizes to multi-agent collaboration with minimal adaptation but also maintains exceptional robustness against noise and scales effectively to massive candidate spaces. These findings provide a strong empirical foundation for universal orchestration in open-ended ecosystems.

