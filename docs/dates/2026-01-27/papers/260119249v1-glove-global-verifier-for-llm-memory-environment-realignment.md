---
layout: default
title: GLOVE: Global Verifier for LLM Memory-Environment Realignment
---

# GLOVE: Global Verifier for LLM Memory-Environment Realignment
**arXiv**：[2601.19249v1](https://arxiv.org/abs/2601.19249) · [PDF](https://arxiv.org/pdf/2601.19249.pdf)  
**作者**：Xingkun Yin, Hongyang Du  

**一句话要点**：提出GLOVE框架，通过相对真值验证解决动态环境中LLM记忆对齐问题

**关键词**：大语言模型记忆系统, 动态环境对齐, 无监督验证, 认知代理, 记忆更新

## 3 点简述
- 核心问题：现有LLM记忆增强方法依赖外部评估或内部认知，在动态漂移环境中失效
- 方法要点：引入全局验证器，通过主动探测记忆与观察的不一致性实现无监督记忆更新
- 实验或效果：在导航、规划和控制基准上，GLOVE显著提升代理成功率

## 摘要（原文）

> Most existing memory-enhanced Large Language Model (LLM) approaches implicitly assume that memory validity can be established either through external evaluators that provide task-specific success signals or through internal model cognition, such as reflection, for editing memory entries. However, these assumptions often break down in practical environments with dynamic drifts. We propose the Global Verifier (GLOVE), a framework that introduces a new design dimension for LLM memory systems by establishing a relative notion of truth. Through active probing to detect inconsistencies between retrieved memories and fresh observations, GLOVE enables memory-environment realignment by verifying and updating memory without access to ground-truth supervision or strong reliance on model introspection. We evaluate GLOVE on diverse benchmarks spanning web navigation, planning, and control, augmented with controlled environmental drifts that introduce non-stationarity beyond the original benchmark settings. Our results show that GLOVE substantially improves agent success rates, suggesting a robust pathway to cognitive agents capable of self-evolving.

