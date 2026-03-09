---
layout: default
title: AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models
---

# AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models
**arXiv**：[2603.05868v1](https://arxiv.org/abs/2603.05868) · [PDF](https://arxiv.org/pdf/2603.05868.pdf)  
**作者**：Hyeongjun Heo, Seungyeon Woo, Sang Min Kim, Junho Kim, Junho Lee, Yonghyeon Lee, Young Min Kim  

**一句话要点**：提出零样本相机适应框架，以增强视觉-语言-动作模型在机器人操作中的视角鲁棒性。

**关键词**：视觉-语言-动作模型, 零样本适应, 新视角合成, 机器人操作, 视角鲁棒性, 实时调整

## 3 点简述
- 核心问题：预训练视觉-语言-动作模型在部署时对相机视角变化敏感，需微调但成本高。
- 方法要点：利用前馈式新视角合成模型实时调整测试图像，匹配训练配置，无需额外数据或模型修改。
- 实验或效果：在LIBERO基准测试和真实机器人场景中，优于基于数据增强或3D特征的基线方法。

## 摘要（原文）

> Despite remarkable progress in Vision-Language-Action models (VLAs) for robot manipulation, these large pre-trained models require fine-tuning to be deployed in specific environments. These fine-tuned models are highly sensitive to camera viewpoint changes that frequently occur in unstructured environments. In this paper, we propose a zero-shot camera adaptation framework without additional demonstration data, policy fine-tuning, or architectural modification. Our key idea is to virtually adjust test-time camera observations to match the training camera configuration in real-time. For that, we use a recent feed-forward novel view synthesis model which outputs high-quality target view images, handling both extrinsic and intrinsic parameters. This plug-and-play approach preserves the pre-trained capabilities of VLAs and applies to any RGB-based policy. Through extensive experiments on the LIBERO benchmark, our method consistently outperforms baselines that use data augmentation for policy fine-tuning or additional 3D-aware features for visual input. We further validate that our approach constantly enhances viewpoint robustness in real-world robotic manipulation scenarios, including settings with varying camera extrinsics, intrinsics, and freely moving handheld cameras.

