---
layout: default
title: Mem-T: Densifying Rewards for Long-Horizon Memory Agents
---

# Mem-T: Densifying Rewards for Long-Horizon Memory Agents
**arXiv**：[2601.23014v1](https://arxiv.org/abs/2601.23014) · [PDF](https://arxiv.org/pdf/2601.23014.pdf)  
**作者**：Yanwei Yue, Guibin Zhang, Boci Peng, Xuanbo Fan, Jiaxin Guo, Qiankun Li, Yan Zhang  

**一句话要点**：提出Mem-T与MoT-GRPO以解决长时程记忆代理中稀疏奖励导致的训练困难

**关键词**：记忆代理, 长时程序列, 强化学习, 稀疏奖励, 内存管理, 端到端优化

## 3 点简述
- 核心问题：现有记忆代理在长时程操作序列中面临稀疏延迟奖励，阻碍端到端优化。
- 方法要点：Mem-T结合分层内存数据库进行动态更新与多轮检索；MoT-GRPO通过树回传与后见信用分配将稀疏反馈转化为密集监督。
- 实验或效果：Mem-T在性能上超越基准框架达14.92%，并减少约24.45%的推理令牌，实现高效准确。

## 摘要（原文）

> Memory agents, which depart from predefined memory-processing pipelines by endogenously managing the processing, storage, and retrieval of memories, have garnered increasing attention for their autonomy and adaptability. However, existing training paradigms remain constrained: agents often traverse long-horizon sequences of memory operations before receiving sparse and delayed rewards, which hinders truly end-to-end optimization of memory management policies. To address this limitation, we introduce Mem-T, an autonomous memory agent that interfaces with a lightweight hierarchical memory database to perform dynamic updates and multi-turn retrieval over streaming inputs. To effectively train long-horizon memory management capabilities, we further propose MoT-GRPO, a tree-guided reinforcement learning framework that transforms sparse terminal feedback into dense, step-wise supervision via memory operation tree backpropagation and hindsight credit assignment, thereby enabling the joint optimization of memory construction and retrieval. Extensive experiments demonstrate that Mem-T is (1) high-performing, surpassing frameworks such as A-Mem and Mem0 by up to $14.92\%$, and (2) economical, operating on a favorable accuracy-efficiency Pareto frontier and reducing inference tokens per query by $\sim24.45\%$ relative to GAM without sacrificing performance.

