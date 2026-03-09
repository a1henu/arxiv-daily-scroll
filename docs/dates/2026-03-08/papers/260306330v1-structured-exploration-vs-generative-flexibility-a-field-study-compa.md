---
layout: default
title: Structured Exploration vs. Generative Flexibility: A Field Study Comparing Bandit and LLM Architectures for Personalised Health Behaviour Interventions
---

# Structured Exploration vs. Generative Flexibility: A Field Study Comparing Bandit and LLM Architectures for Personalised Health Behaviour Interventions
**arXiv**：[2603.06330v1](https://arxiv.org/abs/2603.06330) · [PDF](https://arxiv.org/pdf/2603.06330.pdf)  
**作者**：Dominik P. Hofer, Haochen Song, Rania Islambouli, Laura Hawkins, Ananya Bhattacharjee, Meredith Franklin, Joseph Jay Williams, Jan D. Smeddinck  

**一句话要点**：比较上下文多臂老虎机与LLM架构在个性化健康行为干预中的效果，揭示生成灵活性与结构化探索的权衡。

**关键词**：行为改变技术, 上下文多臂老虎机, 大型语言模型, 个性化健康干预, 实地研究, 探索-利用权衡

## 3 点简述
- 核心问题：数字健康干预中行为改变技术（BCTs）的选择与传递存在挑战，需优化方法以提高感知帮助性。
- 方法要点：通过4周实地研究（N=54），比较随机模板、上下文老虎机、LLM生成、混合老虎机+LLM及带交互历史的LLM五种消息传递方法。
- 实验或效果：LLM方法比模板更受好评，但老虎机优化未显著提升感知帮助性；LLM倾向于聚焦单一BCT，而老虎机强制跨技术探索-利用平衡。

## 摘要（原文）

> Behaviour Change Techniques (BCTs) are central to digital health interventions, yet selecting and delivering effective techniques remains challenging. Contextual bandits enable statistically grounded optimisation of BCT selection, while Large Language Models (LLMs) offer flexible, context-sensitive message generation. We conducted a 4-week study on physical activity motivation (N=54; 9 post-study interviews) that compared five daily messaging approaches: random templates, contextual bandit with templates, LLM generation, hybrid bandit+LLM, and LLM with interaction history. LLM-based approaches were rated substantially more helpful than templates, but no significant differences emerged among LLM conditions. Unexpectedly, bandit optimisation for BCTs selection yielded no additional perceived helpfulness compared with LLM-only approaches. Unconstrained LLMs focused heavily on a single BCT, whereas bandit systems enforced systematic exploration-exploitation across techniques. Quantitative and qualitative findings suggest contextual acknowledgement of user input drove perceived helpfulness. We contribute design suggestions for reflective AI health behaviour change systems that address a trade-off between structured exploration and generative autonomy.

