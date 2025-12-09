---
layout: default
title: DCO: Dynamic Cache Orchestration for LLM Accelerators through Predictive Management
---

# DCO: Dynamic Cache Orchestration for LLM Accelerators through Predictive Management
**arXiv**：[2512.07312v1](https://arxiv.org/abs/2512.07312) · [PDF](https://arxiv.org/pdf/2512.07312.pdf)  
**作者**：Zhongchun Zhou, Chengtao Lai, Yuhang Gu, Wei Zhang  

**一句话要点**：提出动态缓存编排方法，通过预测管理优化LLM加速器性能

**关键词**：AI加速器, 缓存管理, 数据流预测, 性能优化, RTL实现, 大语言模型

## 3 点简述
- 针对AI加速器中缓存层次复杂化问题，研究共享系统级缓存与软件栈数据流引导的管理策略
- 结合死块预测、旁路决策和缓存颠簸缓解机制，在周期精确模拟中实现最高1.80倍加速
- 通过RTL实现验证设计可行性，面积0.064mm²，时钟频率2GHz，支持大规模工作负载扩展

## 摘要（原文）

> The rapid adoption of large language models (LLMs) is pushing AI accelerators toward increasingly powerful and specialized designs. Instead of further complicating software development with deeply hierarchical scratchpad memories (SPMs) and their asynchronous management, we investigate the opposite point of the design spectrum: a multi-core AI accelerator equipped with a shared system-level cache and application-aware management policies, which keeps the programming effort modest. Our approach exploits dataflow information available in the software stack to guide cache replacement (including dead-block prediction), in concert with bypass decisions and mechanisms that alleviate cache thrashing.
>   We assess the proposal using a cycle-accurate simulator and observe substantial performance gains (up to 1.80x speedup) compared with conventional cache architectures. In addition, we build and validate an analytical model that takes into account the actual overlapping behaviors to extend the measurement results of our policies to real-world larger-scale workloads. Experiment results show that when functioning together, our bypassing and thrashing mitigation strategies can handle scenarios both with and without inter-core data sharing and achieve remarkable speedups.
>   Finally, we implement the design in RTL and the area of our design is $\mathbf{0.064mm^2}$ with 15nm process, which can run at 2 GHz clock frequency. Our findings explore the potential of the shared cache design to assist the development of future AI accelerator systems.

