---
layout: default
title: LogicEnvGen: Task-Logic Driven Generation of Diverse Simulated Environments for Embodied AI
---

# LogicEnvGen: Task-Logic Driven Generation of Diverse Simulated Environments for Embodied AI
**arXiv**：[2601.13556v1](https://arxiv.org/abs/2601.13556) · [PDF](https://arxiv.org/pdf/2601.13556.pdf)  
**作者**：Jianan Wang, Siyang Zhang, Bin Li, Juan Chen, Jingtao Qi, Zhuo Zhang, Chen Qian  

**一句话要点**：提出LogicEnvGen方法，通过任务逻辑驱动生成多样化模拟环境以测试具身AI代理

**关键词**：具身AI, 模拟环境生成, 逻辑多样性, 任务逻辑分析, 约束求解, 环境评估基准

## 3 点简述
- 现有模拟环境生成方法过度关注视觉真实性，缺乏逻辑多样性测试视角
- 采用大语言模型分析任务执行逻辑，构建决策树行为计划并实例化具体环境
- 实验显示LogicEnvGen比基线方法提升1.04-2.61倍逻辑多样性，显著增强代理故障发现能力

## 摘要（原文）

> Simulated environments play an essential role in embodied AI, functionally analogous to test cases in software engineering. However, existing environment generation methods often emphasize visual realism (e.g., object diversity and layout coherence), overlooking a crucial aspect: logical diversity from the testing perspective. This limits the comprehensive evaluation of agent adaptability and planning robustness in distinct simulated environments. To bridge this gap, we propose LogicEnvGen, a novel method driven by Large Language Models (LLMs) that adopts a top-down paradigm to generate logically diverse simulated environments as test cases for agents. Given an agent task, LogicEnvGen first analyzes its execution logic to construct decision-tree-structured behavior plans and then synthesizes a set of logical trajectories. Subsequently, it adopts a heuristic algorithm to refine the trajectory set, reducing redundant simulation. For each logical trajectory, which represents a potential task situation, LogicEnvGen correspondingly instantiates a concrete environment. Notably, it employs constraint solving for physical plausibility. Furthermore, we introduce LogicEnvEval, a novel benchmark comprising four quantitative metrics for environment evaluation. Experimental results verify the lack of logical diversity in baselines and demonstrate that LogicEnvGen achieves 1.04-2.61x greater diversity, significantly improving the performance in revealing agent faults by 4.00%-68.00%.

