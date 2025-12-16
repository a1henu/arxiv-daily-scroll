---
layout: default
title: PoseAnything: Universal Pose-guided Video Generation with Part-aware Temporal Coherence
---

# PoseAnything: Universal Pose-guided Video Generation with Part-aware Temporal Coherence
**arXiv**：[2512.13465v1](https://arxiv.org/abs/2512.13465) · [PDF](https://arxiv.org/pdf/2512.13465.pdf)  
**作者**：Ruiyan Wang, Teng Hu, Kaihui Huang, Zihan Su, Ran Yi, Lizhuang Ma  

**一句话要点**：提出PoseAnything框架以解决姿态引导视频生成中仅支持人类姿态的局限性，实现通用姿态控制。

**关键词**：姿态引导视频生成, 通用姿态控制, 部分感知时序一致性, 相机运动解耦, 非人类姿态数据集

## 3 点简述
- 核心问题：现有方法仅接受人类姿态输入，泛化能力差，无法处理非人类角色。
- 方法要点：引入Part-aware Temporal Coherence Module实现细粒度部分一致性，并设计Subject and Camera Motion Decoupled CFG独立控制相机运动。
- 实验或效果：在XPose数据集上验证，显著优于现有方法，支持任意骨骼输入和高质量视频生成。

## 摘要（原文）

> Pose-guided video generation refers to controlling the motion of subjects in generated video through a sequence of poses. It enables precise control over subject motion and has important applications in animation. However, current pose-guided video generation methods are limited to accepting only human poses as input, thus generalizing poorly to pose of other subjects. To address this issue, we propose PoseAnything, the first universal pose-guided video generation framework capable of handling both human and non-human characters, supporting arbitrary skeletal inputs. To enhance consistency preservation during motion, we introduce Part-aware Temporal Coherence Module, which divides the subject into different parts, establishes part correspondences, and computes cross-attention between corresponding parts across frames to achieve fine-grained part-level consistency. Additionally, we propose Subject and Camera Motion Decoupled CFG, a novel guidance strategy that, for the first time, enables independent camera movement control in pose-guided video generation, by separately injecting subject and camera motion control information into the positive and negative anchors of CFG. Furthermore, we present XPose, a high-quality public dataset containing 50,000 non-human pose-video pairs, along with an automated pipeline for annotation and filtering. Extensive experiments demonstrate that Pose-Anything significantly outperforms state-of-the-art methods in both effectiveness and generalization.

