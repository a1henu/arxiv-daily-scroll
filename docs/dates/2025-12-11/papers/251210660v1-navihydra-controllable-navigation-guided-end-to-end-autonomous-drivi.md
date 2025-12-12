---
layout: default
title: NaviHydra: Controllable Navigation-guided End-to-end Autonomous Driving with Hydra-distillation
---

# NaviHydra: Controllable Navigation-guided End-to-end Autonomous Driving with Hydra-distillation
**arXiv**：[2512.10660v1](https://arxiv.org/abs/2512.10660) · [PDF](https://arxiv.org/pdf/2512.10660.pdf)  
**作者**：Hanfeng Wu, Marlon Steiner, Michael Schmidt, Alvaro Marcos-Ramiro, Christoph Stiller  

**一句话要点**：提出NaviHydra以解决自动驾驶中导航指令可控性问题，通过蒸馏方法实现端到端控制。

**关键词**：自动驾驶, 端到端学习, 蒸馏训练, 导航控制, 鸟瞰图, 轨迹生成

## 3 点简述
- 核心问题：传统规则系统在动态环境中适应性差，端到端方法难以遵循显式导航指令。
- 方法要点：基于鸟瞰图的轨迹特征提取，引入导航合规性指标提升可控性和安全性。
- 实验或效果：在NAVSIM基准测试中显著优于基线模型，达到先进水平。

## 摘要（原文）

> The complexity of autonomous driving scenarios requires robust models that can interpret high-level navigation commands and generate safe trajectories. While traditional rule-based systems can react to these commands, they often struggle in dynamic environments, and end-to-end methods face challenges in complying with explicit navigation commands. To address this, we present NaviHydra, a controllable navigation-guided end-to-end model distilled from an existing rule-based simulator. Our framework accepts high-level navigation commands as control signals, generating trajectories that align with specified intentions. We utilize a Bird's Eye View (BEV) based trajectory gathering method to enhance the trajectory feature extraction. Additionally, we introduce a novel navigation compliance metric to evaluate adherence to intended route, improving controllability and navigation safety. To comprehensively assess our model's controllability, we design a test that evaluates its response to various navigation commands. Our method significantly outperforms baseline models, achieving state-of-the-art results in the NAVSIM benchmark, demonstrating its effectiveness in advancing autonomous driving.

