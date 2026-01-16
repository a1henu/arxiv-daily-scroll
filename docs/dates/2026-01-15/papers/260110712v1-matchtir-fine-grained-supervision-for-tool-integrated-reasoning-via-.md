---
layout: default
title: MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching
---

# MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching
**arXiv**：[2601.10712v1](https://arxiv.org/abs/2601.10712) · [PDF](https://arxiv.org/pdf/2601.10712.pdf)  
**作者**：Changle Qu, Sunhao Dai, Hengyi Cai, Jun Xu, Shuaiqiang Wang, Dawei Yin  

**一句话要点**：提出MatchTIR框架，通过二分匹配和双重优势估计解决工具集成推理中的细粒度监督问题。

**关键词**：工具集成推理, 细粒度监督, 二分匹配, 强化学习, 长视野任务, 多回合交互

## 3 点简述
- 现有强化学习方法在工具集成推理中依赖粗粒度奖励，难以区分有效与冗余工具调用。
- MatchTIR利用二分匹配分配回合级奖励，并引入双重优势估计平衡局部精度与全局任务成功。
- 实验表明，MatchTIR在长视野和多回合任务中表现优异，4B模型超越多数8B竞争对手。

## 摘要（原文）

> Tool-Integrated Reasoning (TIR) empowers large language models (LLMs) to tackle complex tasks by interleaving reasoning steps with external tool interactions. However, existing reinforcement learning methods typically rely on outcome- or trajectory-level rewards, assigning uniform advantages to all steps within a trajectory. This coarse-grained credit assignment fails to distinguish effective tool calls from redundant or erroneous ones, particularly in long-horizon multi-turn scenarios. To address this, we propose MatchTIR, a framework that introduces fine-grained supervision via bipartite matching-based turn-level reward assignment and dual-level advantage estimation. Specifically, we formulate credit assignment as a bipartite matching problem between predicted and ground-truth traces, utilizing two assignment strategies to derive dense turn-level rewards. Furthermore, to balance local step precision with global task success, we introduce a dual-level advantage estimation scheme that integrates turn-level and trajectory-level signals, assigning distinct advantage values to individual interaction turns. Extensive experiments on three benchmarks demonstrate the superiority of MatchTIR. Notably, our 4B model surpasses the majority of 8B competitors, particularly in long-horizon and multi-turn tasks. Our codes are available at https://github.com/quchangle1/MatchTIR.

