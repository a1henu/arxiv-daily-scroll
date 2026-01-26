---
layout: default
title: Building a Robust Risk-Based Access Control System to Combat Ransomware's Capability to Encrypt: A Machine Learning Approach
---

# Building a Robust Risk-Based Access Control System to Combat Ransomware's Capability to Encrypt: A Machine Learning Approach
**arXiv**：[2601.16795v1](https://arxiv.org/abs/2601.16795) · [PDF](https://arxiv.org/pdf/2601.16795.pdf)  
**作者**：Kenan Begovic, Abdulaziz Al-Ali, Qutaibah Malluhi  

**一句话要点**：提出基于机器学习的风险访问控制系统，以实时阻止Linux上的勒索软件加密行为。

**关键词**：勒索软件防御, 风险访问控制, 机器学习, 函数级追踪, SELinux策略, 实时加密监管

## 3 点简述
- 核心问题：勒索软件通过未授权加密攻击系统，需在不干扰合法使用下识别恶意加密活动。
- 方法要点：利用函数级追踪构建数据集，结合监督分类器和可解释规则驱动SELinux策略进行实时访问控制。
- 实验或效果：系统在保持检测质量的同时实现规则级响应，量化了操作开销并规划了优化步骤。

## 摘要（原文）

> Ransomware core capability, unauthorized encryption, demands controls that identify and block malicious cryptographic activity without disrupting legitimate use. We present a probabilistic, risk-based access control architecture that couples machine learning inference with mandatory access control to regulate encryption on Linux in real time. The system builds a specialized dataset from the native ftrace framework using the function_graph tracer, yielding high-resolution kernel-function execution traces augmented with resource and I/O counters. These traces support both a supervised classifier and interpretable rules that drive an SELinux policy via lightweight booleans, enabling context-sensitive permit/deny decisions at the moment encryption begins. Compared to approaches centered on sandboxing, hypervisor introspection, or coarse system-call telemetry, the function-level tracing we adopt provides finer behavioral granularity than syscall-only telemetry while avoiding the virtualization/VMI overhead of sandbox-based approaches. Our current user-space prototype has a non-trivial footprint under burst I/O; we quantify it and recognize that a production kernel-space solution should aim to address this. We detail dataset construction, model training and rule extraction, and the run-time integration that gates file writes for suspect encryption while preserving benign cryptographic workflows. During evaluation, the two-layer composition retains model-level detection quality while delivering rule-like responsiveness; we also quantify operational footprint and outline engineering steps to reduce CPU and memory overhead for enterprise deployment. The result is a practical path from behavioral tracing and learning to enforceable, explainable, and risk-proportionate encryption control on production Linux systems.

