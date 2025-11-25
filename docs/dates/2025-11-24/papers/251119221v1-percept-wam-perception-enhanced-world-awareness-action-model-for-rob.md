---
layout: default
title: Percept-WAM: Perception-Enhanced World-Awareness-Action Model for Robust End-to-End Autonomous Driving
---

# Percept-WAM: Perception-Enhanced World-Awareness-Action Model for Robust End-to-End Autonomous Driving
**arXiv**：[2511.19221v1](https://arxiv.org/abs/2511.19221) · [PDF](https://arxiv.org/pdf/2511.19221.pdf)  
**作者**：Jianhua Han, Meng Tian, Jiangtong Zhu, Fan He, Huixin Zhang, Sitong Guo, Dechang Zhu, Hao Tang, Pei Xu, Yuze Guo, Minzhe Niu, Haojie Zhu, Qichao Dong, Xuechao Yan, Siyuan Dong, Lu Hou, Qingqiu Huang, Xiaosong Jia, Hang Xu  

**一句话要点**：提出Percept-WAM模型以增强端到端自动驾驶的感知鲁棒性

**关键词**：自动驾驶, 视觉语言模型, 2D/3D感知, 长尾场景, 轨迹规划

## 3 点简述
- 核心问题：自动驾驶中空间感知不准确和不稳定，尤其在长尾场景和复杂交互中。
- 方法要点：统一2D/3D感知任务于单一视觉语言模型，使用World-PV和World-BEV令牌编码空间信息。
- 实验或效果：在COCO和nuScenes基准上超越经典检测器，集成轨迹解码器提升规划性能。

## 摘要（原文）

> Autonomous driving heavily relies on accurate and robust spatial perception. Many failures arise from inaccuracies and instability, especially in long-tail scenarios and complex interactions. However, current vision-language models are weak at spatial grounding and understanding, and VLA systems built on them therefore show limited perception and localization ability. To address these challenges, we introduce Percept-WAM, a perception-enhanced World-Awareness-Action Model that is the first to implicitly integrate 2D/3D scene understanding abilities within a single vision-language model (VLM). Instead of relying on QA-style spatial reasoning, Percept-WAM unifies 2D/3D perception tasks into World-PV and World-BEV tokens, which encode both spatial coordinates and confidence. We propose a grid-conditioned prediction mechanism for dense object perception, incorporating IoU-aware scoring and parallel autoregressive decoding, improving stability in long-tail, far-range, and small-object scenarios. Additionally, Percept-WAM leverages pretrained VLM parameters to retain general intelligence (e.g., logical reasoning) and can output perception results and trajectory control outputs directly. Experiments show that Percept-WAM matches or surpasses classical detectors and segmenters on downstream perception benchmarks, achieving 51.7/58.9 mAP on COCO 2D detection and nuScenes BEV 3D detection. When integrated with trajectory decoders, it further improves planning performance on nuScenes and NAVSIM, e.g., surpassing DiffusionDrive by 2.1 in PMDS on NAVSIM. Qualitative results further highlight its strong open-vocabulary and long-tail generalization.

