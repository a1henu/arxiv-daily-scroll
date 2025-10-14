---
layout: default
title: Robust Ego-Exo Correspondence with Long-Term Memory
---

# Robust Ego-Exo Correspondence with Long-Term Memory
**arXiv**：[2510.11417v1](https://arxiv.org/abs/2510.11417) · [PDF](https://arxiv.org/pdf/2510.11417.pdf)  
**作者**：Yijun Hu, Bing Fan, Xin Gu, Haiqing Ren, Dongfang Liu, Heng Fan, Libo Zhang  

**一句话要点**：提出基于SAM 2的长记忆EEC框架，解决视角变化与长视频挑战

**关键词**：ego-exo对应, 长视频理解, 双记忆架构, 自适应特征路由, SAM 2改进

## 3 点简述
- 核心问题：视角变化、遮挡和小物体导致ego-exo对应困难，现有方法性能不足
- 方法要点：引入双记忆架构和自适应特征路由模块，提升特征融合与长期记忆能力
- 实验效果：在EgoExo4D基准上实现SOTA，显著优于SAM 2和现有方法

## 摘要（原文）

> Establishing object-level correspondence between egocentric and exocentric
> views is essential for intelligent assistants to deliver precise and intuitive
> visual guidance. However, this task faces numerous challenges, including
> extreme viewpoint variations, occlusions, and the presence of small objects.
> Existing approaches usually borrow solutions from video object segmentation
> models, but still suffer from the aforementioned challenges. Recently, the
> Segment Anything Model 2 (SAM 2) has shown strong generalization capabilities
> and excellent performance in video object segmentation. Yet, when simply
> applied to the ego-exo correspondence (EEC) task, SAM 2 encounters severe
> difficulties due to ineffective ego-exo feature fusion and limited long-term
> memory capacity, especially for long videos. Addressing these problems, we
> propose a novel EEC framework based on SAM 2 with long-term memories by
> presenting a dual-memory architecture and an adaptive feature routing module
> inspired by Mixture-of-Experts (MoE). Compared to SAM 2, our approach features
> (i) a Memory-View MoE module which consists of a dual-branch routing mechanism
> to adaptively assign contribution weights to each expert feature along both
> channel and spatial dimensions, and (ii) a dual-memory bank system with a
> simple yet effective compression strategy to retain critical long-term
> information while eliminating redundancy. In the extensive experiments on the
> challenging EgoExo4D benchmark, our method, dubbed LM-EEC, achieves new
> state-of-the-art results and significantly outperforms existing methods and the
> SAM 2 baseline, showcasing its strong generalization across diverse scenarios.
> Our code and model are available at https://github.com/juneyeeHu/LM-EEC.

