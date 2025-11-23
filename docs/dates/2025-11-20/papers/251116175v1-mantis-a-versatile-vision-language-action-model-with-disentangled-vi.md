---
layout: default
title: Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight
---

# Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight
**arXiv**：[2511.16175v1](https://arxiv.org/abs/2511.16175) · [PDF](https://arxiv.org/pdf/2511.16175.pdf)  
**作者**：Yi Yang, Xueqi Li, Yiyang Chen, Jin Song, Yihan Wang, Zipeng Xiao, Jiadi Su, You Qiaoben, Pengfei Liu, Zhijie Deng  

**一句话要点**：提出Mantis模型，通过解耦视觉预测解决VLA模型训练成本高与推理能力弱的问题。

**关键词**：视觉语言动作模型, 解耦视觉预测, 扩散Transformer, 元查询学习, 机器人操作, 指令跟随能力

## 3 点简述
- 核心问题：VLA模型直接预测高维视觉状态导致训练成本高，压缩视觉信号引发信息瓶颈，且忽视语言监督削弱推理能力。
- 方法要点：引入解耦视觉预测，使用元查询和扩散Transformer头，结合残差连接自动捕获潜在动作以增强显式动作学习。
- 实验或效果：在LIBERO基准上微调后成功率96.7%，超越基线，指令跟随、泛化和推理能力优于开源模型π0.5。

## 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

