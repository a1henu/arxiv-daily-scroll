---
layout: default
title: Can Vision-Language Models Solve the Shell Game?
---

# Can Vision-Language Models Solve the Shell Game?
**arXiv**：[2603.08436v1](https://arxiv.org/abs/2603.08436) · [PDF](https://arxiv.org/pdf/2603.08436.pdf)  
**作者**：Tiedong Liu, Wee Sun Lee  

**一句话要点**：提出时空接地思维链方法，解决视觉语言模型在视频实体跟踪中的根本缺陷

**关键词**：视觉语言模型, 视频实体跟踪, 时空连续性, 思维链推理, 合成基准测试, 状态跟踪问题

## 3 点简述
- 揭示当前视觉语言模型过度依赖静态特征，无法跟踪视觉相同物体的时空连续性
- 提出SGCoT方法，通过生成物体轨迹作为显式中间状态来增强跟踪能力
- 在合成诊断基准VET-Bench上实现超过90%的准确率，显著超越现有方法

## 摘要（原文）

> Visual entity tracking is an innate cognitive ability in humans, yet it remains a critical bottleneck for Vision-Language Models (VLMs). This deficit is often obscured in existing video benchmarks by visual shortcuts. We introduce VET-Bench, a synthetic diagnostic testbed featuring visually identical objects that necessitate tracking exclusively through spatiotemporal continuity. Our experiments reveal that current state-of-the-art VLMs perform at or near chance level on VET-Bench, exposing a fundamental limitation: an over-reliance on static frame-level features and a failure to maintain entity representations over time. We provide a theoretical analysis drawing connections to the state-tracking problem, proving that fixed-depth transformer-based VLMs are fundamentally limited in tracking indistinguishable objects without intermediate supervision due to expressivity constraints. To address this, we propose Spatiotemporal Grounded Chain-of-Thought (SGCoT): generating object trajectories as explicit intermediate states. Leveraging Molmo2's object tracking ability, we elicit SGCoT reasoning by fine-tuning on synthesized text-only data for alignment. Our method achieves state-of-the-art accuracy exceeding 90% on VET-Bench, demonstrating that VLMs can reliably solve the video shell-game task end-to-end without external tools. Our code and data are available at https://vetbench.github.io .

