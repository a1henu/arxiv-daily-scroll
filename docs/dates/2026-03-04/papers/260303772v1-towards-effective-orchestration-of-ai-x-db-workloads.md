---
layout: default
title: Towards Effective Orchestration of AI x DB Workloads
---

# Towards Effective Orchestration of AI x DB Workloads
**arXiv**：[2603.03772v1](https://arxiv.org/abs/2603.03772) · [PDF](https://arxiv.org/pdf/2603.03772.pdf)  
**作者**：Naili Xing, Haotian Gao, Zhanhao Zhao, Shaofeng Cai, Zhaojing Luo, Yuncheng Wu, Zhongle Xie, Meihui Zhang, Beng Chin Ooi  

**一句话要点**：探讨AI与数据库集成中的挑战，提出设计以优化AIxDB查询性能

**关键词**：AI与数据库集成, 查询优化, 执行调度, 分布式执行, 事务管理, 访问控制

## 3 点简述
- 核心问题：AI与数据库集成面临查询优化、执行调度和分布式执行等挑战
- 方法要点：重新审视事务管理和访问控制以支持AI生命周期管理
- 实验或效果：展示初步结果，可能对AIxDB查询性能至关重要

## 摘要（原文）

> AI-driven analytics are increasingly crucial to data-centric decision-making. The practice of exporting data to machine learning runtimes incurs high overhead, limits robustness to data drift, and expands the attack surface, especially in multi-tenant, heterogeneous data systems. Integrating AI directly into database engines, while offering clear benefits, introduces challenges in managing joint query processing and model execution, optimizing end-to-end performance, coordinating execution under resource contention, and enforcing strong security and access-control guarantees.
>   This paper discusses the challenges of joint DB-AI, or AIxDB, data management and query processing within AI-powered data systems. It presents various challenges that need to be addressed carefully, such as query optimization, execution scheduling, and distributed execution over heterogeneous hardware. Database components such as transaction management and access control need to be re-examined to support AI lifecycle management, mitigate data drift, and protect sensitive data from unauthorized AI operations. We present a design and preliminary results to demonstrate what may be key to the performance for serving AIxDB queries.

