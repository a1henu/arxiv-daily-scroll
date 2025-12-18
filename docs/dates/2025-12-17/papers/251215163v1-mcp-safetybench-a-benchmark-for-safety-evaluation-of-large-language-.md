---
layout: default
title: MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers
---

# MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers
**arXiv**：[2512.15163v1](https://arxiv.org/abs/2512.15163) · [PDF](https://arxiv.org/pdf/2512.15163.pdf)  
**作者**：Xuanjun Zong, Zhiqi Shen, Lei Wang, Yunshi Lan, Chao Yang  

**一句话要点**：提出MCP-SafetyBench基准，用于评估大语言模型在真实MCP服务器环境中的安全性风险。

**关键词**：大语言模型安全评估, 模型上下文协议, 多服务器工作流, 安全基准测试, 真实世界部署

## 3 点简述
- 核心问题：MCP协议的多服务器工作流引入新安全风险，现有基准缺乏真实覆盖。
- 方法要点：基于真实MCP服务器构建基准，涵盖五个领域和20种攻击类型的统一分类。
- 实验或效果：评估主流大语言模型，揭示安全性能差异和任务复杂性增加时的漏洞升级。

## 摘要（原文）

> Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage. We present MCP-SafetyBench, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains: browser automation, financial analysis, location navigation, repository management, and web search. It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty. Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing large disparities in safety performance and escalating vulnerabilities as task horizons and server interactions grow. Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments.

