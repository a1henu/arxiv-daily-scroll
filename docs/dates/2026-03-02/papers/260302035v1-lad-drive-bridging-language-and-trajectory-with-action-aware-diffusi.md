---
layout: default
title: LAD-Drive: Bridging Language and Trajectory with Action-Aware Diffusion Transformers
---

# LAD-Drive: Bridging Language and Trajectory with Action-Aware Diffusion Transformers
**arXiv**：[2603.02035v1](https://arxiv.org/abs/2603.02035) · [PDF](https://arxiv.org/pdf/2603.02035.pdf)  
**作者**：Fabian Schmidt, Karol Fedurko, Markus Enzweiler, Abhinav Valada  

**一句话要点**：提出LAD-Drive框架，通过动作感知扩散变换器解决自动驾驶中语言到轨迹转换的挑战。

**关键词**：自动驾驶规划, 多模态大语言模型, 扩散变换器, 轨迹生成, 动作感知解码

## 3 点简述
- 核心问题：多模态大语言模型在自动驾驶中难以将离散语义知识转换为连续轨迹，现有方法受限于单模态规划头。
- 方法要点：使用动作解码器推断概率元动作分布，结合车辆运动状态，通过动作感知扩散解码器生成安全可行的轨迹。
- 实验或效果：在LangAuto基准测试中达到最先进水平，驾驶分数提升高达59%，减少路线偏差和碰撞。

## 摘要（原文）

> While multimodal large language models (MLLMs) provide advanced reasoning for autonomous driving, translating their discrete semantic knowledge into continuous trajectories remains a fundamental challenge. Existing methods often rely on unimodal planning heads that inherently limit their ability to represent multimodal driving behavior. Furthermore, most generative approaches frequently condition on one-hot encoded actions, discarding the nuanced navigational uncertainty critical for complex scenarios. To resolve these limitations, we introduce LAD-Drive, a generative framework that structurally disentangles high-level intention from low-level spatial planning. LAD-Drive employs an action decoder to infer a probabilistic meta-action distribution, establishing an explicit belief state that preserves the nuanced intent typically lost by one-hot encodings. This distribution, fused with the vehicle's kinematic state, conditions an action-aware diffusion decoder that utilizes a truncated denoising process to refine learned motion anchors into safe, kinematically feasible trajectories. Extensive evaluations on the LangAuto benchmark demonstrate that LAD-Drive achieves state-of-the-art results, outperforming competitive baselines by up to 59% in Driving Score while significantly reducing route deviations and collisions. We will publicly release the code and models on https://github.com/iis-esslingen/lad-drive.

