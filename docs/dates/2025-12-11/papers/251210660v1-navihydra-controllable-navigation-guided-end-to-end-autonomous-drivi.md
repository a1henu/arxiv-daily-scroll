---
layout: default
title: NaviHydra: Controllable Navigation-guided End-to-end Autonomous Driving with Hydra-distillation
---

# NaviHydra: Controllable Navigation-guided End-to-end Autonomous Driving with Hydra-distillation
**arXiv**：[2512.10660v1](https://arxiv.org/abs/2512.10660) · [PDF](https://arxiv.org/pdf/2512.10660.pdf)  
**作者**：Hanfeng Wu, Marlon Steiner, Michael Schmidt, Alvaro Marcos-Ramiro, Christoph Stiller  

**一句话要点**：提出NaviHydra可控导航引导端到端自动驾驶模型，通过Hydra蒸馏解决导航命令遵从问题

**关键词**：自动驾驶, 端到端学习, 导航命令遵从, 蒸馏训练, BEV轨迹提取, 可控性评估

## 3 点简述
- 核心问题：端到端自动驾驶模型难以遵从显式导航命令，传统规则系统在动态环境中表现不佳
- 方法要点：从规则模拟器蒸馏，结合BEV轨迹特征提取和导航遵从度量，增强可控性
- 实验或效果：在NAVSIM基准测试中显著优于基线，实现先进性能，提升导航安全性

## 摘要（原文）

> The complexity of autonomous driving scenarios requires robust models that can interpret high-level navigation commands and generate safe trajectories. While traditional rule-based systems can react to these commands, they often struggle in dynamic environments, and end-to-end methods face challenges in complying with explicit navigation commands. To address this, we present NaviHydra, a controllable navigation-guided end-to-end model distilled from an existing rule-based simulator. Our framework accepts high-level navigation commands as control signals, generating trajectories that align with specified intentions. We utilize a Bird's Eye View (BEV) based trajectory gathering method to enhance the trajectory feature extraction. Additionally, we introduce a novel navigation compliance metric to evaluate adherence to intended route, improving controllability and navigation safety. To comprehensively assess our model's controllability, we design a test that evaluates its response to various navigation commands. Our method significantly outperforms baseline models, achieving state-of-the-art results in the NAVSIM benchmark, demonstrating its effectiveness in advancing autonomous driving.

