---
layout: default
title: EAGLE-Pangu: Accelerator-Safe Tree Speculative Decoding on Ascend NPUs
---

# EAGLE-Pangu: Accelerator-Safe Tree Speculative Decoding on Ascend NPUs
**arXiv**：[2603.08088v1](https://arxiv.org/abs/2603.08088) · [PDF](https://arxiv.org/pdf/2603.08088.pdf)  
**作者**：Chang Han, Yijie Hu, Jingling Liu  

**一句话要点**：提出EAGLE-Pangu系统，在昇腾NPU上实现加速器安全的树状推测解码以提升LLM推理效率

**关键词**：推测解码, 树状结构, 昇腾NPU, KV缓存, 加速器安全, 吞吐量优化

## 3 点简述
- 核心问题：树状推测解码在异构加速器后端移植时因注意力掩码、KV缓存布局等差异易失效
- 方法要点：基于Cache API构建分支/提交缓存管理器，设计加速器安全的树张量化消除负索引
- 实验或效果：在MT-Bench和HumanEval提示上，解码吞吐量平均提升1.27倍，最高达2.46倍

## 摘要（原文）

> Autoregressive decoding remains a primary bottleneck in large language model (LLM) serving, motivating speculative decoding methods that reduce expensive teacher-model invocations by verifying multiple candidate tokens per step. Tree-structured speculation further increases parallelism, but is often brittle when ported across heterogeneous backends and accelerator stacks, where attention masking, KV-cache layouts, and indexing semantics are not interchangeable. We present EAGLE-Pangu, a reproducible system that ports EAGLE-3-style tree speculative decoding to a Pangu teacher backend on Ascend NPUs. EAGLE-Pangu contributes (i) an explicit branch/commit cache manager built on the Cache API, (ii) accelerator-safe tree tensorization that removes undefined negative indices by construction and validates structural invariants, and (iii) a fused-kernel-compatible teacher verification path with a debuggable eager fallback. On 240 turns from MT-Bench and HumanEval-style prompts, EAGLE-Pangu improves end-to-end decoding throughput by 1.27x on average, up to 2.46x at p99, over teacher-only greedy decoding in the fused-kernel performance path. We also provide a fused-kernel-free reference path with structured traces and invariant checks to support reproducible debugging and ablation across execution modes and tree budgets.

