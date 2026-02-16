---
layout: default
title: Backdoor Attacks on Contrastive Continual Learning for IoT Systems
---

# Backdoor Attacks on Contrastive Continual Learning for IoT Systems
**arXiv**：[2602.13062v1](https://arxiv.org/abs/2602.13062) · [PDF](https://arxiv.org/pdf/2602.13062.pdf)  
**作者**：Alfous Tim, Kuniyilh Simi D  

**一句话要点**：分析物联网系统中对比持续学习的后门攻击，评估其持久性威胁与防御策略

**关键词**：物联网安全, 对比持续学习, 后门攻击, 嵌入对齐, 重放机制, 防御策略

## 3 点简述
- 核心问题：对比持续学习在物联网系统中因几何目标和重放机制易受后门攻击，导致恶意行为持久化
- 方法要点：形式化嵌入级攻击目标，分析物联网部署的持久机制，构建分层分类法
- 实验或效果：比较不同学习范式的漏洞，在内存有限、边缘计算等约束下评估防御策略

## 摘要（原文）

> The Internet of Things (IoT) systems increasingly depend on continual learning to adapt to non-stationary environments. These environments can include factors such as sensor drift, changing user behavior, device aging, and adversarial dynamics. Contrastive continual learning (CCL) combines contrastive representation learning with incremental adaptation, enabling robust feature reuse across tasks and domains. However, the geometric nature of contrastive objectives, when paired with replay-based rehearsal and stability-preserving regularization, introduces new security vulnerabilities. Notably, backdoor attacks can exploit embedding alignment and replay reinforcement, enabling the implantation of persistent malicious behaviors that endure through updates and deployment cycles. This paper provides a comprehensive analysis of backdoor attacks on CCL within IoT systems. We formalize the objectives of embedding-level attacks, examine persistence mechanisms unique to IoT deployments, and develop a layered taxonomy tailored to IoT. Additionally, we compare vulnerabilities across various learning paradigms and evaluate defense strategies under IoT constraints, including limited memory, edge computing, and federated aggregation. Our findings indicate that while CCL is effective for enhancing adaptive IoT intelligence, it may also elevate long-lived representation-level threats if not adequately secured.

