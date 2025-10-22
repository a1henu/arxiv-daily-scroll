---
layout: default
title: OmniNWM: Omniscient Driving Navigation World Models
---

# OmniNWM: Omniscient Driving Navigation World Models
**arXiv**：[2510.18313v1](https://arxiv.org/abs/2510.18313) · [PDF](https://arxiv.org/pdf/2510.18313.pdf)  
**作者**：Bohan Li, Zhuang Ma, Dalong Du, Baorui Peng, Zhujin Liang, Zhenqiang Liu, Chao Ma, Yueming Jin, Hao Zhao, Wenjun Zeng, Xin Jin  

**一句话要点**：提出OmniNWM全景导航世界模型，统一解决自动驾驶状态、动作和奖励维度问题。

**关键词**：自动驾驶世界模型, 全景视频生成, 3D占用, 动作控制, 奖励函数, 长序列生成

## 3 点简述
- 现有模型状态模态受限、序列短、动作控制不精确且缺乏奖励意识。
- 联合生成全景RGB、语义、深度和3D占用视频，使用归一化Plucker射线图编码动作。
- 实验显示在视频生成、控制精度和长序列稳定性上达到先进水平，并提供闭环评估框架。

## 摘要（原文）

> Autonomous driving world models are expected to work effectively across three
> core dimensions: state, action, and reward. Existing models, however, are
> typically restricted to limited state modalities, short video sequences,
> imprecise action control, and a lack of reward awareness. In this paper, we
> introduce OmniNWM, an omniscient panoramic navigation world model that
> addresses all three dimensions within a unified framework. For state, OmniNWM
> jointly generates panoramic videos of RGB, semantics, metric depth, and 3D
> occupancy. A flexible forcing strategy enables high-quality long-horizon
> auto-regressive generation. For action, we introduce a normalized panoramic
> Plucker ray-map representation that encodes input trajectories into pixel-level
> signals, enabling highly precise and generalizable control over panoramic video
> generation. Regarding reward, we move beyond learning reward functions with
> external image-based models: instead, we leverage the generated 3D occupancy to
> directly define rule-based dense rewards for driving compliance and safety.
> Extensive experiments demonstrate that OmniNWM achieves state-of-the-art
> performance in video generation, control accuracy, and long-horizon stability,
> while providing a reliable closed-loop evaluation framework through
> occupancy-grounded rewards. Project page is available at
> https://github.com/Arlo0o/OmniNWM.

