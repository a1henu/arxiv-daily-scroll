---
layout: default
title: CoFL: Continuous Flow Fields for Language-Conditioned Navigation
---

# CoFL: Continuous Flow Fields for Language-Conditioned Navigation
**arXiv**：[2603.02854v1](https://arxiv.org/abs/2603.02854) · [PDF](https://arxiv.org/pdf/2603.02854.pdf)  
**作者**：Haokun Liu, Zhaoqi Ma, Yicheng Chen, Masaki Kitagawa, Wentao Zhang, Jinjie Li, Moju Zhao  

**一句话要点**：提出CoFL，一种端到端策略，通过连续流场实现语言条件导航，以解决模块化组件脆弱和动作序列生成成本高的问题。

**关键词**：语言条件导航, 连续流场, 端到端策略, 鸟瞰图观察, 数值积分, 零样本部署

## 3 点简述
- 语言条件导航常依赖脆弱模块或高成本动作序列生成，导致性能受限。
- CoFL直接映射鸟瞰图观察和语言指令到连续流场，输出瞬时速度，通过数值积分生成平滑轨迹。
- 在未见场景中，CoFL显著优于模块化VLM规划器和生成策略基线，并在真实世界实验中保持高成功率。

## 摘要（原文）

> Language-conditioned navigation pipelines often rely on brittle modular components or costly action-sequence generation. To address these limitations, we present CoFL, an end-to-end policy that directly maps a bird's-eye view (BEV) observation and a language instruction to a continuous flow field for navigation. Instead of predicting discrete action tokens or sampling action chunks via iterative denoising, CoFL outputs instantaneous velocities that can be queried at arbitrary 2D projected locations. Trajectories are obtained by numerical integration of the predicted field, producing smooth motion that remains reactive under closed-loop execution. To enable large-scale training, we build a dataset of over 500k BEV image-instruction pairs, each procedurally annotated with a flow field and a trajectory derived from BEV semantic maps built on Matterport3D and ScanNet. By training on a mixed distribution, CoFL significantly outperforms modular Vision-Language Model (VLM)-based planners and generative policy baselines on strictly unseen scenes. Finally, we deploy CoFL zero-shot in real-world experiments with overhead BEV observations across multiple layouts, maintaining reliable closed-loop control and a high success rate.

