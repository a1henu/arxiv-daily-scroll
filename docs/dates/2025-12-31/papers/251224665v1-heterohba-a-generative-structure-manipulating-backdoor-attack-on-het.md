---
layout: default
title: HeteroHBA: A Generative Structure-Manipulating Backdoor Attack on Heterogeneous Graphs
---

# HeteroHBA: A Generative Structure-Manipulating Backdoor Attack on Heterogeneous Graphs
**arXiv**：[2512.24665v1](https://arxiv.org/abs/2512.24665) · [PDF](https://arxiv.org/pdf/2512.24665.pdf)  
**作者**：Honglin Gao, Lan Zhao, Junhao Ren, Xiang Li, Gaoxi Xiao  

**一句话要点**：提出HeteroHBA以解决异质图节点分类中的后门攻击问题

**关键词**：异质图神经网络, 后门攻击, 节点分类, 生成式框架, 隐蔽性优化, 防御评估

## 3 点简述
- 针对异质图节点分类，研究后门攻击，通过注入触发节点和连接来误导分类
- 采用生成式框架，基于显著性筛选辅助邻居，合成多样触发特征和连接模式以匹配异质上下文
- 结合AdaIN和MMD损失提升隐蔽性，双层优化平衡攻击成功率和清洁准确性，实验显示攻击成功率高且防御有效

## 摘要（原文）

> Heterogeneous graph neural networks (HGNNs) have achieved strong performance in many real-world applications, yet targeted backdoor poisoning on heterogeneous graphs remains less studied. We consider backdoor attacks for heterogeneous node classification, where an adversary injects a small set of trigger nodes and connections during training to force specific victim nodes to be misclassified into an attacker-chosen label at test time while preserving clean performance. We propose HeteroHBA, a generative backdoor framework that selects influential auxiliary neighbors for trigger attachment via saliency-based screening and synthesizes diverse trigger features and connection patterns to better match the local heterogeneous context. To improve stealthiness, we combine Adaptive Instance Normalization (AdaIN) with a Maximum Mean Discrepancy (MMD) loss to align the trigger feature distribution with benign statistics, thereby reducing detectability, and we optimize the attack with a bilevel objective that jointly promotes attack success and maintains clean accuracy. Experiments on multiple real-world heterogeneous graphs with representative HGNN architectures show that HeteroHBA consistently achieves higher attack success than prior backdoor baselines with comparable or smaller impact on clean accuracy; moreover, the attack remains effective under our heterogeneity-aware structural defense, CSD. These results highlight practical backdoor risks in heterogeneous graph learning and motivate the development of stronger defenses.

