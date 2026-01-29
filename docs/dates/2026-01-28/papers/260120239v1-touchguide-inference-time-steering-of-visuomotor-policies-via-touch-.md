---
layout: default
title: TouchGuide: Inference-Time Steering of Visuomotor Policies via Touch Guidance
---

# TouchGuide: Inference-Time Steering of Visuomotor Policies via Touch Guidance
**arXiv**：[2601.20239v1](https://arxiv.org/abs/2601.20239) · [PDF](https://arxiv.org/pdf/2601.20239.pdf)  
**作者**：Zhemeng Zhang, Jiahua Ma, Xincheng Yang, Xin Wen, Yuzhi Zhang, Boyan Li, Yiran Qin, Jin Liu, Can Zhao, Li Kang, Haoqin Hong, Zhenfei Yin, Philip Torr, Hao Su, Ruimao Zhang, Daolin Ma  

**一句话要点**：提出TouchGuide，通过触觉引导在推理时优化视觉运动策略，以解决精细接触式操作难题。

**关键词**：触觉引导, 视觉运动策略, 推理时优化, 接触式操作, 跨模态融合, 对比学习

## 3 点简述
- 核心问题：机器人精细接触式操作中触觉反馈利用不足，导致性能受限。
- 方法要点：采用两阶段跨策略融合，先视觉生成粗动作，再触觉模型引导细化，确保物理接触可行性。
- 实验或效果：在鞋带系结等五个任务上，TouchGuide显著优于现有视觉触觉策略，验证其有效性。

## 摘要（原文）

> Fine-grained and contact-rich manipulation remain challenging for robots, largely due to the underutilization of tactile feedback. To address this, we introduce TouchGuide, a novel cross-policy visuo-tactile fusion paradigm that fuses modalities within a low-dimensional action space. Specifically, TouchGuide operates in two stages to guide a pre-trained diffusion or flow-matching visuomotor policy at inference time. First, the policy produces a coarse, visually-plausible action using only visual inputs during early sampling. Second, a task-specific Contact Physical Model (CPM) provides tactile guidance to steer and refine the action, ensuring it aligns with realistic physical contact conditions. Trained through contrastive learning on limited expert demonstrations, the CPM provides a tactile-informed feasibility score to steer the sampling process toward refined actions that satisfy physical contact constraints. Furthermore, to facilitate TouchGuide training with high-quality and cost-effective data, we introduce TacUMI, a data collection system. TacUMI achieves a favorable trade-off between precision and affordability; by leveraging rigid fingertips, it obtains direct tactile feedback, thereby enabling the collection of reliable tactile data. Extensive experiments on five challenging contact-rich tasks, such as shoe lacing and chip handover, show that TouchGuide consistently and significantly outperforms state-of-the-art visuo-tactile policies.

