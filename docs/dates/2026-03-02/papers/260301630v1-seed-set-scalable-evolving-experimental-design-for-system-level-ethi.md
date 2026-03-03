---
layout: default
title: SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing
---

# SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing
**arXiv**：[2603.01630v1](https://arxiv.org/abs/2603.01630) · [PDF](https://arxiv.org/pdf/2603.01630.pdf)  
**作者**：Anjali Parashar, Yingke Li, Eric Yang Yu, Fei Chen, James Neidhoefer, Devesh Upadhyay, Chuchu Fan  

**一句话要点**：提出SEED-SET框架以解决自主系统伦理测试中的可扩展性和主观性挑战

**关键词**：自主系统伦理测试, 贝叶斯实验设计, 分层高斯过程, 主观价值建模, 可扩展测试框架

## 3 点简述
- 核心问题：自主系统在人类中心领域部署时，缺乏普遍伦理评估指标和主观性建模方法。
- 方法要点：基于贝叶斯实验设计，结合客观评估和主观价值判断，使用分层高斯过程建模。
- 实验或效果：在应用中验证，生成最多2倍最优测试候选，高维搜索空间覆盖提升1.25倍。

## 摘要（原文）

> As autonomous systems such as drones, become increasingly deployed in high-stakes, human-centric domains, it is critical to evaluate the ethical alignment since failure to do so imposes imminent danger to human lives, and long term bias in decision-making. Automated ethical benchmarking of these systems is understudied due to the lack of ubiquitous, well-defined metrics for evaluation, and stakeholder-specific subjectivity, which cannot be modeled analytically. To address these challenges, we propose SEED-SET, a Bayesian experimental design framework that incorporates domain-specific objective evaluations, and subjective value judgments from stakeholders. SEED-SET models both evaluation types separately with hierarchical Gaussian Processes, and uses a novel acquisition strategy to propose interesting test candidates based on learnt qualitative preferences and objectives that align with the stakeholder preferences. We validate our approach for ethical benchmarking of autonomous agents on two applications and find our method to perform the best. Our method provides an interpretable and efficient trade-off between exploration and exploitation, by generating up to $2\times$ optimal test candidates compared to baselines, with $1.25\times$ improvement in coverage of high dimensional search spaces.

