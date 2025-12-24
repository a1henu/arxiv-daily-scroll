---
layout: default
title: TableGPT-R1: Advancing Tabular Reasoning Through Reinforcement Learning
---

# TableGPT-R1: Advancing Tabular Reasoning Through Reinforcement Learning
**arXiv**：[2512.20312v1](https://arxiv.org/abs/2512.20312) · [PDF](https://arxiv.org/pdf/2512.20312.pdf)  
**作者**：Saisai Yang, Qingyi Huang, Jing Yuan, Liangyu Zha, Kai Tang, Yuhang Yang, Ning Wang, Yucheng Wei, Liyao Li, Wentao Ye, Hao Chen, Tao Zhang, Junlin Zhou, Haobo Wang, Gang Chen, Junbo Zhao  

**一句话要点**：提出TableGPT-R1强化学习框架以解决表格数据复杂推理与代码执行的挑战

**关键词**：表格推理, 强化学习, 代码执行, 数据工程, 奖励系统, 多阶段训练

## 3 点简述
- 核心问题：现有模型在表格任务中面临多步推理和代码执行不足，强化学习应用存在数据稀缺、反馈异质和知识遗忘难题。
- 方法要点：通过数据工程合成轨迹、任务自适应奖励系统结合规则验证与过程奖励，以及多阶段训练框架稳定推理。
- 实验或效果：在权威基准测试中达到最先进性能，显著超越基线模型并保持通用能力。

## 摘要（原文）

> Tabular data serves as the backbone of modern data analysis and scientific research. While Large Language Models (LLMs) fine-tuned via Supervised Fine-Tuning (SFT) have significantly improved natural language interaction with such structured data, they often fall short in handling the complex, multi-step reasoning and robust code execution required for real-world table tasks. Reinforcement Learning (RL) offers a promising avenue to enhance these capabilities, yet its application in the tabular domain faces three critical hurdles: the scarcity of high-quality agentic trajectories with closed-loop code execution and environment feedback on diverse table structures, the extreme heterogeneity of feedback signals ranging from rigid SQL execution to open-ended data interpretation, and the risk of catastrophic forgetting of general knowledge during vertical specialization. To overcome these challenges and unlock advanced reasoning on complex tables, we introduce \textbf{TableGPT-R1}, a specialized tabular model built on a systematic RL framework. Our approach integrates a comprehensive data engineering pipeline that synthesizes difficulty-stratified agentic trajectories for both supervised alignment and RL rollouts, a task-adaptive reward system that combines rule-based verification with a criteria-injected reward model and incorporates process-level step reward shaping with behavioral regularization, and a multi-stage training framework that progressively stabilizes reasoning before specializing in table-specific tasks. Extensive evaluations demonstrate that TableGPT-R1 achieves state-of-the-art performance on authoritative benchmarks, significantly outperforming baseline models while retaining robust general capabilities. Our model is available at https://huggingface.co/tablegpt/TableGPT-R1.

