---
layout: default
title: Sim-and-Human Co-training for Data-Efficient and Generalizable Robotic Manipulation
---

# Sim-and-Human Co-training for Data-Efficient and Generalizable Robotic Manipulation
**arXiv**：[2601.19406v1](https://arxiv.org/abs/2601.19406) · [PDF](https://arxiv.org/pdf/2601.19406.pdf)  
**作者**：Kaipeng Fang, Weiqing Liang, Yuyang Li, Ji Zhang, Pengpeng Zeng, Lianli Gao, Jingkuan Song, Heng Tao Shen  

**一句话要点**：提出SimHum协同训练框架，利用仿真与人类数据互补，实现数据高效且泛化的机器人操作。

**关键词**：机器人操作, 仿真到真实, 数据高效学习, 协同训练, 泛化能力

## 3 点简述
- 核心问题：仿真数据存在视觉差距，人类数据存在动作差距，限制机器人策略在真实场景的泛化。
- 方法要点：从仿真数据提取动作先验，从人类数据提取视觉先验，通过协同训练结合两者。
- 实验或效果：在相同数据预算下性能提升达40%，仅用80个真实数据实现62.5%的OOD成功率。

## 摘要（原文）

> Synthetic simulation data and real-world human data provide scalable alternatives to circumvent the prohibitive costs of robot data collection. However, these sources suffer from the sim-to-real visual gap and the human-to-robot embodiment gap, respectively, which limits the policy's generalization to real-world scenarios. In this work, we identify a natural yet underexplored complementarity between these sources: simulation offers the robot action that human data lacks, while human data provides the real-world observation that simulation struggles to render. Motivated by this insight, we present SimHum, a co-training framework to simultaneously extract kinematic prior from simulated robot actions and visual prior from real-world human observations. Based on the two complementary priors, we achieve data-efficient and generalizable robotic manipulation in real-world tasks. Empirically, SimHum outperforms the baseline by up to $\mathbf{40\%}$ under the same data collection budget, and achieves a $\mathbf{62.5\%}$ OOD success with only 80 real data, outperforming the real only baseline by $7.1\times$. Videos and additional information can be found at \href{https://kaipengfang.github.io/sim-and-human}{project website}.

