---
layout: default
title: Xiaomi MiMo-VL-Miloco Technical Report
---

# Xiaomi MiMo-VL-Miloco Technical Report
**arXiv**：[2512.17436v1](https://arxiv.org/abs/2512.17436) · [PDF](https://arxiv.org/pdf/2512.17436.pdf)  
**作者**：Jiaze Li, Jingyang Chen, Yuxun Qu, Jianzhong Ju, Zhenbo Luo, Jian Luan, Shijie Xu, Zhenru Lin, Junyou Zhu, Boshen Xu, Wenhui Tan, Pei Fu  

**一句话要点**：提出MiMo-VL-Miloco-7B，专为智能家居场景优化的视觉语言模型，提升手势识别与多模态推理性能。

**关键词**：智能家居视觉语言模型, 手势识别, 多模态推理, 强化学习训练, 开源模型部署

## 3 点简述
- 核心问题：智能家居场景下的视觉语言理解与多模态推理能力不足，需平衡专业性与通用性。
- 方法要点：基于MiMo-VL-7B，采用两阶段训练，结合监督微调与基于Group Relative Policy Optimization的强化学习，融入思维链监督和令牌预算感知推理。
- 实验或效果：在家庭场景理解基准上取得领先F1分数，并在视频和语言理解基准上表现优异，开源模型与工具支持实际部署。

## 摘要（原文）

> We open-source \textbf{MiMo-VL-Miloco-7B} and its quantized variant \textbf{MiMo-VL-Miloco-7B-GGUF}, a pair of home-centric vision-language models that achieve strong performance on both home-scenario understanding and general multimodal reasoning. Built on the MiMo-VL-7B backbone, MiMo-VL-Miloco-7B is specialized for smart-home environments, attaining leading F1 scores on gesture recognition and common home-scenario understanding, while also delivering consistent gains across video benchmarks such as Video-MME, Video-MMMU, and Charades-STA, as well as language understanding benchmarks including MMMU-Pro and MMLU-Pro. In our experiments, MiMo-VL-Miloco-7B outperforms strong closed-source and open-source baselines on home-scenario understanding and several multimodal reasoning benchmarks. To balance specialization and generality, we design a two-stage training pipeline that combines supervised fine-tuning with reinforcement learning based on Group Relative Policy Optimization, leveraging efficient multi-domain data. We further incorporate chain-of-thought supervision and token-budget-aware reasoning, enabling the model to learn knowledge in a data-efficient manner while also performing reasoning efficiently. Our analysis shows that targeted home-scenario training not only enhances activity and gesture understanding, but also improves text-only reasoning with only modest trade-offs on document-centric tasks. Model checkpoints, quantized GGUF weights, and our home-scenario evaluation toolkit are publicly available at \href{https://github.com/XiaoMi/xiaomi-mimo-vl-miloco}{https://github.com/XiaoMi/xiaomi-mimo-vl-miloco} to support research and deployment in real-world smart-home applications.

