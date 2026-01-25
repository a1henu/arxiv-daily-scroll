---
layout: default
title: SoK: Challenges in Tabular Membership Inference Attacks
---

# SoK: Challenges in Tabular Membership Inference Attacks
**arXiv**：[2601.15874v1](https://arxiv.org/abs/2601.15874) · [PDF](https://arxiv.org/pdf/2601.15874.pdf)  
**作者**：Cristina Pêra, Tânia Carvalho, Maxime Cordy, Luís Antunes  

**一句话要点**：系统分析表格数据中的成员推断攻击挑战，涵盖集中与联邦学习场景。

**关键词**：成员推断攻击, 表格数据隐私, 联邦学习安全, 攻击分类, 单点记录脆弱性, 代理模型

## 3 点简述
- 核心问题：成员推断攻击在表格数据中的隐私评估存在未探索的挑战，如单点记录的高脆弱性。
- 方法要点：扩展攻击分类，评估多种攻击策略与防御，包括联邦学习中的外部对手威胁。
- 实验或效果：攻击在表格数据中普遍表现不佳，但能有效暴露单点记录，且使用不同代理模型可提升攻击效果。

## 摘要（原文）

> Membership Inference Attacks (MIAs) are currently a dominant approach for evaluating privacy in machine learning applications. Despite their significance in identifying records belonging to the training dataset, several concerns remain unexplored, particularly with regard to tabular data. In this paper, first, we provide an extensive review and analysis of MIAs considering two main learning paradigms: centralized and federated learning. We extend and refine the taxonomy for both. Second, we demonstrate the efficacy of MIAs in tabular data using several attack strategies, also including defenses. Furthermore, in a federated learning scenario, we consider the threat posed by an outsider adversary, which is often neglected. Third, we demonstrate the high vulnerability of single-outs (records with a unique signature) to MIAs. Lastly, we explore how MIAs transfer across model architectures. Our results point towards a general poor performance of these attacks in tabular data which contrasts with previous state-of-the-art. Notably, even attacks with limited attack performance can still successfully expose a large portion of single-outs. Moreover, our findings suggest that using different surrogate models makes MIAs more effective.

