---
layout: default
title: OffSeeker: Online Reinforcement Learning Is Not All You Need for Deep Research Agents
---

# OffSeeker: Online Reinforcement Learning Is Not All You Need for Deep Research Agents
**arXiv**：[2601.18467v1](https://arxiv.org/abs/2601.18467) · [PDF](https://arxiv.org/pdf/2601.18467.pdf)  
**作者**：Yuhang Zhou, Kai Zheng, Qiguang Chen, Mengkang Hu, Qingfeng Sun, Can Xu, Jingjing Chen  

**一句话要点**：提出OffSeeker离线训练套件以解决深度研究代理在线强化学习成本高的问题

**关键词**：深度研究代理, 离线训练, 任务合成, 强化学习, 开源数据集

## 3 点简述
- 核心问题：在线强化学习成本高，离线训练缺乏高质量研究轨迹
- 方法要点：开发DeepForge任务合成框架和开源数据集，支持大规模离线训练
- 实验或效果：OffSeeker在六个基准测试中领先同规模代理，与30B在线训练系统竞争

## 摘要（原文）

> Deep research agents have shown remarkable potential in handling long-horizon tasks. However, state-of-the-art performance typically relies on online reinforcement learning (RL), which is financially expensive due to extensive API calls. While offline training offers a more efficient alternative, its progress is hindered by the scarcity of high-quality research trajectories. In this paper, we demonstrate that expensive online reinforcement learning is not all you need to build powerful research agents. To bridge this gap, we introduce a fully open-source suite designed for effective offline training. Our core contributions include DeepForge, a ready-to-use task synthesis framework that generates large-scale research queries without heavy preprocessing; and a curated collection of 66k QA pairs, 33k SFT trajectories, and 21k DPO pairs. Leveraging these resources, we train OffSeeker (8B), a model developed entirely offline. Extensive evaluations across six benchmarks show that OffSeeker not only leads among similar-sized agents but also remains competitive with 30B-parameter systems trained via heavy online RL.

