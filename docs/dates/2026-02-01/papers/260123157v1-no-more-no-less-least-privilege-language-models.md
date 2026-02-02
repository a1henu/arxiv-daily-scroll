---
layout: default
title: No More, No Less: Least-Privilege Language Models
---

# No More, No Less: Least-Privilege Language Models
**arXiv**：[2601.23157v1](https://arxiv.org/abs/2601.23157) · [PDF](https://arxiv.org/pdf/2601.23157.pdf)  
**作者**：Paulius Rauba, Dominykas Seputis, Patrikas Vanagas, Mihaela van der Schaar  

**一句话要点**：提出最小特权语言模型以在部署时动态控制模型内部计算访问

**关键词**：最小特权原则, 语言模型部署, 内部计算控制, 特权分配, 能力抑制, 部署范式

## 3 点简述
- 核心问题：语言模型部署缺乏最小特权原则，导致不必要能力暴露
- 方法要点：定义特权为前向传播可达内部计算，提出嵌套最小特权网络作为可逆控制机制
- 实验或效果：展示特权-效用前沿，实现目标能力选择性抑制且副作用有限

## 摘要（原文）

> Least privilege is a core security principle: grant each request only the minimum access needed to achieve its goal. Deployed language models almost never follow it, instead being exposed through a single API endpoint that serves all users and requests. This gap exists not because least privilege would be unhelpful; deployments would benefit greatly from reducing unnecessary capability exposure. The real obstacle is definitional and mechanistic: what does "access" mean inside a language model, and how can we enforce it without retraining or deploying multiple models? We take inspiration from least privilege in computer systems and define a class of models called least-privilege language models, where privilege is reachable internal computation during the forward pass. In this view, lowering privilege literally shrinks the model's accessible function class, as opposed to denying access via learned policies. We formalize deployment-time control as a monitor-allocator-enforcer stack, separating (i) request-time signals, (ii) a decision rule that allocates privilege, and (iii) an inference-time mechanism that selects privilege. We then propose Nested Least-Privilege Networks, a shape-preserving, rank-indexed intervention that provides a smooth, reversible control knob. We show that this knob yields policy-usable privilege-utility frontiers and enables selective suppression of targeted capabilities with limited collateral degradation across various policies. Most importantly, we argue for a new deployment paradigm that challenges the premise that language models can only be controlled at the output level.

