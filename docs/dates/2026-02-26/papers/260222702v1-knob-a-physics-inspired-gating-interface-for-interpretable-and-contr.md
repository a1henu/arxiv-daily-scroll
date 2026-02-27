---
layout: default
title: Knob: A Physics-Inspired Gating Interface for Interpretable and Controllable Neural Dynamics
---

# Knob: A Physics-Inspired Gating Interface for Interpretable and Controllable Neural Dynamics
**arXiv**：[2602.22702v1](https://arxiv.org/abs/2602.22702) · [PDF](https://arxiv.org/pdf/2602.22702.pdf)  
**作者**：Siyu Jiang, Sanshuai Cui, Hui Zeng  

**一句话要点**：提出Knob框架，通过物理启发的门控接口实现可解释和可控的神经动态，用于动态模型校准。

**关键词**：神经动态控制, 模型校准, 物理启发接口, 二阶系统映射, 可解释AI, 连续推理

## 3 点简述
- 现有校准方法忽视动态推理，Knob将神经门控映射到二阶机械系统，提供可调接口。
- 核心机制使用logit级凸融合作为输入自适应温度缩放，减少模型置信度冲突。
- 实验验证校准机制，在连续模式下门响应符合二阶控制特征，支持可预测人机调优。

## 摘要（原文）

> Existing neural network calibration methods often treat calibration as a static, post-hoc optimization task. However, this neglects the dynamic and temporal nature of real-world inference. Moreover, existing methods do not provide an intuitive interface enabling human operators to dynamically adjust model behavior under shifting conditions. In this work, we propose Knob, a framework that connects deep learning with classical control theory by mapping neural gating dynamics to a second-order mechanical system. By establishing correspondences between physical parameters -- damping ratio ($ζ$) and natural frequency ($ω_n$) -- and neural gating, we create a tunable "safety valve". The core mechanism employs a logit-level convex fusion, functioning as an input-adaptive temperature scaling. It tends to reduce model confidence particularly when model branches produce conflicting predictions. Furthermore, by imposing second-order dynamics (Knob-ODE), we enable a \textit{dual-mode} inference: standard i.i.d. processing for static tasks, and state-preserving processing for continuous streams. Our framework allows operators to tune "stability" and "sensitivity" through familiar physical analogues. This paper presents an exploratory architectural interface; we focus on demonstrating the concept and validating its control-theoretic properties rather than claiming state-of-the-art calibration performance. Experiments on CIFAR-10-C validate the calibration mechanism and demonstrate that, in Continuous Mode, the gate responses are consistent with standard second-order control signatures (step settling and low-pass attenuation), paving the way for predictable human-in-the-loop tuning.

