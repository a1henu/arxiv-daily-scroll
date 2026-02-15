---
layout: default
title: Move What Matters: Parameter-Efficient Domain Adaptation via Optimal Transport Flow for Collaborative Perception
---

# Move What Matters: Parameter-Efficient Domain Adaptation via Optimal Transport Flow for Collaborative Perception
**arXiv**：[2602.11565v1](https://arxiv.org/abs/2602.11565) · [PDF](https://arxiv.org/pdf/2602.11565.pdf)  
**作者**：Zesheng Jia, Jin Wang, Siao Liu, Lingzhi Li, Ziyao Huang, Yunjiang Xu, Jianping Wang  

**一句话要点**：提出FlowAdapt框架，基于最优传输理论解决V2X协同感知中的参数高效域适应问题

**关键词**：协同感知, 参数高效域适应, 最优传输, 多智能体系统, V2X通信

## 3 点简述
- 核心问题：PEFT在多智能体协同感知中因异构流冗余和深层语义侵蚀导致性能下降与训练不稳定
- 方法要点：引入Wasserstein贪婪采样减少冗余样本，设计渐进知识传输模块缓解语义退化
- 实验或效果：在三个基准测试中以仅1%可训练参数实现最优性能，提升样本效率与泛化能力

## 摘要（原文）

> Fast domain adaptation remains a fundamental challenge for deploying multi-agent systems across diverse environments in Vehicle-to-Everything (V2X) collaborative perception. Despite the success of Parameter-Efficient Fine-Tuning (PEFT) in natural language processing and conventional vision tasks, directly applying PEFT to multi-agent settings leads to significant performance degradation and training instability. In this work, we conduct a detailed analysis and identify two key factors: (i) inter-frame redundancy in heterogeneous sensory streams, and (ii) erosion of fine-grained semantics in deep-layer representations under PEFT adaptation. To address these issues, we propose FlowAdapt, a parameter-efficient framework grounded in optimal transport theory, which minimizes information transport costs across both data distributions and network hierarchies. Specifically, we introduce a Wasserstein Greedy Sampling strategy to selectively filter redundant samples via a bounded covering radius. Furthermore, Progressive Knowledge Transfer module is designed to progressively inject compressed early-stage representations into later stages through learnable pathways, alleviating semantic degradation in late-stage adaptation. Extensive experiments on three benchmarks demonstrate that FlowAdapt achieves state-of-the-art performance with only 1% of trainable parameters, effectively bridging domain gaps with superior sample efficiency and generalization.

