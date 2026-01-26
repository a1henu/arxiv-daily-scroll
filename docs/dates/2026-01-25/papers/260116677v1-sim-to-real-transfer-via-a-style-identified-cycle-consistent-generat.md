---
layout: default
title: Sim-to-Real Transfer via a Style-Identified Cycle Consistent Generative Adversarial Network: Zero-Shot Deployment on Robotic Manipulators through Visual Domain Adaptation
---

# Sim-to-Real Transfer via a Style-Identified Cycle Consistent Generative Adversarial Network: Zero-Shot Deployment on Robotic Manipulators through Visual Domain Adaptation
**arXiv**：[2601.16677v1](https://arxiv.org/abs/2601.16677) · [PDF](https://arxiv.org/pdf/2601.16677.pdf)  
**作者**：Lucía Güitta-López, Lionel Güitta-López, Jaime Boal, Álvaro Jesús López-López  

**一句话要点**：提出基于风格识别循环一致生成对抗网络的视觉域适应方法，实现机器人操作零样本从仿真到真实部署。

**关键词**：仿真到真实迁移, 视觉域适应, 生成对抗网络, 零样本部署, 机器人操作, 深度强化学习

## 3 点简述
- 核心问题：深度强化学习样本效率低，仿真到真实迁移存在视觉差距，阻碍工业应用。
- 方法要点：使用StyleID-CycleGAN将虚拟观测转换为真实合成图像，创建混合域训练代理，实现零样本部署。
- 实验或效果：在拾放操作中，虚拟成功率90-100%，真实部署准确率超95%，泛化至不同颜色和形状物体。

## 摘要（原文）

> The sample efficiency challenge in Deep Reinforcement Learning (DRL) compromises its industrial adoption due to the high cost and time demands of real-world training. Virtual environments offer a cost-effective alternative for training DRL agents, but the transfer of learned policies to real setups is hindered by the sim-to-real gap. Achieving zero-shot transfer, where agents perform directly in real environments without additional tuning, is particularly desirable for its efficiency and practical value. This work proposes a novel domain adaptation approach relying on a Style-Identified Cycle Consistent Generative Adversarial Network (StyleID-CycleGAN or SICGAN), an original Cycle Consistent Generative Adversarial Network (CycleGAN) based model. SICGAN translates raw virtual observations into real-synthetic images, creating a hybrid domain for training DRL agents that combines virtual dynamics with real-like visual inputs. Following virtual training, the agent can be directly deployed, bypassing the need for real-world training. The pipeline is validated with two distinct industrial robots in the approaching phase of a pick-and-place operation. In virtual environments agents achieve success rates of 90 to 100\%, and real-world deployment confirms robust zero-shot transfer (i.e., without additional training in the physical environment) with accuracies above 95\% for most workspace regions. We use augmented reality targets to improve the evaluation process efficiency, and experimentally demonstrate that the agent successfully generalizes to real objects of varying colors and shapes, including LEGO\textsuperscript{\textregistered}~cubes and a mug. These results establish the proposed pipeline as an efficient, scalable solution to the sim-to-real problem.

