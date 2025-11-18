---
layout: default
title: DiffuDepGrasp: Diffusion-based Depth Noise Modeling Empowers Sim2Real Robotic Grasping
---

# DiffuDepGrasp: Diffusion-based Depth Noise Modeling Empowers Sim2Real Robotic Grasping
**arXiv**：[2511.12912v1](https://arxiv.org/abs/2511.12912) · [PDF](https://arxiv.org/pdf/2511.12912.pdf)  
**作者**：Yingting Zhou, Wenbo Cui, Weiheng Liu, Guixing Chen, Haoran Li, Dongbin Zhao  

**一句话要点**：提出DiffuDepGrasp框架，通过扩散模型模拟深度噪声，实现零样本Sim2Real抓取。

**关键词**：Sim2Real迁移, 扩散模型, 深度噪声建模, 机器人抓取, 零样本学习

## 3 点简述
- 核心问题：真实深度图中的传感器伪影（如空洞和噪声）阻碍仿真到现实的策略迁移。
- 方法要点：使用扩散深度生成器合成仿真深度，结合噪声嫁接模块注入传感器真实噪声。
- 实验效果：零样本转移下，在12个物体抓取中平均成功率95.7%，泛化性强。

## 摘要（原文）

> Transferring the depth-based end-to-end policy trained in simulation to physical robots can yield an efficient and robust grasping policy, yet sensor artifacts in real depth maps like voids and noise establish a significant sim2real gap that critically impedes policy transfer. Training-time strategies like procedural noise injection or learned mappings suffer from data inefficiency due to unrealistic noise simulation, which is often ineffective for grasping tasks that require fine manipulation or dependency on paired datasets heavily. Furthermore, leveraging foundation models to reduce the sim2real gap via intermediate representations fails to mitigate the domain shift fully and adds computational overhead during deployment. This work confronts dual challenges of data inefficiency and deployment complexity. We propose DiffuDepGrasp, a deploy-efficient sim2real framework enabling zero-shot transfer through simulation-exclusive policy training. Its core innovation, the Diffusion Depth Generator, synthesizes geometrically pristine simulation depth with learned sensor-realistic noise via two synergistic modules. The first Diffusion Depth Module leverages temporal geometric priors to enable sample-efficient training of a conditional diffusion model that captures complex sensor noise distributions, while the second Noise Grafting Module preserves metric accuracy during perceptual artifact injection. With only raw depth inputs during deployment, DiffuDepGrasp eliminates computational overhead and achieves a 95.7% average success rate on 12-object grasping with zero-shot transfer and strong generalization to unseen objects.Project website: https://diffudepgrasp.github.io/.

