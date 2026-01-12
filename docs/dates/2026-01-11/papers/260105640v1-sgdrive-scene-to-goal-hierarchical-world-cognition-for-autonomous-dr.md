---
layout: default
title: SGDrive: Scene-to-Goal Hierarchical World Cognition for Autonomous Driving
---

# SGDrive: Scene-to-Goal Hierarchical World Cognition for Autonomous Driving
**arXiv**：[2601.05640v1](https://arxiv.org/abs/2601.05640) · [PDF](https://arxiv.org/pdf/2601.05640.pdf)  
**作者**：Jingyu Li, Junjie Wu, Dongnan Hu, Xiangkai Huang, Bin Sun, Zhihui Hao, Xianpeng Lang, Xiatian Zhu, Li Zhang  

**一句话要点**：提出SGDrive框架，通过场景-智能体-目标层次化认知增强视觉语言模型在自动驾驶中的规划能力。

**关键词**：自动驾驶规划, 视觉语言模型, 层次化认知, 时空表示, 端到端学习

## 3 点简述
- 问题：通用视觉语言模型缺乏对自动驾驶中3D时空推理的专业理解，难以构建结构化表示。
- 方法：基于预训练视觉语言模型，引入场景-智能体-目标层次化分解，模拟人类驾驶认知过程。
- 效果：在NAVSIM基准测试中，SGDrive在仅摄像头方法中达到最优性能，验证了层次化知识结构的有效性。

## 摘要（原文）

> Recent end-to-end autonomous driving approaches have leveraged Vision-Language Models (VLMs) to enhance planning capabilities in complex driving scenarios. However, VLMs are inherently trained as generalist models, lacking specialized understanding of driving-specific reasoning in 3D space and time. When applied to autonomous driving, these models struggle to establish structured spatial-temporal representations that capture geometric relationships, scene context, and motion patterns critical for safe trajectory planning. To address these limitations, we propose SGDrive, a novel framework that explicitly structures the VLM's representation learning around driving-specific knowledge hierarchies. Built upon a pre-trained VLM backbone, SGDrive decomposes driving understanding into a scene-agent-goal hierarchy that mirrors human driving cognition: drivers first perceive the overall environment (scene context), then attend to safety-critical agents and their behaviors, and finally formulate short-term goals before executing actions. This hierarchical decomposition provides the structured spatial-temporal representation that generalist VLMs lack, integrating multi-level information into a compact yet comprehensive format for trajectory planning. Extensive experiments on the NAVSIM benchmark demonstrate that SGDrive achieves state-of-the-art performance among camera-only methods on both PDMS and EPDMS, validating the effectiveness of hierarchical knowledge structuring for adapting generalist VLMs to autonomous driving.

