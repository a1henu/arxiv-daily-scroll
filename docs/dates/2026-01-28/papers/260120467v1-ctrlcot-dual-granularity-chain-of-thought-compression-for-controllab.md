---
layout: default
title: CtrlCoT: Dual-Granularity Chain-of-Thought Compression for Controllable Reasoning
---

# CtrlCoT: Dual-Granularity Chain-of-Thought Compression for Controllable Reasoning
**arXiv**：[2601.20467v1](https://arxiv.org/abs/2601.20467) · [PDF](https://arxiv.org/pdf/2601.20467.pdf)  
**作者**：Zhenxuan Fan, Jie Cao, Yang Dai, Zheqi Lv, Wenqiao Zhang, Zhongle Xie, Peng LU, Beng Chin Ooi  

**一句话要点**：提出CtrlCoT框架，通过双粒度压缩优化链式思维推理的效率和可控性。

**关键词**：链式思维压缩, 双粒度推理, 逻辑保持蒸馏, 分布对齐生成, 可控推理优化

## 3 点简述
- 核心问题：链式思维推理因冗长轨迹导致高延迟和内存成本，现有压缩方法在语义保守或令牌激进间难以平衡。
- 方法要点：结合分层推理抽象、逻辑保持蒸馏和分布对齐生成，实现语义与令牌级压缩的协调。
- 实验或效果：在MATH-500数据集上，使用Qwen2.5-7B-Instruct模型，减少30.7%令牌同时提升7.6个百分点准确率。

## 摘要（原文）

> Chain-of-thought (CoT) prompting improves LLM reasoning but incurs high latency and memory cost due to verbose traces, motivating CoT compression with preserved correctness. Existing methods either shorten CoTs at the semantic level, which is often conservative, or prune tokens aggressively, which can miss task-critical cues and degrade accuracy. Moreover, combining the two is non-trivial due to sequential dependency, task-agnostic pruning, and distribution mismatch. We propose \textbf{CtrlCoT}, a dual-granularity CoT compression framework that harmonizes semantic abstraction and token-level pruning through three components: Hierarchical Reasoning Abstraction produces CoTs at multiple semantic granularities; Logic-Preserving Distillation trains a logic-aware pruner to retain indispensable reasoning cues (e.g., numbers and operators) across pruning ratios; and Distribution-Alignment Generation aligns compressed traces with fluent inference-time reasoning styles to avoid fragmentation. On MATH-500 with Qwen2.5-7B-Instruct, CtrlCoT uses 30.7\% fewer tokens while achieving 7.6 percentage points higher than the strongest baseline, demonstrating more efficient and reliable reasoning. Our code will be publicly available at https://github.com/fanzhenxuan/Ctrl-CoT.

