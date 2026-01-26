---
layout: default
title: ReViP: Reducing False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance
---

# ReViP: Reducing False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance
**arXiv**：[2601.16667v1](https://arxiv.org/abs/2601.16667) · [PDF](https://arxiv.org/pdf/2601.16667.pdf)  
**作者**：Zhuohao Li, Yinghao Li, Jian-Jian Jiang, Lang Zhou, Tianyu Zhang, Wei-Shi Zheng  

**一句话要点**：提出ReViP框架，通过视觉-本体感觉再平衡减少视觉-语言-动作模型中的错误完成

**关键词**：视觉-语言-动作模型, 模态平衡, 错误完成, 机器人操作, 视觉-本体感觉调制, 基准测试

## 3 点简述
- 核心问题：VLA模型因模态不平衡，过度依赖内部状态导致执行失败时的错误完成
- 方法要点：引入任务感知环境先验，通过特征级线性调制增强视觉证据利用
- 实验或效果：在False-Completion Benchmark Suite上降低错误完成率，提升成功率，并推广至其他数据集和真实世界

## 摘要（原文）

> Vision-Language-Action (VLA) models have advanced robotic manipulation by combining vision, language, and proprioception to predict actions. However, previous methods fuse proprioceptive signals directly with VLM-encoded vision-language features, resulting in state-dominant bias and false completions despite visible execution failures. We attribute this to modality imbalance, where policies over-rely on internal state while underusing visual evidence. To address this, we present ReViP, a novel VLA framework with Vision-Proprioception Rebalance to enhance visual grounding and robustness under perturbations. The key insight is to introduce auxiliary task-aware environment priors to adaptively modulate the coupling between semantic perception and proprioceptive dynamics. Specifically, we use an external VLM as a task-stage observer to extract real-time task-centric visual cues from visual observations, which drive a Vision-Proprioception Feature-wise Linear Modulation to enhance environmental awareness and reduce state-driven errors. Moreover, to evaluate false completion, we propose the first False-Completion Benchmark Suite built on LIBERO with controlled settings such as Object-Drop. Extensive experiments show that ReViP effectively reduces false-completion rates and improves success rates over strong VLA baselines on our suite, with gains extending to LIBERO, RoboTwin 2.0, and real-world evaluations.

