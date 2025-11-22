---
layout: default
title: Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight
---

# Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight
**arXiv**：[2511.16175v1](https://arxiv.org/abs/2511.16175) · [PDF](https://arxiv.org/pdf/2511.16175.pdf)  
**作者**：Yi Yang, Xueqi Li, Yiyang Chen, Jin Song, Yihan Wang, Zipeng Xiao, Jiadi Su, You Qiaoben, Pengfei Liu, Zhijie Deng  

**一句话要点**：提出Mantis框架以解决视觉-语言-动作模型中视觉预测与推理能力不足的问题

**关键词**：视觉-语言-动作模型, 解耦视觉预测, 扩散Transformer, 元查询学习, 机器人操作, 指令跟随

## 3 点简述
- 核心问题：现有VLA模型视觉状态预测分散模型能力，且语言监督不足导致推理能力弱
- 方法要点：引入解耦视觉预测，使用元查询和扩散Transformer自动捕获潜在动作
- 实验或效果：在LIBERO基准上达到96.7%成功率，优于基线模型并展示高泛化能力

## 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

