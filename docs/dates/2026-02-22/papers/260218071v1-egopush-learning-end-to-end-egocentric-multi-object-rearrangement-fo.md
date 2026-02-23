---
layout: default
title: EgoPush: Learning End-to-End Egocentric Multi-Object Rearrangement for Mobile Robots
---

# EgoPush: Learning End-to-End Egocentric Multi-Object Rearrangement for Mobile Robots
**arXiv**：[2602.18071v1](https://arxiv.org/abs/2602.18071) · [PDF](https://arxiv.org/pdf/2602.18071.pdf)  
**作者**：Boyuan An, Zhexiong Wang, Yipeng Wang, Jiaqi Li, Sihang Li, Jing Zhang, Chen Feng  

**一句话要点**：提出EgoPush框架，以单目视觉实现移动机器人的长时程多物体非抓取重排任务。

**关键词**：自我中心视觉, 多物体重排, 强化学习蒸馏, 长时程任务, 仿真到现实迁移

## 3 点简述
- 核心问题：移动机器人在动态场景中依赖全局状态估计易失败，需解决长时程多物体非抓取重排。
- 方法要点：设计物体中心潜在空间编码相对空间关系，通过特权RL教师蒸馏到纯视觉学生策略，并引入阶段奖励分解长时程任务。
- 实验或效果：仿真实验显示优于端到端RL基线，零样本仿真到现实迁移验证有效性。

## 摘要（原文）

> Humans can rearrange objects in cluttered environments using egocentric perception, navigating occlusions without global coordinates. Inspired by this capability, we study long-horizon multi-object non-prehensile rearrangement for mobile robots using a single egocentric camera. We introduce EgoPush, a policy learning framework that enables egocentric, perception-driven rearrangement without relying on explicit global state estimation that often fails in dynamic scenes. EgoPush designs an object-centric latent space to encode relative spatial relations among objects, rather than absolute poses. This design enables a privileged reinforcement-learning (RL) teacher to jointly learn latent states and mobile actions from sparse keypoints, which is then distilled into a purely visual student policy. To reduce the supervision gap between the omniscient teacher and the partially observed student, we restrict the teacher's observations to visually accessible cues. This induces active perception behaviors that are recoverable from the student's viewpoint. To address long-horizon credit assignment, we decompose rearrangement into stage-level subproblems using temporally decayed, stage-local completion rewards. Extensive simulation experiments demonstrate that EgoPush significantly outperforms end-to-end RL baselines in success rate, with ablation studies validating each design choice. We further demonstrate zero-shot sim-to-real transfer on a mobile platform in the real world. Code and videos are available at https://ai4ce.github.io/EgoPush/.

