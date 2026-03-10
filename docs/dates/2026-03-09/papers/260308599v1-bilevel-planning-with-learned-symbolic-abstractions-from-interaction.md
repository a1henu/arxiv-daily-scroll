---
layout: default
title: Bilevel Planning with Learned Symbolic Abstractions from Interaction Data
---

# Bilevel Planning with Learned Symbolic Abstractions from Interaction Data
**arXiv**：[2603.08599v1](https://arxiv.org/abs/2603.08599) · [PDF](https://arxiv.org/pdf/2603.08599.pdf)  
**作者**：Fatih Dogangun, Burcu Kilic, Serdar Bahar, Emre Ugur  

**一句话要点**：提出双层神经符号框架以解决复杂环境中连续动态与离散表示的规划问题

**关键词**：神经符号规划, 双层规划, 概率符号规则, 连续效应模型, 多物体操作

## 3 点简述
- 核心问题：现有符号抽象方法依赖确定性符号域，缺乏验证机制，难以捕捉环境连续动态
- 方法要点：高层使用学习到的概率符号规则快速生成候选计划，低层用连续效应模型验证计划并在必要时进行前向搜索
- 实验或效果：在多物体操作任务中，该方法优于纯符号方法，通过验证可靠识别失败计划，规划性能与连续前向搜索统计相当

## 摘要（原文）

> Intelligent agents must reason over both continuous dynamics and discrete representations to generate effective plans in complex environments. Previous studies have shown that symbolic abstractions can emerge from neural effect predictors trained with a robot's unsupervised exploration. However, these methods rely on deterministic symbolic domains, lack mechanisms to verify the generated symbolic plans, and operate only at the abstract level, often failing to capture the continuous dynamics of the environment. To overcome these limitations, we propose a bilevel neuro-symbolic framework in which learned probabilistic symbolic rules generate candidate plans rapidly at the high level, and learned continuous effect models verify these plans and perform forward search when necessary at the low level. Our experiments on multi-object manipulation tasks demonstrate that the proposed bilevel method outperforms symbolic-only approaches, reliably identifying failing plans through verification, and achieves planning performance statistically comparable to continuous forward search while resolving most problems via efficient symbolic reasoning.

