---
layout: default
title: SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models
---

# SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models
**arXiv**：[2512.05955v1](https://arxiv.org/abs/2512.05955) · [PDF](https://arxiv.org/pdf/2512.05955.pdf)  
**作者**：Haowen Liu, Shaoxiong Yao, Haonan Chen, Jiawei Gao, Jiayuan Mao, Jia-Bin Huang, Yilun Du  

**一句话要点**：提出SIMPACT框架，通过模拟增强视觉语言模型在机器人精细操作任务中的物理推理能力。

**关键词**：视觉语言模型, 物理模拟, 机器人操作, 动作规划, 物理推理, 测试时增强

## 3 点简述
- 核心问题：视觉语言模型缺乏物理动态理解，难以应用于需要物理推理的机器人精细操作任务。
- 方法要点：在测试时利用单次RGB-D观测构建物理模拟，结合语言推理迭代优化动作规划，无需额外训练。
- 实验或效果：在五个真实世界刚体和可变形物体操作任务中实现最先进性能，超越现有通用机器人操作模型。

## 摘要（原文）

> Vision-Language Models (VLMs) exhibit remarkable common-sense and semantic reasoning capabilities. However, they lack a grounded understanding of physical dynamics. This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes. Consequently, it remains challenging to leverage VLMs for fine-grained robotic manipulation tasks that require physical understanding, reasoning, and corresponding action planning. To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any additional training. From a single RGB-D observation, SIMPACT efficiently constructs physics simulations, enabling the VLM to propose informed actions, observe simulated rollouts, and iteratively refine its reasoning. By integrating language reasoning with physics prediction, our simulation-enabled VLM can understand contact dynamics and action outcomes in a physically grounded way. Our method demonstrates state-of-the-art performance on five challenging, real-world rigid-body and deformable manipulation tasks that require fine-grained physical reasoning, outperforming existing general-purpose robotic manipulation models. Our results demonstrate that embedding physics understanding via efficient simulation into VLM reasoning at test time offers a promising path towards generalizable embodied intelligence. Project webpage can be found at https://simpact-bot.github.io

