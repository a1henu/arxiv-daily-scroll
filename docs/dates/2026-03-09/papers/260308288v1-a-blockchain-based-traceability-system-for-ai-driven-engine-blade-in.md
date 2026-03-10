---
layout: default
title: A Blockchain-based Traceability System for AI-Driven Engine Blade Inspection
---

# A Blockchain-based Traceability System for AI-Driven Engine Blade Inspection
**arXiv**：[2603.08288v1](https://arxiv.org/abs/2603.08288) · [PDF](https://arxiv.org/pdf/2603.08288.pdf)  
**作者**：Mahmoud Hafez, Eman Ouda, Mohammed A. Mohammed Eltoum, Khaled Salah, Yusra Abdulrahman  

**一句话要点**：提出BladeChain区块链系统，为航空发动机叶片AI检测提供不可篡改的追溯性

**关键词**：区块链追溯系统, 航空发动机叶片检测, AI模型溯源, Hyperledger Fabric, 不可篡改记录, 多利益相关方协作

## 3 点简述
- 核心问题：现有叶片检测记录系统分散、难审计、易篡改，影响多利益相关方协作。
- 方法要点：基于Hyperledger Fabric构建四利益方网络，集成状态机自动调度检测，链下存储检测数据并链接AI模型版本。
- 实验或效果：原型在100叶片负载下实现100%生命周期完成，吞吐量26操作/分钟，篡改检测延迟17毫秒。

## 摘要（原文）

> Aircraft engine blade maintenance relies on inspection records shared across manufacturers, airlines, maintenance organizations, and regulators. Yet current systems are fragmented, difficult to audit, and vulnerable to tampering. This paper presents BladeChain, a blockchain-based system providing immutable traceability for blade inspections throughout the component life cycle. BladeChain is the first system to integrate multi-stakeholder endorsement, automated inspection scheduling, AI model provenance, and cryptographic evidence binding, delivering auditable maintenance traceability for aerospace deployments. Built on a four-stakeholder Hyperledger Fabric network (OEM, Airline, MRO, Regulator), BladeChain captures every life-cycle event in a tamper-evident ledger. A chaincode-enforced state machine governs blade status transitions and automatically triggers inspections when configurable flight hour, cycle, or calendar thresholds are exceeded, eliminating manual scheduling errors. Inspection artifacts are stored off-chain in IPFS and linked to on-chain records via SHA-256 hashes, with each inspection record capturing the AI model name and version used for defect detection. This enables regulators to audit both what defects were found and how they were found. The detection module is pluggable, allowing organizations to adopt or upgrade inspection models without modifying the ledger or workflows. We built a prototype and evaluated it on workloads of up to 100 blades, demonstrating 100% life cycle completion with consistent throughput of 26 operations per minute. A centralized SQL baseline quantifies the consensus overhead and highlights the security trade-off. Security validation confirms tamper detection within 17~ms through hash verification.

