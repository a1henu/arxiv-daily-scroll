---
layout: default
title: FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation
---

# FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation
**arXiv**：[2510.20774v1](https://arxiv.org/abs/2510.20774) · [PDF](https://arxiv.org/pdf/2510.20774.pdf)  
**作者**：Wenhao Wang, Kehe Ye, Xinyu Zhou, Tianxing Chen, Cao Min, Qiaoming Zhu, Xiaokang Yang, Yongjian Shen, Yang Yang, Maoqing Yao, Yao Mu  

**一句话要点**：提出FieldGen框架以解决机器人操作数据收集的规模、多样性和质量平衡问题

**关键词**：机器人操作, 数据生成, 吸引场, 轨迹多样性, 奖励标注, sim-to-real

## 3 点简述
- 核心问题：现有机器人操作数据收集方法难以平衡规模、多样性和质量，仿真有sim-to-real差距，遥操作成本高且多样性有限
- 方法要点：将操作分解为预操作和精细操作阶段，利用吸引场自动生成多样轨迹，结合精确监督和奖励标注
- 实验或效果：实验显示，基于FieldGen训练的策略比遥操作基线成功率更高、稳定性更好，并显著减少人力成本

## 摘要（原文）

> Large-scale and diverse datasets are vital for training robust robotic
> manipulation policies, yet existing data collection methods struggle to balance
> scale, diversity, and quality. Simulation offers scalability but suffers from
> sim-to-real gaps, while teleoperation yields high-quality demonstrations with
> limited diversity and high labor cost. We introduce FieldGen, a field-guided
> data generation framework that enables scalable, diverse, and high-quality
> real-world data collection with minimal human supervision. FieldGen decomposes
> manipulation into two stages: a pre-manipulation phase, allowing trajectory
> diversity, and a fine manipulation phase requiring expert precision. Human
> demonstrations capture key contact and pose information, after which an
> attraction field automatically generates diverse trajectories converging to
> successful configurations. This decoupled design combines scalable trajectory
> diversity with precise supervision. Moreover, FieldGen-Reward augments
> generated data with reward annotations to further enhance policy learning.
> Experiments demonstrate that policies trained with FieldGen achieve higher
> success rates and improved stability compared to teleoperation-based baselines,
> while significantly reducing human effort in long-term real-world data
> collection. Webpage is available at https://fieldgen.github.io/.

