---
layout: default
title: READY: Reward Discovery for Meta-Black-Box Optimization
---

# READY: Reward Discovery for Meta-Black-Box Optimization
**arXiv**：[2601.21847v1](https://arxiv.org/abs/2601.21847) · [PDF](https://arxiv.org/pdf/2601.21847.pdf)  
**作者**：Zechuan Huang, Zhiguang Cao, Hongshu Guo, Yue-Jiao Gong, Zeyuan Ma  

**一句话要点**：提出READY框架，利用大语言模型自动发现奖励函数以提升元黑盒优化性能。

**关键词**：元黑盒优化, 奖励函数发现, 大语言模型应用, 演化算法, 多任务学习

## 3 点简述
- 核心问题：现有元黑盒优化中奖励函数依赖人工设计，存在偏差和奖励黑客风险。
- 方法要点：基于大语言模型，结合演化启发式和多任务架构，实现高效并行奖励发现。
- 实验或效果：实证表明发现的奖励函数能提升现有元黑盒优化方法，强调奖励设计重要性。

## 摘要（原文）

> Meta-Black-Box Optimization (MetaBBO) is an emerging avenue within Optimization community, where algorithm design policy could be meta-learned by reinforcement learning to enhance optimization performance. So far, the reward functions in existing MetaBBO works are designed by human experts, introducing certain design bias and risks of reward hacking. In this paper, we use Large Language Model~(LLM) as an automated reward discovery tool for MetaBBO. Specifically, we consider both effectiveness and efficiency sides. On effectiveness side, we borrow the idea of evolution of heuristics, introducing tailored evolution paradigm in the iterative LLM-based program search process, which ensures continuous improvement. On efficiency side, we additionally introduce multi-task evolution architecture to support parallel reward discovery for diverse MetaBBO approaches. Such parallel process also benefits from knowledge sharing across tasks to accelerate convergence. Empirical results demonstrate that the reward functions discovered by our approach could be helpful for boosting existing MetaBBO works, underscoring the importance of reward design in MetaBBO. We provide READY's project at https://anonymous.4open.science/r/ICML_READY-747F.

