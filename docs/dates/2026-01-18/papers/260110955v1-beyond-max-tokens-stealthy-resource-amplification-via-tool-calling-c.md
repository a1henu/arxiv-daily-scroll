---
layout: default
title: Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents
---

# Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents
**arXiv**：[2601.10955v1](https://arxiv.org/abs/2601.10955) · [PDF](https://arxiv.org/pdf/2601.10955.pdf)  
**作者**：Kaiyu Zhou, Yongsen Zheng, Yicheng He, Meng Xue, Xueluan Gong, Yuji Wang, Kwok-Yan Lam  

**一句话要点**：提出基于工具调用链的隐蔽资源放大攻击，以解决LLM代理中多轮经济拒绝服务问题。

**关键词**：LLM代理安全, 经济拒绝服务攻击, 工具调用链, 蒙特卡洛树搜索优化, 资源放大, 协议兼容性

## 3 点简述
- 核心问题：现有DoS攻击在LLM代理中因单轮和任务导向不足而无效，无法利用多轮交互的复合成本。
- 方法要点：通过调整工具服务器的文本可见字段和返回策略，使用MCTS优化，引导代理进入冗长工具调用序列。
- 实验或效果：在多个基准上，攻击使任务轨迹超6万令牌，成本膨胀达658倍，GPU KV缓存占用升至35-74%。

## 摘要（原文）

> The agent-tool communication loop is a critical attack surface in modern Large Language Model (LLM) agents. Existing Denial-of-Service (DoS) attacks, primarily triggered via user prompts or injected retrieval-augmented generation (RAG) context, are ineffective for this new paradigm. They are fundamentally single-turn and often lack a task-oriented approach, making them conspicuous in goal-oriented workflows and unable to exploit the compounding costs of multi-turn agent-tool interactions. We introduce a stealthy, multi-turn economic DoS attack that operates at the tool layer under the guise of a correctly completed task. Our method adjusts text-visible fields and a template-governed return policy in a benign, Model Context Protocol (MCP)-compatible tool server, optimizing these edits with a Monte Carlo Tree Search (MCTS) optimizer. These adjustments leave function signatures unchanged and preserve the final payload, steering the agent into prolonged, verbose tool-calling sequences using text-only notices. This compounds costs across turns, escaping single-turn caps while keeping the final answer correct to evade validation. Across six LLMs on the ToolBench and BFCL benchmarks, our attack expands tasks into trajectories exceeding 60,000 tokens, inflates costs by up to 658x, and raises energy by 100-560x. It drives GPU KV cache occupancy from <1% to 35-74% and cuts co-running throughput by approximately 50%. Because the server remains protocol-compatible and task outcomes are correct, conventional checks fail. These results elevate the agent-tool interface to a first-class security frontier, demanding a paradigm shift from validating final answers to monitoring the economic and computational cost of the entire agentic process.

