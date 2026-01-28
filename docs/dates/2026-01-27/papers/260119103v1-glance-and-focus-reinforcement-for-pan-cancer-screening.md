---
layout: default
title: Glance and Focus Reinforcement for Pan-cancer Screening
---

# Glance and Focus Reinforcement for Pan-cancer Screening
**arXiv**：[2601.19103v1](https://arxiv.org/abs/2601.19103) · [PDF](https://arxiv.org/pdf/2601.19103.pdf)  
**作者**：Linshan Wu, Jiaxin Zhuang, Hao Chen  

**一句话要点**：提出GF-Screen强化学习框架以解决大规模CT扫描中泛癌筛查的病灶定位难题

**关键词**：泛癌筛查, CT扫描分析, 强化学习, 病灶分割, 计算机辅助诊断

## 3 点简述
- 核心问题：大规模CT扫描中微小病灶定位困难，前景-背景极度不平衡导致效率低和假阳性高。
- 方法要点：采用Glance模型定位病灶区域，Focus模型精确分割，通过强化学习利用分割结果奖励Glance模型。
- 实验或效果：在16个内部和7个外部数据集上验证有效性，在MICCAI FLARE25挑战中领先，性能显著提升。

## 摘要（原文）

> Pan-cancer screening in large-scale CT scans remains challenging for existing AI methods, primarily due to the difficulty of localizing diverse types of tiny lesions in large CT volumes. The extreme foreground-background imbalance significantly hinders models from focusing on diseased regions, while redundant focus on healthy regions not only decreases the efficiency but also increases false positives. Inspired by radiologists' glance and focus diagnostic strategy, we introduce GF-Screen, a Glance and Focus reinforcement learning framework for pan-cancer screening. GF-Screen employs a Glance model to localize the diseased regions and a Focus model to precisely segment the lesions, where segmentation results of the Focus model are leveraged to reward the Glance model via Reinforcement Learning (RL). Specifically, the Glance model crops a group of sub-volumes from the entire CT volume and learns to select the sub-volumes with lesions for the Focus model to segment. Given that the selecting operation is non-differentiable for segmentation training, we propose to employ the segmentation results to reward the Glance model. To optimize the Glance model, we introduce a novel group relative learning paradigm, which employs group relative comparison to prioritize high-advantage predictions and discard low-advantage predictions within sub-volume groups, not only improving efficiency but also reducing false positives. In this way, for the first time, we effectively extend cutting-edge RL techniques to tackle the specific challenges in pan-cancer screening. Extensive experiments on 16 internal and 7 external datasets across 9 lesion types demonstrated the effectiveness of GF-Screen. Notably, GF-Screen leads the public validation leaderboard of MICCAI FLARE25 pan-cancer challenge, surpassing the FLARE24 champion solution by a large margin (+25.6% DSC and +28.2% NSD).

