---
layout: default
title: Robust Long-term Test-Time Adaptation for 3D Human Pose Estimation through Motion Discretization
---

# Robust Long-term Test-Time Adaptation for 3D Human Pose Estimation through Motion Discretization
**arXiv**：[2511.18851v1](https://arxiv.org/abs/2511.18851) · [PDF](https://arxiv.org/pdf/2511.18851.pdf)  
**作者**：Yilin Wen, Kechuan Dong, Yusuke Sugano  

**一句话要点**：提出基于运动离散化的长时测试时适应方法，以解决3D人体姿态估计中的误差累积问题。

**关键词**：3D人体姿态估计, 测试时适应, 运动离散化, 误差累积缓解, 在线学习, 自监督学习

## 3 点简述
- 核心问题：在线测试时适应中，依赖不完美预测的自监督导致误差累积，性能随时间下降。
- 方法要点：通过无监督聚类获取锚定运动，利用其规律性监督姿态估计器并实现高效自回放。
- 实验或效果：在长时在线适应实验中，方法优于先前方法，验证了设计有效性。

## 摘要（原文）

> Online test-time adaptation addresses the train-test domain gap by adapting the model on unlabeled streaming test inputs before making the final prediction. However, online adaptation for 3D human pose estimation suffers from error accumulation when relying on self-supervision with imperfect predictions, leading to degraded performance over time. To mitigate this fundamental challenge, we propose a novel solution that highlights the use of motion discretization. Specifically, we employ unsupervised clustering in the latent motion representation space to derive a set of anchor motions, whose regularity aids in supervising the human pose estimator and enables efficient self-replay. Additionally, we introduce an effective and efficient soft-reset mechanism by reverting the pose estimator to its exponential moving average during continuous adaptation. We examine long-term online adaptation by continuously adapting to out-of-domain streaming test videos of the same individual, which allows for the capture of consistent personal shape and motion traits throughout the streaming observation. By mitigating error accumulation, our solution enables robust exploitation of these personal traits for enhanced accuracy. Experiments demonstrate that our solution outperforms previous online test-time adaptation methods and validate our design choices.

