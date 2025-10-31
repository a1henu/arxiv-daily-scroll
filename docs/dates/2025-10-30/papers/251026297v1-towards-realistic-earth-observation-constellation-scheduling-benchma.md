---
layout: default
title: Towards Realistic Earth-Observation Constellation Scheduling: Benchmark and Methodology
---

# Towards Realistic Earth-Observation Constellation Scheduling: Benchmark and Methodology
**arXiv**：[2510.26297v1](https://arxiv.org/abs/2510.26297) · [PDF](https://arxiv.org/pdf/2510.26297.pdf)  
**作者**：Luting Wang, Yinghao Xiang, Hongliang Huang, Dongjun Li, Chen Gao, Si Liu  

**一句话要点**：提出AEOS-Bench基准和AEOS-Former模型以解决大规模敏捷地球观测卫星星座调度问题

**关键词**：地球观测卫星调度, 基准套件, Transformer模型, 约束感知机制, 大规模场景模拟

## 3 点简述
- 核心问题：大规模敏捷地球观测卫星星座调度在动态环境和严格约束下性能受限
- 方法要点：引入统一框架，包括高保真基准套件和基于Transformer的约束感知调度模型
- 实验或效果：AEOS-Former在任务完成率和能效上优于基线，并通过消融研究验证组件贡献

## 摘要（原文）

> Agile Earth Observation Satellites (AEOSs) constellations offer unprecedented
> flexibility for monitoring the Earth's surface, but their scheduling remains
> challenging under large-scale scenarios, dynamic environments, and stringent
> constraints. Existing methods often simplify these complexities, limiting their
> real-world performance. We address this gap with a unified framework
> integrating a standardized benchmark suite and a novel scheduling model. Our
> benchmark suite, AEOS-Bench, contains $3,907$ finely tuned satellite assets and
> $16,410$ scenarios. Each scenario features $1$ to $50$ satellites and $50$ to
> $300$ imaging tasks. These scenarios are generated via a high-fidelity
> simulation platform, ensuring realistic satellite behavior such as orbital
> dynamics and resource constraints. Ground truth scheduling annotations are
> provided for each scenario. To our knowledge, AEOS-Bench is the first
> large-scale benchmark suite tailored for realistic constellation scheduling.
> Building upon this benchmark, we introduce AEOS-Former, a Transformer-based
> scheduling model that incorporates a constraint-aware attention mechanism. A
> dedicated internal constraint module explicitly models the physical and
> operational limits of each satellite. Through simulation-based iterative
> learning, AEOS-Former adapts to diverse scenarios, offering a robust solution
> for AEOS constellation scheduling. Experimental results demonstrate that
> AEOS-Former outperforms baseline models in task completion and energy
> efficiency, with ablation studies highlighting the contribution of each
> component. Code and data are provided in
> https://github.com/buaa-colalab/AEOSBench.

