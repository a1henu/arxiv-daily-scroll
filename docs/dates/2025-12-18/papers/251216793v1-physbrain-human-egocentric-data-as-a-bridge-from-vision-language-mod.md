---
layout: default
title: PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence
---

# PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence
**arXiv**：[2512.16793v1](https://arxiv.org/abs/2512.16793) · [PDF](https://arxiv.org/pdf/2512.16793.pdf)  
**作者**：Xiaopeng Lin, Shijie Lian, Bin Yu, Ruoqi Yang, Changti Wu, Yuzhuo Miao, Yurun Jin, Yukun Shi, Cong Huang, Bojun Cheng, Kai Chen  

**一句话要点**：提出PhysBrain，利用人类第一人称视频作为桥梁，从视觉语言模型迁移到物理智能。

**关键词**：第一人称视频理解, 物理智能, 视觉语言模型, 机器人控制, 数据集构建

## 3 点简述
- 核心问题：视觉语言模型基于第三人称数据训练，与人形机器人的第一人称视角不匹配，阻碍物理智能发展。
- 方法要点：设计Egocentric2Embodiment翻译管道，将第一人称视频转换为结构化多级VQA监督，构建E2E-3M数据集。
- 实验或效果：PhysBrain在EgoThink上规划能力提升，作为初始化使VLA微调更高效，SimperEnv成功率53.9%。

## 摘要（原文）

> Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. However, most VLMs are trained primarily on third-person data, creating a fundamental viewpoint mismatch for humanoid robots. Scaling robot egocentric data collection remains impractical due to high cost and limited diversity, whereas large-scale human egocentric videos offer a scalable alternative that naturally capture rich interaction context and causal structure. The key challenge is to convert raw egocentric videos into structured and reliable embodiment training supervision. Accordingly, we propose an Egocentric2Embodiment translation pipeline that transforms first-person videos into multi-level, schema-driven VQA supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning on EgoThink. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher SimplerEnv success rates (53.9\%), demonstrating effective transfer from human egocentric supervision to downstream robot control.

