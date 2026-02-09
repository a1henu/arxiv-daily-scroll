---
layout: default
title: Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2
---

# Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2
**arXiv**：[2602.06345v1](https://arxiv.org/abs/2602.06345) · [PDF](https://arxiv.org/pdf/2602.06345.pdf)  
**作者**：Qianlong Lan, Anuj Kaul, Shaun Jones, Stephanie Westrum  

**一句话要点**：提出零信任运行时验证框架以解决AP2协议在代理支付系统中的重放和上下文绑定失效问题

**关键词**：代理支付协议, 零信任安全, 运行时验证, 授权强制执行, 并发攻击缓解, AP2协议

## 3 点简述
- 核心问题：AP2协议在代理执行时面临运行时行为（如重试、并发）导致的授权强制执行缺口。
- 方法要点：采用动态生成的时间绑定随机数，强制执行显式上下文绑定和一次性消费语义。
- 实验或效果：在高并发模拟中，框架能抵御所有评估攻击，验证延迟约3.8毫秒，状态开销受峰值并发限制。

## 摘要（原文）

> The deployment of autonomous AI agents capable of executing commercial transactions has motivated the adoption of mandate-based payment authorization protocols, including the Universal Commerce Protocol (UCP) and the Agent Payments Protocol (AP2). These protocols replace interactive, session-based authorization with cryptographically issued mandates, enabling asynchronous and autonomous execution. While AP2 provides specification-level guarantees through signature verification, explicit binding, and expiration semantics, real-world agentic execution introduces runtime behaviors such as retries, concurrency, and orchestration that challenge implicit assumptions about mandate usage.
>   In this work, we present a security analysis of the AP2 mandate lifecycle and identify enforcement gaps that arise during runtime in agent-based payment systems. We propose a zero-trust runtime verification framework that enforces explicit context binding and consume-once mandate semantics using dynamically generated, time-bound nonces, ensuring that authorization decisions are evaluated at execution time rather than assumed from static issuance properties.
>   Through simulation-based evaluation under high concurrency, we show that context-aware binding and consume-once enforcement address distinct and complementary attack classes, and that both are required to prevent replay and context-redirect attacks. The proposed framework mitigates all evaluated attacks while maintaining stable verification latency of approximately 3.8~ms at throughput levels up to 10{,}000 transactions per second. We further demonstrate that the required runtime state is bounded by peak concurrency rather than cumulative transaction history, indicating that robust runtime security for agentic payment execution can be achieved with minimal and predictable overhead.

