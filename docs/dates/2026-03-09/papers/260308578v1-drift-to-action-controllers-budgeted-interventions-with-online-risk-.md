---
layout: default
title: Drift-to-Action Controllers: Budgeted Interventions with Online Risk Certificates
---

# Drift-to-Action Controllers: Budgeted Interventions with Online Risk Certificates
**arXiv**：[2603.08578v1](https://arxiv.org/abs/2603.08578) · [PDF](https://arxiv.org/pdf/2603.08578.pdf)  
**作者**：Ismail Lamaakal, Chaymae Yahyati, Khalid El Makkaoui, Ibrahim Ouahbi, Yassine Maleh  

**一句话要点**：提出Drift2Act控制器，在预算约束下实现分布漂移的安全干预决策

**关键词**：分布漂移监控, 在线风险认证, 预算干预决策, 机器学习安全, 流式学习

## 3 点简述
- 核心问题：机器学习系统部署中分布漂移监控常止于警报，缺乏安全响应机制
- 方法要点：结合感知层与在线风险证书，通过延迟标签查询生成风险上界，指导低成本或升级干预
- 实验或效果：在真实流式协议中，Drift2Act实现近零安全违规和快速恢复，优于多种基线方法

## 摘要（原文）

> Deployed machine learning systems face distribution drift, yet most monitoring pipelines stop at alarms and leave the response underspecified under labeling, compute, and latency constraints. We introduce Drift2Act, a drift-to-action controller that treats monitoring as constrained decision-making with explicit safety. Drift2Act combines a sensing layer that maps unlabeled monitoring signals to a belief over drift types with an active risk certificate that queries a small set of delayed labels from a recent window to produce an anytime-valid upper bound $U_t(δ)$ on current risk. The certificate gates operation: if $U_t(δ) \le τ$, the controller selects low-cost actions (e.g., recalibration or test-time adaptation); if $U_t(δ) > τ$, it activates abstain/handoff and escalates to rollback or retraining under cooldowns. In a realistic streaming protocol with label delay and explicit intervention costs, Drift2Act achieves near-zero safety violations and fast recovery at moderate cost on WILDS Camelyon17, DomainNet, and a controlled synthetic drift stream, outperforming alarm-only monitoring, adapt-always adaptation, schedule-based retraining, selective prediction alone, and an ablation without certification. Overall, online risk certification enables reliable drift response and reframes monitoring as decision-making with safety.

