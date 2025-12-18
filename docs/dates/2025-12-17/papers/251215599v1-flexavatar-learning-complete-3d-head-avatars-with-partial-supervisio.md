---
layout: default
title: FlexAvatar: Learning Complete 3D Head Avatars with Partial Supervision
---

# FlexAvatar: Learning Complete 3D Head Avatars with Partial Supervision
**arXiv**：[2512.15599v1](https://arxiv.org/abs/2512.15599) · [PDF](https://arxiv.org/pdf/2512.15599.pdf)  
**作者**：Tobias Kirschstein, Simon Giebenhain, Matthias Nießner  

**一句话要点**：提出FlexAvatar方法，通过偏置汇设计解决单目训练中3D头像不完整问题。

**关键词**：3D头像重建, 单目训练, Transformer模型, 多视图监督, 身份插值

## 3 点简述
- 核心问题：单目视频训练导致3D头像重建不完整，源于驱动信号与目标视角的纠缠。
- 方法要点：基于Transformer的3D肖像动画模型，引入可学习数据源令牌（偏置汇），统一训练单目和多视图数据。
- 实验或效果：在单视图、少样本和单目头像创建任务中验证有效性，生成完整3D头像并支持身份插值。

## 摘要（原文）

> We introduce FlexAvatar, a method for creating high-quality and complete 3D head avatars from a single image. A core challenge lies in the limited availability of multi-view data and the tendency of monocular training to yield incomplete 3D head reconstructions. We identify the root cause of this issue as the entanglement between driving signal and target viewpoint when learning from monocular videos. To address this, we propose a transformer-based 3D portrait animation model with learnable data source tokens, so-called bias sinks, which enables unified training across monocular and multi-view datasets. This design leverages the strengths of both data sources during inference: strong generalization from monocular data and full 3D completeness from multi-view supervision. Furthermore, our training procedure yields a smooth latent avatar space that facilitates identity interpolation and flexible fitting to an arbitrary number of input observations. In extensive evaluations on single-view, few-shot, and monocular avatar creation tasks, we verify the efficacy of FlexAvatar. Many existing methods struggle with view extrapolation while FlexAvatar generates complete 3D head avatars with realistic facial animations. Website: https://tobias-kirschstein.github.io/flexavatar/

