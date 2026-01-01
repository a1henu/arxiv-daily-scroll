---
layout: default
title: MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use
---

# MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use
**arXiv**：[2512.24565v1](https://arxiv.org/abs/2512.24565) · [PDF](https://arxiv.org/pdf/2512.24565.pdf)  
**作者**：Wenrui Liu, Zixiang Liu, Elsie Dai, Wenhan Yu, Lei Yu, Tong Yang  

**一句话要点**：提出MCPAgentBench基准以评估LLM代理在真实MCP工具使用中的能力

**关键词**：LLM代理评估, MCP工具使用, 基准测试, 动态沙盒, 任务完成率, 执行效率

## 3 点简述
- 当前MCP评估依赖外部服务且缺乏难度感知，存在局限性
- 构建基于真实MCP定义的数据集，包含模拟工具和动态沙盒环境
- 实验显示主流LLM在复杂多步工具调用中性能差异显著

## 摘要（原文）

> Large Language Models (LLMs) are increasingly serving as autonomous agents, and their utilization of external tools via the Model Context Protocol (MCP) is considered a future trend. Current MCP evaluation sets suffer from issues such as reliance on external MCP services and a lack of difficulty awareness. To address these limitations, we propose MCPAgentBench, a benchmark based on real-world MCP definitions designed to evaluate the tool-use capabilities of agents. We construct a dataset containing authentic tasks and simulated MCP tools. The evaluation employs a dynamic sandbox environment that presents agents with candidate tool lists containing distractors, thereby testing their tool selection and discrimination abilities. Furthermore, we introduce comprehensive metrics to measure both task completion rates and execution efficiency. Experiments conducted on various latest mainstream Large Language Models reveal significant performance differences in handling complex, multi-step tool invocations. All code is open-source at Github.

