---
layout: default
title: Tactile Memory with Soft Robot: Robust Object Insertion via Masked Encoding and Soft Wrist
---

# Tactile Memory with Soft Robot: Robust Object Insertion via Masked Encoding and Soft Wrist
**arXiv**：[2601.19275v1](https://arxiv.org/abs/2601.19275) · [PDF](https://arxiv.org/pdf/2601.19275.pdf)  
**作者**：Tatsuya Kamijo, Mai Nishimura, Cristian C. Beltran-Hernandez, Nodoka Shibasaki, Masashi Hamaya  

**一句话要点**：提出TaMeSo-bot系统，通过软手腕和掩码编码实现不确定环境下稳健的物体插入任务。

**关键词**：触觉记忆, 软机器人, 掩码编码, 稳健操作, 时空建模

## 3 点简述
- 核心问题：在不确定环境下，如钥匙插入，触觉记忆对接触丰富任务至关重要。
- 方法要点：集成软手腕和MAT³模型，通过掩码令牌预测学习时空表示，无需显式子任务分割。
- 实验或效果：在真实机器人实验中，MAT³在多种条件下比基线成功率更高，能适应未见场景。

## 摘要（原文）

> Tactile memory, the ability to store and retrieve touch-based experience, is critical for contact-rich tasks such as key insertion under uncertainty. To replicate this capability, we introduce Tactile Memory with Soft Robot (TaMeSo-bot), a system that integrates a soft wrist with tactile retrieval-based control to enable safe and robust manipulation. The soft wrist allows safe contact exploration during data collection, while tactile memory reuses past demonstrations via retrieval for flexible adaptation to unseen scenarios. The core of this system is the Masked Tactile Trajectory Transformer (MAT$^\text{3}$), which jointly models spatiotemporal interactions between robot actions, distributed tactile feedback, force-torque measurements, and proprioceptive signals. Through masked-token prediction, MAT$^\text{3}$ learns rich spatiotemporal representations by inferring missing sensory information from context, autonomously extracting task-relevant features without explicit subtask segmentation. We validate our approach on peg-in-hole tasks with diverse pegs and conditions in real-robot experiments. Our extensive evaluation demonstrates that MAT$^\text{3}$ achieves higher success rates than the baselines over all conditions and shows remarkable capability to adapt to unseen pegs and conditions.

