---
layout: default
title: EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines
---

# EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines
**arXiv**：[2601.09465v1](https://arxiv.org/abs/2601.09465) · [PDF](https://arxiv.org/pdf/2601.09465.pdf)  
**作者**：Shuo Zhang, Chaofa Yuan, Ryan Guo, Xiaomin Yu, Rui Xu, Zhangquan Chen, Zinuo Li, Zhi Yang, Shuhao Guan, Zhenheng Tang, Sen Hu, Liwen Zhang, Ronghao Chen, Huacan Wang  

**一句话要点**：提出EvoFSM框架，通过有限状态机实现可控自进化以解决深度研究中的适应性问题

**关键词**：自进化框架, 有限状态机, 可控优化, 多跳问答, 交互决策

## 3 点简述
- 现有LLM代理依赖固定工作流，难以适应开放查询，导致适应性不足
- EvoFSM将优化空间解耦为宏观流程和微观技能，通过受限操作进化有限状态机
- 在五个多跳QA基准上评估，DeepSearch准确率达58.0%，验证了有效性

## 摘要（原文）

> While LLM-based agents have shown promise for deep research, most existing approaches rely on fixed workflows that struggle to adapt to real-world, open-ended queries. Recent work therefore explores self-evolution by allowing agents to rewrite their own code or prompts to improve problem-solving ability, but unconstrained optimization often triggers instability, hallucinations, and instruction drift. We propose EvoFSM, a structured self-evolving framework that achieves both adaptability and control by evolving an explicit Finite State Machine (FSM) instead of relying on free-form rewriting. EvoFSM decouples the optimization space into macroscopic Flow (state-transition logic) and microscopic Skill (state-specific behaviors), enabling targeted improvements under clear behavioral boundaries. Guided by a critic mechanism, EvoFSM refines the FSM through a small set of constrained operations, and further incorporates a self-evolving memory that distills successful trajectories as reusable priors and failure patterns as constraints for future queries. Extensive evaluations on five multi-hop QA benchmarks demonstrate the effectiveness of EvoFSM. In particular, EvoFSM reaches 58.0% accuracy on the DeepSearch benchmark. Additional results on interactive decision-making tasks further validate its generalization.

