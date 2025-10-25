---
layout: default
title: RubbleSim: A Photorealistic Structural Collapse Simulator for Confined Space Mapping
---

# RubbleSim: A Photorealistic Structural Collapse Simulator for Confined Space Mapping
**arXiv**：[2510.20529v1](https://arxiv.org/abs/2510.20529) · [PDF](https://arxiv.org/pdf/2510.20529.pdf)  
**作者**：Constantine Frost, Chad Council, Margaret McGuinness, Nathaniel Hanson  

**一句话要点**：提出RubbleSim以解决结构倒塌内部空间数据获取难题

**关键词**：结构倒塌模拟, 空隙空间映射, 物理模拟, 运动恢复结构, 开源仿真

## 3 点简述
- 核心问题：结构倒塌内部空隙数据因法律和专有原因难以获取
- 方法要点：基于Unity开发开源模拟器，使用物理方法生成随机碎石堆
- 实验或效果：应用运动恢复结构算法，展示感知性能在模拟空隙中的退化

## 摘要（原文）

> Despite well-reported instances of robots being used in disaster response,
> there is scant published data on the internal composition of the void spaces
> within structural collapse incidents. Data collected during these incidents is
> mired in legal constraints, as ownership is often tied to the responding
> agencies, with little hope of public release for research. While engineered
> rubble piles are used for training, these sites are also reluctant to release
> information about their proprietary training grounds. To overcome this access
> challenge, we present RubbleSim -- an open-source, reconfigurable simulator for
> photorealistic void space exploration. The design of the simulation assets is
> directly informed by visits to numerous training rubble sites at differing
> levels of complexity. The simulator is implemented in Unity with
> multi-operating system support. The simulation uses a physics-based approach to
> build stochastic rubble piles, allowing for rapid iteration between simulation
> worlds while retaining absolute knowledge of the ground truth. Using RubbleSim,
> we apply a state-of-the-art structure-from-motion algorithm to illustrate how
> perception performance degrades under challenging visual conditions inside the
> emulated void spaces. Pre-built binaries and source code to implement are
> available online: https://github.com/mit-ll/rubble_pile_simulator.

