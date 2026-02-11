---
layout: default
title: AgentCgroup: Understanding and Controlling OS Resources of AI Agents
---

# AgentCgroup: Understanding and Controlling OS Resources of AI Agents
**arXiv**：[2602.09345v1](https://arxiv.org/abs/2602.09345) · [PDF](https://arxiv.org/pdf/2602.09345.pdf)  
**作者**：Yusheng Zheng, Jiakun Fan, Quanzhi Fu, Yiwei Yang, Wei Zhang, Andi Quinn  

**一句话要点**：提出AgentCgroup以解决AI代理在容器中资源控制不匹配问题

**关键词**：AI代理资源控制, eBPF内核监控, 容器资源管理, 多租户隔离, 工具调用动态

## 3 点简述
- 核心问题：AI代理在沙盒容器中资源需求动态且不可预测，现有控制存在粒度、响应性和适应性不匹配
- 方法要点：基于eBPF设计分层cgroup控制器，通过内核监控和自适应策略对齐工具调用边界
- 实验或效果：初步评估显示改善了多租户隔离并减少了资源浪费

## 摘要（原文）

> AI agents are increasingly deployed in multi-tenant cloud environments, where they execute diverse tool calls within sandboxed containers, each call with distinct resource demands and rapid fluctuations. We present a systematic characterization of OS-level resource dynamics in sandboxed AI coding agents, analyzing 144 software engineering tasks from the SWE-rebench benchmark across two LLM models. Our measurements reveal that (1) OS-level execution (tool calls, container and agent initialization) accounts for 56-74% of end-to-end task latency; (2) memory, not CPU, is the concurrency bottleneck; (3) memory spikes are tool-call-driven with a up to 15.4x peak-to-average ratio; and (4) resource demands are highly unpredictable across tasks, runs, and models. Comparing these characteristics against serverless, microservice, and batch workloads, we identify three mismatches in existing resource controls: a granularity mismatch (container-level policies vs. tool-call-level dynamics), a responsiveness mismatch (user-space reaction vs. sub-second unpredictable bursts), and an adaptability mismatch (history-based prediction vs. non-deterministic stateful execution). We propose AgentCgroup , an eBPF-based resource controller that addresses these mismatches through hierarchical cgroup structures aligned with tool-call boundaries, in-kernel enforcement via sched_ext and memcg_bpf_ops, and runtime-adaptive policies driven by in-kernel monitoring. Preliminary evaluation demonstrates improved multi-tenant isolation and reduced resource waste.

