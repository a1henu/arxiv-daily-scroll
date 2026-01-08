---
layout: default
title: CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos
---

# CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos
**arXiv**：[2601.04061v1](https://arxiv.org/abs/2601.04061) · [PDF](https://arxiv.org/pdf/2601.04061.pdf)  
**作者**：Chubin Zhang, Jianan Wang, Zifeng Gao, Yue Su, Tianru Dai, Cai Zhou, Jiwen Lu, Yansong Tang  

**一句话要点**：提出对比潜在动作预训练框架，以解决从人类视频学习视觉-语言-动作模型时的视觉纠缠问题。

**关键词**：对比学习, 潜在动作模型, 视觉-语言-动作对齐, 技能迁移, 机器人操作, 人类视频学习

## 3 点简述
- 核心问题：通用视觉-语言-动作模型因机器人数据稀缺而受限，现有潜在动作模型易受视觉噪声影响。
- 方法要点：通过对比学习对齐视频视觉潜在空间与机器人本体感知潜在空间，映射到可执行代码本。
- 实验或效果：CLAP显著超越基线，有效将人类视频技能迁移至机器人执行，支持指令跟随和精确操作。

## 摘要（原文）

> Generalist Vision-Language-Action models are currently hindered by the scarcity of robotic data compared to the abundance of human video demonstrations. Existing Latent Action Models attempt to leverage video data but often suffer from visual entanglement, capturing noise rather than manipulation skills. To address this, we propose Contrastive Latent Action Pretraining (CLAP), a framework that aligns the visual latent space from videos with a proprioceptive latent space from robot trajectories. By employing contrastive learning, CLAP maps video transitions onto a quantized, physically executable codebook. Building on this representation, we introduce a dual-formulation VLA framework offering both CLAP-NTP, an autoregressive model excelling at instruction following and object generalization, and CLAP-RF, a Rectified Flow-based policy designed for high-frequency, precise manipulation. Furthermore, we propose a Knowledge Matching (KM) regularization strategy to mitigate catastrophic forgetting during fine-tuning. Extensive experiments demonstrate that CLAP significantly outperforms strong baselines, enabling the effective transfer of skills from human videos to robotic execution. Project page: https://lin-shan.com/CLAP/.

