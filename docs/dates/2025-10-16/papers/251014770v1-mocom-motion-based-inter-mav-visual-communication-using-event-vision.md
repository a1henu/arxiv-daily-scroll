---
layout: default
title: MoCom: Motion-based Inter-MAV Visual Communication Using Event Vision and Spiking Neural Networks
---

# MoCom: Motion-based Inter-MAV Visual Communication Using Event Vision and Spiking Neural Networks
**arXiv**：[2510.14770v1](https://arxiv.org/abs/2510.14770) · [PDF](https://arxiv.org/pdf/2510.14770.pdf)  
**作者**：Zhang Nengbo, Hann Woei Ho, Ye Zhou  

**一句话要点**：提出基于运动和事件视觉的MAV视觉通信框架，以解决无线电通信在受限环境中的问题。

**关键词**：微型飞行器通信, 事件视觉, 脉冲神经网络, 运动模式识别, 视觉码本, 低功耗通信

## 3 点简述
- 核心问题：MAV群在频谱拥堵和干扰环境中，无线电通信不可靠且功耗高。
- 方法要点：使用事件相机捕捉MAV运动模式，通过SNN和预定义码本解码信息。
- 实验或效果：实验验证解码准确且功耗低，适用于受限环境。

## 摘要（原文）

> Reliable communication in Micro Air Vehicle (MAV) swarms is challenging in
> environments, where conventional radio-based methods suffer from spectrum
> congestion, jamming, and high power consumption. Inspired by the waggle dance
> of honeybees, which efficiently communicate the location of food sources
> without sound or contact, we propose a novel visual communication framework for
> MAV swarms using motion-based signaling. In this framework, MAVs convey
> information, such as heading and distance, through deliberate flight patterns,
> which are passively captured by event cameras and interpreted using a
> predefined visual codebook of four motion primitives: vertical (up/down),
> horizontal (left/right), left-to-up-to-right, and left-to-down-to-right,
> representing control symbols (``start'', ``end'', ``1'', ``0''). To decode
> these signals, we design an event frame-based segmentation model and a
> lightweight Spiking Neural Network (SNN) for action recognition. An integrated
> decoding algorithm then combines segmentation and classification to robustly
> interpret MAV motion sequences. Experimental results validate the framework's
> effectiveness, which demonstrates accurate decoding and low power consumption,
> and highlights its potential as an energy-efficient alternative for MAV
> communication in constrained environments.

