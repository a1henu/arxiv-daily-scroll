---
layout: default
title: SoK: Challenges in Tabular Membership Inference Attacks
---

# SoK: Challenges in Tabular Membership Inference Attacks
**arXiv**：[2601.15874v1](https://arxiv.org/abs/2601.15874) · [PDF](https://arxiv.org/pdf/2601.15874.pdf)  
**作者**：Cristina Pêra, Tânia Carvalho, Maxime Cordy, Luís Antunes  

**一句话要点**：系统分析表格数据中的成员推断攻击挑战，揭示单点记录高脆弱性及攻击跨架构转移性

**关键词**：成员推断攻击, 表格数据隐私, 联邦学习安全, 单点记录脆弱性, 攻击转移性

## 3 点简述
- 核心问题：成员推断攻击在表格数据中性能普遍较差，但单点记录仍高度脆弱
- 方法要点：扩展攻击分类学，评估集中式和联邦学习场景，包括外部攻击者威胁
- 实验或效果：攻击性能有限，但能暴露大量单点记录，不同代理模型提升攻击效果

## 摘要（原文）

> Membership Inference Attacks (MIAs) are currently a dominant approach for evaluating privacy in machine learning applications. Despite their significance in identifying records belonging to the training dataset, several concerns remain unexplored, particularly with regard to tabular data. In this paper, first, we provide an extensive review and analysis of MIAs considering two main learning paradigms: centralized and federated learning. We extend and refine the taxonomy for both. Second, we demonstrate the efficacy of MIAs in tabular data using several attack strategies, also including defenses. Furthermore, in a federated learning scenario, we consider the threat posed by an outsider adversary, which is often neglected. Third, we demonstrate the high vulnerability of single-outs (records with a unique signature) to MIAs. Lastly, we explore how MIAs transfer across model architectures. Our results point towards a general poor performance of these attacks in tabular data which contrasts with previous state-of-the-art. Notably, even attacks with limited attack performance can still successfully expose a large portion of single-outs. Moreover, our findings suggest that using different surrogate models makes MIAs more effective.

