---
layout: default
title: Nimbus: A Unified Embodied Synthetic Data Generation Framework
---

# Nimbus: A Unified Embodied Synthetic Data Generation Framework
**arXiv**：[2601.21449v1](https://arxiv.org/abs/2601.21449) · [PDF](https://arxiv.org/pdf/2601.21449.pdf)  
**作者**：Zeyu He, Yuchang Zhang, Yuanzhen Zhou, Miao Tao, Hengjie Li, Yang Tian, Jia Zeng, Tai Wang, Wenzhe Cai, Yilun Chen, Ning Gao, Jiangmiao Pang  

**一句话要点**：提出Nimbus统一框架以解决具身智能合成数据生成中的碎片化与低效问题

**关键词**：具身智能, 合成数据生成, 统一框架, 分布式系统, 异步处理, 资源优化

## 3 点简述
- 核心问题：现有合成数据生成管道碎片化且任务特定，导致工程效率低下和系统不稳定，难以支持基础模型训练所需的高吞吐量数据生成
- 方法要点：采用模块化四层架构，通过解耦执行模型将轨迹规划、渲染和存储分离为异步阶段，并实施动态调度、负载均衡和容错机制
- 实验或效果：相比未优化基线，Nimbus实现端到端吞吐量提升2-3倍，确保大规模分布式环境中的稳健长期运行

## 摘要（原文）

> Scaling data volume and diversity is critical for generalizing embodied intelligence. While synthetic data generation offers a scalable alternative to expensive physical data acquisition, existing pipelines remain fragmented and task-specific. This isolation leads to significant engineering inefficiency and system instability, failing to support the sustained, high-throughput data generation required for foundation model training. To address these challenges, we present Nimbus, a unified synthetic data generation framework designed to integrate heterogeneous navigation and manipulation pipelines. Nimbus introduces a modular four-layer architecture featuring a decoupled execution model that separates trajectory planning, rendering, and storage into asynchronous stages. By implementing dynamic pipeline scheduling, global load balancing, distributed fault tolerance, and backend-specific rendering optimizations, the system maximizes resource utilization across CPU, GPU, and I/O resources. Our evaluation demonstrates that Nimbus achieves a 2-3X improvement in end-to-end throughput compared to unoptimized baselines and ensuring robust, long-term operation in large-scale distributed environments. This framework serves as the production backbone for the InternData suite, enabling seamless cross-domain data synthesis.

