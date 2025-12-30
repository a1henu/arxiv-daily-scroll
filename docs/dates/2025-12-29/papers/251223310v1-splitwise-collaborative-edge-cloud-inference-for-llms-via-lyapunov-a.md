---
layout: default
title: Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL
---

# Splitwise: Collaborative Edge-Cloud Inference for LLMs via Lyapunov-Assisted DRL
**arXiv**：[2512.23310v1](https://arxiv.org/abs/2512.23310) · [PDF](https://arxiv.org/pdf/2512.23310.pdf)  
**作者**：Abolfazl Younesi, Abbas Shabrang Maryan, Elyas Oustad, Zahra Najafabadi Samani, Mohsen Ansari, Thomas Fahringer  

**一句话要点**：提出Splitwise框架，通过Lyapunov辅助的深度强化学习实现LLM在边缘与云端的自适应细粒度划分，以优化延迟、能耗和精度。

**关键词**：边缘计算, LLM推理, 深度强化学习, Lyapunov优化, 自适应划分, Transformer分解

## 3 点简述
- 核心问题：LLM在边缘设备部署受限，云端推理延迟高，静态划分难以适应带宽波动。
- 方法要点：将Transformer层分解为注意力头和前馈子块，基于Lyapunov优化指导的DRL策略进行自适应划分，确保队列稳定性和鲁棒性。
- 实验或效果：在多种设备和模型上，Splitwise降低端到端延迟1.4-2.8倍，能耗减少高达41%，95%延迟降低53-61%，保持精度和适度内存需求。

## 摘要（原文）

> Deploying large language models (LLMs) on edge devices is challenging due to their limited memory and power resources. Cloud-only inference reduces device burden but introduces high latency and cost. Static edge-cloud partitions optimize a single metric and struggle when bandwidth fluctuates. We propose Splitwise, a novel Lyapunov-assisted deep reinforcement learning (DRL) framework for fine-grained, adaptive partitioning of LLMs across edge and cloud environments. Splitwise decomposes transformer layers into attention heads and feed-forward sub-blocks, exposing more partition choices than layer-wise schemes. A hierarchical DRL policy, guided by Lyapunov optimization, jointly minimizes latency, energy consumption, and accuracy degradation while guaranteeing queue stability under stochastic workloads and variable network bandwidth. Splitwise also guarantees robustness via partition checkpoints with exponential backoff recovery in case of communication failures. Experiments on Jetson Orin NX, Galaxy S23, and Raspberry Pi 5 with GPT-2 (1.5B), LLaMA-7B, and LLaMA-13B show that Splitwise reduces end-to-end latency by 1.4x-2.8x and cuts energy consumption by up to 41% compared with existing partitioners. It lowers the 95th-percentile latency by 53-61% relative to cloud-only execution, while maintaining accuracy and modest memory requirements.

