---
layout: default
title: TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution
---

# TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution
**arXiv**：[2602.09662v1](https://arxiv.org/abs/2602.09662) · [PDF](https://arxiv.org/pdf/2602.09662.pdf)  
**作者**：Deyang Jiang, Jing Huang, Xuanle Zhao, Lei Chen, Liming Zheng, Fanfan Liu, Haibo Qiu, Peng Shi, Zhixiong Zeng  

**一句话要点**：提出TreeCUA以高效扩展GUI自动化，通过树结构可验证演化解决GUI规划数据收集难题。

**关键词**：GUI自动化, 树结构演化, 多智能体协作, 自适应探索, 轨迹规划, 泛化能力

## 3 点简述
- 核心问题：现有GUI自动化工作侧重GUI定位而非GUI规划，后者需更复杂数据收集，限制扩展性。
- 方法要点：设计多智能体协作框架，结合树结构存储、自适应探索算法和知识引导，生成高质量GUI轨迹。
- 实验或效果：实验显示TreeCUA和TreeCUA-DPO显著提升性能，OOD研究验证强泛化能力，代码开源。

## 摘要（原文）

> Effectively scaling GUI automation is essential for computer-use agents (CUAs); however, existing work primarily focuses on scaling GUI grounding rather than the more crucial GUI planning, which requires more sophisticated data collection. In reality, the exploration process of a CUA across apps/desktops/web pages typically follows a tree structure, with earlier functional entry points often being explored more frequently. Thus, organizing large-scale trajectories into tree structures can reduce data cost and streamline the data scaling of GUI planning. In this work, we propose TreeCUA to efficiently scale GUI automation with tree-structured verifiable evolution. We propose a multi-agent collaborative framework to explore the environment, verify actions, summarize trajectories, and evaluate quality to generate high-quality and scalable GUI trajectories. To improve efficiency, we devise a novel tree-based topology to store and replay duplicate exploration nodes, and design an adaptive exploration algorithm to balance the depth (\emph{i.e.}, trajectory difficulty) and breadth (\emph{i.e.}, trajectory diversity). Moreover, we develop world knowledge guidance and global memory backtracking to avoid low-quality generation. Finally, we naturally extend and propose the TreeCUA-DPO method from abundant tree node information, improving GUI planning capability by referring to the branch information of adjacent trajectories. Experimental results show that TreeCUA and TreeCUA-DPO offer significant improvements, and out-of-domain (OOD) studies further demonstrate strong generalization. All trajectory node information and code will be available at https://github.com/UITron-hub/TreeCUA.

