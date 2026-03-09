---
layout: default
title: The World Won't Stay Still: Programmable Evolution for Agent Benchmarks
---

# The World Won't Stay Still: Programmable Evolution for Agent Benchmarks
**arXiv**：[2603.05910v1](https://arxiv.org/abs/2603.05910) · [PDF](https://arxiv.org/pdf/2603.05910.pdf)  
**作者**：Guangrui Li, Yaochen Xie, Yi Liu, Ziwei Dong, Xingyuan Pan, Tianqi Zheng, Jason Choi, Michael J. Morais, Binit Jha, Shaunak Mishra, Bingrou Zhou, Chen Luo, Monica Xiao Cheng, Dawn Song  

**一句话要点**：提出ProEvolve框架，通过图编程实现可扩展可控的代理环境演化，以评估代理对动态环境的适应性。

**关键词**：代理基准测试, 环境演化, 图编程, 类型化关系图, 任务沙箱, 鲁棒性评估

## 3 点简述
- 核心问题：现有基准假设静态环境，忽略真实世界演化及代理对环境变化的鲁棒性评估。
- 方法要点：基于类型化关系图统一表示环境，通过图变换编程演化动态，自动生成环境和任务沙箱。
- 实验或效果：将单一环境演化为200个环境和3000个任务沙箱，并据此对代表性代理进行基准测试。

## 摘要（原文）

> LLM-powered agents fulfill user requests by interacting with environments, querying data, and invoking tools in a multi-turn process. Yet, most existing benchmarks assume static environments with fixed schemas and toolsets, neglecting the evolutionary nature of the real world and agents' robustness to environmental changes. In this paper, we study a crucial problem: how to evolve the agent environment in a scalable and controllable way, thereby better evaluating agents' adaptability to real-world dynamics. We propose ProEvolve, a graph-based framework that makes environment evolution programmable. At its core, a typed relational graph provides a unified, explicit representation of the environment: data, tools, and schema. Under this formalism, adding, removing, or modifying capabilities are expressed as graph transformations that coherently propagate updates across tools, schemas, and data access. Building on this, ProEvolve can (1) program the evolutionary dynamics as graph transformations to generate environments automatically, and (2) instantiate task sandboxes via subgraph sampling and programming. We validate ProEvolve by evolving a single environment into 200 environments and 3,000 task sandboxes, and benchmark representative agents accordingly.

