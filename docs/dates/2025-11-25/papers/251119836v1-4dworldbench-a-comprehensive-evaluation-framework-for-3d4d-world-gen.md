---
layout: default
title: 4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models
---

# 4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models
**arXiv**：[2511.19836v1](https://arxiv.org/abs/2511.19836) · [PDF](https://arxiv.org/pdf/2511.19836.pdf)  
**作者**：Yiting Lu, Wei Luo, Peiyan Tu, Haoran Li, Hanxin Zhu, Zihao Yu, Xingrui Wang, Xinyi Chen, Xinge Peng, Xin Li, Zhibo Chen  

**一句话要点**：提出4DWorldBench以统一评估3D/4D世界生成模型的真实性与一致性

**关键词**：世界生成模型, 4D评估基准, 多模态对齐, 物理一致性, 自适应评估

## 3 点简述
- 核心问题：现有基准缺乏对世界生成模型真实性与一致性的统一评估
- 方法要点：引入多维度评估框架，包括感知质量、条件对齐、物理真实性和4D一致性
- 实验或效果：自适应工具选择与人类主观判断更一致，支持多模态输入统一评估

## 摘要（原文）

> World Generation Models are emerging as a cornerstone of next-generation multimodal intelligence systems. Unlike traditional 2D visual generation, World Models aim to construct realistic, dynamic, and physically consistent 3D/4D worlds from images, videos, or text. These models not only need to produce high-fidelity visual content but also maintain coherence across space, time, physics, and instruction control, enabling applications in virtual reality, autonomous driving, embodied intelligence, and content creation. However, prior benchmarks emphasize different evaluation dimensions and lack a unified assessment of world-realism capability. To systematically evaluate World Models, we introduce the 4DWorldBench, which measures models across four key dimensions: Perceptual Quality, Condition-4D Alignment, Physical Realism, and 4D Consistency. The benchmark covers tasks such as Image-to-3D/4D, Video-to-4D, Text-to-3D/4D. Beyond these, we innovatively introduce adaptive conditioning across multiple modalities, which not only integrates but also extends traditional evaluation paradigms. To accommodate different modality-conditioned inputs, we map all modality conditions into a unified textual space during evaluation, and further integrate LLM-as-judge, MLLM-as-judge, and traditional network-based methods. This unified and adaptive design enables more comprehensive and consistent evaluation of alignment, physical realism, and cross-modal coherence. Preliminary human studies further demonstrate that our adaptive tool selection achieves closer agreement with subjective human judgments. We hope this benchmark will serve as a foundation for objective comparisons and improvements, accelerating the transition from "visual generation" to "world generation." Our project can be found at https://yeppp27.github.io/4DWorldBench.github.io/.

