---
layout: default
title: MAXS: Meta-Adaptive Exploration with LLM Agents
---

# MAXS: Meta-Adaptive Exploration with LLM Agents
**arXiv**：[2601.09259v1](https://arxiv.org/abs/2601.09259) · [PDF](https://arxiv.org/pdf/2601.09259.pdf)  
**作者**：Jian Zhang, Zhiyuan Wang, Zhangqi Wang, Yu He, Haoran Luo, li yuan, Lingling Zhang, Rui Mao, Qika Lin, Jun Liu  

**一句话要点**：提出MAXS框架以解决LLM代理推理中的短视与轨迹不稳定问题

**关键词**：LLM代理推理, 前瞻策略, 轨迹稳定性, 多工具协作, 计算效率优化

## 3 点简述
- 核心问题：LLM代理推理存在局部短视生成和轨迹不稳定，影响全局效果与计算效率平衡
- 方法要点：采用前瞻策略评估工具优势值，结合步一致性与趋势斜率选择稳定高价值推理步骤
- 实验或效果：在三个基础模型和五个数据集上验证，MAXS在性能和推理效率上优于现有方法

## 摘要（原文）

> Large Language Model (LLM) Agents exhibit inherent reasoning abilities through the collaboration of multiple tools. However, during agent inference, existing methods often suffer from (i) locally myopic generation, due to the absence of lookahead, and (ii) trajectory instability, where minor early errors can escalate into divergent reasoning paths. These issues make it difficult to balance global effectiveness and computational efficiency. To address these two issues, we propose meta-adaptive exploration with LLM agents https://github.com/exoskeletonzj/MAXS, a meta-adaptive reasoning framework based on LLM Agents that flexibly integrates tool execution and reasoning planning. MAXS employs a lookahead strategy to extend reasoning paths a few steps ahead, estimating the advantage value of tool usage, and combines step consistency variance and inter-step trend slopes to jointly select stable, consistent, and high-value reasoning steps. Additionally, we introduce a trajectory convergence mechanism that controls computational cost by halting further rollouts once path consistency is achieved, enabling a balance between resource efficiency and global effectiveness in multi-tool reasoning. We conduct extensive empirical studies across three base models (MiMo-VL-7B, Qwen2.5-VL-7B, Qwen2.5-VL-32B) and five datasets, demonstrating that MAXS consistently outperforms existing methods in both performance and inference efficiency. Further analysis confirms the effectiveness of our lookahead strategy and tool usage.

