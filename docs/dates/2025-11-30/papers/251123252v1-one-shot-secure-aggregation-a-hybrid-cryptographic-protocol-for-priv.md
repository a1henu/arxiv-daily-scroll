---
layout: default
title: One-Shot Secure Aggregation: A Hybrid Cryptographic Protocol for Private Federated Learning in IoT
---

# One-Shot Secure Aggregation: A Hybrid Cryptographic Protocol for Private Federated Learning in IoT
**arXiv**：[2511.23252v1](https://arxiv.org/abs/2511.23252) · [PDF](https://arxiv.org/pdf/2511.23252.pdf)  
**作者**：Imraul Emmaka, Tran Viet Xuan Phuong  

**一句话要点**：提出Hyb-Agg协议，通过混合加密技术解决物联网联邦学习中的通信效率问题

**关键词**：安全聚合, 联邦学习, 物联网, 同态加密, 通信效率, 隐私保护

## 3 点简述
- 物联网联邦学习中，传统安全聚合协议因多轮交互和大负载导致通信开销过高
- Hyb-Agg结合MK-CKKS同态加密和ECDH掩码，实现单轮非交互式安全聚合，降低通信成本
- 实验在资源受限设备上验证了亚秒级执行时间和约12倍恒定通信扩展因子

## 摘要（原文）

> Federated Learning (FL) offers a promising approach to collaboratively train machine learning models without centralizing raw data, yet its scalability is often throttled by excessive communication overhead. This challenge is magnified in Internet of Things (IoT) environments, where devices face stringent bandwidth, latency, and energy constraints. Conventional secure aggregation protocols, while essential for protecting model updates, frequently require multiple interaction rounds, large payload sizes, and per-client costs rendering them impractical for many edge deployments.
>   In this work, we present Hyb-Agg, a lightweight and communication-efficient secure aggregation protocol that integrates Multi-Key CKKS (MK-CKKS) homomorphic encryption with Elliptic Curve Diffie-Hellman (ECDH)-based additive masking. Hyb-Agg reduces the secure aggregation process to a single, non-interactive client-to-server transmission per round, ensuring that per-client communication remains constant regardless of the number of participants. This design eliminates partial decryption exchanges, preserves strong privacy under the RLWE, CDH, and random oracle assumptions, and maintains robustness against collusion by the server and up to $N-2$ clients.
>   We implement and evaluate Hyb-Agg on both high-performance and resource-constrained devices, including a Raspberry Pi 4, demonstrating that it delivers sub-second execution times while achieving a constant communication expansion factor of approximately 12x over plaintext size. By directly addressing the communication bottleneck, Hyb-Agg enables scalable, privacy-preserving federated learning that is practical for real-world IoT deployments.

