---
layout: default
title: IronEngine: Towards General AI Assistant
---

# IronEngine: Towards General AI Assistant
**arXiv**：[2603.08425v1](https://arxiv.org/abs/2603.08425) · [PDF](https://arxiv.org/pdf/2603.08425.pdf)  
**作者**：Xi Mo  

**一句话要点**：提出IronEngine通用AI助手平台，通过统一编排核心支持多接口、模型与工具集成，实现任务规划与执行分离。

**关键词**：AI助手平台, 任务编排, 模型管理, 工具执行, 内存架构, 性能基准

## 3 点简述
- 核心问题：构建通用AI助手需整合用户界面、模型后端、工具执行与内存管理，以提升任务完成效率与适应性。
- 方法要点：采用三阶段流水线（讨论、模型切换、执行）和分层内存架构，支持VRAM感知的模型管理与智能工具路由。
- 实验或效果：在文件操作基准测试中实现100%任务完成率，平均总时间1541秒，优于ChatGPT等代表性系统。

## 摘要（原文）

> This paper presents IronEngine, a general AI assistant platform organized around a unified orchestration core that connects a desktop user interface, REST and WebSocket APIs, Python clients, local and cloud model backends, persistent memory, task scheduling, reusable skills, 24-category tool execution, MCP-compatible extensibility, and hardware-facing integration. IronEngine introduces a three-phase pipeline -- Discussion (Planner--Reviewer collaboration), Model Switch (VRAM-aware transition), and Execution (tool-augmented action loop) -- that separates planning quality from execution capability. The system features a hierarchical memory architecture with multi-level consolidation, a vectorized skill repository backed by ChromaDB, an adaptive model management layer supporting 92 model profiles with VRAM-aware context budgeting, and an intelligent tool routing system with 130+ alias normalization and automatic error correction. We present experimental results on file operation benchmarks achieving 100\% task completion with a mean total time of 1541 seconds across four heterogeneous tasks, and provide detailed comparisons with representative AI assistant systems including ChatGPT, Claude Desktop, Cursor, Windsurf, and open-source agent frameworks. Without disclosing proprietary prompts or core algorithms, this paper analyzes the platform's architectural decomposition, subsystem design, experimental performance, safety boundaries, and comparative engineering advantages. The resulting study positions IronEngine as a system-oriented foundation for general-purpose personal assistants, automation frameworks, and future human-centered agent platforms.

