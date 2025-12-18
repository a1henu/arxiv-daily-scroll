---
layout: default
title: Autonomous Pressure Control in MuVacAS via Deep Reinforcement Learning and Deep Learning Surrogate Models
---

# Autonomous Pressure Control in MuVacAS via Deep Reinforcement Learning and Deep Learning Surrogate Models
**arXiv**：[2512.15521v1](https://arxiv.org/abs/2512.15521) · [PDF](https://arxiv.org/pdf/2512.15521.pdf)  
**作者**：Guillermo Rodriguez-Llorente, Galo Gallardo, Rodrigo Morant Navascués, Nikita Khvatkin Petrovsky, Anderson Sabogal, Roberto Gómez-Espinosa Martín  

**一句话要点**：提出基于深度强化学习和深度学习代理模型的自主压力控制方法，用于MuVacAS原型中的氩气压力调节。

**关键词**：自主压力控制, 深度强化学习, 深度学习代理模型, 数字孪生, 粒子加速器, 核聚变材料测试

## 3 点简述
- 核心问题：在IFMIF-DONES设施中，精确控制MuVacAS原型超高压真空室内的氩气压力至关重要。
- 方法要点：使用深度学习代理模型模拟氩气注入系统动态，作为训练深度强化学习代理的快速仿真环境。
- 实验或效果：代理成功学习控制策略，在动态干扰下维持压力在严格操作限内。

## 摘要（原文）

> The development of nuclear fusion requires materials that can withstand extreme conditions. The IFMIF-DONES facility, a high-power particle accelerator, is being designed to qualify these materials. A critical testbed for its development is the MuVacAS prototype, which replicates the final segment of the accelerator beamline. Precise regulation of argon gas pressure within its ultra-high vacuum chamber is vital for this task. This work presents a fully data-driven approach for autonomous pressure control. A Deep Learning Surrogate Model, trained on real operational data, emulates the dynamics of the argon injection system. This high-fidelity digital twin then serves as a fast-simulation environment to train a Deep Reinforcement Learning agent. The results demonstrate that the agent successfully learns a control policy that maintains gas pressure within strict operational limits despite dynamic disturbances. This approach marks a significant step toward the intelligent, autonomous control systems required for the demanding next-generation particle accelerator facilities.

