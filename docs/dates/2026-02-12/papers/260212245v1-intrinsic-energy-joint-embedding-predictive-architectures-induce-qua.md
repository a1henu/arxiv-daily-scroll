---
layout: default
title: Intrinsic-Energy Joint Embedding Predictive Architectures Induce Quasimetric Spaces
---

# Intrinsic-Energy Joint Embedding Predictive Architectures Induce Quasimetric Spaces
**arXiv**：[2602.12245v1](https://arxiv.org/abs/2602.12245) · [PDF](https://arxiv.org/pdf/2602.12245.pdf)  
**作者**：Anthony Kobanda, Waris Radji  

**一句话要点**：提出内在能量JEPA诱导拟度量空间，连接表示学习与目标导向控制

**关键词**：联合嵌入预测架构, 拟度量强化学习, 内在能量, 目标导向控制, 表示学习, 不对称动态

## 3 点简述
- 核心问题：JEPA能量函数与QRL拟度量值在不对称动态下的结构匹配问题
- 方法要点：限制JEPA能量为内在能量，证明其构成拟度量，连接最优成本函数
- 实验或效果：理论分析表明对称能量不匹配单向可达性，支持拟度量能量应用

## 摘要（原文）

> Joint-Embedding Predictive Architectures (JEPAs) aim to learn representations by predicting target embeddings from context embeddings, inducing a scalar compatibility energy in a latent space. In contrast, Quasimetric Reinforcement Learning (QRL) studies goal-conditioned control through directed distance values (cost-to-go) that support reaching goals under asymmetric dynamics. In this short article, we connect these viewpoints by restricting attention to a principled class of JEPA energy functions : intrinsic (least-action) energies, defined as infima of accumulated local effort over admissible trajectories between two states. Under mild closure and additivity assumptions, any intrinsic energy is a quasimetric. In goal-reaching control, optimal cost-to-go functions admit exactly this intrinsic form ; inversely, JEPAs trained to model intrinsic energies lie in the quasimetric value class targeted by QRL. Moreover, we observe why symmetric finite energies are structurally mismatched with one-way reachability, motivating asymmetric (quasimetric) energies when directionality matters.

