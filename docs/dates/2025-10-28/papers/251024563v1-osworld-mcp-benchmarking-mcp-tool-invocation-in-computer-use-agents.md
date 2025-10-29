---
layout: default
title: OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents
---

# OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents
**arXiv**：[2510.24563v1](https://arxiv.org/abs/2510.24563) · [PDF](https://arxiv.org/pdf/2510.24563.pdf)  
**作者**：Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei Ye, Fei Huang  

**一句话要点**：提出OSWorld-MCP基准以公平评估计算机使用代理的工具调用与GUI操作能力

**关键词**：计算机使用代理, 工具调用基准, 多模态评估, 模型上下文协议, 自动化代码生成, 任务成功率

## 3 点简述
- 核心问题：现有评估多关注GUI交互，忽视工具调用能力，导致不公平比较
- 方法要点：通过自动化代码生成和手动验证构建158个高质量工具，覆盖7个常见应用
- 实验或效果：MCP工具提升任务成功率，但最强模型工具调用率仅36.3%，显示改进空间

## 摘要（原文）

> With advances in decision-making and reasoning capabilities, multimodal
> agents show strong potential in computer application scenarios. Past
> evaluations have mainly assessed GUI interaction skills, while tool invocation
> abilities, such as those enabled by the Model Context Protocol (MCP), have been
> largely overlooked. Comparing agents with integrated tool invocation to those
> evaluated only on GUI interaction is inherently unfair. We present OSWorld-MCP,
> the first comprehensive and fair benchmark for assessing computer-use agents'
> tool invocation, GUI operation, and decision-making abilities in a real-world
> environment. We design a novel automated code-generation pipeline to create
> tools and combine them with a curated selection from existing tools. Rigorous
> manual validation yields 158 high-quality tools (covering 7 common
> applications), each verified for correct functionality, practical
> applicability, and versatility. Extensive evaluations of state-of-the-art
> multimodal agents on OSWorld-MCP show that MCP tools generally improve task
> success rates (e.g., from 8.3% to 20.4% for OpenAI o3 at 15 steps, from 40.1%
> to 43.3% for Claude 4 Sonnet at 50 steps), underscoring the importance of
> assessing tool invocation capabilities. However, even the strongest models have
> relatively low tool invocation rates, Only 36.3%, indicating room for
> improvement and highlighting the benchmark's challenge. By explicitly measuring
> MCP tool usage skills, OSWorld-MCP deepens understanding of multimodal agents
> and sets a new standard for evaluating performance in complex, tool-assisted
> environments. Our code, environment, and data are publicly available at
> https://osworld-mcp.github.io.

