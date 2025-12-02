---
layout: default
title: SocialDriveGen: Generating Diverse Traffic Scenarios with Controllable Social Interactions
---

# SocialDriveGen: Generating Diverse Traffic Scenarios with Controllable Social Interactions
**arXiv**：[2512.01363v1](https://arxiv.org/abs/2512.01363) · [PDF](https://arxiv.org/pdf/2512.01363.pdf)  
**作者**：Jiaguo Tian, Zhengbang Zhu, Shenyu Zhang, Li Xu, Bo Zheng, Xu Liu, Weiji Peng, Shizeng Yao, Weinan Zhang  

**一句话要点**：提出SocialDriveGen，通过分层框架生成可控社交交互的多样化交通场景

**关键词**：交通场景生成, 社交交互建模, 生成轨迹合成, 自动驾驶仿真, 可控多样性

## 3 点简述
- 核心问题：现有仿真框架缺乏真实世界驾驶的保真度和多样性，忽视社交偏好对驾驶行为的影响。
- 方法要点：集成语义推理和社交偏好建模，以利己主义和利他主义为维度，实现可控的驾驶员个性和交互风格。
- 实验或效果：在Argoverse 2数据集上生成从合作到对抗的多样化高保真场景，显著增强策略鲁棒性和泛化能力。

## 摘要（原文）

> The generation of realistic and diverse traffic scenarios in simulation is essential for developing and evaluating autonomous driving systems. However, most simulation frameworks rely on rule-based or simplified models for scene generation, which lack the fidelity and diversity needed to represent real-world driving. While recent advances in generative modeling produce more realistic and context-aware traffic interactions, they often overlook how social preferences influence driving behavior. SocialDriveGen addresses this gap through a hierarchical framework that integrates semantic reasoning and social preference modeling with generative trajectory synthesis. By modeling egoism and altruism as complementary social dimensions, our framework enables controllable diversity in driver personalities and interaction styles. Experiments on the Argoverse 2 dataset show that SocialDriveGen generates diverse, high-fidelity traffic scenarios spanning cooperative to adversarial behaviors, significantly enhancing policy robustness and generalization to rare or high-risk situations.

