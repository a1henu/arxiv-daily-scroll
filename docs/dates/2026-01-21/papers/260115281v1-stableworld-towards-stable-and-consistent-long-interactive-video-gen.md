---
layout: default
title: StableWorld: Towards Stable and Consistent Long Interactive Video Generation
---

# StableWorld: Towards Stable and Consistent Long Interactive Video Generation
**arXiv**：[2601.15281v1](https://arxiv.org/abs/2601.15281) · [PDF](https://arxiv.org/pdf/2601.15281.pdf)  
**作者**：Ying Yang, Zhengyao Lv, Tianlin Pan, Haofan Wang, Binxin Yang, Hubery Yin, Chen Li, Ziwei Liu, Chenyang Si  

**一句话要点**：提出StableWorld动态帧剔除机制以解决交互式长视频生成中的稳定性与时间一致性问题

**关键词**：交互式视频生成, 时间一致性, 稳定性优化, 动态帧剔除, 长视频合成, 模型无关方法

## 3 点简述
- 核心问题：交互式视频生成存在稳定性差和时间退化，导致空间漂移和场景崩溃
- 方法要点：通过动态剔除退化帧并保留几何一致帧，从源头防止误差累积
- 实验或效果：在多个模型上验证，提升稳定性、时间一致性和泛化能力

## 摘要（原文）

> In this paper, we explore the overlooked challenge of stability and temporal consistency in interactive video generation, which synthesizes dynamic and controllable video worlds through interactive behaviors such as camera movements and text prompts. Despite remarkable progress in world modeling, current methods still suffer from severe instability and temporal degradation, often leading to spatial drift and scene collapse during long-horizon interactions. To better understand this issue, we initially investigate the underlying causes of instability and identify that the major source of error accumulation originates from the same scene, where generated frames gradually deviate from the initial clean state and propagate errors to subsequent frames. Building upon this observation, we propose a simple yet effective method, \textbf{StableWorld}, a Dynamic Frame Eviction Mechanism. By continuously filtering out degraded frames while retaining geometrically consistent ones, StableWorld effectively prevents cumulative drift at its source, leading to more stable and temporal consistency of interactive generation. Promising results on multiple interactive video models, \eg, Matrix-Game, Open-Oasis, and Hunyuan-GameCraft, demonstrate that StableWorld is model-agnostic and can be applied to different interactive video generation frameworks to substantially improve stability, temporal consistency, and generalization across diverse interactive scenarios.

