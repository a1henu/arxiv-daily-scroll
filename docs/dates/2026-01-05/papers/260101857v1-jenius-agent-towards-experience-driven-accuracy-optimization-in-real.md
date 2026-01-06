---
layout: default
title: Jenius Agent: Towards Experience-Driven Accuracy Optimization in Real-World Scenarios
---

# Jenius Agent: Towards Experience-Driven Accuracy Optimization in Real-World Scenarios
**arXiv**：[2601.01857v1](https://arxiv.org/abs/2601.01857) · [PDF](https://arxiv.org/pdf/2601.01857.pdf)  
**作者**：Defei Xia, Bingfeng Pi, Shenbin Zhang, Song Hua, Yunfei Wei, Lei Zuo  

**一句话要点**：提出Jenius-Agent框架，基于实践经验优化LLM代理在真实场景中的任务准确性

**关键词**：LLM代理优化, 自适应提示生成, 上下文感知工具编排, 分层记忆机制, 真实场景部署, 任务准确性提升

## 3 点简述
- 核心问题：LLM代理在上下文理解、工具使用和响应生成方面的系统优化不足
- 方法要点：自适应提示生成、上下文感知工具编排和分层记忆机制
- 实验或效果：任务准确性提升20%，同时降低令牌成本、响应延迟和调用失败

## 摘要（原文）

> As agent systems powered by large language models (LLMs) advance, improving the task performance of an autonomous agent, especially in context understanding, tool usage, and response generation, has become increasingly critical. Although prior studies have advanced the overall design of LLM-based agents, systematic optimization of their internal reasoning and tool-use pipelines remains underexplored. This paper introduces an agent framework grounded in real-world practical experience, with three key innovations: (1) an adaptive prompt generation strategy that aligns with the agent's state and task goals to improve reliability and robustness; (2) a context-aware tool orchestration module that performs tool categorization, semantic retrieval, and adaptive invocation based on user intent and context; and (3) a layered memory mechanism that integrates session memory, task history, and external summaries to improve relevance and efficiency through dynamic summarization and compression. An end-to-end framework named Jenius-Agent has been integrated with three key optimizations, including tools based on the Model Context Protocol (MCP), file input/output (I/O), and execution feedback. The experiments show a 20 percent improvement in task accuracy, along with a reduced token cost, response latency, and invocation failures. The framework is already deployed in Jenius (https://www.jenius.cn), providing a lightweight and scalable solution for robust, protocol-compatible autonomous agents.

