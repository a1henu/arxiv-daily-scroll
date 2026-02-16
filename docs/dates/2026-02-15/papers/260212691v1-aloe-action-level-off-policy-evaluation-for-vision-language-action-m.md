---
layout: default
title: ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training
---

# ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training
**arXiv**：[2602.12691v1](https://arxiv.org/abs/2602.12691) · [PDF](https://arxiv.org/pdf/2602.12691.pdf)  
**作者**：Rushuai Yang, Hecheng Wang, Chiming Liu, Xiaohan Yan, Yunlong Wang, Xuan Du, Shuoyu Yue, Yongcheng Liu, Chuheng Zhang, Lizhe Qi, Yi Chen, Wei Shan, Maoqing Yao  

**一句话要点**：提出ALOE框架，通过动作级离策略评估提升视觉-语言-动作模型在真实世界中的在线强化学习效率。

**关键词**：离策略评估, 视觉-语言-动作模型, 强化学习, 动作序列评估, 稀疏奖励, 真实世界操作

## 3 点简述
- 核心问题：从混合数据源（如历史策略和人类干预）中评估当前行为质量是离策略评估问题，现有方法常采用保守的在线策略估计，限制学习效果。
- 方法要点：ALOE采用基于分块的时序差分自举法，评估单个动作序列而非最终任务结果，改进稀疏奖励下关键动作块的信用分配。
- 实验或效果：在智能手机包装、衣物折叠和双手抓放三个真实世界操作任务中，ALOE提高了学习效率，未影响执行速度。

## 摘要（原文）

> We study how to improve large foundation vision-language-action (VLA) systems through online reinforcement learning (RL) in real-world settings. Central to this process is the value function, which provides learning signals to guide VLA learning from experience. In practice, the value function is estimated from trajectory fragments collected from different data sources, including historical policies and intermittent human interventions. Estimating the value function of current behavior quality from the mixture data is inherently an off-policy evaluation problem. However, prior work often adopts conservative on-policy estimation for stability, which avoids direct evaluation of the current high-capacity policy and limits learning effectiveness. In this paper, we propose ALOE, an action-level off-policy evaluation framework for VLA post-training. ALOE applies chunking-based temporal-difference bootstrapping to evaluate individual action sequences instead of predicting final task outcomes. This design improves effective credit assignment to critical action chunks under sparse rewards and supports stable policy improvement. We evaluate our method on three real-world manipulation tasks, including smartphone packing as a high-precision task, laundry folding as a long-horizon deformable-object task, and bimanual pick-and-place involving multi-object perception. Across all tasks, ALOE improves learning efficiency without compromising execution speed, showing that off-policy RL can be reintroduced in a reliable manner for real-world VLA post-training. Videos and additional materials are available at our project website.

