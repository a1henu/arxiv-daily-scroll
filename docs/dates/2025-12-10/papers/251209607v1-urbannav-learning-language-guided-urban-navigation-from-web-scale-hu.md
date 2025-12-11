---
layout: default
title: UrbanNav: Learning Language-Guided Urban Navigation from Web-Scale Human Trajectories
---

# UrbanNav: Learning Language-Guided Urban Navigation from Web-Scale Human Trajectories
**arXiv**：[2512.09607v1](https://arxiv.org/abs/2512.09607) · [PDF](https://arxiv.org/pdf/2512.09607.pdf)  
**作者**：Yanghong Mei, Yirong Yang, Longteng Guo, Qunbo Wang, Ming-Ming Yu, Xingjian He, Wenjun Wu, Jing Liu  

**一句话要点**：提出UrbanNav框架，利用网络规模人类轨迹训练具身代理遵循自由语言指令进行城市导航

**关键词**：城市导航, 语言引导导航, 具身代理, 大规模轨迹数据, 空间推理, 泛化能力

## 3 点简述
- 核心问题：城市环境中自然语言导航面临噪声指令、模糊空间参考和动态场景挑战，现有方法依赖精确目标格式，限制实际应用
- 方法要点：基于网络规模城市行走视频，开发可扩展标注流程，对齐人类轨迹与基于真实地标的语言指令，构建大规模数据集
- 实验或效果：模型在复杂城市场景中展现优越空间推理和泛化能力，显著超越现有方法，验证大规模网络视频数据潜力

## 摘要（原文）

> Navigating complex urban environments using natural language instructions poses significant challenges for embodied agents, including noisy language instructions, ambiguous spatial references, diverse landmarks, and dynamic street scenes. Current visual navigation methods are typically limited to simulated or off-street environments, and often rely on precise goal formats, such as specific coordinates or images. This limits their effectiveness for autonomous agents like last-mile delivery robots navigating unfamiliar cities. To address these limitations, we introduce UrbanNav, a scalable framework that trains embodied agents to follow free-form language instructions in diverse urban settings. Leveraging web-scale city walking videos, we develop an scalable annotation pipeline that aligns human navigation trajectories with language instructions grounded in real-world landmarks. UrbanNav encompasses over 1,500 hours of navigation data and 3 million instruction-trajectory-landmark triplets, capturing a wide range of urban scenarios. Our model learns robust navigation policies to tackle complex urban scenarios, demonstrating superior spatial reasoning, robustness to noisy instructions, and generalization to unseen urban settings. Experimental results show that UrbanNav significantly outperforms existing methods, highlighting the potential of large-scale web video data to enable language-guided, real-world urban navigation for embodied agents.

