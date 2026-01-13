---
layout: default
title: NanoCockpit: Performance-optimized Application Framework for AI-based Autonomous Nanorobotics
---

# NanoCockpit: Performance-optimized Application Framework for AI-based Autonomous Nanorobotics
**arXiv**：[2601.07476v1](https://arxiv.org/abs/2601.07476) · [PDF](https://arxiv.org/pdf/2601.07476.pdf)  
**作者**：Elia Cereda, Alessandro Giusti, Daniele Palossi  

**一句话要点**：提出NanoCockpit框架以优化基于AI的自主纳米机器人应用性能

**关键词**：纳米无人机, TinyML, 嵌入式系统, 性能优化, 协程多任务, 自主控制

## 3 点简述
- 核心问题：纳米无人机资源受限，现有软件层无法高效利用多核MCU，导致控制性能不佳。
- 方法要点：通过协程多任务实现时间最优流水线，优化图像采集、计算、数据交换和Wi-Fi流传输。
- 实验或效果：在三个真实TinyML应用中实现零开销延迟，位置误差降低30%，任务成功率从40%提升至100%。

## 摘要（原文）

> Autonomous nano-drones, powered by vision-based tiny machine learning (TinyML) models, are a novel technology gaining momentum thanks to their broad applicability and pushing scientific advancement on resource-limited embedded systems. Their small form factor, i.e., a few 10s grams, severely limits their onboard computational resources to sub-\SI{100}{\milli\watt} microcontroller units (MCUs). The Bitcraze Crazyflie nano-drone is the \textit{de facto} standard, offering a rich set of programmable MCUs for low-level control, multi-core processing, and radio transmission. However, roboticists very often underutilize these onboard precious resources due to the absence of a simple yet efficient software layer capable of time-optimal pipelining of multi-buffer image acquisition, multi-core computation, intra-MCUs data exchange, and Wi-Fi streaming, leading to sub-optimal control performances. Our \textit{NanoCockpit} framework aims to fill this gap, increasing the throughput and minimizing the system's latency, while simplifying the developer experience through coroutine-based multi-tasking. In-field experiments on three real-world TinyML nanorobotics applications show our framework achieves ideal end-to-end latency, i.e. zero overhead due to serialized tasks, delivering quantifiable improvements in closed-loop control performance ($-$30\% mean position error, mission success rate increased from 40\% to 100\%).

