---
layout: default
title: VideoWorld 2: Learning Transferable Knowledge from Real-world Videos
---

# VideoWorld 2: Learning Transferable Knowledge from Real-world Videos
**arXiv**：[2602.10102v1](https://arxiv.org/abs/2602.10102) · [PDF](https://arxiv.org/pdf/2602.10102.pdf)  
**作者**：Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  

**一句话要点**：提出VideoWorld 2，通过动态增强的潜在动态模型从原始真实世界视频中学习可迁移知识。

**关键词**：视频理解, 潜在动态模型, 可迁移学习, 机器人操作, 长视频推理

## 3 点简述
- 核心问题：从无标签视频数据中学习可迁移知识，以应用于新环境。
- 方法要点：引入dLDM，解耦动作动态与视觉外观，利用预训练视频扩散模型建模外观，学习紧凑的任务相关动态潜在码。
- 实验或效果：在真实世界手工艺任务中提升任务成功率高达70%，并在机器人操作中从Open-X数据集获取知识，改善CALVIN性能。

## 摘要（原文）

> Learning transferable knowledge from unlabeled video data and applying it in new environments is a fundamental capability of intelligent agents. This work presents VideoWorld 2, which extends VideoWorld and offers the first investigation into learning transferable knowledge directly from raw real-world videos. At its core, VideoWorld 2 introduces a dynamic-enhanced Latent Dynamics Model (dLDM) that decouples action dynamics from visual appearance: a pretrained video diffusion model handles visual appearance modeling, enabling the dLDM to learn latent codes that focus on compact and meaningful task-related dynamics. These latent codes are then modeled autoregressively to learn task policies and support long-horizon reasoning. We evaluate VideoWorld 2 on challenging real-world handcraft making tasks, where prior video generation and latent-dynamics models struggle to operate reliably. Remarkably, VideoWorld 2 achieves up to 70% improvement in task success rate and produces coherent long execution videos. In robotics, we show that VideoWorld 2 can acquire effective manipulation knowledge from the Open-X dataset, which substantially improves task performance on CALVIN. This study reveals the potential of learning transferable world knowledge directly from raw videos, with all code, data, and models to be open-sourced for further research.

