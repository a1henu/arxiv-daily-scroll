---
layout: default
title: Anagent For Enhancing Scientific Table & Figure Analysis
---

# Anagent For Enhancing Scientific Table & Figure Analysis
**arXiv**：[2602.10081v1](https://arxiv.org/abs/2602.10081) · [PDF](https://arxiv.org/pdf/2602.10081.pdf)  
**作者**：Xuehang Guo, Zhiyong Lu, Tom Hope, Qingyun Wang  

**一句话要点**：提出Anagent多智能体框架以增强科学图表分析能力

**关键词**：科学图表分析, 多智能体框架, 长上下文处理, 基准测试, 强化学习优化

## 3 点简述
- 核心问题：科学图表分析面临复杂性、异构结构和长上下文需求等挑战，现有AI系统难以稳定处理。
- 方法要点：通过Planner、Expert、Solver和Critic四个专业智能体协同，结合监督微调和强化学习优化能力。
- 实验或效果：在AnaBench基准上，Anagent在免训练和微调设置下分别提升13.43%和42.12%，显示任务导向推理的重要性。

## 摘要（原文）

> In scientific research, analysis requires accurately interpreting complex multimodal knowledge, integrating evidence from different sources, and drawing inferences grounded in domain-specific knowledge. However, current artificial intelligence (AI) systems struggle to consistently demonstrate such capabilities. The complexity and variability of scientific tables and figures, combined with heterogeneous structures and long-context requirements, pose fundamental obstacles to scientific table \& figure analysis. To quantify these challenges, we introduce AnaBench, a large-scale benchmark featuring $63,178$ instances from nine scientific domains, systematically categorized along seven complexity dimensions. To tackle these challenges, we propose Anagent, a multi-agent framework for enhanced scientific table \& figure analysis through four specialized agents: Planner decomposes tasks into actionable subtasks, Expert retrieves task-specific information through targeted tool execution, Solver synthesizes information to generate coherent analysis, and Critic performs iterative refinement through five-dimensional quality assessment. We further develop modular training strategies that leverage supervised finetuning and specialized reinforcement learning to optimize individual capabilities while maintaining effective collaboration. Comprehensive evaluation across 170 subdomains demonstrates that Anagent achieves substantial improvements, up to $\uparrow 13.43\%$ in training-free settings and $\uparrow 42.12\%$ with finetuning, while revealing that task-oriented reasoning and context-aware problem-solving are essential for high-quality scientific table \& figure analysis. Our project page: https://xhguo7.github.io/Anagent/.

