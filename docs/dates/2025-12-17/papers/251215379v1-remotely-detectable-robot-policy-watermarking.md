---
layout: default
title: Remotely Detectable Robot Policy Watermarking
---

# Remotely Detectable Robot Policy Watermarking
**arXiv**：[2512.15379v1](https://arxiv.org/abs/2512.15379) · [PDF](https://arxiv.org/pdf/2512.15379.pdf)  
**作者**：Michael Amir, Manon Flageat, Amanda Prorok  

**一句话要点**：提出Colored Noise Coherency方法，通过远程观测检测机器人策略水印以保护知识产权。

**关键词**：机器人策略水印, 远程检测, 知识产权保护, 频谱信号嵌入, 物理观测差距, 非侵入式验证

## 3 点简述
- 核心问题：机器人训练策略作为知识产权，需远程验证所有权，但现有方法依赖内部状态，存在物理观测差距。
- 方法要点：利用策略固有随机性嵌入频谱信号，保持动作分布不变，实现非侵入式远程水印检测。
- 实验或效果：在模拟和真实机器人实验中，通过运动捕捉和视频等多种远程模态展示强健检测效果。

## 摘要（原文）

> The success of machine learning for real-world robotic systems has created a new form of intellectual property: the trained policy. This raises a critical need for novel methods that verify ownership and detect unauthorized, possibly unsafe misuse. While watermarking is established in other domains, physical policies present a unique challenge: remote detection. Existing methods assume access to the robot's internal state, but auditors are often limited to external observations (e.g., video footage). This ``Physical Observation Gap'' means the watermark must be detected from signals that are noisy, asynchronous, and filtered by unknown system dynamics. We formalize this challenge using the concept of a \textit{glimpse sequence}, and introduce Colored Noise Coherency (CoNoCo), the first watermarking strategy designed for remote detection. CoNoCo embeds a spectral signal into the robot's motions by leveraging the policy's inherent stochasticity. To show it does not degrade performance, we prove CoNoCo preserves the marginal action distribution. Our experiments demonstrate strong, robust detection across various remote modalities, including motion capture and side-way/top-down video footage, in both simulated and real-world robot experiments. This work provides a necessary step toward protecting intellectual property in robotics, offering the first method for validating the provenance of physical policies non-invasively, using purely remote observations.

