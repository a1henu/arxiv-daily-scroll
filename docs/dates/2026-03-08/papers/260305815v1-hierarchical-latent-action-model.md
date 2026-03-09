---
layout: default
title: Hierarchical Latent Action Model
---

# Hierarchical Latent Action Model
**arXiv**：[2603.05815v1](https://arxiv.org/abs/2603.05815) · [PDF](https://arxiv.org/pdf/2603.05815.pdf)  
**作者**：Hanjung Kim, Lerrel Pinto, Seon Joo Kim  

**一句话要点**：提出HiLAM分层潜在动作模型，以从无动作视频中发现长时技能

**关键词**：分层潜在动作模型, 长时技能发现, 无动作视频学习, 潜在动作序列, 动态模式提取, 机器人控制

## 3 点简述
- 现有潜在动作模型关注短时帧过渡，忽略长时结构，难以捕获高级技能
- HiLAM利用预训练模型提取低层动作序列，聚合为高层潜在技能，建模长时依赖
- 实验显示HiLAM优于基线，在动态技能发现上表现稳健

## 摘要（原文）

> Latent Action Models (LAMs) enable learning from actionless data for applications ranging from robotic control to interactive world models. However, existing LAMs typically focus on short-horizon frame transitions and capture low-level motion while overlooking longer-term temporal structure. In contrast, actionless videos often contain temporally extended and high-level skills. We present HiLAM, a hierarchical latent action model that discovers latent skills by modeling long-term temporal information. To capture these dependencies across long horizons, we utilize a pretrained LAM as a low-level extractor. This architecture aggregates latent action sequences, which contain the underlying dynamic patterns of the video, into high-level latent skills. Our experiments demonstrate that HiLAM improves over the baseline and exhibits robust dynamic skill discovery.

