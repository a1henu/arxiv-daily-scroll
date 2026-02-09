---
layout: default
title: Implementing Grassroots Logic Programs with Multiagent Transition Systems and AI
---

# Implementing Grassroots Logic Programs with Multiagent Transition Systems and AI
**arXiv**：[2602.06934v1](https://arxiv.org/abs/2602.06934) · [PDF](https://arxiv.org/pdf/2602.06934.pdf)  
**作者**：Ehud Shapiro  

**一句话要点**：提出dGLP和madGLP以支持AI在Dart中实现草根逻辑程序

**关键词**：草根逻辑程序, 多代理系统, 操作语义, 分布式实现, Dart编程

## 3 点简述
- 核心问题：草根逻辑程序（GLP）需在分布式系统中实现，支持多代理并发和异步通信。
- 方法要点：开发dGLP和madGLP作为确定性操作语义，用于单代理和多代理GLP，并证明其正确性。
- 实验或效果：AI基于dGLP和madGLP在Dart中开发工作站和智能手机实现，支持草根平台部署。

## 摘要（原文）

> Grassroots Logic Programs (GLP) is a concurrent logic programming language with variables partitioned into paired \emph{readers} and \emph{writers}, conjuring both linear logic and futures/promises: an assignment is produced at most once via the sole occurrence of a writer (promise) and consumed at most once via the sole occurrence of its paired reader (future), and may contain additional readers and/or writers, enabling the concise expression of rich multidirectional communication modalities.
>   GLP was designed as a language for grassroots platforms -- distributed systems with multiple instances that can operate independently of each other and of any global resource, and can coalesce into ever larger instances -- with its target architecture being smartphones communicating peer-to-peer. The operational semantics of Concurrent (single-agent) GLP and of multiagent GLP (maGLP) were defined via transition systems/multiagent transition systems, respectively.
>   Here, we describe the mathematics developed to facilitate the workstation- and smartphone-based implementations of GLP by AI in Dart. We developed dGLP -- implementation-ready deterministic operational semantics for single-agent GLP -- and proved it correct with respect to the Concurrent GLP operational semantics; dGLP was used by AI as a formal spec, from which it developed a workstation-based implementation of GLP. We developed madGLP -- an implementation-ready multiagent operational semantics for maGLP -- and proved it correct with respect to the maGLP operational semantics; madGLP is deterministic at the agent level (not at the system level due to communication asynchrony), and is being used by AI as a formal spec from which it develops a smartphone-based implementation of maGLP.

