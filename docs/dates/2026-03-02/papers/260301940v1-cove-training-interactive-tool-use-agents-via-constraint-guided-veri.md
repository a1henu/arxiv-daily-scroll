---
layout: default
title: CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification
---

# CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification
**arXiv**：[2603.01940v1](https://arxiv.org/abs/2603.01940) · [PDF](https://arxiv.org/pdf/2603.01940.pdf)  
**作者**：Jinpeng Chen, Cheng Gong, Hanbo Li, Ziru Liu, Zichen Tian, Xinyu Fu, Shi Wu, Chenyang Zhang, Wu Zhang, Suiyun Zhang, Dandan Tu, Rui Liu  

**一句话要点**：提出CoVe框架，通过约束引导验证合成高质量数据，训练多轮交互式工具使用智能体。

**关键词**：交互式工具使用智能体, 约束引导验证, 数据合成框架, 监督微调, 强化学习, 多轮交互

## 3 点简述
- 核心问题：真实用户需求复杂模糊，但智能体需执行确定性动作以满足需求，训练数据质量与正确性难以保证。
- 方法要点：定义明确任务约束，既指导生成复杂轨迹，又作为确定性验证器评估轨迹质量，支持监督微调和强化学习。
- 实验或效果：在τ²-bench基准测试中，CoVe-4B模型在航空和零售领域分别达到43.0%和59.4%成功率，性能优于同规模基线，与更大模型竞争。

## 摘要（原文）

> Developing multi-turn interactive tool-use agents is challenging because real-world user needs are often complex and ambiguous, yet agents must execute deterministic actions to satisfy them. To address this gap, we introduce \textbf{CoVe} (\textbf{Co}nstraint-\textbf{Ve}rification), a post-training data synthesis framework designed for training interactive tool-use agents while ensuring both data complexity and correctness. CoVe begins by defining explicit task constraints, which serve a dual role: they guide the generation of complex trajectories and act as deterministic verifiers for assessing trajectory quality. This enables the creation of high-quality training trajectories for supervised fine-tuning (SFT) and the derivation of accurate reward signals for reinforcement learning (RL). Our evaluation on the challenging $τ^2$-bench benchmark demonstrates the effectiveness of the framework. Notably, our compact \textbf{CoVe-4B} model achieves success rates of 43.0\% and 59.4\% in the Airline and Retail domains, respectively; its overall performance significantly outperforms strong baselines of similar scale and remains competitive with models up to $17\times$ its size. These results indicate that CoVe provides an effective and efficient pathway for synthesizing training data for state-of-the-art interactive tool-use agents. To support future research, we open-source our code, trained model, and the full set of 12K high-quality trajectories used for training.

