---
layout: default
title: What Papers Don't Tell You: Recovering Tacit Knowledge for Automated Paper Reproduction
---

# What Papers Don't Tell You: Recovering Tacit Knowledge for Automated Paper Reproduction
**arXiv**：[2603.01801v1](https://arxiv.org/abs/2603.01801) · [PDF](https://arxiv.org/pdf/2603.01801.pdf)  
**作者**：Lehui Li, Ruining Wang, Haochen Song, Yaoxin Mao, Tong Zhang, Yuyao Wang, Jiayi Fan, Yitong Zhang, Jieping Ye, Chengqi Zhang, Yongshun Gong  

**一句话要点**：提出基于图的智能体框架以恢复论文隐含知识，提升自动化代码生成性能

**关键词**：自动化论文复现, 隐含知识恢复, 图智能体框架, 关系知识, 执行反馈, 知识归纳

## 3 点简述
- 核心问题：自动化论文复现受限于关系、体感和集体三类隐含知识，而非信息检索
- 方法要点：通过节点级关系聚合、执行反馈精炼和图级知识归纳机制逐步恢复隐含知识
- 实验或效果：在扩展ReproduceBench上，平均性能差距为10.04%，优于基线24.68%

## 摘要（原文）

> Automated paper reproduction -- generating executable code from academic papers -- is bottlenecked not by information retrieval but by the tacit knowledge that papers inevitably leave implicit. We formalize this challenge as the progressive recovery of three types of tacit knowledge -- relational, somatic, and collective -- and propose \method, a graph-based agent framework with a dedicated mechanism for each: node-level relation-aware aggregation recovers relational knowledge by analyzing implementation-unit-level reuse and adaptation relationships between the target paper and its citation neighbors; execution-feedback refinement recovers somatic knowledge through iterative debugging driven by runtime signals; and graph-level knowledge induction distills collective knowledge from clusters of papers sharing similar implementations. On an extended ReproduceBench spanning 3 domains, 10 tasks, and 40 recent papers, \method{} achieves an average performance gap of 10.04\% against official implementations, improving over the strongest baseline by 24.68\%. The code will be publicly released upon acceptance; the repository link will be provided in the final version.

