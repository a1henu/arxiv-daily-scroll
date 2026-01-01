---
layout: default
title: Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search
---

# Vulcan: Instance-Optimal Systems Heuristics Through LLM-Driven Search
**arXiv**：[2512.25065v1](https://arxiv.org/abs/2512.25065) · [PDF](https://arxiv.org/pdf/2512.25065.pdf)  
**作者**：Rohit Dwivedula, Divyanshu Saxena, Sujay Yadalam, Daehyeok Kim, Aditya Akella  

**一句话要点**：提出Vulcan系统，利用LLM生成代码合成实例最优启发式以优化系统资源管理。

**关键词**：实例最优启发式, LLM驱动搜索, 系统资源管理, 代码生成, 进化搜索, 缓存优化

## 3 点简述
- 核心问题：系统资源管理依赖人工设计启发式，成本高且难以适应硬件、工作负载和环境变化。
- 方法要点：通过LLM友好的任务无关接口分离策略与机制，基于进化搜索合成针对特定实例的启发式。
- 实验或效果：在缓存驱逐和内存分层任务中，合成启发式性能分别提升高达69%和7.9%，超越现有最优算法。

## 摘要（原文）

> Resource-management tasks in modern operating and distributed systems continue to rely primarily on hand-designed heuristics for tasks such as scheduling, caching, or active queue management. Designing performant heuristics is an expensive, time-consuming process that we are forced to continuously go through due to the constant flux of hardware, workloads and environments.
>   We propose a new alternative: synthesizing instance-optimal heuristics -- specialized for the exact workloads and hardware where they will be deployed -- using code-generating large language models (LLMs). To make this synthesis tractable, Vulcan separates policy and mechanism through LLM-friendly, task-agnostic interfaces. With these interfaces, users specify the inputs and objectives of their desired policy, while Vulcan searches for performant policies via evolutionary search over LLM-generated code. This interface is expressive enough to capture a wide range of system policies, yet sufficiently constrained to allow even small, inexpensive LLMs to generate correct and executable code.
>   We use Vulcan to synthesize performant heuristics for cache eviction and memory tiering, and find that these heuristics outperform all human-designed state-of-the-art algorithms by upto 69% and 7.9% in performance for each of these tasks respectively.

