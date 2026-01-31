---
layout: default
title: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
---

# Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
**arXiv**：[2601.21363v1](https://arxiv.org/abs/2601.21363) · [PDF](https://arxiv.org/pdf/2601.21363.pdf)  
**作者**：Weidong Huang, Zhehan Li, Hangxin Liu, Biao Hou, Yao Su, Jingwen Zhang  

**一句话要点**：提出结合SAC大规模预训练与模型微调的方法，以弥合人形机器人控制中预训练与高效适应间的差距。

**关键词**：人形机器人控制, 强化学习, 大规模预训练, 模型微调, 样本效率

## 3 点简述
- 核心问题：人形机器人控制中，大规模预训练与高效微调之间存在样本效率差距，限制新环境安全适应。
- 方法要点：使用SAC进行大规模预训练，支持零部署；微调时采用模型方法，分离确定性执行与随机探索。
- 实验或效果：实现零部署到真实机器人，并在新环境中通过微调提升适应能力，兼顾效率与安全性。

## 摘要（原文）

> Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning.

