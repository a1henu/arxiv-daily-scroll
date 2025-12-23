---
layout: default
title: REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation
---

# REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation
**arXiv**：[2512.19562v1](https://arxiv.org/abs/2512.19562) · [PDF](https://arxiv.org/pdf/2512.19562.pdf)  
**作者**：Martin Sedlacek, Pavlo Yefanov, Georgy Ponimatkin, Jai Bardhan, Simon Pilc, Mederic Fourmy, Evangelos Kazakos, Cees G. M. Snoek, Josef Sivic, Vladimir Petrik  

**一句话要点**：提出REALM仿真环境与基准以评估视觉语言动作模型的泛化能力

**关键词**：视觉语言动作模型, 机器人操作, 仿真基准, 泛化评估, 高保真仿真

## 3 点简述
- 核心问题：VLA模型在真实世界泛化能力评估困难且昂贵
- 方法要点：通过高保真视觉和对齐控制建立仿真与真实性能强相关性
- 实验或效果：评估多个VLA模型，显示泛化与鲁棒性仍是开放挑战

## 摘要（原文）

> Vision-Language-Action (VLA) models empower robots to understand and execute tasks described by natural language instructions. However, a key challenge lies in their ability to generalize beyond the specific environments and conditions they were trained on, which is presently difficult and expensive to evaluate in the real-world. To address this gap, we present REALM, a new simulation environment and benchmark designed to evaluate the generalization capabilities of VLA models, with a specific emphasis on establishing a strong correlation between simulated and real-world performance through high-fidelity visuals and aligned robot control. Our environment offers a suite of 15 perturbation factors, 7 manipulation skills, and more than 3,500 objects. Finally, we establish two task sets that form our benchmark and evaluate the π_{0}, π_{0}-FAST, and GR00T N1.5 VLA models, showing that generalization and robustness remain an open challenge. More broadly, we also show that simulation gives us a valuable proxy for the real-world and allows us to systematically probe for and quantify the weaknesses and failure modes of VLAs. Project page: https://martin-sedlacek.com/realm

