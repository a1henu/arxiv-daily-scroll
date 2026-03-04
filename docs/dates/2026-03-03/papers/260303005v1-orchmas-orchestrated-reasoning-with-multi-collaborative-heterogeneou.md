---
layout: default
title: OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents
---

# OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents
**arXiv**：[2603.03005v1](https://arxiv.org/abs/2603.03005) · [PDF](https://arxiv.org/pdf/2603.03005.pdf)  
**作者**：Yichao Feng, Haoran Luo, Zhenghong Lin, Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh, Anh Tuan Luu  

**一句话要点**：提出OrchMAS框架以解决科学领域多智能体推理中的静态性、刚性及同质化问题

**关键词**：多智能体系统, 科学推理, 异构模型协作, 动态编排, 迭代更新, 模型无关框架

## 3 点简述
- 核心问题：现有多智能体系统在科学领域存在静态提示、刚性流程和同质模型依赖，导致领域适应差、推理灵活性低。
- 方法要点：采用双层编排框架，动态构建领域感知推理管道，支持异构模型协作和迭代更新。
- 实验或效果：实验显示在多样推理和科学基准上优于现有系统和基线，提升鲁棒性和专业化。

## 摘要（原文）

> Multi-agent large language model frameworks are promising for complex multi step reasoning, yet existing systems remain weak for scientific and knowledge intensive domains due to static prompts and agent roles, rigid workflows, and homogeneous model reliance, leading to poor domain adaptation, limited reasoning flexibility, and high latency on heterogeneous or long-horizon scientific tasks. They also struggle to revise earlier decisions when intermediate reasoning diverges, reducing reliability in structured and calculation heavy settings. To address these limitations, we propose a scientific domain oriented interactive two tier multi model orchestration framework. A dedicated orchestration model analyzes each task, dynamically constructs a domain aware reasoning pipeline, and instantiates specialized expert agents with tailored prompts, while an execution model performs each step under generated role and instruction specifications. The orchestrator iteratively updates the pipeline based on intermediate feedback, enabling dynamic replanning, role reallocation, and prompt refinement across multi turn interactions, strengthening robustness and specialization for scientific reasoning through structured heterogeneous model collaboration. The framework is model agnostic and supports heterogeneous LLM integration with different capacities or costs, enabling flexible performance efficiency trade offs in practical scientific deployments. Experiments show consistent improvements over existing multi agent systems and strong baselines across diverse reasoning and scientific style benchmarks.

