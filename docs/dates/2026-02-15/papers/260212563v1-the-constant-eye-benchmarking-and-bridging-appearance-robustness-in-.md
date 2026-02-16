---
layout: default
title: The Constant Eye: Benchmarking and Bridging Appearance Robustness in Autonomous Driving
---

# The Constant Eye: Benchmarking and Bridging Appearance Robustness in Autonomous Driving
**arXiv**：[2602.12563v1](https://arxiv.org/abs/2602.12563) · [PDF](https://arxiv.org/pdf/2602.12563.pdf)  
**作者**：Jiabao Wang, Hongyu Zhou, Yuanbo Yang, Jiahao Shao, Yiyi Liao  

**一句话要点**：提出navdream基准与基于DINOv3的通用感知接口，以解决自动驾驶中外观变化导致的规划算法脆弱性问题。

**关键词**：自动驾驶鲁棒性, 外观分布偏移, 基准测试, 视觉基础模型, 零样本泛化, 规划算法

## 3 点简述
- 核心问题：自动驾驶算法在外观分布偏移下性能显著下降，但现有研究未区分外观与结构变化的影响。
- 方法要点：利用生成式像素对齐风格转移创建navdream基准，隔离外观影响；采用冻结视觉基础模型提取外观不变特征作为规划器接口。
- 实验或效果：评估显示现有规划算法在外观OOD条件下退化；提出的接口实现零样本泛化，跨多种规划范式保持性能稳定。

## 摘要（原文）

> Despite rapid progress, autonomous driving algorithms remain notoriously fragile under Out-of-Distribution (OOD) conditions. We identify a critical decoupling failure in current research: the lack of distinction between appearance-based shifts, such as weather and lighting, and structural scene changes. This leaves a fundamental question unanswered: Is the planner failing because of complex road geometry, or simply because it is raining? To resolve this, we establish navdream, a high-fidelity robustness benchmark leveraging generative pixel-aligned style transfer. By creating a visual stress test with negligible geometric deviation, we isolate the impact of appearance on driving performance. Our evaluation reveals that existing planning algorithms often show significant degradation under OOD appearance conditions, even when the underlying scene structure remains consistent. To bridge this gap, we propose a universal perception interface leveraging a frozen visual foundation model (DINOv3). By extracting appearance-invariant features as a stable interface for the planner, we achieve exceptional zero-shot generalization across diverse planning paradigms, including regression-based, diffusion-based, and scoring-based models. Our plug-and-play solution maintains consistent performance across extreme appearance shifts without requiring further fine-tuning. The benchmark and code will be made available.

