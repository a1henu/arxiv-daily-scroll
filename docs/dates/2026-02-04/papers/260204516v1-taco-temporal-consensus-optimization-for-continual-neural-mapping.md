---
layout: default
title: TACO: Temporal Consensus Optimization for Continual Neural Mapping
---

# TACO: Temporal Consensus Optimization for Continual Neural Mapping
**arXiv**：[2602.04516v1](https://arxiv.org/abs/2602.04516) · [PDF](https://arxiv.org/pdf/2602.04516.pdf)  
**作者**：Xunlan Zhou, Hongrui Zhao, Negar Mehr  

**一句话要点**：提出TACO框架以解决动态环境中持续神经映射的内存与适应性问题

**关键词**：持续学习, 神经隐式映射, 时间共识优化, 动态环境适应, 无重放框架

## 3 点简述
- 核心问题：现有神经隐式映射方法无法在内存和计算受限下适应动态场景变化
- 方法要点：将映射重构为时间共识优化，利用历史模型快照作为时间邻居进行加权共识更新
- 实验或效果：在模拟和真实实验中，TACO无需重放数据，在场景变化下优于其他持续学习基线

## 摘要（原文）

> Neural implicit mapping has emerged as a powerful paradigm for robotic navigation and scene understanding. However, real-world robotic deployment requires continual adaptation to changing environments under strict memory and computation constraints, which existing mapping systems fail to support. Most prior methods rely on replaying historical observations to preserve consistency and assume static scenes. As a result, they cannot adapt to continual learning in dynamic robotic settings. To address these challenges, we propose TACO (TemporAl Consensus Optimization), a replay-free framework for continual neural mapping. We reformulate mapping as a temporal consensus optimization problem, where we treat past model snapshots as temporal neighbors. Intuitively, our approach resembles a model consulting its own past knowledge. We update the current map by enforcing weighted consensus with historical representations. Our method allows reliable past geometry to constrain optimization while permitting unreliable or outdated regions to be revised in response to new observations. TACO achieves a balance between memory efficiency and adaptability without storing or replaying previous data. Through extensive simulated and real-world experiments, we show that TACO robustly adapts to scene changes, and consistently outperforms other continual learning baselines.

