---
layout: default
title: zkFL-Health: Blockchain-Enabled Zero-Knowledge Federated Learning for Medical AI Privacy
---

# zkFL-Health: Blockchain-Enabled Zero-Knowledge Federated Learning for Medical AI Privacy
**arXiv**：[2512.21048v1](https://arxiv.org/abs/2512.21048) · [PDF](https://arxiv.org/pdf/2512.21048.pdf)  
**作者**：Savvy Sharma, George Petrovic, Sarthak Kaushik  

**一句话要点**：提出zkFL-Health架构，结合零知识证明与可信执行环境，解决医疗AI联邦学习中的隐私泄露与聚合器信任问题。

**关键词**：医疗AI隐私, 联邦学习, 零知识证明, 可信执行环境, 区块链审计, 隐私保护机器学习

## 3 点简述
- 医疗AI需多机构数据，但隐私约束阻碍共享，联邦学习仍面临梯度泄露和聚合器信任风险。
- zkFL-Health使用零知识证明和可信执行环境，确保聚合过程隐私且可验证，无需信任单一节点。
- 性能评估计划涵盖准确性、隐私风险、延迟和成本，旨在实现强保密性、完整性和可审计性。

## 摘要（原文）

> Healthcare AI needs large, diverse datasets, yet strict privacy and governance constraints prevent raw data sharing across institutions. Federated learning (FL) mitigates this by training where data reside and exchanging only model updates, but practical deployments still face two core risks: (1) privacy leakage via gradients or updates (membership inference, gradient inversion) and (2) trust in the aggregator, a single point of failure that can drop, alter, or inject contributions undetected. We present zkFL-Health, an architecture that combines FL with zero-knowledge proofs (ZKPs) and Trusted Execution Environments (TEEs) to deliver privacy-preserving, verifiably correct collaborative training for medical AI. Clients locally train and commit their updates; the aggregator operates within a TEE to compute the global update and produces a succinct ZK proof (via Halo2/Nova) that it used exactly the committed inputs and the correct aggregation rule, without revealing any client update to the host. Verifier nodes validate the proof and record cryptographic commitments on-chain, providing an immutable audit trail and removing the need to trust any single party. We outline system and threat models tailored to healthcare, the zkFL-Health protocol, security/privacy guarantees, and a performance evaluation plan spanning accuracy, privacy risk, latency, and cost. This framework enables multi-institutional medical AI with strong confidentiality, integrity, and auditability, key properties for clinical adoption and regulatory compliance.

